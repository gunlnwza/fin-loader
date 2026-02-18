#!/bin/bash

set -e

# Major pairs (1day)
python3 main.py alpha_vantage AUD USD 1 day
python3 main.py alpha_vantage NZD USD 1 day
python3 main.py alpha_vantage EUR USD 1 day
python3 main.py alpha_vantage GBP USD 1 day
python3 main.py alpha_vantage USD JPY 1 day
python3 main.py alpha_vantage USD CHF 1 day
python3 main.py alpha_vantage USD CAD 1 day
