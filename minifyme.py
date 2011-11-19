#!/usr/bin/env python

import sys
import re

from helper import compose


def remove_line_feeds(input):
    return input.replace("\n", "")


def remove_line_comments(input):
    return '\n'.join([re.sub(r'(.*)//(.*)', '\\1', line) for line in input.split('\n')])


def minifyme(input):
   return compose([remove_line_comments, remove_line_feeds], input)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print minifyme(open(sys.argv[1]).read())
    else:
        print "Usage: minifyme file.js"
