#!/usr/bin/env python3
list = open("input.txt").readlines()
# Add a newline to make sure that we catch all passports
list.append("\n")

passports = []
count = 0

data = ""
for line in list:
    if line == "\n":
        passports.append(data)
        data = ""        
    else:
        data = data + " " + line.rstrip()

for passport in passports:
    fields = {}
    for field in passport.split():
        item = field.split(':')
        fields[item[0]] = item[1]
    if ( 
        "byr" in fields and
        "iyr" in fields and
        "eyr" in fields and
        "hgt" in fields and
        "hcl" in fields and
        "ecl" in fields and
        "pid" in fields
    ):
        count += 1

print(f"Found {count} valid passports")