
from collections import defaultdict

def readFile(filepath):
    out = []
    infile = open(filepath, 'r')
    for number in infile:
        out.append(int(number))
    
    infile.close()
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


def sumToTwentyTwenty_three(report):
    SUM_TO_FIND = 2020
    seen = defaultdict(int)
    for i in range(len(report)):

        for j in range(i+1, len(report)):
            seen[report[i] + report[j]] = report[i] * report[j]

    for number in report:
        needed = SUM_TO_FIND - number
        if needed in seen:
            return seen[needed] * number
    
    return -1
if __name__ == "__main__":
    numlist = readFile('input.txt')
    print(sumToTwentyTwenty_two(numlist))
    print(sumToTwentyTwenty_three(numlist))
