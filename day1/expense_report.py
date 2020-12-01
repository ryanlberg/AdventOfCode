
def readFile(filepath):
    out = []
    infile = open(filepath, 'r')
    for number in infile:
        out.append(int(number))
    
    return out

def sumToTwentyTwenty_two(report):
    SUM_TO_FIND = 2020
    seen = set()
    for number in report:
        needed = SUM_TO_FIND - number
        if needed in seen:
            return number * needed
        seen.add(number)
    return -1 


def sumToTwentyTwenty_three(report))

if __name__ == "__main__":
    numlist = readFile('input.txt')
    print(sumToTwentyTwenty(numlist))
