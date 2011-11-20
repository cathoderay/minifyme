#!/usr/bin/env python

import sys

from helper import compose


def remove_line_feeds(input):
    return input.replace("\n", "")


def remove_line_comments(input):
    output = "" 
    inside_string = False
    string_delimiter = ''
    inside_comment = False
    inside_regex = False

    #XXX: perhaps use stack?
    for index, char in enumerate(input):
        if inside_comment:
            if char == '\n':
                inside_comment = False
                output += char
            continue

        if inside_regex:
            if char == '/':
                inside_regex = False
                output += char
            continue

        if (not inside_regex) and (not inside_string) and (char == '/') and \
            (index + 1 < len(input)) and (input[index + 1] != '/'):
            inside_regex = True
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

#XXX: duplicated code! 
def remove_multiline_comments(input):
    output = "" 
    inside_string = False
    string_delimiter = ''
    inside_comment = False
    not_output = False

    #XXX: perhaps use stack?
    for index, char in enumerate(input):
        if not_output:
            not_output = False
            continue

        if inside_comment:
            if char == '*' and index + 1 < len(input) and input[index + 1] == '/':
                inside_comment = False
                not_output = True
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
           (index + 1 < len(input)) and (input[index + 1] == '*'):
            inside_comment = True
            continue
        output += char
    return output


def minifyme(input):
   return compose([remove_multiline_comments, \
                   remove_line_comments, \
                   remove_line_feeds], input)


def print_statistics(input, output):
    input_size = len(input)
    output_size = len(output)
    removed = (input_size - output_size)/float(input_size)
    print """
Statistics
==========    
    Original file size: %s bytes  
    Minified file size: %s bytes

    Removed bytes: %.4s%% 
""" % (input_size, output_size, removed)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            input = open(sys.argv[1]).read()
            output = minifyme(input)
            output_filename = "%s.min.js" % sys.argv[1][:-3]
            f = open(output_filename, 'w+')
            f.write(output)
            print_statistics(input, output)
            print "File %s written." % output_filename
        except:
            print "Something wrong."
    else:
        print "Usage: minifyme file.js"
