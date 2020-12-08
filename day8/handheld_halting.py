def readFile(input):
    out = []
    infile = open(input, 'r')
    for line in infile:
        out.append(line.strip())
    
    infile.close()

    return out

def runProgram(instructionlist):
    acc = 0
    pc = 0
    seen = set()
    while pc < len(instructionlist) and  pc not in seen:
        seen.add(pc)
        acc, pc = operate(instructionlist[pc], acc, pc)

    return acc, pc

def operate(instruction, acc, pc):
    
    op, value = instruction.split(' ')
    value = int(value)
    if op == 'nop':
        return acc, pc+1
    elif op == 'acc':
        return acc + value, pc + 1
    elif op == 'jmp':
        return acc, pc + value
    return acc, pc


def bruteForce(instructions):
    for i, instruction in enumerate(instructions):
        if instruction[:3] == "nop":
            instructions[i] = "jmp" + instruction[3:]
            acc, pc = runProgram(instructions)
           
            if pc == len(instructions):
                return acc
            else:
                instructions[i] = 'nop' + instruction[3:]
        elif instruction[:3] == 'jmp':
            instructions[i] = 'nop' + instruction[3:]
            acc, pc = runProgram(instructions)
           
            if pc == len(instructions):
                return acc
            else:
                instructions[i] = 'jmp' + instruction[3:]
    return 0


def main():
    instructions = readFile('input.txt')
    print(runProgram(instructions)[0])
    print(bruteForce(instructions))

if __name__ == "__main__":
    main()