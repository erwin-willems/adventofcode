#!/usr/bin/env python3
import time

list = open("input.txt").readlines()

accumulator = 0
step = 0
done = []
while step<len(list):
    line = list[step]
    instruction = line.split()[0]
    data = int(line.split()[1])
    if not step in done:
        done.append(step)
    else:
        break # Loop detected
    if instruction == "nop":
        step += 1
    if instruction == "acc":
        accumulator += data
        step += 1
    if instruction == "jmp":
        step += data
print(f"accumulator: {accumulator}")
