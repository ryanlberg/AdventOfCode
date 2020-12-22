from collections import deque

def readFile(input):
    out = []
    with open(input, 'r') as inFile:
        out = inFile.read().split("\n\n")
    return out

def getDecks(player):
    playerid, numbers = player.split(":\n")
    return list(map(int, numbers.split("\n")))

def battle(deckOne, deckTwo):
    while deckOne and deckTwo:
        one = deckOne.popleft()
        two = deckTwo.popleft()
        if one > two:
            deckOne.append(one)
            deckOne.append(two)
        else:
            deckTwo.append(two)
            deckTwo.append(one)
    
    if deckOne:
        return deckOne
    return deckTwo


def recursiveCombat(deckOne, deckTwo, seengame):
    while deckOne and deckTwo:
        order = genOrder(deckOne, deckTwo)
        if order in seengame:
            deckOne.append(deckOne.popleft())
            deckOne.append(deckTwo.popleft())
        else:
            seengame.add(order)
            
            a = deckOne.popleft()
            b = deckTwo.popleft()
            if len(deckOne) >= a and len(deckTwo) >= b:
                newa = list(deckOne)[:a]
                newb = list(deckTwo)[:b]
                q = playSubGame(deque(newa), deque(newb), set())
                if q == 1:
                    deckOne.append(a)
                    deckOne.append(b)
                else:
                    deckTwo.append(b)
                    deckTwo.append(a)
            else:
                if a > b:
                    deckOne.append(a)
                    deckOne.append(b)
                else:
                    deckTwo.append(b)
                    deckTwo.append(a)

    if deckOne:
       return deckOne
    return deckTwo

def playSubGame(deckOne, deckTwo, seenGame):
    while deckOne and deckTwo:
        order = genOrder(deckOne, deckTwo)
        if order in seenGame:
            return 1
        else:
            seenGame.add(order)
            a = deckOne.popleft()
            b = deckTwo.popleft()
            if len(deckOne) >= a and len(deckTwo) >= b:
                newa = list(deckOne)[:a]
                newb = list(deckTwo)[:b]
                q = playSubGame(deque(newa), deque(newb), set())
                if q == 1:
                    deckOne.append(a)
                    deckOne.append(b)
                else:
                    deckTwo.append(b)
                    deckTwo.append(a)
            else:
                if a > b:
                    deckOne.append(a)
                    deckOne.append(b)
                else:
                    deckTwo.append(b)
                    deckTwo.append(a)
    if deckOne:
        return 1
    return 2

def genOrder(deck, decktwo):
    return (tuple(deck), tuple(decktwo))

def calcPoints(deck):
    points = 0
    cardseen = 1
    while deck:
        points += deck.pop() * cardseen
        cardseen += 1
    return points

def main():
    players = readFile('input.txt')
    decks = []
    for player in players:
        decks.append(deque(getDecks(player)))
    winner2 = recursiveCombat(decks[0], decks[1], set())
    print(calcPoints(winner2))

if __name__ == "__main__":
    main()