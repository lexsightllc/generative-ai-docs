<!-- SPDX-License-Identifier: MPL-2.0 -->
# Google Gemini API Website & Documentation

These are the source files for the guide and tutorials on
the [Generative AI developer site](https://ai.google.dev/), home to
the Gemini API and Gemma.

| Path | Description |
| ---- | ----------- |
| [`site/`](site/) | Notebooks and other content used directly on ai.google.dev. |
| [`demos/`](demos/) | Demos apps. Larger than examples, typically consists of working apps. |
| [`examples/`](examples/) | Examples. Smaller, single-purpose code for demonstrating specific concepts. |



To contribute to the site documentation, please read
[CONTRIBUTING.md](CONTRIBUTING.md).

To contribute as a demo app maintainer, please read
[DEMO_MAINTAINERS.md](DEMO_MAINTAINERS.md).

To file an issue, please use the
[GitHub issue tracker](https://github.com/google/generative-ai-docs/issues/new).

## License

This project is distributed under the [Mozilla Public License 2.0](LICENSE). Any
modifications to MPL-covered files must be shared under the same license, while
larger works that merely include those files may remain under proprietary
terms.

## Credits

Project stewardship and ongoing development are documented in
[NOTICE](NOTICE), which also records bundled third-party attributions.

## Developer Tasks

Run these standardized commands to work with the repository. Each command maps
to the scripts in `./scripts`.

| Task | Description |
| ---- | ----------- |
| `make bootstrap` | Create the Python virtual environment, install tooling, and configure git hooks. |
| `make dev` | Serve the documentation sources locally for rapid iteration. |
| `make lint` | Run Ruff static analysis; pass `--fix` via `scripts/lint --fix` for autofixes. |
| `make fmt` | Apply formatting with Ruff. |
| `make typecheck` | Execute mypy in strict mode on scripts and tests. |
| `make test` | Run unit and integration test suites with pytest. |
| `make e2e` | Execute pytest with the `e2e` marker for end-to-end flows. |
| `make coverage` | Run tests with coverage thresholds enforced. |
| `make build` | Produce a timestamped archive of site, demo, and example content. |
| `make package` | Create a distributable tarball under `dist/`. |
| `make release` | Perform a conventional commit release bump via Commitizen. |
| `make update-deps` | Display outdated Python tooling dependencies. |
| `make security-scan` | Audit Python dependencies for known vulnerabilities. |
| `make sbom` | Generate a CycloneDX SBOM at `sbom/sbom.json`. |
| `make gen-docs` | Build the internal MkDocs documentation portal. |
| `make migrate` | Placeholder for executing schema migrations. |
| `make clean` | Remove build artifacts, caches, and virtual environments. |
| `make check` | Run the full local CI equivalent (lint, typecheck, tests, coverage, security scan). |
