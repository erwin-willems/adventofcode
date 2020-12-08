#!/usr/bin/env python3
import string

list = open("input.txt").readlines()

bags = {}
for line in list:
    words = line.split()
    if words[5] != "other":
        bags[words[0]+words[1]]=words[5]+words[6]
    if len(words)>8:
        bags[words[0]+words[1]]+=" "+words[9]+words[10]
    if len(words)>12:
        bags[words[0]+words[1]]+=" "+words[13]+words[14]
    if len(words)>16:
        bags[words[0]+words[1]]+=" "+words[17]+words[18]
count=0
baglist=[]
baglist.append('shinygold')
result=[]
while len(baglist)>0:
    for bag in bags:
        if baglist[0] in bags[bag]:
            baglist.append(bag)
            if not(bag in result):
                result.append(bag)
    baglist.pop(0)
print(f"{len(result)}")