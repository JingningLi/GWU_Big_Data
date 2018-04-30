#!/usr/bin/env python
#
# This file has been provided as a starting point. You need to modify this file.
# Reads whole lines stdin; writes key/value pairs to stdout
# http://docs.aws.amazon.com/emr/latest/ReleaseGuide/UseCase_Streaming.html
# --- DO NOT MODIFY ANYTHING ABOVE THIS LINE ---

import sys
import re
import datetime

prog = re.compile('\[[0-9][0-9]\/[A-Z][a-z][a-z]\/[0-9][0-9][0-9][0-9]')

def main(argv):
    try:
        for line in sys.stdin:
            line = line.rstrip()
            words = line.split()
            for word in words:
                if prog.match(word):
                    word = word[4:12]
                    word = datetime.datetime.strptime(word, '%b/%Y')
                    word = word.strftime('%Y-%m')
                    print( word + "\t" + "1")
    except EOFError:
        return None


if __name__ == "__main__":
    main(sys.argv)
