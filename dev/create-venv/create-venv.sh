#! /usr/bin/env bash

SCRIPT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_PATH="${SCRIPT_PATH%quick-notes*}quick-notes"

INPUT_FOLDER="${SCRIPT_PATH}/input"
OUTPUT_FOLDER="${SCRIPT_PATH}/output"
mkdir -p "${OUTPUT_FOLDER}"

set -e

pushd "${PROJECT_PATH}" >/dev/null

trap "echo 'Aborted!'" err
python3.8 -m venv .venv

source .venv/bin/activate

pip install --upgrade pip
pip install -e .
pip install build tox

popd >/dev/null
