#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    newLine = re.split(",", line)
    finishLine = ""
    count = 0
    for word in newLine:
        if count == 6:
            word = word[2:]
        count = count + 1
        finishLine += word
    print(finishLine.split("\n")[0])
