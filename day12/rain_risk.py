def readFile(input):
    out = []
    with open(input, 'r') as infile:
        out = list(infile.read().splitlines())
    return out

class Ship():

    def __init__(self):
        self.directions = [0, 0, 0, 0] #north, east, south, west... just use an enum.
        self.north = 0
        self.east = 1
        self.south = 2
        self.west = 3 
        self.direction = 1
        self.waypoint = [1, 10, 0, 0]
        self.directionways = set(['N', 'S', 'E', 'W', 'F'])
    
    def move(self, instruction):
        
        action, amount = self.parse(instruction)
        if action in self.directionways:
            self.makeMovement(action, amount)
        else:
            self.rotate(action, amount)

    def parse(self, instruction):
        return instruction[0], int(instruction[1:])

    def makeMovement(self, action, amount):
        if action == 'N':
            self.directions[0] += amount
        elif action == 'E':
            self.directions[1] += amount
        elif action == 'S':
            self.directions[2] += amount
        elif action == 'W':
            self.directions[3] += amount
        else:
            self.directions[self.direction] += amount

    
    def rotate(self, way, amount):
        if self.direction == 0:
            if amount == 180:
                self.direction = 2
            elif way == "R":
                if amount == 90:
                    self.direction = 1
                else:
                    self.direction = 3
            else:
                if amount == 90:
                    self.direction = 3
                else:
                    self.direction = 1

        elif self.direction == 2:
            if amount == 180:
                self.direction = 0
            elif way == "R":
                if amount == 90:
                    self.direction = 3
                else:
                    self.direction = 1
            else:
                if amount == 90:
                    self.direction = 1
                else:
                    self.direction = 3

        elif self.direction == 1:
            if amount == 180:
                self.direction = 3
            elif way == "R":
                if amount == 90:
                    self.direction = 2
                else:
                    self.direction = 0
            else:
                if amount == 90:
                    self.direction = 0
                else:
                    self.direction = 2
        
        elif self.direction == 3:
            if amount == 180:
                self.direction = 1
            elif way == "R":
                if amount == 90:
                    self.direction = 0
                else:
                    self.direction = 2
            else:
                if amount == 90:
                    self.direction = 2
                else:
                    self.direction = 0

    def moveTwo(self, instruction):
        action, amount = self.parse(instruction)
        if action in self.directionways:
            self.makeMovementTwo(action, amount)
        else:
            self.rotateTwo(action, amount)

    def makeMovementTwo(self, action, amount):
        if action == 'N':
            self.waypoint[self.north] += amount
        elif action == 'E':
            self.waypoint[self.east] += amount
        elif action == 'S':
            self.waypoint[self.south] += amount
        elif action == 'W':
            self.waypoint[self.west] += amount
        else:
            for x in range(len(self.waypoint)):
                self.directions[x] += amount * self.waypoint[x]
        
    def rotateTwo(self, action, amount):
        direction = self.waypoint + self.waypoint

        if action == 'L':
            if amount == 90:
                self.waypoint = direction[1:5]

            elif amount == 180:
                self.waypoint = direction[2:6]
                
            else:
                self.waypoint = direction[3:7]
                
        else:
            if amount == 90:
                self.waypoint = direction[3:7]
                
            elif amount == 180:
                self.waypoint = direction[2:6]
               
            else:
                self.waypoint = direction[1:5]
               
            
    def getManhattan(self):
        return abs(self.directions[0] - self.directions[2]) + abs(self.directions[1] - self.directions[3])

def main():
    out = readFile('test.txt')
    ferry = Ship()
    for direction in out:
        ferry.move(direction)
    print(ferry.getManhattan())
    ferry_two = Ship()
    for direction in out:
        ferry_two.moveTwo(direction)
    print(ferry_two.getManhattan())

if __name__ == "__main__":
    main()