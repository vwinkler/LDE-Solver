#!/bin/bash
python3 prettyprint.py < $1 && echo "" && python solve.py < $1
