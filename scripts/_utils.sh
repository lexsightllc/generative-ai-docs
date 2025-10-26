#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_PATH="${ROOT_DIR}/.venv"
PYTHON_BIN="${PYTHON_BIN:-python3}"

ensure_venv() {
  if [[ ! -d "${VENV_PATH}" ]]; then
    echo "Creating virtual environment in ${VENV_PATH}" >&2
    "${PYTHON_BIN}" -m venv "${VENV_PATH}"
  fi
  # shellcheck disable=SC1090
  source "${VENV_PATH}/bin/activate"
}

run_with_venv() {
  ensure_venv
  if [[ -f "${ROOT_DIR}/configs/python/requirements.txt" ]]; then
    pip install --upgrade pip >/dev/null
    pip install --requirement "${ROOT_DIR}/configs/python/requirements.txt" >/dev/null
  fi
}
