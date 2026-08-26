#!/usr/bin/env python3
"""Report whether an FDTDX/JAX environment is ready and which backend it uses."""

from __future__ import annotations

import argparse
import importlib.metadata
import inspect
import json
import os
import platform
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


SKILL_ROOT = Path(__file__).resolve().parents[1]
BUNDLED_API_INDEX = SKILL_ROOT / "doc" / "api-index.json"


def source_git_commit(module_file: Path) -> str:
    for parent in (module_file.parent, *module_file.parents):
        if not (parent / ".git").exists():
            continue
        try:
            result = subprocess.run(
                ["git", "-C", str(parent), "rev-parse", "HEAD"],
                check=True,
                capture_output=True,
                text=True,
                timeout=3,
            )
            return result.stdout.strip()
        except (FileNotFoundError, subprocess.SubprocessError):
            return ""
    return ""


def compare_bundled_api(fdtdx: Any, signature: str) -> dict[str, Any]:
    if not BUNDLED_API_INDEX.exists():
        return {"available": False}
    try:
        index = json.loads(BUNDLED_API_INDEX.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"available": False, "error": f"{type(exc).__name__}: {exc}"}
    installed = set(getattr(fdtdx, "__all__", []))
    bundled = {entry["name"] for entry in index.get("entries", [])}
    bundled_config = next(
        (entry.get("signature", "") for entry in index.get("entries", []) if entry.get("name") == "SimulationConfig"),
        "",
    )
    return {
        "available": True,
        "metadata": index.get("metadata", {}),
        "export_names_match": installed == bundled,
        "missing_from_installed": sorted(bundled - installed),
        "extra_in_installed": sorted(installed - bundled),
        "simulation_config_signature_match": signature == bundled_config,
    }


def collect(project: Path | None = None) -> dict[str, Any]:
    data: dict[str, Any] = {
        "python": {
            "version": platform.python_version(),
            "executable": sys.executable,
            "supported": (3, 11) <= sys.version_info[:2] < (3, 15),
            "virtual_environment": sys.prefix != getattr(sys, "base_prefix", sys.prefix),
        },
        "platform": {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
        },
        "environment": {
            key: os.environ.get(key, "")
            for key in (
                "CUDA_VISIBLE_DEVICES",
                "JAX_PLATFORMS",
                "JAX_PLATFORM_NAME",
                "XLA_FLAGS",
                "XLA_PYTHON_CLIENT_ALLOCATOR",
                "XLA_PYTHON_CLIENT_PREALLOCATE",
            )
        },
    }
    if project is not None:
        project = project.resolve()
        data["project"] = {
            "path": str(project),
            "pyproject": (project / "pyproject.toml").exists(),
            "uv_lock": (project / "uv.lock").exists(),
            "git": (project / ".git").exists(),
        }

    try:
        data["fdtdx_distribution_version"] = importlib.metadata.version("fdtdx")
    except importlib.metadata.PackageNotFoundError:
        data["fdtdx_distribution_version"] = None

    with tempfile.TemporaryDirectory(prefix="fdtdx-doctor-") as temp_dir:
        os.environ.setdefault("TIDY3D_BASE_DIR", temp_dir)
        try:
            import fdtdx

            module_file = Path(fdtdx.__file__).resolve()
            config_signature = str(inspect.signature(fdtdx.SimulationConfig.__init__))
            data["fdtdx"] = {
                "import_ok": True,
                "file": str(module_file),
                "public_exports": len(getattr(fdtdx, "__all__", [])),
                "simulation_config_signature": config_signature,
                "config_api": "grid" if "grid" in inspect.signature(fdtdx.SimulationConfig.__init__).parameters else "resolution",
                "source_git_commit": source_git_commit(module_file),
                "bundled_api_comparison": compare_bundled_api(fdtdx, config_signature),
            }
        except Exception as exc:
            data["fdtdx"] = {
                "import_ok": False,
                "error": f"{type(exc).__name__}: {exc}",
            }

        try:
            import jax

            devices = []
            for device in jax.devices():
                devices.append(
                    {
                        "platform": device.platform,
                        "kind": getattr(device, "device_kind", ""),
                        "id": device.id,
                    }
                )
            data["jax"] = {
                "import_ok": True,
                "version": jax.__version__,
                "default_backend": jax.default_backend(),
                "devices": devices,
                "x64_enabled": bool(jax.config.jax_enable_x64),
            }
        except Exception as exc:
            data["jax"] = {
                "import_ok": False,
                "error": f"{type(exc).__name__}: {exc}",
            }
    return data


def render(data: dict[str, Any]) -> str:
    lines = [
        f"Python: {data['python']['version']} ({data['python']['executable']})",
        f"Supported Python: {data['python']['supported']} (requires >=3.11,<3.15)",
        f"Virtual environment: {data['python']['virtual_environment']}",
        f"Platform: {data['platform']['system']} {data['platform']['release']} {data['platform']['machine']}",
        f"FDTDX distribution: {data.get('fdtdx_distribution_version') or 'not installed'}",
    ]
    fdtdx_data = data.get("fdtdx", {})
    if fdtdx_data.get("import_ok"):
        lines.append(f"FDTDX import: OK ({fdtdx_data['file']})")
        lines.append(f"Public exports: {fdtdx_data['public_exports']}")
        lines.append(f"SimulationConfig API: {fdtdx_data['config_api']}")
        lines.append(f"SimulationConfig signature: {fdtdx_data['simulation_config_signature']}")
        if fdtdx_data.get("source_git_commit"):
            lines.append(f"Source commit: {fdtdx_data['source_git_commit']}")
        comparison = fdtdx_data.get("bundled_api_comparison", {})
        if comparison.get("available"):
            exact = comparison.get("export_names_match") and comparison.get("simulation_config_signature_match")
            lines.append(f"Bundled API shape match: {bool(exact)}")
            if not exact:
                lines.append("  Inspect the installed source/lock file; do not mix bundled and installed APIs.")
    else:
        lines.append(f"FDTDX import: FAILED ({fdtdx_data.get('error', 'unknown error')})")
    jax_data = data.get("jax", {})
    if jax_data.get("import_ok"):
        lines.append(f"JAX: {jax_data['version']} / backend={jax_data['default_backend']}")
        for device in jax_data["devices"]:
            lines.append(f"  device {device['id']}: {device['platform']} {device['kind']}")
    else:
        lines.append(f"JAX import: FAILED ({jax_data.get('error', 'unknown error')})")
    if data["platform"]["system"] == "Windows" and jax_data.get("default_backend") == "cpu":
        lines.append("Note: official JAX CUDA wheels require Linux/WSL; native Windows normally uses CPU.")
    if "project" in data:
        project = data["project"]
        lines.append(f"Project: {project['path']}")
        lines.append(f"  pyproject={project['pyproject']} uv.lock={project['uv_lock']} git={project['git']}")
    overrides = {k: v for k, v in data["environment"].items() if v}
    if overrides:
        lines.append("Relevant environment overrides:")
        lines.extend(f"  {key}={value}" for key, value in overrides.items())
    return "\n".join(lines)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--require-backend", choices=("cpu", "gpu", "tpu", "METAL"))
    args = parser.parse_args()
    data = collect(args.project)
    print(json.dumps(data, indent=2) if args.json else render(data))
    if not data.get("fdtdx", {}).get("import_ok") or not data.get("jax", {}).get("import_ok"):
        return 1
    if args.require_backend and data["jax"].get("default_backend") != args.require_backend:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
