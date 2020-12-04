from passport import Passport
from collections import defaultdict

def readFile(input):
    entries = []
    infile = open(input, 'r')
    curpass = ""
    for line in infile:
        if line == "\n":
            entries.append(curpass.rstrip())
            curpass = ""
        else:
            line = line.replace("\n", " ")
            curpass += line
    entries.append(curpass)

    infile.close()

    return entries


def getpopulatedPassports(entries):
    passports = []

    for entry in entries:
        separated = entry.split(' ')
        currentEntry = defaultdict(str)
        for field in separated:
            key, value = field.split(':')
            currentEntry[key] = value

        passport = Passport(currentEntry['byr'], 
                            currentEntry['iyr'],
                            currentEntry['eyr'],
                            currentEntry['hgt'],
                            currentEntry['hcl'],
                            currentEntry['ecl'],
                            currentEntry['pid'],
                            currentEntry['cid'])
        
        passports.append(passport)
    
    return passports


def getValidPassportCount(passports):
    valid = 0
    for passport in passports:
        if passport.isValidOne():
            valid += 1
    return valid

def getUpdatedValidPassportCount(passports):
    valid = 0
    for passport in passports:
        if passport.isValidTwo():
            valid += 1
    return valid

if __name__ == "__main__":
    entries = readFile('input.txt')
    passports = getpopulatedPassports(entries)
    print(getValidPassportCount(passports))
    print(getUpdatedValidPassportCount(passports))
