#!/usr/bin/env python3
import time

list = open("input.txt").readlines()

accumulator = 0
step = 0
done = []
bugfix = -1
while step<len(list):
    line = list[step]
    instruction = line.split()[0]
    data = int(line.split()[1])
    if instruction == "nop":
        if bugfix == step:
            step += data # Act like a jmp
        else:
            step += 1
    if instruction == "acc":
        accumulator += data
        step += 1
    if instruction == "jmp":
        if bugfix == step:
            step += 1 # Act like a nop
        else:    
            step += data
    if not step in done:
        done.append(step)
    else:
        accumulator = 0
        step = 0
        done = []
        bugfix += 1
print(f"accumulator: {accumulator}. Bug was on line: {bugfix}")