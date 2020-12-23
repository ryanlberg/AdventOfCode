class CupGame():

    class Node():

        def __init__(self, val):
            self.val = val
            self.next = None
            self.prev = None
    
    def __init__(self, cuporder, maxcups):
        self.maxcup = maxcups
        self.mincup = 1
        self.nextcuplocs = [x for x in range(self.maxcup + 1)]
        self.cupgame = self.getGameList(cuporder, self.maxcup)
       

    def getGameList(self, game, maxcup):
        start = None
        prev = None
        ret = None
        maxseen = 0
        for number in game:
            num = int(number)
            maxseen = max(maxseen, num)
            start = self.Node(num)
            self.nextcuplocs[num-1] = start
            if not ret:
                ret = start
            if prev:
                prev.next = start
                start.prev = prev
            prev = start
        for x in range(maxseen+1, maxcup+1):
            start = self.Node(x)
            self.nextcuplocs[x-1] = start
            prev.next = start
            start.prev = prev
            prev = start

        ret.prev = start
        start.next = ret
        return ret

    def simGame(self, moves):
        for _ in range(moves):
            #print(self)
            self.move()

            

    def move(self):
        start = self.cupgame
        
        start_three = start.next
        end_three = start.next.next.next

        next_three = [start.next.val, start.next.next.val, start.next.next.next.val]
        needed = self.getNextCup(next_three, start.val-1)

        startnext = start.next.next.next.next
        loc = self.nextcuplocs[needed-1]
        
        if startnext == loc:
            temp = loc.next
            start.next = loc
            loc.prev = start
            loc.next = start_three
            start_three.prev = loc
            end_three.next = temp
            temp.prev = end_three
            self.cupgame = self.cupgame.next
        else:
            temp = loc.next
            start.next = startnext
            startnext.prev = start
            loc.next = start_three
            start_three.prev = loc
            end_three.next = temp
            temp.prev = end_three
            self.cupgame = self.cupgame.next
            


            

    def getNextCup(self, next_three, currentcup):
        if currentcup < self.mincup:
            currentcup = self.maxcup
        while currentcup in next_three:
            currentcup -= 1
            if currentcup < self.mincup:
                currentcup = self.maxcup
        return currentcup

    def __str__(self):
        out = ""
        i = 0
        start = self.cupgame
        while i < self.maxcup:
            out += str(start.val) + " "
            i += 1
            start = start.next
        return out


def main():
    game = "963275481"
    cupgame = CupGame(game, 1000000)
    cupgame.simGame(10000000)
    onecup = cupgame.nextcuplocs[0]
    print(onecup.next.val*onecup.next.next.val)

if __name__ == "__main__":
    main()