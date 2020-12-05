#!/usr/bin/env python3
list = open("input.txt").readlines()
valid = 0
for line in list:
  values = line.split()
  range = values[0].split('-')
  pos1 = int(range[0])-1
  pos2 = int(range[1])-1
  char = values[1][0]
  password = values[2]
  if (
    password[pos1]==char or password[pos2]==char
  ) and ((  
    password[pos1]==char and password[pos2]!=char
  ) or (
    password[pos1]!=char and password[pos2]==char
  )):
    valid += 1
print(f"Valid passwords {valid}")
