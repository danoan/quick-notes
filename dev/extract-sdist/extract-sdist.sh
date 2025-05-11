#! /usr/bin/env bash

set -euo pipefail

SCRIPT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_PATH="${SCRIPT_PATH%quick-notes*}quick-notes"

OUTPUT_FOLDER="${SCRIPT_PATH}/output"
mkdir -p "${OUTPUT_FOLDER}"

pushd "${PROJECT_PATH}" >/dev/null

source .venv/bin/activate

DIST_FOLDER="${OUTPUT_FOLDER}/dist"
mkdir -p "${DIST_FOLDER}"

EXTRACT_FOLDER="${OUTPUT_FOLDER}/extract"
mkdir -p "${EXTRACT_FOLDER}"

pyproject-build --outdir "${DIST_FOLDER}" .

tar -xf ${DIST_FOLDER}/quick_notes-*.tar.gz -C "${EXTRACT_FOLDER}"

popd >/dev/null
