
def readFile(input):
    out = []
    infile = open(input, 'r')
    for line in infile:
        out.append(line.strip())
    infile.close()
    return out


def translate(rowValues, low, totalRows):
    if len(rowValues) == 1:
        if rowValues[0] == "F" or rowValues[0] == "L":
            return low
        else:
            return totalRows
    if rowValues[0] == "F" or rowValues[0] == "L":
        return translate(rowValues[1:], low, (low+totalRows)//2)
    return translate(rowValues[1:], (low+totalRows)//2+1, totalRows)
    
def getSeatId(passenger):
    row = passenger[0:7]
    seat = passenger[7:]
    return translate(row, 0, 127) * 8 + translate(seat, 0, 7)


def getMaxPassengerSeatId(passengers):
    seatIds = []
    for passenger in passengers:
        seatIds.append(getSeatId(passenger))
    print("My Seat: ", findMySeat(seatIds))
    return max(seatIds)

def findMySeat(seatIds):
    seatIds = sorted(seatIds)
    start = seatIds[0]
    for seat in seatIds:
        if not seat == start:
            return start
        start += 1
    return -1

if __name__ == "__main__":
    passengers = readFile('input.txt')
    print("Max Seat:", getMaxPassengerSeatId(passengers))