#!/usr/bin/env python3
list = open("input.txt").readlines()
valid = 0
for line in list:
  values = line.split()
  range = values[0].split('-')
  min = int(range[0])
  max = int(range[1])
  char = values[1][0]
  count = values[2].count(char)
  if count>=min and count<=max:
    valid += 1
print(f"Valid passwords: {valid}")
