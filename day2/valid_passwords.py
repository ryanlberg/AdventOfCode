from collections import defaultdict

def readFile(filepath):
    pwRange = []
    pw = []
    infile = open(filepath, 'r')
    for password in infile:
        line = password.split(':')
        pwRange.append(line[0])
        pw.append(line[1].rstrip())

    infile.close()

    return pwRange, pw


def getRange(current_letterRange):
    currentItem = current_letterRange.split(' ')
    curLetter = currentItem[1]
    r = currentItem[0].split('-')
    return [int(r[0]), int(r[1]), curLetter]



def getValidPasswords_one(letterRanges, passwords):
    validPws = 0
    for i in range(len(letterRanges)):
        if isValid(getRange(letterRanges[i]), passwords[i].strip()):
            validPws += 1
    return validPws

def isValid(letterRange, password):
    restriction = letterRange[2]
    letters = defaultdict(int)
    for letter in password:
        letters[letter] += 1
    count = letters[restriction]

    return count >= letterRange[0] and count <= letterRange[1]

def getValidPasswords_two(letterRanges, passwords):
    validPws = 0
    for i in range(len(letterRanges)):
        curRange = getRange(letterRanges[i])
        curPw = passwords[i].strip()
        if (curPw[curRange[0]-1] == curRange[2]) != (curPw[curRange[1]-1] == curRange[2]):
            validPws += 1
    return validPws 

if __name__ == "__main__":
    letterRanges, passwords = readFile('input.txt')
    print(getValidPasswords_one(letterRanges, passwords))
    print(getValidPasswords_two(letterRanges, passwords))
    