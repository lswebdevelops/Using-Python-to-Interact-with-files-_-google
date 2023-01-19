#!/usr/bin/env python3

import sys
# for each of the lines of the file, to delete the new line caracter at the end
# the the capitalize method to make the first letter of the line uppercase
for line in sys.stdin:
    print(line.strip().capitalize())

