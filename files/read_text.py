#!/usr/bin/env python3
"""
Simple file reading example.
"""

# Read a text file and print its content
with open('data/text/sample.txt', 'r') as file:
    content = file.read()
    print(content)