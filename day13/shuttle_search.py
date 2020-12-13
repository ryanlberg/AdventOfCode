import math
def readFile(input):
    out = []
    with open(input, 'r') as infile:
        out = list(infile.read().splitlines())
    return out


def lcm(a, b):
    return abs(a*b)// math.gcd(a, b)

def getlcm(l):
    x = l[0]
    for y in range(1, len(l)):
        x = lcm(x, l[y])
    return x

def getEarliestTime(schedule):
    canleave = int(schedule[0])
    newSched = schedule[1].split(',')
    mindif = float('inf')
    minid = 0
    for departTime in newSched:
        if not departTime == 'x':
            deparTime = int(departTime)
            towait = deparTime - (canleave % deparTime)
            if towait < mindif:
                mindif = towait
                minid = deparTime
    
    return mindif * minid

def solveContest(schedule):
    needed = schedule[1].split(',')
    reallyNeeded = []
    for i, item in enumerate(needed):
        if not item == 'x':
            reallyNeeded.append([int(item), i])
    
    start = 1 
    counter = 1
    cando = False
    seen = 2
    while seen <= len(reallyNeeded):
       
        cando = True
        for x in reallyNeeded[:seen]:
            
            if not inRightPosition(start, x):
                cando = False
                break
        if cando:
            counter = getlcm([x[0] for x in reallyNeeded[:seen]])
            seen += 1
        start += counter
    
    return start - counter

def inRightPosition(start, bus):
    return ((start+bus[1])%bus[0]) == 0

def main():
    schedule = readFile('input.txt')
    print(getEarliestTime(schedule))
    print(solveContest(schedule))


if __name__ == "__main__":
    main()