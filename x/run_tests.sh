#!/bin/bash
## Auxiliary script to run unit-tests on Python source
#
# Call from repository root as
#   ./x/run_tests.sh
#
# NOTE Define ${UT_ARGS} as "discover" if more than one test-py file are at hand and
# all of them need to be run.
UT_ARGS="test_xkcd1930.py"
cd test/
python3 -m unittest ${UT_ARGS} -vv
