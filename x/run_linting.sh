#!/bin/bash
## Run Code Linting Using Pylint
#
#  Lint the relevant Python files using Pylint. Linting options are defined in
#    config/pylintrc
#
#  Usage:
#    $ ./x/run_linting.sh Runs linting of all relevant Python source files.
#    $ ./x/run_linting.sh <path_to_filename> Runs specific file only
#
CONFIG_FILE="config/pylintrc"
OPTIONS="--rcfile ${CONFIG_FILE}"

if [ "$1" == "" ]; then
  declare -a SOURCE_FILES=(
    "xkcd1930.py"
    "test/test_xkcd1930.py"
  )
else
  declare -a SOURCE_FILES=("$1")
fi

for src in ${SOURCE_FILES[@]}; do
  echo "### Linting $src ###"
  pylint $OPTIONS $src
done
