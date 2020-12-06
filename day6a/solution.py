#!/usr/bin/env python3
import string

list = open("input.txt").readlines()
# Add a newline to make sure that we catch all groups
list.append("\n")

groups = []

data = ""
for line in list:
    if line == "\n":        
        groups.append(data)
        data = ""        
    else:
        data += line.rstrip()

total=0
for group in groups:
    for character in string.ascii_lowercase:
        if character in group:
            total+=1
print(f"Total: {total}")
