#!/bin/bash
set -e

# install python3
make dev-env

# Activate environment
source $PWD/.env/Scripts/activate

if [ $? -eq 0 ]; then
    echo "OK - python3 virtual env activated."
else
    echo "FAIL - python3 virtual env activation failed."
    exit 1
fi

# Install python packages available in requirement.txt
make init

# Install Oracle Instaclient & utPql client
python install-binaries.py

# Provide execution permission to the executables
chmod -R 777 .cli

# Verify ctest commantline is working
ctest version

echo
echo LETS SETUP SOME CONFIGURATIONS

# Configure test case path, this is the path where the test case details available
ctest config set-testrepo-location

# Configure DB Connection details
ctest config set-target

# ctest runtest command help
echo
echo ALL SET! RUN THE FOLLOWING COMMAND TO GET STARTED
ctest runtest --help
