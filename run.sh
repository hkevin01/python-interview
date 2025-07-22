#!/bin/bash
# check for and fix function definition errors: missing function implementations, incorrect function signatures, undefined methods in classes, and functions that exist in one file but are imported incorrectly in another

# Get the directory of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Set the PYTHONPATH to include the project root
export PYTHONPATH="${SCRIPT_DIR}:${PYTHONPATH}"

# Change to the script directory
cd "${SCRIPT_DIR}"

# Activate the virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run the Python Interview Assistant GUI
python src/main.py
