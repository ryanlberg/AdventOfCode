from collections import deque

def readFile(input):
    out = []
    with open(input, 'r') as infile:
        l = infile.read().split("\n\n")
        for line in l:
            number, board = line.split(":")
            out.append([int(number.split(" ")[1]), board.split("\n")[1:]])
    return out


class Tile():

    def __init__(self, id, board):
        self.ident = id
        self.board = board
        self.sideone = board[0]
        self.sidetwo = board[-1]
        self.sidethree = ''.join([board[x][0] for x in range(len(board))])
        self.sidefour = ''.join([board[x][-1] for x in range(len(board))])
        self.connected = {}
    
    def canConnect(self, tiletwo):
        a = self.getSides()
        b = tiletwo.getSides()
        for i, aside in enumerate(a):
            for j, bside in enumerate(b):
                if aside == bside:
                    self.connected[tiletwo.ident] = [[i+1, j+1], bside, tiletwo]
                    tiletwo.connected[self.ident] = [[j+1, i+1], aside, self]
                elif aside == bside[::-1]:
                    self.connected[tiletwo.ident] = [[i+1,-(j+1)], bside, tiletwo]
                    tiletwo.connected[self.ident] = [[-j+1, i+1], aside, self]
                    

    def getConnection(self, tiletwo):
        a = self.getSides()
        b = tiletwo.getSides()
        for i, aside in enumerate(a):
            for j, bside in enumerate(b):
                if aside == bside:
                    return [i+1, j+1]
                elif aside == bside[::-1]:
                    return [i+1, -(j+1)]
        return -1

    def getSides(self):
        return [self.sideone, self.sidetwo, self.sidethree, self.sidefour]

    

def flipHorizontal(board):
        out = [x[::-1] for x in board]
        return out

def flipVertical(board):
    out = [board[-1-i] for i in range(len(board))]
    return out

def rotate(board):
    out = [['' for x in range(len(board))] for y in range(len(board))]
    x = 0
    y = len(board)-1
    for tile in board:
        for letter in tile:
            out[x][y] = letter
            x += 1
        x = 0
        y -= 1
    return [''.join(row) for row in out]


def buildBoard(cornerPiece, size):
    out = [[None for x in range(size)] for y in range(size)]
    conns = set()
    for key in cornerPiece.connected.keys():
        conns.add(cornerPiece.connected[key][0][0])
    start = getStart(conns, size)
    frontier = deque([[start, cornerPiece]])
    while len(frontier) > 0:
        currentTile = frontier.popleft()
        #print(currentTile)
        loc = currentTile[0]
        tile = currentTile[1]
        out[loc[0]][loc[1]] = tile
        for key in tile.connected.keys():
            nextloc, side, nexttile = tile.connected[key]
            togo, nexttile = getNextTile(loc, tile, nexttile)
            #print(loc, togo, nexttile.ident, nexttile.connected)
            #print(togo)
            #print(out[togo[0]][togo[1]])
            #print(togo[0], togo[1], out[togo[0]][togo[1]])
            if not out[togo[0]][togo[1]]:
                frontier.append([togo, nexttile])
            for x in out:
                print(x)
    return out

def getNextTile(loc, currentTile, nextTile):
    nextloc = currentTile.getConnection(nextTile)
    print("howdy", currentTile.ident, nextTile.ident, nextloc)
    if nextloc[0] == 4:
        if nextloc[1] == 3:
            return [loc[0], loc[1] + 1], nextTile
        else: 
            return [loc[0], loc[1] + 1], genNewTile(nextloc[0], nextloc[1], nextTile)
    elif nextloc[0] == 3:
        if nextloc[1] == 4:
            return [loc[0], loc[1] - 1], nextTile
        else:
            return [loc[0], loc[1] - 1], genNewTile(nextloc[0], nextloc[1], nextTile)
    elif nextloc[0] == 2:
        if nextloc[1] == 1:
            return [loc[0] + 1, loc[1]], nextTile
        else:
            return [loc[0] + 1, loc[1]], genNewTile(nextloc[0], nextloc[1], nextTile)
    else:
        if nextloc[1] == 2:
            return [loc[0]-1, loc[1]], nextTile
        else:
            return [loc[0]-1, loc[1]], genNewTile(nextloc[0], nextLoc[1], nextTile)

