#!/bin/bash

set -e

# Major pairs (1day)
python3 main.py massive AUD USD 1 day
python3 main.py massive NZD USD 1 day
python3 main.py massive EUR USD 1 day
python3 main.py massive GBP USD 1 day
python3 main.py massive USD JPY 1 day
python3 main.py massive USD CHF 1 day
python3 main.py massive USD CAD 1 day
