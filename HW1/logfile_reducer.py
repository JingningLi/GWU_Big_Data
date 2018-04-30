#!/usr/bin/env python
#
# This file has been provided as a starting point. You need to modify this file.
# Reads key/value pairs from stdin, writes key/value pairs to stdout
# --- DO NOT MODIFY ANYTHING ABOVE THIS LINE ---

import sys

def main(argv):
    try:
        oldWord   = None
        oldSum    = 0
        for line in sys.stdin:
            (key,value) = line.rstrip().split('\t')
            if key!=oldWord:
                if oldWord:
                    print("{}  {}".format(oldWord,oldSum))
                oldWord = key
                oldSum  = 0
            oldSum += int(value)
    except EOFError:
        pass
    if oldWord:
        print("{}  {}".format(oldWord,oldSum))
    return None

if __name__ == "__main__":
    main(sys.argv)

