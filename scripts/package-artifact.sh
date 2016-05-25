#!/bin/bash
set -ev

rm -rf build
mkdir build
cp application.py build/
cp README.md build/
cp digest.yml build/

cd build

zip src.zip *
