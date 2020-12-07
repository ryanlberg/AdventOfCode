from collections import defaultdict

def readFile(input):
    out = []
    infile = open(input, 'r')
    for line in infile:
        out.append(line.strip())
    
    infile.close()
    
    return out

def consumeRule(rule):
    bag, contains = rule.split('contain')
    bag = bag.strip()[:-1]

    containlist  = []
    innerbags = contains.split(',')
    for smallerBag in innerbags:
        smallerBag = smallerBag.strip()
        smallerBag = smallerBag.replace('.', '')
        if smallerBag[-1] == "s":
            smallerBag = smallerBag[:-1]
        number, innerbag = smallerBag.split(" ", 1)
        if number == "no":
            break
        else:
            containlist.append([int(number), innerbag])

    return bag, containlist

def generateGraph(rules):
    bagGraph = defaultdict(list)
    for rule in rules:
        bag, innerbags = consumeRule(rule)
        baglist = bagGraph[bag]
        for curbag in innerbags:
            baglist.append(curbag)
        bagGraph[bag] = baglist

    return bagGraph
    

def canContainGold(bagGraph):
    seenToContain = defaultdict(bool)
   
    def explore(bag):
        if bag == "shiny gold bag":
            seenToContain["shiny gold bag"] = False
            return True
        elif bag in seenToContain:
            return seenToContain[bag]
        elif len(bagGraph[bag]) == 0:
            seenToContain[bag] = False
            return False
        can = [explore(contains[1]) for contains in bagGraph[bag]]
    
        seenToContain[bag] = any(can)
        return seenToContain[bag]

        

    for bag in bagGraph.keys():
        if bag not in seenToContain:
            explore(bag)

    count = 0
    for bag in seenToContain.keys():
        if seenToContain[bag]:
            count += 1

  
    return count
    


def shinyGoldContains(bagGraph):

    seen = defaultdict(int)
    
    def explore(bag):
        
        if len(bagGraph[bag]) == 0:
            seen[bag] = 1
            return 0
        elif bag in seen:
            return seen[bag]
        else:
            bagsIn = bagGraph[bag]
            seen[bag] = sum([s[0] + s[0] * explore(s[1]) for s in bagsIn])
            return seen[bag]

    return explore("shiny gold bag")
    
def main():
    rules = readFile('input.txt')
    bagGraph = generateGraph(rules)
    print(canContainGold(bagGraph))
    print(shinyGoldContains(bagGraph))

if __name__ == "__main__":
    main()