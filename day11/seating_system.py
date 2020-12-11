def readFile(input):
    out = []
    with open(input, 'r') as infile:
        out = list(map(list, infile.read().splitlines()))
    
    return out


class ferry():

    def __init__(self, seatingChart):
        self.currentSeating = seatingChart
        self.width = len(seatingChart[0])
        self.height = len(seatingChart)
        self.updateSeating = [["0" for x in range(self.width)] for y in range(self.height)]
        self.updated = False
        
    
    def isValid(self, row, col):
        return row >= 0 and row < self.height and col >= 0 and col < self.width

    def __str__(self):
        out = ""
        for x in self.currentSeating:
            out += ''.join(x) + "\n"
        return out

    def updateCurrentSeating(self):
        self.updated = False
        for row in range(self.height):
            for column in range(self.width):
                previous = self.currentSeating[row][column]
                self.updateSeating[row][column] = self.updateSeat(row, column)
                if not self.updateSeating[row][column] == previous:
                    self.updated = True
        self.currentSeating = self.updateSeating.copy()
        self.updateSeating = [["0" for x in range(self.width)] for y in range(self.height)]

    def updateSeat(self, row, col):
        currentItem = self.currentSeating[row][col]
        around = [[0, 1],[0, -1],[1, 0],[-1, 0],[1, 1],[1, -1],[-1, 1],[-1, -1]]
        if currentItem == '.':
            return '.'
        elif currentItem == 'L':
            for place in around:
                nextrow = place[0] + row
                nextcol = place[1] + col
                if self.isValid(nextrow, nextcol) and self.currentSeating[nextrow][nextcol] == '#':
                    return 'L'
            return '#'
        elif currentItem == '#':
            occupiedAround = 0
            for place in around:
                nextrow = place[0] + row
                nextcol = place[1] + col
                if self.isValid(nextrow, nextcol) and self.currentSeating[nextrow][nextcol] == '#':       
                    occupiedAround += 1
            
            if occupiedAround > 3:
                return 'L'
            return '#'

    def newUpdateCurrentSeating(self):
        self.updated = False
        for row in range(self.height):
            for column in range(self.width):
                previous = self.currentSeating[row][column]
                self.updateSeating[row][column] = self.newUpdateSeat(row, column)
                if not self.updateSeating[row][column] == previous:
                    self.updated = True
        self.currentSeating = self.updateSeating.copy()
        self.updateSeating = [["0" for x in range(self.width)] for y in range(self.height)]

    def newUpdateSeat(self, row, col):
        currentItem = self.currentSeating[row][col]
        around = [[0, 1],[0, -1],[1, 0],[-1, 0],[1, 1],[1, -1],[-1, 1],[-1, -1]]
       
        if currentItem == '.':
            return '.'
        elif currentItem == 'L':
            count = 0
            for direction in around:
                count += self.updateHelper(row, col, direction)
            if count == 0:
                return '#'
            return 'L'
        else:
            count = 0
            for direction in around:
                count += self.updateHelper(row, col, direction)
            if count > 4:
                return 'L'
            return '#'

    def updateHelper(self, row, col, direction):
        newrow = direction[0] + row
        newcol = direction[1] + col
        if not self.isValid(newrow, newcol):
            return 0
        elif self.currentSeating[newrow][newcol] == 'L':
            return 0
        elif self.currentSeating[newrow][newcol] == '#':
            return 1
        return self.updateHelper(newrow, newcol, direction)

    def runSim(self):
        count = 0
        self.updated = True
        while self.updated:
            
            self.updateCurrentSeating() 
            count += 1
            
        return count

   
    def runNewSim(self):
        count = 0
        self.updated = True
        while self.updated:
            
            self.newUpdateCurrentSeating() 
            count += 1
            
        return count

    def countOccupied(self):
        occupied = 0
        for row in range(self.height):
            for column in range(self.width):
                if self.currentSeating[row][column] == "#":
                    occupied += 1
        return occupied

    

def main():
    seating = readFile('input.txt')
    fer = ferry(seating)    
    #print(fer.runSim())
    #print(fer.countOccupied())
    print(fer.runNewSim())
    print(fer.countOccupied())

if __name__ == "__main__":
    main()
