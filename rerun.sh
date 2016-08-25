#!/bin/bash

cd pyrsvd;
make;
python setup.py install;
cd ../;
python run.py