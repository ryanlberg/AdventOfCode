from collections import defaultdict
def readFile(input):
    out = []
    with open(input, 'r') as infile:
        out = list(map(int, infile.read().split(',')))

    return out

def playMemGame(memory, time):
    seen = defaultdict(list)
    for i, x in enumerate(memory):
        seen[x] = [0, i+1]
    
    current_num = 0
    current_len = len(memory)+1
    while current_len < time:
        if current_num in seen:
            locs = seen[current_num]
            locs[0] = locs[1]
            locs[1] = current_len
            seen[current_num] = locs
            current_num = locs[1] - locs[0]
            
        else:
            seen[current_num] = [0, current_len]
            current_num = 0

        current_len += 1
    return current_num

def main():
    memory = readFile('input.txt')
    print(playMemGame(memory, 2020))
    print(playMemGame(memory, 30000000))

if __name__ == "__main__":
    main()