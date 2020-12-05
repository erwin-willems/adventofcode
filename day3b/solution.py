#!/usr/bin/env python3
list = open("input.txt").readlines()
pattern = []


# Patern right 1, down 2
count=0
pos = 0
num = 0
for line in list:
    if (num % 2) == 0:
        pos += 1
        if pos>30:
            pos = pos - 31
        if line[pos]=="#":
            count += 1 
    num += 1        
pattern.append(count)


list.pop(0) # Skip the fist line

# Patern right 1, down 1
count = 0
pos = 0
for line in list:
    pos += 1
    if pos>30:
        pos = pos - 31
    if line[pos]=="#":
        count += 1 
pattern.append(count)

# Patern right 3, down 1
count=0
pos = 0
for line in list:
    pos += 3
    if pos>30:
        pos = pos - 31
    if line[pos]=="#":
        count += 1 
pattern.append(count)

# Patern right 5, down 1
count=0
pos = 0
for line in list:
    pos += 5
    if pos>30:
        pos = pos - 31
    if line[pos]=="#":
        count += 1 
pattern.append(count)

# Patern right 7, down 1
count=0
pos = 0
for line in list:
    pos += 7
    if pos>30:
        pos = pos - 31
    if line[pos]=="#":
        count += 1 
pattern.append(count)

count = pattern[0] * pattern[1] * pattern[2] * pattern[3] * pattern[4]
print(count)