#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    newLine = line[0:18]+line[20:]
    print(newLine.split("\n")[0])
