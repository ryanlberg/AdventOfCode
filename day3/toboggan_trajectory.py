
def readFile(input):
    out = []
    infile = open(input, 'r')
    for line in infile:
        out.append(list(line.strip()))
    
    infile.close()

    return out

def treeEncounter(tobogganMap, right, down):
    RIGHT = right
    DOWN = down
    acrosslen = len(tobogganMap[0])
    downlen = len(tobogganMap)

    starti = 0
    startj = 0

    treeCount = 0
    while starti < downlen:
        if tobogganMap[starti][startj] == '#':
            treeCount += 1
        startj = (startj + RIGHT) % acrosslen
        starti += DOWN

    return treeCount


def minimizeProb(tobogganMap):
    traversals = [[1,1], [3,1], [5, 1], [7,1], [1, 2]]
    multiplications = 1
    for route in traversals:
        multiplications *= treeEncounter(tobogganMap, route[0], route[1])
    
    return multiplications


if __name__ == "__main__":
    area = readFile('input.txt')
    print(treeEncounter(area, 3, 1))
    print(minimizeProb(area))
