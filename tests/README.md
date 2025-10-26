<!-- SPDX-License-Identifier: MPL-2.0 -->
# Test Suite Layout

Automated tests are organized by scope. Use the provided folders to keep
unit, integration, and end-to-end coverage isolated and deterministic.

- `unit/`: Fast, isolated tests that mock external systems.
- `integration/`: Service-level tests that exercise multiple components with
  controlled dependencies.
- `e2e/`: Black-box flows representing user journeys.

All tests should use deterministic seeds and fixtures stored under
`tests/fixtures/`.
