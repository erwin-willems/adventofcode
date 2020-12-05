#!/usr/bin/env python3
list = open("input.txt").readlines()

count = 0
pos = 0
# Skip first line
list.pop(0)
for line in list:
    pos += 3
    if pos>30:
        pos = pos - 31
    if line[pos]=="#":
        count += 1 
print(count)