#!/bin/bash
set -ev

###########################################################
# this is the simple src artifact bundler
# Only the code needed to run the application in a Prod or
# Prod-like environment is included
###########################################################

rm -rf build
mkdir build
cp application.py build/
cp README.md build/

cd build

zip src.zip *

aws s3 ls
