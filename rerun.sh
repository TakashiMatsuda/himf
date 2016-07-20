#!/bin/bash

cd pyrsvd;
make;
cd ../;
python himf.py 10 0.01 10;
