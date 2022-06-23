#!/bin/bash

###########################################################################
# Generate documentation and place it at desired location
#
# Generate documentation using pydoc and move it to the doc/ subdirectory.
# For this to work as intended, call it from the repository root as
#   ./x/generate_docu.sh
###########################################################################
DEST="./doc/"
MODULENAME="xkcd1930"
pydoc -w ${MODULENAME}
mv *.html ${DEST}
