# Bundled Corpus Manifest

## Snapshot

This is a historical offline snapshot used for fallback searches and reproducible examples. It is not an assertion of the latest upstream FDTDX version; resolve “latest” from official upstream sources at task time.

- FDTDX package/repository: current main commit `b93f90412db852527393c4a95a448c25aed1f6a8`, reporting version 0.6.2; 59 commits after tag `v0.6.2`.
- FDTDX notebook repository: commit `99c6709469f487f260372faf4d3bd4f11ed72ede`.
- Read the Docs archive URL: `https://fdtdx.readthedocs.io/_/downloads/en/latest/htmlzip/`.
- Archive last-modified header: 2026-07-16 13:03:53 GMT.
- Archive SHA-256: `D12CE5FF2983D4CCB583499C704FCEFBD4BEF3854A798E1509C1F5096BEE0534`.
- Standalone API pages: all 141 pages under `https://fdtdx.readthedocs.io/en/latest/api/`, retrieved 2026-07-16 with per-page hashes in `doc/readthedocs/api-pages-manifest.json`.
- API index: 141 public exports generated from the installed editable 0.6.2 package.

## Contents

| Path | Contents |
| --- | --- |
| `doc/readthedocs/site/` | Complete official HTML ZIP plus all standalone API pages under `site/api/`, sharing the archived assets |
| `doc/readthedocs/full.md` | Searchable Markdown conversion of the official single-page documentation |
| `doc/readthedocs/api-markdown/` | Clean, searchable Markdown conversions of all 141 API pages |
| `doc/readthedocs/source/` | Versioned Sphinx source and static assets |
| `doc/notebooks/source/` | All nine official notebook sources plus metadata/license |
| `doc/notebooks/markdown/` | Output-cleared, searchable Markdown conversions of all notebooks |
| `doc/api-index.json` | Static public API signatures, docstrings, fields, members, and source locations |
| `doc/examples/` | All eight current official Python examples |
| `doc/package-src/` | Complete Python source snapshot for FDTDX 0.6.2 |
| `doc/tests/` | Complete Python test source snapshot (173 files) |
| `doc/pyproject.toml`, `doc/uv.lock` | Package/dependency metadata and lock snapshot |

The searchable text corpus contains 452 documentation/notebook/example/source/test files plus metadata. Raw images and HTML assets remain available for visual context but are excluded from the default text search.

## Refresh policy

When updating this skill:

1. Refresh the FDTDX and notebook repository snapshots together.
2. Download the official Read the Docs HTML archive and record URL, timestamp, and SHA-256.
3. Fetch every standalone API page listed by `docs/source/07_api.rst`; record per-page checksums.
4. Regenerate clean Markdown from each `<article class="bd-article">` element.
5. Regenerate output-cleared notebook Markdown.
6. Run `scripts/build_api_index.py` against the refreshed installed package.
7. Re-run the API completeness test and skill validation.
8. Re-audit the known documentation drift and capability limits.
9. Forward-test at least a basic simulation, S-parameter task, and inverse-design/debugging task.
