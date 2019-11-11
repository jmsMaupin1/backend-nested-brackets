#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: Takes in a file and checks if each line has proper bracket nesting.

with help of Piero Madar and Derek Barnes
"""
__author__ = "jmsMaupin1"

import sys
import re

def write_to_file(filename, lines):
    file = open(filename, 'w')
    for line in lines:
        file.write(line + "\n")
    file.close()


def process_lines(filename):
    lines = []
    with open('input.txt') as text_file:
        lines = [line for line in text_file]

    write_to_file("output.txt", map(validate, lines))


def validate(line):
    brackets = {
       "(": ")",
       "(*": "*)",
       "[": "]",
       "{": "}",
       "<": ">",
   }
    stack = []
    count = 0
    while line:
        token = line[0]
        if line.startswith('(*'):
            token = '(*'
        elif line.startswith('*)'):
            token = '*)'

        count += 1

        if token in brackets:
            stack.append(token)
        elif token in brackets.values():
            if brackets[stack.pop()] != token:
                return 'NO %d' % count

        line = line[len(token):]

    if len(stack) > 0:
        return 'NO %d' % count

    return 'YES'
        

def main(args):
    if len(args) != 2:
        print('usage: python nested.py file-to-read')
        sys.exit(1)

    process_lines(args[1])


if __name__ == '__main__':
    main(sys.argv)
