#!/usr/bin/env python

import sys


def minifyme(input):
   return input.replace("\n", "")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print minifyme(open(sys.argv[1]).read())
    else:
        print "Usage: minifyme file.js"