def genNewTile(start, end, tile):
    board = tile.board
    if start == 4:
        if abs(end) == 1 or abs(end) == 2:
            newboard = rotate(tile.board)
            if end == 2:
                newtile = Tile(tile.ident, newboard)
                newtile.connected = tile.connected
                return newtile
            if end == -2:
                newboard = flipVertical(newboard)
                newtile = Tile(tile.ident, newboard)
                newtile.connected = tile.connected
                return newtile
            if end == 1:
                newboard = flipHorizontal(newboard)
                newtile = Tile(tile.ident, newboard)
                newtile.connected = tile.connected
                return newtile
            if end == -1:
                newboard = flipHorizontal(newboard)
                newboard = flipVertical(newboard)
                newtile = Tile(tile.ident, newboard)
                newtile.connected = tile.connected
                return newtile
        if end == -3:
            newboard = flipVertical(tile.board)
            newtile = Tile(tile.ident, newboard)
            newtile.connected = tile.connected
            return newtile
        if end == 4:
            newboard = flipHorizontal(tile.board)
            newtile = Tile(tile.ident, newboard)
            newtile.connected = tile.connected
            return newtile
        if end == -4:
            newboard = flipHorizontal(tile.board)
            newboard = flipVertical(newboard)
            newtile = Tile(tile.ident, newboard)
            newtile.connected = tile.connected
            return newtile
    elif start == 2:
        if abs(end) == 3 or abs(end) == 4:
            newboard = rotate(tile.board)
            if end == 3:
                newtile = Tile(tile.ident, newboard)
                newtile.connected = tile.connected
                return newtile
            if end == -3:
                newboard = flipHorizontal(newboard)
                newtile = Tile(tile.ident, newboard)
                newtile.connected = tile.connected
                return newtile
            if end == 4:
                newboard = flipVertical(newboard)
                newtile = Tile(tile.ident, newboard)
                newtile.connected = tile.connected
                return newtile
            if end == -4:
                newboard = flipHorizontal(newboard)
                newboard = flipVertical(newboard)
                newtile = Tile(tile.ident, newboard)
                newtile.connected = tile.connected
                return newtile
        if end == -1:
            newboard = flipHorizontal(tile.board)
            newtile = Tile(tile.ident, newboard)
            newtile.connected = tile.connected
            return newtile
        if end == 2:
            newboard = flipVertical(tile.board)
            newtile = Tile(tile.ident, newboard)
            newtile.connected = tile.connected
            return newtile
        if end == -2:
            newboard = flipHorizontal(tile.board)
            newboard = flipVertical(newboard)
            newtile = Tile(tile.ident, newboard)
            newtile.connected = tile.connected
            return newtile
    elif start == 1:
        if abs(end) == 3 or abs(end) == 4:
            newboard = rotate(tile.board)
            if end == 4:
                newtile = Tile(tile.ident, newboard)
                newtile.connected = tile.connected
                return newtile
            if end == -4:
                newboard = flipHorizontal(newboard)
                newtile = Tile(tile.ident, newboard)
                newtile.connected = tile.connected
                return newtile
            if end == 3:
                newboard = flipVertical(newboard)
                newtile = Tile(tile.ident, newboard)
                newtile.connected = tile.connected
                return newtile
            if end == -3:
                newboard = flipHorizontal(newboard)
                newboard = flipVertical(newboard)
                newtile = Tile(tile.ident, newboard)
                newtile.connected = tile.connected
                return newtile
        if end == -2:
            newboard = flipHorizontal(tile.board)
            newtile = Tile(tile.ident, newboard)
            newtile.connected = tile.connected
            return newtile
        if end == 1:
            newboard = flipVertical(tile.board)
            newtile = Tile(tile.ident, newboard)
            newtile.connected = tile.connected
            return newtile
        if end == -1:
            newboard = flipHorizontal(tile.board)
            newboard = flipVertical(newboard)
            newtile = Tile(tile.ident, newboard)
            newtile.connected = tile.connected
            return newtile
    elif start == 3:
        if abs(end) == 1 or abs(end) == 2:
            newboard = rotate(tile.board)
            if end == 1:
                newtile = Tile(tile.ident, newboard)
                newtile.connected = tile.connected
                return newtile
            if end == -1:
                newboard = flipVertical(newboard)
                newtile = Tile(tile.ident, newboard)
                newtile.connected = tile.connected
                return newtile
            if end == 2:
                newboard = flipHorizontal(newboard)
                newtile = Tile(tile.ident, newboard)
                newtile.connected = tile.connected
                return newtile
            if end == -2:
                newboard = flipHorizontal(newboard)
                newboard = flipVertical(newboard)
                newtile = Tile(tile.ident, newboard)
                newtile.connected = tile.connected
                return newtile
        if end == -4:
            newboard = flipVertical(tile.board)
            newtile = Tile(tile.ident, newboard)
            newtile.connected = tile.connected
            return newtile
        if end == 3:
            newboard = flipHorizontal(tile.board)
            newtile = Tile(tile.ident, newboard)
            newtile.connected = tile.connected
            return newtile
        if end == -3:
            newboard = flipHorizontal(tile.board)
            newboard = flipVertical(newboard)
            newtile = Tile(tile.ident, newboard)
            newtile.connected = tile.connected
            return newtile

def getStart(conns, size):
    if 1 in conns and 4 in conns:
        return [size-1, 0]
    elif 1 in conns and 3 in conns:
        return [size-1, size-1]
    elif 2 in conns and 4 in conns:
        return [0, 0]
    else:
        return [0, size-1]

def main():
    tilefile = readFile('test.txt')
    tiles = []
    for tile in tilefile:
        tiles.append(Tile(tile[0], tile[1]))

    for i in range(len(tiles)):
        for j in range(i+1, len(tiles)):
            tiles[i].canConnect(tiles[j])
        print(tiles[i].connected)
    
    sides = []
    for tile in tiles:
        if len(tile.connected) == 2:
            sides.append(tile)

    print(len(tiles))
    out = 1
    for side in sides:
        out *= side.ident
    print("1:", out)

    monstermap = buildBoard(sides[0], 3)
    for x in monstermap:
        print(x)

    print("2:", 0)
if __name__ == "__main__":
    main()