from collections import defaultdict

def readFile(input):
    out = []
    with open(input, 'r') as inFile:
        out = inFile.read().split("\n")
    return out

class  Lobby():

    def __init__(self):
        self.blacktiles = set()
    

    def flipTiles(self, instructions, i, du, de):
      
        if i < len(instructions):
            if instructions[i] == "s" or instructions[i] == "n":
                newdu, newde = self.getValues(instructions[i:i+2], du, de)
                self.flipTiles(instructions, i+2, newdu, newde)
            else:
                newdu, newde = self.getValues(instructions[i], du, de) 
                self.flipTiles(instructions, i+1, newdu, newde)
        else:
            loc = (du, de)
            if loc in self.blacktiles:
                self.blacktiles.remove(loc)
            else:
                self.blacktiles.add(loc)

    def getValues(self, instruction, du, de):
        if instruction == "e":
            return du, de+1
        elif instruction == "se": 
            return du-1, de+0.5
        elif instruction == "sw":
            return du-1, de-0.5
        elif instruction == "w":
            return du, de-1
        elif instruction == "ne":
            return du+1, de+0.5
        elif instruction == "nw":
            return du+1, de-0.5

    def shimmer(self, days):
        around = [[0, 1], [-1, 0.5], [-1, -0.5], [0, -1], [1, 0.5], [1, -0.5]]
        for i in range(days):
            self.change(around)
            print(str(i+1) + ":", len(self.blacktiles))
        
    
    def change(self, around):
        seen = set()
        frontier = []
        newwhite = set()
        newblack = set()

        for tile in self.blacktiles:
            frontier.append(tile)
            seen.add(tile)

        while frontier:
            cur = frontier.pop()
            count = 0
            potentials = []
            for n, e in around:
                nextn = cur[0] + n
                nexte = cur[1] + e
                if (nextn, nexte) not in self.blacktiles:
                    if (nextn, nexte) not in seen:
                        potentials.append((nextn, nexte))
                else:
                    count += 1
            if cur in self.blacktiles:
                for tile in potentials:
                    if not tile in seen:
                        frontier.append(tile)
                        seen.add(tile)
                if count == 0 or count > 2:
                    newwhite.add(cur)
            else:
                if count > 0:
                    for tile in potentials:
                        if tile not in seen:
                            frontier.append(tile)
                            seen.add(tile)
                if count == 2:
                    newblack.add(cur)

        for tile in newwhite:
            self.blacktiles.remove(tile)
        
        for tile in newblack:
            self.blacktiles.add(tile)

def main():
    swaplist = readFile("input.txt")
    lobby = Lobby()
    for instruction in swaplist:
        lobby.flipTiles(instruction, 0, 0.0, 0.0)
    print(len(lobby.blacktiles))
    lobby.shimmer(100)


if __name__ == "__main__":
    main()