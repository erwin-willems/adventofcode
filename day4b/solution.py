#!/usr/bin/python3
import re

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
        if (
            int(fields['byr']) >= 1920 and int(fields['byr']) <= 2002 and
            int(fields['iyr']) >= 2010 and int(fields['iyr']) <= 2020 and
            int(fields['eyr']) >= 2020 and int(fields['eyr']) <= 2030 and
            (
                (fields['hgt'].endswith('cm') and int(fields['hgt'][0:-2]) >= 150 and int(fields['hgt'][0:-2]) <= 193)
                or
                (fields['hgt'].endswith('in') and int(fields['hgt'][0:-2]) >= 59 and int(fields['hgt'][0:-2]) <= 76)
            ) and
            fields['hcl'].startswith('#') and re.match("\#[0-9a-f]{6}",fields['hcl']) and
            (
                fields['ecl'] == "amb" or
                fields['ecl'] == "blu" or
                fields['ecl'] == "brn" or
                fields['ecl'] == "gry" or
                fields['ecl'] == "grn" or
                fields['ecl'] == "hzl" or
                fields['ecl'] == "oth"
            ) and
            len(fields['pid']) == 9 and re.match("\d{9}",fields['pid'])
        ):
            count += 1

print(f"Found {count} valid passports")
