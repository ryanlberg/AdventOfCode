def readFile(input):
    out = []
    infile = open(input, 'r')
    for line in infile:
        out.append(int(line.strip()))
    
    infile.close()

    return out


def isValid(input, start, end, tofind):
    for value in range(start, end):
        for nextValue in range(start+1, end):
            if input[value] + input[nextValue] == tofind:
                return True
    
    return False

def getFirstInvalid(input, preambleSize):
    for entry in range(preambleSize, len(input)):
        if not isValid(input, entry-preambleSize, entry, input[entry]):
            return input[entry]
    return -1


def getEncryptionWeakness(input, value):
    start = 0
    end = 0
    currentsum = 0
    while end < len(input):
        while end < len(input) and currentsum < value:
            currentsum += input[end]
            end += 1
        
        if currentsum == value:
            return getsum(input, start, end-1)

        while start < end and currentsum > value:
            currentsum -= input[start]
            start += 1

    return -1 


def getsum(input, start, end):
    curlist = input[start:end+1]
    return min(curlist) + max(curlist)

def main():
    data = readFile('input.txt')
    invalid = getFirstInvalid(data, 25)
    print('1: ' + str(invalid))
    weakness = getEncryptionWeakness(data, invalid)
    print('2: ' + str(weakness))

if __name__ == "__main__":
    main()