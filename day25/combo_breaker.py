
def getLoopSize(subjectNumber, key):
    startValue = 1
    counter = 0
    while startValue != key:
        startValue = (startValue * subjectNumber) % 20201227
        counter += 1
    return counter

def getEncrypthionKey(subjectNumber, loopcounter):
    start = 1
    for _ in range(loopcounter):
        start = (start * subjectNumber) % 20201227

    return start


def main():
    cardPub = 8458505
    doorPub = 16050997
    b = getLoopSize(7, cardPub)
    a = getLoopSize(7, doorPub)
    print(a, b)
    print(getEncrypthionKey(cardPub, a))
    print(getEncrypthionKey(doorPub, b))

if __name__ == "__main__":
    main()