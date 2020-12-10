def readFile(input):
    out = []
    with open(input, 'r') as infile:
        out = list(map(int, infile.readlines()))
    return out


def joltDifferences(adapters):
    adapters = sorted(adapters)
    previous = 0
    diffs = [0, 0, 0]
    for adapter in adapters:
        diff = adapter - previous
        diffs[diff-1] += 1
        previous = adapter

    diffs[2] += 1

    return diffs

def countWays(adapters):
    seen = {}
   
    adapters = sorted(adapters)
    needed = max(adapters) + 3
    def countHelper(i, cur):
        
        if needed - cur == 3:
            return 1 
        if i >= len(adapters)-1:
            return 0
        elif (i, cur) in seen:
            return seen[(i, cur)]
        else:
            seen[(i, cur)] = 0
            for x in range(i, min(i+4, len(adapters))):
                if adapters[x] - cur <= 3:
                    seen[(i, cur)] += countHelper(x, adapters[x])
            return seen[(i, cur)]
    
    ways = countHelper(0, 0)
    return ways


def main():
    adapters = readFile('input.txt')
    diffs = joltDifferences(adapters)
    print(diffs[0] * diffs[2])
    print(countWays(adapters))

if __name__ == "__main__":
    main()