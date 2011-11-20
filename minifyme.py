#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

from helper import compose, read_input, write_output


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
        #end of a comment
        if inside_comment:
            if (input [index - 1] != '\\' and
                char == '\n'):
                inside_comment = False
                output += char
            continue

        #end of regex
        if inside_regex:
            if (input[index - 1] != '\\' and
                char == '/'):
                inside_regex = False
            output += char
            continue
        
        #end of string
        if inside_string:
            if (input[index -1] != '\\' and
                char == string_delimiter):
                inside_string = False
            output += char
            continue

        #start of regex
        if (char == '/' and
            index + 1 < len(input) and
            (input[index + 1] != '/') and 
             input[index + 1] != '*'):
            inside_regex = True
            output += char
            continue

        #start of string
        if (char == "'" or char == '"'):
            inside_string = True
            string_delimiter = char
            output += char
            continue

        #start of a line comment
        if char == '/':
            if (index + 1 < len(input) and
                input[index + 1] == '/'):
                inside_comment = True
                continue

        #otherwise
        output += char
    return output


#XXX: duplicated code! 
def remove_multiline_comments(input):
    output = "" 
    inside_string = False
    string_delimiter = ''
    inside_line_comment = False
    inside_multiline_comment = False
    inside_regex = False
    not_output_next = False

    #XXX: perhaps use stack?
    for index, char in enumerate(input):
        if not_output_next:
            not_output_next = False
            continue

        #end of line comment
        if inside_line_comment:
            if (input [index - 1] != '\\' and
                char == '\n'):
                inside_line_comment = False
            output += char
            continue

        #end of a multiline comment
        if inside_multiline_comment:
            if (input[index - 1] != '\\' and
                char == '*' and
                index + 1 < len(input) and
                input[index + 1] == "/"):
                inside_multiline_comment = False
                not_output_next = True
            continue

        #end of regex
        if inside_regex:
            if (input[index - 1] != '\\' and
                char == '/'):
                inside_regex = False
            output += char
            continue
        
        #end of string
        if inside_string:
            if (input[index -1] != '\\' and
                char == string_delimiter):
                inside_string = False
            output += char
            continue

        #start of regex, line comment or multiline comment
        if char == '/':
            if index + 1 < len(input):
               if input[index + 1] == '/':
                   inside_line_comment = True
                   output += char
                   continue
               elif input[index + 1] == '*':
                   inside_multiline_comment = True
                   continue
               else:
                   inside_regex = True
                   output += char
                   continue

        #start of string
        if (char == "'" or char == '"'):
            inside_string = True
            string_delimiter = char
            output += char
            continue

        #otherwise
        output += char
    return output


def minifyme(input):
   return compose([remove_multiline_comments,
                   remove_line_comments,
                   remove_line_feeds], input)


def print_statistics(input, output):
    input_size = len(input)
    output_size = len(output)
    removed = 100*(input_size - output_size)/float(input_size)
    print """
Statistics
==========    
    Original file size: %s bytes  
    Minified file size: %s bytes

    Removed: %s%% bytes
""" % (input_size, output_size, removed)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            filename = sys.argv[1]
            if os.path.getsize(filename) == 0: 
                print "C'mon, don't bug me! Empty file?!"
                exit(-1)

            input = read_input(filename)

            output = minifyme(input)

            output_filename = "%s.min.js" % sys.argv[1][:-3]
            write_output(output_filename, output)

            print_statistics(input, output)
            print "File %s written." % output_filename
        except Exception, e:
            print "Something wrong."
            print e
    else:
        print "Usage: minifyme file.js"
