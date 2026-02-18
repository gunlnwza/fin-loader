#!/bin/bash

set -e

# Gold (1day, 1hour, 5min)
python3 main.py twelve_data XAU USD 1 day
python3 main.py twelve_data XAU USD 1 hour
python3 main.py twelve_data XAU USD 5 min

# Major pairs (1hour, 5min)
python3 main.py twelve_data AUD USD 1 hour
python3 main.py twelve_data NZD USD 1 hour
python3 main.py twelve_data EUR USD 1 hour
python3 main.py twelve_data GBP USD 1 hour
python3 main.py twelve_data USD JPY 1 hour
python3 main.py twelve_data USD CHF 1 hour
python3 main.py twelve_data USD CAD 1 hour

python3 main.py twelve_data AUD USD 5 min
python3 main.py twelve_data NZD USD 5 min
python3 main.py twelve_data EUR USD 5 min
python3 main.py twelve_data GBP USD 5 min
python3 main.py twelve_data USD JPY 5 min
python3 main.py twelve_data USD CHF 5 min
python3 main.py twelve_data USD CAD 5 min
