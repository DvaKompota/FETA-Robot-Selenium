#!/bin/bash
# Builds and runs the Pytest command

# Test running command:
test_command="robot"

# Setup test path:
export PYTHONPATH=:./../..

# Setup test scope:
if [ -z "$1" ]; then
  test_command="${test_command}"
else
  test_command="${test_command} -i '$1'"
fi

# Setup reports path:
test_command="${test_command} -d `pwd`/reports"

# Setup test path:
test_command="${test_command} `pwd`/tests/demoqa/features/"

# Run the commands
echo $test_command;
eval $test_command;
