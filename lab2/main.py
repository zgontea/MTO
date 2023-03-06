#!/usr/bin/env python3

import sys

def my_printf(format_string, param):
    #print(format_string)
    shouldDo = 0
    stringMaxLen = 0
    for idx in range(0, len(format_string)):
        currCharacter = format_string[idx]
        if shouldDo == 0:
            if currCharacter == '#' and format_string[idx + 1] == 'k':
                print(param.swapcase(), end = "")
                shouldDo += 1
            elif currCharacter == '#' and format_string[idx + 1] == '.' and format_string[idx + 2].isnumeric() and format_string[idx + 3] == 'k':
                stringMaxLen = int(format_string[idx + 2])
                print(param.swapcase()[:stringMaxLen], end = "")
                shouldDo += 3
            else:
                print(currCharacter, end = "")
        else:
            if shouldDo > 0:
                shouldDo -= 1
            else:
                shouldDo = 0
    print("")

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(),data[i + 1].rstrip())
