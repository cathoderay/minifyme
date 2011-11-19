#!/usr/bin/env python

import sys
import re


def removeLineFeeds(input):
    return input.replace("\n", "")


def removeLineComments(input):
    return '\n'.join([re.sub(r'(.*)//(.*)', '\\1', line) for line in input.split('\n')])


def minifyme(input):
   return removeLineFeeds(removeLineComments(input))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print minifyme(open(sys.argv[1]).read())
    else:
        print "Usage: minifyme file.js"

