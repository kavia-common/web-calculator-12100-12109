#!/bin/bash
cd /home/kavia/workspace/code-generation/web-calculator-12100-12109/calculator_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

