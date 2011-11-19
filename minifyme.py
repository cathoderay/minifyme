#!/usr/bin/env python

import sys
import re

from helper import compose


def remove_line_feeds(input):
    return input.replace("\n", "")


def remove_line_comments(input):
    output = "" 
    inside_string = False
    string_delimiter = ''
    inside_comment = False

    #XXX: perhaps use stack?
    for index, char in enumerate(input):
        if inside_comment:
            if char == '\n':
                inside_comment = False
                output += char
            continue

        if (not inside_string) and (char == "'" or char == '"'):
            inside_string = True
            string_delimiter = char
            output += char
            continue
        
        if (inside_string) and (char == string_delimiter):
            inside_string = False
            output += char
            continue

        if (not inside_string) and (char == '/') and \
           (index + 1 < len(input)) and (input[index + 1] == '/'):
            inside_comment = True
            continue
        output += char
    return output


def minifyme(input):
   return compose([remove_line_comments, remove_line_feeds], input)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print minifyme(open(sys.argv[1]).read())
    else:
        print "Usage: minifyme file.js"
