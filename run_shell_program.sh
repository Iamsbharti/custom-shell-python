#!/bin/sh
#
# Use this script to run the program LOCALLY.
#

set -e # Exit early if any commands fail

exec pipenv run python3 -u -m app.main "$@"
