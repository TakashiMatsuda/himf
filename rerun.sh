#!/bin/bash

cd pyrsvd;
make;
python setup install;
cd ../;
python run.py
