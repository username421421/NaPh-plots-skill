#!/usr/bin/env python3
"""Scrape official Lumerical FDTD documentation into citation-safe Markdown.

The scraper intentionally does not mirror complete Ansys articles. It stores
source metadata, headings, links, code-block inventory, and a bounded official
excerpt for traceability. Put synthesized guidance in references/*.md.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import html
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable


SOURCE_DOCS = [
    {
        "area": "Main reference",
        "title": "FDTD product reference manual",
        "url": "https://optics.ansys.com/hc/en-us/articles/360033154434-FDTD-product-reference-manual",
        "topic": "Index of FDTD solver, materials, objects, sources, monitors, analysis, convergence",
    },
    {
        "area": "Python API",
        "title": "Python API overview",
        "url": "https://optics.ansys.com/hc/en-us/articles/360037824513-Python-API-overview",
        "topic": "Legacy bundled lumapi, lumopt, lumslurm, automation overview",
    },
    {
        "area": "Python API",
        "title": "Installation and Getting Started - Python API",
        "url": "https://optics.ansys.com/hc/en-us/articles/39744901602707-Installation-and-Getting-Started-Python-API",
        "topic": "Import paths, embedded Python, external Python setup",
    },
    {
        "area": "Python API",
        "title": "Session Management - Python API",
        "url": "https://optics.ansys.com/hc/en-us/articles/360041873053-Session-Management-Python-API",
        "topic": "Local/remote sessions, context manager, serverArgs, close behavior",
    },
    {
        "area": "Python API",
        "title": "Script Commands as Methods - Python API",
        "url": "https://optics.ansys.com/hc/en-us/articles/360041579954-Script-Commands-as-Methods-Python-API",
        "topic": "Calling script commands as Python methods",
    },
    {
        "area": "Python API",
        "title": "Working with Simulation Objects - Python API",
        "url": "https://optics.ansys.com/hc/en-us/articles/39744946400659-Working-with-Simulation-Objects-Python-API",
        "topic": "Object construction, ordered properties, linked properties, handles",
    },
    {
        "area": "Python API",
        "title": "Passing Data - Python API",
        "url": "https://optics.ansys.com/hc/en-us/articles/360041401434-Passing-Data-Python-API",
        "topic": "Python/Lumerical type conversion, getv, putv, performance",
    },
    {
        "area": "Python API",
        "title": "Accessing Simulation Results - Python API",
        "url": "https://optics.ansys.com/hc/en-us/articles/39744236202771-Accessing-Simulation-Results-Python-API",
        "topic": "getresult, getdata, dataset dictionaries, raw arrays",
    },
    {
        "area": "Python API",
        "title": "Lumerical Python API Reference",
        "url": "https://optics.ansys.com/hc/en-us/articles/38660003331859-Lumerical-Python-API-Reference",
        "topic": "FDTD, MODE, DEVICE, INTERCONNECT constructors and options",
    },
    {
        "area": "PyLumerical",
        "title": "PyLumerical home",
        "url": "https://lumerical.docs.pyansys.com/version/stable/index.html",
        "topic": "ansys.lumerical.core package positioning",
    },
    {
        "area": "PyLumerical",
        "title": "PyLumerical getting started",
        "url": "https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html",
        "topic": "ansys-lumerical-core, autodiscovery, LUMERICAL_HOME",
    },
    {
        "area": "PyLumerical",
        "title": "PyLumerical API reference",
        "url": "https://lumerical.docs.pyansys.com/version/stable/api/index.html",
        "topic": "PyAnsys Lumerical API reference",
    },
    {
        "area": "PyLumerical",
        "title": "PyLumerical examples",
        "url": "https://lumerical.docs.pyansys.com/version/stable/examples.html",
        "topic": "Official PyLumerical example categories",
    },
    {
        "area": "PyLumerical",
        "title": "PyLumerical user guide",
        "url": "https://lumerical.docs.pyansys.com/version/stable/user_guide/index.html",
        "topic": "Simulation automation and lumopt2 guide router",
    },
    {
        "area": "PyLumerical",
        "title": "PyLumerical session management",
        "url": "https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html",
        "topic": "Product sessions, context managers, serverArgs, close behavior",
    },
    {
        "area": "PyLumerical",
        "title": "PyLumerical script commands as methods",
        "url": "https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html",
        "topic": "Lumerical script commands, constructors, custom functions, unsupported methods",
    },
    {
        "area": "PyLumerical",
        "title": "PyLumerical working with simulation objects",
        "url": "https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html",
        "topic": "Object construction, OrderedDict, keyword args, object handles, duplicate names",
    },
    {
        "area": "PyLumerical",
        "title": "PyLumerical passing data",
        "url": "https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html",
        "topic": "Type conversions, copies between Python and Lumerical, getv, putv",
    },
    {
        "area": "PyLumerical",
        "title": "PyLumerical accessing simulation results",
        "url": "https://lumerical.docs.pyansys.com/version/stable/user_guide/accessing_simulation_results.html",
        "topic": "getresult, getdata, datasets, raw arrays",
    },
    {
        "area": "PyLumerical",
        "title": "PyLumerical interface classes",
        "url": "https://lumerical.docs.pyansys.com/version/stable/api/interface_class.html",
        "topic": "FDTD, MODE, DEVICE, INTERCONNECT classes",
    },
    {
        "area": "PyLumerical",
        "title": "PyLumerical auxiliary classes",
        "url": "https://lumerical.docs.pyansys.com/version/stable/api/simobject_class.html",
        "topic": "SimObject, SimObjectResults, SimObjectId",
    },
    {
        "area": "PyLumerical",
        "title": "PyLumerical autodiscovery",
        "url": "https://lumerical.docs.pyansys.com/version/stable/api/autodiscovery.html",
        "topic": "Lumerical install autodiscovery and manual path fallback",
    },
    {
        "area": "PyLumerical",
        "title": "Basic session management",
        "url": "https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html",
        "topic": "Initialize local sessions using PyLumerical",
    },
    {
        "area": "PyLumerical",
        "title": "Basic FDTD Simulation - Lumerical style commands",
        "url": "https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html",
        "topic": "FDTD setup using command-style PyLumerical calls",
    },
    {
        "area": "PyLumerical",
        "title": "Basic FDTD Simulation - Python style commands",
        "url": "https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_pythonic/fdtd_example1_pythonic.html",
        "topic": "FDTD setup using Pythonic PyLumerical constructors",
    },
    {
        "area": "PyLumerical",
        "title": "PyLumerical Metalens (FDTD)",
        "url": "https://lumerical.docs.pyansys.com/version/stable/examples/Multiple_Solver_Workflows/metalens_FDTD_with_projections/metalens_FDTD_with_projections.html",
        "topic": "RCWA to FDTD metalens workflow, symmetry, far-field projection",
    },
    {
        "area": "PyLumerical",
        "title": "Photonic Crystal Bandstructure (FDTD)",
        "url": "https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/photonic_crystal_bandstructure/photonic_crystal_bandstructure.html",
        "topic": "FDTD structure/analysis groups, Bloch boundaries, sweeps",
    },
    {
        "area": "PyLumerical",
        "title": "Simple Waveguide (MODE FDE)",
        "url": "https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/waveguide_FDE/waveguide_FDE.html",
        "topic": "MODE workflow useful for mode-source and waveguide context",
    },
    {
        "area": "PyLumerical",
        "title": "Simple Ring Resonator (INTERCONNECT)",
        "url": "https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/ring_resonator_interconnect/ring_resonator_interconnect.html",
        "topic": "INTERCONNECT workflow useful for photonic circuit context",
    },
    {
        "area": "PyLumerical",
        "title": "Introduction to photonic inverse design with lumopt2",
        "url": "https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html",
        "topic": "lumopt2 installation, import, and workflow overview",
    },
    {
        "area": "PyLumerical",
        "title": "Getting started with lumopt2: simple metalens",
        "url": "https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html",
        "topic": "Basic lumopt2 project setup and run pattern",
    },
    {
        "area": "PyLumerical",
        "title": "Getting started with lumopt2: L-bend",
        "url": "https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html",
        "topic": "Closed-curve parametrization, ports, FOM, optimizer, callbacks",
    },
    {
        "area": "PyLumerical",
        "title": "Optimization session in lumopt2",
        "url": "https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html",
        "topic": "Project, base simulation, parametrization, FOM, callbacks",
    },
    {
        "area": "PyLumerical",
        "title": "lumopt2 API reference",
        "url": "https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/index.html",
        "topic": "lumopt2 classes and methods",
    },
    {
        "area": "Solver",
        "title": "FDTD solver - Simulation Object",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034382534-FDTD-solver-Simulation-Object",
        "topic": "Region geometry, mesh type, boundary conditions, advanced settings, status",
    },
    {
        "area": "Solver",
        "title": "Units and normalization conventions",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034397034-Units-and-normalization-conventions-in-Lumerical-solvers",
        "topic": "SI units, field units, source amplitudes, dipole amplitude units",
    },
    {
        "area": "Solver",
        "title": "Convergence testing process for FDTD simulations",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034915833-Convergence-testing-process-for-FDTD-simulations",
        "topic": "PML distance/layers, mesh, material fit, source/monitor errors",
    },
    {
        "area": "Mesh",
        "title": "Mesh override - Simulation Object",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034901833-Mesh-override-Simulation-Object",
        "topic": "Override precedence, dx/dy/dz, equivalent index, structure-based mesh",
    },
    {
        "area": "Mesh",
        "title": "Understanding Mesh Refinement and Conformal Mesh in FDTD",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034382594-Understanding-Mesh-Refinement-and-Conformal-Mesh-in-FDTD",
        "topic": "Conformal mesh motivation, finite mesh errors, scaling",
    },
    {
        "area": "Mesh",
        "title": "Selecting the best mesh refinement option",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034382614-Selecting-the-best-mesh-refinement-option-in-the-FDTD-simulation-object",
        "topic": "Staircase, conformal, precise volume average, inverse-design note",
    },
    {
        "area": "Boundaries",
        "title": "PML boundary conditions",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034382674-PML-boundary-conditions-in-FDTD-and-MODE",
        "topic": "PML profiles, layers, stabilized and steep-angle usage",
    },
    {
        "area": "Boundaries",
        "title": "Symmetric and anti-symmetric boundary conditions",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034382694-Symmetric-and-anti-symmetric-BCs-in-FDTD-and-MODE",
        "topic": "Symmetry parity, source polarization rules, full-domain validation",
    },
    {
        "area": "Boundaries",
        "title": "Bloch boundary conditions",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034382714-Bloch-boundary-conditions-in-FDTD-and-MODE",
        "topic": "Angled periodic sources, phase correction, complex fields",
    },
    {
        "area": "Boundaries",
        "title": "Periodic boundary conditions",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034382734-Periodic-boundary-conditions-in-FDTD-and-MODE",
        "topic": "Unit-cell setup, periodic field requirement, PML pairing",
    },
    {
        "area": "Sources",
        "title": "Plane wave and beam source",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034382854-Plane-wave-and-beam-source-Simulation-object",
        "topic": "Plane/Gaussian/beam settings, angled injection, scalar vs thin-lens",
    },
    {
        "area": "Sources",
        "title": "Understanding injection angles in broadband simulations",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034382894-Understanding-injection-angles-in-broadband-simulations",
        "topic": "Angle/frequency dependence, Bloch, BFAST, PML reflection",
    },
    {
        "area": "Sources",
        "title": "Tips and best practices when using the FDTD TFSF source",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034382934-Tips-and-best-practices-when-using-the-FDTD-TFSF-source",
        "topic": "Scattering setup, source box placement, uniform mesh, normalization",
    },
    {
        "area": "Sources",
        "title": "Dipole source - Simulation Object",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034382794-Dipole-source-Simulation-object",
        "topic": "Dipole orientation, record local field, dipolepower/Purcell",
    },
    {
        "area": "Sources",
        "title": "Mode source - Simulation Object",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034902153-Mode-source-Simulation-object",
        "topic": "Guided-mode injection, mode selection, broadband mode calculation",
    },
    {
        "area": "Sources",
        "title": "Ports (FDTD) - Simulation Object",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034382554-Ports-FDTD-Simulation-Object",
        "topic": "Port group, source port/mode, S-parameter extraction",
    },
    {
        "area": "Monitors",
        "title": "Frequency-domain monitor - Simulation Object",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034902393-Frequency-domain-monitor-Simulation-object",
        "topic": "DFT monitor memory, output fields/power, interpolation",
    },
    {
        "area": "Monitors",
        "title": "Field time monitor - Simulation Object",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034902353-Field-time-monitor-Simulation-object",
        "topic": "Time traces, resonances, sampling, spectrum",
    },
    {
        "area": "Monitors",
        "title": "Mode expansion monitor - Simulation Object",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034902413-Mode-expansion-monitor-Simulation-object",
        "topic": "Forward/backward mode amplitudes, S-parameters",
    },
    {
        "area": "Monitors",
        "title": "Using and understanding Mode Expansion Monitors",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034902433-Using-and-understanding-Mode-Expansion-Monitors",
        "topic": "Mode expansion analysis best practices",
    },
    {
        "area": "Monitors",
        "title": "Tips for accurately measuring reflection in an FDTD simulation",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034915753-Tips-for-accurately-measuring-reflection-in-an-FDTD-simulation",
        "topic": "Monitor placement behind/in front of source, reference normalization",
    },
    {
        "area": "Monitors",
        "title": "Far field projections in FDTD overview",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034914713-Far-field-projections-in-FDTD-overview",
        "topic": "Near-to-far requirements, planes/closed surfaces, homogeneous projection region",
    },
    {
        "area": "Examples",
        "title": "Reflection and transmission calculations using a planewave",
        "url": "https://optics.ansys.com/hc/en-us/articles/360042089573-Reflection-and-transmission-calculations-using-a-planewave",
        "topic": "Plane-wave R/T, angle sweep, mesh sensitivity, steep-angle PML",
    },
    {
        "area": "Scripting",
        "title": "Lumerical scripting language alphabetical list",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034923553-Lumerical-scripting-language-Alphabetical-list",
        "topic": "Command lookup and deprecation notes",
    },
    {
        "area": "Script command",
        "title": "addfdtd",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034924173-addfdtd-Script-command",
        "topic": "Add FDTD solver region",
    },
    {
        "area": "Script command",
        "title": "addmesh",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034924253-addmesh-Script-command",
        "topic": "Add mesh override region",
    },
    {
        "area": "Script command",
        "title": "adddftmonitor",
        "url": "https://optics.ansys.com/hc/en-us/articles/36957320687763-adddftmonitor-Script-command",
        "topic": "Add frequency-domain monitor",
    },
    {
        "area": "Script command",
        "title": "addmode",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034924353-addmode-Script-command",
        "topic": "Add FDTD mode source",
    },
    {
        "area": "Script command",
        "title": "addmodeexpansion",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034924573-addmodeexpansion-Script-command",
        "topic": "Add mode expansion monitor",
    },
    {
        "area": "Script command",
        "title": "addport",
        "url": "https://optics.ansys.com/hc/en-us/articles/360034924793-addport-FDTD-Script-command",
        "topic": "Add FDTD port object",
    },
]

DISCOVERY_KEYWORDS = (
    "fdtd",
    "python-api",
    "python",
    "lumapi",
    "lumopt",
    "pylumerical",
    "script-command",
    "script",
    "command",
    "solver",
    "mesh",
    "material",
    "structure",
    "geometry",
    "import",
    "analysis",
    "group",
    "sweep",
    "optimization",
    "normalization",
    "dataset",
    "grating",
    "boundary",
    "pml",
    "symmetry",
    "bloch",
    "periodic",
    "source",
    "monitor",
    "far-field",
    "reflection",
    "transmission",
    "s-parameter",
    "far",
    "mode",
    "port",
    "dipole",
    "tfsf",
    "plane",
    "gaussian",
    "bfast",
    "convergence",
)

SKIP_TAGS = {"script", "style", "noscript", "svg", "form", "button", "header", "footer", "nav"}

BROWSER_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/125.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
}


@dataclass
class ArticleDoc:
    url: str
    title: str
    markdown: str
    plain_text: str
    headings: list[str]
    links: list[tuple[str, str]]
    code_blocks: list[str]
    inline_codes: list[str]
    tables: list[dict[str, list]]


class _MarkdownParser(HTMLParser):
    def __init__(self, base_url: str):
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.blocks: list[str] = []
        self.current: list[str] = []
        self.headings: list[str] = []
        self.links: list[tuple[str, str]] = []
        self.code_blocks: list[str] = []
        self.inline_codes: list[str] = []
        self.skip_depth = 0
        self.heading_level: int | None = None
        self.in_pre = False
        self.in_inline_code = False
        self.pre_buffer: list[str] = []
        self.inline_code_buffer: list[str] = []
        self.anchor_href: str | None = None
        self.anchor_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        attr = {key.lower(): value or "" for key, value in attrs}
        if tag in SKIP_TAGS:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self._start_block("#" * int(tag[1]) + " ")
            self.heading_level = int(tag[1])
        elif tag == "p":
            self._start_block()
        elif tag == "li":
            self._start_block("- ")
        elif tag == "br":
            self._append_text("\n")
        elif tag == "pre":
            self._flush()
            self.in_pre = True
            self.pre_buffer = []
        elif tag == "code" and not self.in_pre:
            self._append_text("`")
            self.in_inline_code = True
            self.inline_code_buffer = []
        elif tag == "a":
            href = attr.get("href", "").strip()
            self.anchor_href = urllib.parse.urljoin(self.base_url, href) if href else None
            self.anchor_text = []
        elif tag in {"td", "th"}:
            self._append_text(" | ")
        elif tag == "tr":
            self._start_block()

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in SKIP_TAGS:
            if self.skip_depth:
                self.skip_depth -= 1
            return
        if self.skip_depth:
            return
        if tag == "pre":
            self.in_pre = False
            code = html.unescape("".join(self.pre_buffer)).strip()
            if code:
                self.code_blocks.append(code)
                self.blocks.append("```text\n" + code + "\n```")
            self.pre_buffer = []
        elif tag == "code" and not self.in_pre:
            code = self._clean_inline("".join(self.inline_code_buffer))
            if code:
                self.inline_codes.append(code)
            self.in_inline_code = False
            self.inline_code_buffer = []
            self._append_text("`")
        elif tag == "a":
            text = self._clean_inline("".join(self.anchor_text))
            if text:
                if self.anchor_href:
                    self._append_text(f"[{text}]({self.anchor_href})")
                    self.links.append((text, self.anchor_href))
                else:
                    self._append_text(text)
            self.anchor_href = None
            self.anchor_text = []
        elif tag in {"p", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6"}:
            block = self._flush()
            if tag.startswith("h") and block:
                self.headings.append(re.sub(r"^#+\s*", "", block).strip())
                self.heading_level = None

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        if self.in_pre:
            self.pre_buffer.append(data)
            return
        if self.in_inline_code:
            self.inline_code_buffer.append(data)
        if self.anchor_href is not None:
            self.anchor_text.append(data)
            return
        self._append_text(data)

    def _start_block(self, prefix: str = "") -> None:
        self._flush()
        self.current = [prefix] if prefix else []

    def _append_text(self, text: str) -> None:
        cleaned = self._clean_inline(text)
        if not cleaned:
            return
        if self.current:
            previous = self.current[-1]
            if previous and not previous.endswith((" ", "\n", "`", "(", "[", "|")):
                if not cleaned.startswith((".", ",", ":", ";", ")", "]", "`", "|")):
                    self.current.append(" ")
        self.current.append(cleaned)

    def _flush(self) -> str:
        if not self.current:
            return ""
        block = "".join(self.current).strip()
        block = re.sub(r"[ \t]+", " ", block)
        block = re.sub(r"\s+\|", " |", block)
        block = re.sub(r"\|\s+", "| ", block)
        self.current = []
        if block:
            self.blocks.append(block)
        return block

    @staticmethod
    def _clean_inline(text: str) -> str:
        return re.sub(r"\s+", " ", html.unescape(text)).strip()

    def markdown(self) -> str:
        self._flush()
        text = "\n\n".join(block for block in self.blocks if block)
        return re.sub(r"\n{3,}", "\n\n", text).strip()


def fetch_url(url: str, timeout: int = 45) -> str:
    request = urllib.request.Request(
        url,
        headers=BROWSER_HEADERS,
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def slug_from_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    stem = parsed.path.strip("/").split("/")[-1] or parsed.netloc
    stem = re.sub(r"\.html?$", "", stem, flags=re.I)
    if stem.lower() in {"", "index"}:
        path_stem = "-".join(part for part in parsed.path.strip("/").split("/") if part and part.lower() != "index.html")
        stem = f"{parsed.netloc}-{path_stem}" if path_stem else parsed.netloc
    stem = re.sub(r"[^A-Za-z0-9]+", "-", stem).strip("-").lower()
    return stem[:120] or "source"


def _slice_article_html(raw_html: str) -> str:
    for tag in ("article", "main"):
        match = re.search(rf"(?is)<{tag}\b[^>]*>(.*?)</{tag}>", raw_html)
        if match:
            return match.group(1)
    match = re.search(r'(?is)<div\b[^>]*(?:class|id)=["\'][^"\']*article[^"\']*["\'][^>]*>(.*?)</div>', raw_html)
    if match:
        return match.group(1)
    body = re.search(r"(?is)<body\b[^>]*>(.*?)</body>", raw_html)
    return body.group(1) if body else raw_html


def _title_from_html(raw_html: str) -> str:
    h1 = re.search(r"(?is)<h1\b[^>]*>(.*?)</h1>", raw_html)
    if h1:
        return _plain_text(h1.group(1))
    title = re.search(r"(?is)<title\b[^>]*>(.*?)</title>", raw_html)
    return _plain_text(title.group(1)) if title else "Untitled"


def _plain_text(fragment: str) -> str:
    fragment = re.sub(r"(?is)<script\b.*?</script>", " ", fragment)
    fragment = re.sub(r"(?is)<style\b.*?</style>", " ", fragment)
    fragment = re.sub(r"(?is)<[^>]+>", " ", fragment)
    return re.sub(r"\s+", " ", html.unescape(fragment)).strip()


def markdown_to_plain_text(markdown: str) -> str:
    text = re.sub(r"(?s)```.*?```", " ", markdown)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"(?m)^#{1,6}\s*", "", text)
    text = re.sub(r"(?m)^-\s*", "", text)
    return re.sub(r"\s+", " ", text).strip()


def extract_tables(raw_html: str) -> list[dict[str, list]]:
    tables: list[dict[str, list]] = []
    for table_html in re.findall(r"(?is)<table\b[^>]*>(.*?)</table>", raw_html):
        parsed_rows: list[list[str]] = []
        header_flags: list[bool] = []
        for row_html in re.findall(r"(?is)<tr\b[^>]*>(.*?)</tr>", table_html):
            cells = re.findall(r"(?is)<t([dh])\b[^>]*>(.*?)</t[dh]>", row_html)
            if not cells:
                continue
            parsed_rows.append([_plain_text(cell_html) for _, cell_html in cells])
            header_flags.append(any(kind.lower() == "h" for kind, _ in cells))
        if not parsed_rows:
            continue
        headers: list[str] = []
        rows = parsed_rows
        if header_flags[0]:
            headers = parsed_rows[0]
            rows = parsed_rows[1:]
        tables.append({"headers": headers, "rows": rows})
    return tables


def extract_article(url: str, raw_html: str) -> ArticleDoc:
    article_html = _slice_article_html(raw_html)
    parser = _MarkdownParser(url)
    parser.feed(article_html)
    markdown = parser.markdown()
    plain_text = markdown_to_plain_text(markdown)
    title = parser.headings[0] if parser.headings else _title_from_html(raw_html)
    return ArticleDoc(
        url=url,
        title=title,
        markdown=markdown,
        plain_text=plain_text,
        headings=parser.headings,
        links=_dedupe_pairs(parser.links),
        code_blocks=parser.code_blocks,
        inline_codes=sorted(set(parser.inline_codes)),
        tables=extract_tables(article_html),
    )


def _dedupe_pairs(pairs: Iterable[tuple[str, str]]) -> list[tuple[str, str]]:
    seen: set[tuple[str, str]] = set()
    result: list[tuple[str, str]] = []
    for text, href in pairs:
        key = (text.strip(), href.strip())
        if key[0] and key[1] and key not in seen:
            seen.add(key)
            result.append(key)
    return result


def bounded_excerpt(markdown: str, max_words: int) -> str:
    without_code = re.sub(r"(?s)```.*?```", " ", markdown)
    without_markup = re.sub(r"(?m)^#{1,6}\s*", "", without_code)
    without_markup = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", without_markup)
    words = re.findall(r"\S+", without_markup)
    if len(words) <= max_words:
        return " ".join(words)
    return " ".join(words[:max_words]) + " ..."


def detected_key_terms(doc: ArticleDoc) -> list[str]:
    haystack = f"{doc.title} {doc.plain_text} {doc.url}".lower()
    terms = sorted({keyword for keyword in DISCOVERY_KEYWORDS if keyword in haystack})
    return terms


def link_group(href: str) -> str:
    parsed = urllib.parse.urlparse(href)
    if parsed.netloc in {"optics.ansys.com", "lumerical.docs.pyansys.com"}:
        return "official"
    if parsed.netloc.endswith("ansys.com") or parsed.netloc.endswith("pyansys.com"):
        return "ansys-related"
    return "external"


def render_links(links: list[tuple[str, str]], group: str, limit: int = 500) -> str:
    filtered = [(text, href) for text, href in links if link_group(href) == group]
    if not filtered:
        return "- None"
    lines = [f"- [{text}]({href})" for text, href in filtered[:limit]]
    if len(filtered) > limit:
        lines.append(f"- ... {len(filtered) - limit} additional link(s) omitted from this generated page")
    return "\n".join(lines)


def render_table_inventory(tables: list[dict[str, list]], limit: int = 80) -> str:
    if not tables:
        return "- No tables detected"
    lines: list[str] = []
    for index, table in enumerate(tables[:limit], start=1):
        headers = table.get("headers", [])
        rows = table.get("rows", [])
        column_count = len(headers) if headers else max((len(row) for row in rows), default=0)
        lines.append(f"- Table {index}: {column_count} column(s), {len(rows)} row(s)")
        if headers:
            lines.append(f"  - Headers: {', '.join(headers[:12])}")
        if rows:
            sample = " | ".join(rows[0][:8])
            lines.append(f"  - First row sample: {sample[:240]}")
    if len(tables) > limit:
        lines.append(f"- ... {len(tables) - limit} additional table(s) omitted from this generated page")
    return "\n".join(lines)


def render_inline_code_inventory(inline_codes: list[str], limit: int = 120) -> str:
    if not inline_codes:
        return "- No inline code terms detected"
    lines = [f"- `{code[:160]}`" for code in inline_codes[:limit]]
    if len(inline_codes) > limit:
        lines.append(f"- ... {len(inline_codes) - limit} additional inline code term(s) omitted")
    return "\n".join(lines)


def make_local_summary(source: dict[str, str], doc: ArticleDoc) -> str:
    headings = ", ".join(doc.headings[:8]) if doc.headings else "no captured headings"
    terms = ", ".join(detected_key_terms(doc)[:16]) or "no configured FDTD keywords detected"
    return (
        f"This local capture indexes the official page `{doc.title}` for the topic `{source['topic']}`. "
        f"It captured {len(doc.headings)} heading(s), {len(doc.links)} link(s), "
        f"{len(doc.code_blocks)} code block(s), {len(doc.inline_codes)} inline code term(s), "
        f"and {len(doc.tables)} table(s). Main headings: {headings}. Key detected terms: {terms}."
    )


def render_scraped_page(
    source: dict[str, str],
    doc: ArticleDoc,
    last_checked: str,
    max_excerpt_words: int = 180,
) -> str:
    excerpt = bounded_excerpt(doc.markdown, max_excerpt_words)
    headings = "\n".join(f"- {heading}" for heading in doc.headings[:200]) or "- No headings extracted"
    terms = "\n".join(f"- {term}" for term in detected_key_terms(doc)) or "- No configured key terms detected"
    code_inventory = []
    for index, code in enumerate(doc.code_blocks[:100], start=1):
        first_line = next((line.strip() for line in code.splitlines() if line.strip()), "")
        line_count = len(code.splitlines())
        code_inventory.append(f"- Code block {index}: {line_count} line(s); first line `{first_line[:160]}`")
    code_blocks = "\n".join(code_inventory) or "- No code blocks detected"
    return f"""# {doc.title}

