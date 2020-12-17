
def readFile(input):
    out = []
    with open(input, 'r') as infile:
        out = list(infile.read().split('\n'))
    return out

class ConwayCube():
    
    def __init__(self, startstate):
        self.currentstate = [[startstate]]
        self.x = len(startstate) 
        self.y = len(startstate[0])
        self.z = 1
        self.w = 1
        self.around = []
        for w in range(-1, 2):
            for x in range(-1, 2):
                for y in range(-1, 2):
                    for z in range(-1, 2):
                        if not (x == 0 and y == 0 and z == 0 and w == 0):
                            self.around.append([x, y, z, w])

    def expand(self):
        self.x += 2
        self.y += 2
        self.z += 2
        self.w += 2
        newstate = [[[["." for x in range(self.x)] for y in range(self.y)] for z in range(self.z)] for w in range(self.w)]
        for w in range(1, self.w-1):
            for z in range(1, self.z-1):
                for x in range(1, self.x-1):
                    for y in range(1, self.y-1):
                        newstate[w][z][x][y] = self.currentstate[w-1][z-1][x-1][y-1]
        self.currentstate = newstate


    def isValid(self, curx, cury, curz, curw):
        return curx >= 0 and curx < self.x and cury >= 0 and cury < self.y and curz >= 0 and curz < self.z and curw >= 0 and curw < self.w


    def proliferate(self):
        newstate = [[[['.' for x in range(self.x)] for y in range(self.y)] for z in range(self.z)] for w in range(self.w)]
        for w in range(self.w):
            for z in range(self.z):
                for x in range(self.x):
                    for y in range(self.y):
                        count = 0
                        for a,b,c,d in self.around:
                            nextw = w + a
                            nextz = z + b
                            nextx = x + c
                            nexty = y + d
                            if self.isValid(nextx, nexty, nextz, nextw) and self.currentstate[nextw][nextz][nextx][nexty] == "#":
                                count += 1
                        if self.currentstate[w][z][x][y] == "#":
                            if count == 2 or count == 3:
                                newstate[w][z][x][y] = "#"
                        else:
                            if count == 3:
                                newstate[w][z][x][y] = "#"

        self.currentstate = newstate

    def sim(self, amount):
        for x in range(amount):
            self.expand()
            self.proliferate()

    def countActiveCubes(self):
        active = 0
        for w in range(self.w):
            for z in range(self.z):
                for x in range(self.x):
                    for y in range(self.y):
                        if self.currentstate[w][z][x][y] == "#":
                            active += 1
        return active

    def __str__(self):
        out = ""
        for w in range(self.w):
            for z in range(self.z):
                for x in range(self.x):
                    currow = ""
                    for y in range(self.y):
                        currow += self.currentstate[w][z][x][y]
                    currow += "\n"
                    out += currow
                out += "\n"
        return out

def main():
    board = readFile('input.txt')
    cube = ConwayCube(board)
    cube.sim(6)
    print(cube.countActiveCubes())

if __name__ == "__main__":
    main()