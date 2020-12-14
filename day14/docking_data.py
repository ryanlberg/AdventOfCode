import re
from collections import defaultdict

def readFile(input):
    out = []
    with open(input, 'r') as infile:
        out = list(infile.read().splitlines())
   
    return out

def parseProgram(program):
    progorder = []
    for instruction in program:
        operation, value = instruction.split(' = ')
       
        if operation == 'mask':
            progorder.append([operation, value])
        else:
            progorder.append(['mem', parseMem(operation, value)])
    return progorder

def parseMem(operation, value):
    pattern = re.compile(r"\d+")
    loc = pattern.findall(operation)[0]
   
    return [int(loc), int(value)]


def runProgram(program, number=1):
    memory = defaultdict(int)
    currentMask = program[0][1]
    for i in range(1, len(program)):
        task, item = program[i]
        if task == 'mask':
            currentMask = item
        elif number == 1:
            memory[item[0]] = updateMemory(currentMask, item[1])
        else:
            addresses = getNewAddresses(currentMask, item[0])
            for address in addresses:
                memory[address] = item[1]

    return getMemorySum(memory)

def updateMemory(mask, number):
    maskedNumber = ''
    numberBin = '{:036b}'.format(number)
    for i, number in enumerate(mask):
        if not number == 'X':
            maskedNumber += number
        else:
            maskedNumber += numberBin[i]
    return int(maskedNumber, 2)
    
def getNewAddresses(mask, address):
    maskedAddress = getMaskedAddress(mask, address)
    addresslist = []
    needed = ['0', '1']
    def makeList(i, currentAddress):
        if i >= len(maskedAddress):
            addresslist.append(currentAddress)
        else:
            if maskedAddress[i] == 'X':
                for x in needed:
                    makeList(i+1, currentAddress + x)
            else:
                makeList(i+1, currentAddress + maskedAddress[i])
    makeList(0, "")
    return addresslist

def getMemorySum(memory):
    total = 0
    for item in memory.keys():
        total += memory[item]

    return total

def getMaskedAddress(mask, address):
    out = ""
    addressBin = '{:036b}'.format(address)
    for i, number in enumerate(mask):
        if number == 'X' or number == '1':
            out += number
        else:
            out += addressBin[i]
    return out



def main():
    program = readFile('input.txt')
    prog = parseProgram(program)
    out = runProgram(prog, 1)
    out2 = runProgram(prog, 2)
    print(out)
    print(out2)

if __name__ == "__main__":
    main()