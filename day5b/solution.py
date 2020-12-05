#!/usr/bin/env python3
list = open("input.txt").readlines()

highest = 0
lowest = 806
sumofseats = 0
for line in list:
    seat = 0
    row = 0
    column = 0
    for i in range(7):
        if line[i] == "B":
            row += 2**(6-i)
    for i in range(3):
        if line[i+7] == "R":
            column += 2**(2-i)     
    seat = row * 8 + column
    if seat > highest:
        highest = seat
    if seat < lowest:
        lowest = seat
    sumofseats += seat     

sumofallseats=0
for i in range(lowest,highest+1):
   sumofallseats += i
print(f"My seat ID: {sumofallseats - sumofseats}")