Source URL: {source["url"]}  
Area: {source["area"]}  
Topic: {source["topic"]}  
Discovery depth: {source.get("depth", 0)}  
Last checked: {last_checked}  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

{make_local_summary(source, doc)}

## Key Terms

{terms}

## Captured Headings

{headings}

## Official Text Excerpt

> {excerpt}

## Code Block Inventory

{code_blocks}

## Inline Code Inventory

{render_inline_code_inventory(doc.inline_codes)}

## Table Inventory

{render_table_inventory(doc.tables)}

## Official Links Found

{render_links(doc.links, "official")}

## Ansys-Related External Links Found

{render_links(doc.links, "ansys-related")}

## External Links Found

{render_links(doc.links, "external")}
"""


def write_inventory(sources: list[dict[str, str]], output: Path) -> None:
    lines = [
        "# Lumerical FDTD Official Source Inventory",
        "",
        "Generated by `scripts/scrape_lumerical_docs.py`.",
        "",
        "| Area | Official source | Topic | Depth | Last checked | Local file | Words | Headings | Links | Code | Tables | Status |",
        "| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for source in sources:
        title = source.get("title", "Untitled").replace("|", "\\|")
        topic = source.get("topic", "").replace("|", "\\|")
        area = source.get("area", "").replace("|", "\\|")
        lines.append(
            f"| {area} | [{title}]({source['url']}) | {topic} | "
            f"{source.get('depth', 0)} | {source.get('last_checked', '')} | {source.get('local_file', '')} | "
            f"{source.get('word_count', '')} | {source.get('heading_count', '')} | {source.get('link_count', '')} | "
            f"{source.get('code_count', '')} | {source.get('table_count', '')} | {source.get('status', '')} |"
        )
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_report(sources: list[dict[str, str]], output: Path, last_checked: str) -> None:
    ok = [source for source in sources if source.get("status") == "ok"]
    failed = [source for source in sources if source.get("status") != "ok"]
    by_area: dict[str, list[dict[str, str]]] = defaultdict(list)
    by_status: dict[str, int] = defaultdict(int)
    for source in sources:
        by_area[source.get("area", "Unknown")].append(source)
        by_status[source.get("status", "unknown")] += 1
    total_words = sum(int(source.get("word_count") or 0) for source in ok)
    total_links = sum(int(source.get("link_count") or 0) for source in ok)
    total_tables = sum(int(source.get("table_count") or 0) for source in ok)
    total_code = sum(int(source.get("code_count") or 0) for source in ok)
    lines = [
        "# Lumerical FDTD Scrape Report",
        "",
        f"Generated: {last_checked}",
        f"Sources attempted: {len(sources)}",
        f"Successful captures: {len(ok)}",
        f"Failed captures: {len(failed)}",
        f"Captured words indexed: {total_words}",
        f"Captured links indexed: {total_links}",
        f"Captured tables indexed: {total_tables}",
        f"Captured code blocks indexed: {total_code}",
        "",
        "## Status Counts",
        "",
    ]
    for status, count in sorted(by_status.items()):
        lines.append(f"- {status}: {count}")
    lines.extend([
        "",
        "## Area Coverage",
        "",
        "| Area | Total | Captured | Failed |",
        "| --- | ---: | ---: | ---: |",
    ])
    for area, area_sources in sorted(by_area.items()):
        area_ok = sum(1 for source in area_sources if source.get("status") == "ok")
        lines.append(f"| {area} | {len(area_sources)} | {area_ok} | {len(area_sources) - area_ok} |")
    lines.extend([
        "",
        "## Failed Captures",
        "",
    ])
    if failed:
        lines.extend(f"- [{source['title']}]({source['url']}): {source.get('status', 'failed')}" for source in failed)
    else:
        lines.append("- None")
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_corpus_indexes(sources: list[dict[str, str]], parsed_docs: list[tuple[dict[str, str], ArticleDoc]], output_root: Path) -> None:
    by_area: dict[str, list[dict[str, str]]] = defaultdict(list)
    for source in sources:
        by_area[source.get("area", "Unknown")].append(source)

    corpus_lines = [
        "# Lumerical FDTD Local Corpus Index",
        "",
        "Generated by `scripts/scrape_lumerical_docs.py` from official source metadata.",
        "",
        "## Coverage By Area",
        "",
    ]
    for area, area_sources in sorted(by_area.items()):
        corpus_lines.append(f"### {area}")
        corpus_lines.append("")
        corpus_lines.append("| Source | Local file | Words | Links | Tables | Code | Status |")
        corpus_lines.append("| --- | --- | ---: | ---: | ---: | ---: | --- |")
        for source in sorted(area_sources, key=lambda item: item.get("title", "")):
            corpus_lines.append(
                f"| [{source.get('title', 'Untitled')}]({source.get('url', '')}) | {source.get('local_file', '')} | "
                f"{source.get('word_count', '')} | {source.get('link_count', '')} | {source.get('table_count', '')} | "
                f"{source.get('code_count', '')} | {source.get('status', '')} |"
            )
        corpus_lines.append("")
    (output_root / "corpus-index.md").write_text("\n".join(corpus_lines).rstrip() + "\n", encoding="utf-8")

    link_lines = [
        "# Lumerical FDTD Official Link Graph",
        "",
        "Only links captured from successfully fetched official pages are listed.",
        "",
    ]
    for source, doc in sorted(parsed_docs, key=lambda item: item[0].get("title", "")):
        link_lines.append(f"## {source.get('title', doc.title)}")
        link_lines.append("")
        link_lines.append(f"Source: [{source.get('url', doc.url)}]({source.get('url', doc.url)})")
        link_lines.append("")
        official_links = [(text, href) for text, href in doc.links if link_group(href) in {"official", "ansys-related"}]
        if official_links:
            for text, href in official_links:
                link_lines.append(f"- [{text}]({href})")
        else:
            link_lines.append("- No official links captured")
        link_lines.append("")
    (output_root / "link-graph.md").write_text("\n".join(link_lines).rstrip() + "\n", encoding="utf-8")

    keyword_rows: dict[str, list[str]] = defaultdict(list)
    for source, doc in parsed_docs:
        for term in detected_key_terms(doc):
            keyword_rows[term].append(f"[{source.get('title', doc.title)}]({source.get('local_file', source.get('url', ''))})")
    keyword_lines = [
        "# Lumerical FDTD Keyword Index",
        "",
        "| Keyword | Local captures |",
        "| --- | --- |",
    ]
    for term, rows in sorted(keyword_rows.items()):
        keyword_lines.append(f"| {term} | {'; '.join(rows[:30])} |")
    (output_root / "keyword-index.md").write_text("\n".join(keyword_lines) + "\n", encoding="utf-8")


def discover_sources(
    seed_docs: list[tuple[dict[str, str], ArticleDoc]],
    existing_urls: set[str],
    limit: int,
    depth: int = 1,
) -> list[dict[str, str]]:
    discovered: list[dict[str, str]] = []
    for source, doc in seed_docs:
        for text, href in doc.links:
            if len(discovered) >= limit:
                return discovered
            parsed = urllib.parse.urlparse(href)
            normalized = urllib.parse.urlunparse((parsed.scheme, parsed.netloc, parsed.path, "", "", ""))
            haystack = f"{text} {normalized}".lower()
            if parsed.netloc not in {"optics.ansys.com", "lumerical.docs.pyansys.com"}:
                continue
            if normalized in existing_urls:
                continue
            if "/articles/" not in parsed.path and "lumerical.docs.pyansys.com" not in parsed.netloc:
                continue
            if not any(keyword in haystack for keyword in DISCOVERY_KEYWORDS):
                continue
            existing_urls.add(normalized)
            discovered.append(
                {
                    "area": "Discovered official source",
                    "title": text[:120] or slug_from_url(normalized),
                    "url": normalized,
                    "topic": f"Discovered from {source['title']}",
                    "depth": depth,
                }
            )
    return discovered


def scrape(
    output_dir: Path,
    inventory_path: Path,
    report_path: Path,
    *,
    discover: bool = False,
    max_discovered: int = 60,
    discover_rounds: int = 1,
    max_total: int = 180,
    max_excerpt_words: int = 180,
    sleep_seconds: float = 0.2,
) -> list[dict[str, str]]:
    output_dir.mkdir(parents=True, exist_ok=True)
    last_checked = _dt.date.today().isoformat()
    queue = [dict(source, depth=0) for source in SOURCE_DOCS]
    finished: list[dict[str, str]] = []
    parsed_docs: list[tuple[dict[str, str], ArticleDoc]] = []
    seen_urls = {source["url"] for source in queue}
    used_slugs: dict[str, int] = {}
    discovered_count = 0

    index = 0
    while index < len(queue) and len(finished) < max_total:
        source = queue[index]
        index += 1
        source["last_checked"] = last_checked
        base_slug = slug_from_url(source["url"])
        used_slugs[base_slug] = used_slugs.get(base_slug, 0) + 1
        slug = base_slug if used_slugs[base_slug] == 1 else f"{base_slug}-{used_slugs[base_slug]}"
        local_file = f"scraped/{slug}.md"
        source["local_file"] = local_file
        try:
            raw_html = fetch_url(source["url"])
            doc = extract_article(source["url"], raw_html)
            page = render_scraped_page(source, doc, last_checked, max_excerpt_words=max_excerpt_words)
            (output_dir / f"{slug}.md").write_text(page, encoding="utf-8")
            source["status"] = "ok"
            source["word_count"] = str(len(doc.plain_text.split()))
            source["heading_count"] = str(len(doc.headings))
            source["link_count"] = str(len(doc.links))
            source["code_count"] = str(len(doc.code_blocks))
            source["table_count"] = str(len(doc.tables))
            parsed_docs.append((source, doc))
            if (
                discover
                and int(source.get("depth", 0)) < discover_rounds
                and discovered_count < max_discovered
                and len(queue) < max_total
            ):
                remaining_discovered = min(max_discovered - discovered_count, max_total - len(queue))
                additions = discover_sources(
                    [(source, doc)],
                    seen_urls,
                    remaining_discovered,
                    depth=int(source.get("depth", 0)) + 1,
                )
                queue.extend(additions)
                discovered_count += len(additions)
        except urllib.error.HTTPError as exc:
            reason = exc.reason or ""
            source["status"] = f"failed: HTTPError {exc.code} {reason}".strip()
        except (urllib.error.URLError, TimeoutError, OSError, UnicodeError) as exc:
            source["status"] = f"failed: {exc.__class__.__name__}"
        for key in ("word_count", "heading_count", "link_count", "code_count", "table_count"):
            source.setdefault(key, "")
        finished.append(source)
        if sleep_seconds:
            time.sleep(sleep_seconds)

    write_inventory(finished, inventory_path)
    write_report(finished, report_path, last_checked)
    write_corpus_indexes(finished, parsed_docs, inventory_path.parent)
    return finished


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    default_root = Path(__file__).resolve().parents[1] / "references"
    parser.add_argument("--output-dir", type=Path, default=default_root / "scraped")
    parser.add_argument("--inventory", type=Path, default=default_root / "source-inventory.md")
    parser.add_argument("--report", type=Path, default=default_root / "scrape-report.md")
    parser.add_argument("--discover", action="store_true", help="add related official links discovered from seed pages")
    parser.add_argument("--max-discovered", type=int, default=200)
    parser.add_argument("--discover-rounds", type=int, default=2, help="crawl depth for official links discovered from captured pages")
    parser.add_argument("--max-total", type=int, default=300, help="maximum total URLs to attempt")
    parser.add_argument("--max-excerpt-words", type=int, default=180)
    parser.add_argument("--sleep", type=float, default=0.2, help="seconds between requests")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    sources = scrape(
        args.output_dir,
        args.inventory,
        args.report,
        discover=args.discover,
        max_discovered=args.max_discovered,
        discover_rounds=args.discover_rounds,
        max_total=args.max_total,
        max_excerpt_words=args.max_excerpt_words,
        sleep_seconds=args.sleep,
    )
    ok = sum(1 for source in sources if source.get("status") == "ok")
    print(f"Captured {ok}/{len(sources)} official documentation pages")
    print(f"Inventory: {args.inventory}")
    print(f"Report: {args.report}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
