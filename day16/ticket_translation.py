from collections import defaultdict

def readFile(input):
    infile = open(input, 'r').read().split('\n\n')
    return infile

def parseFields(fields):
    classes = defaultdict(list)
    separated = fields.split('\n')
    for field in separated:
        name, ranges = field.split(': ')
        separatedRanges = ranges.split(' or ')
        for ind_range in separatedRanges:
            l, r = ind_range.split('-')
            classes[name].append([int(l), int(r)])
    return classes

def parseTickets(ticketlist):
    tickets = ticketlist.split('\n')
    ticketList = []
    for ticket in range(1, len(tickets)):
        ticketList.append(list(map(int, tickets[ticket].split(','))))
    return ticketList

def getCardsAndCalcErrorRate(fields, tickets):
    errorRate = 0
    errorcards = set()
    for i, ticket in enumerate(tickets):
        for number in ticket:
            seen = False
            for key in fields.keys():
                if not seen:
                    ranges = fields[key]
                    for l, r in ranges:
                        if number >= l and number <= r:
                            seen = True
                            break
                if seen:
                    break
            if not seen:
                errorRate += number
                errorcards.add(i)

    return errorcards, errorRate


def getClassTranslation(ticketClasses, validTickets):
    potentTranslate = defaultdict(list)
    for ticket in validTickets:
        for i, number in enumerate(ticket):
            for key in ticketClasses.keys():
                if not key in potentTranslate:
                    potentTranslate[key] = [0 for _ in range(len(ticketClasses))]
                ranges = ticketClasses[key]
                if potentialClassValidity(number, ranges):
                    potentTranslate[key][i] += 1

    translation = refinePotentialTranslation(potentTranslate, len(validTickets))
    
    return translation

def refinePotentialTranslation(potentials, needed_nums):
    finalTranslation = {}
    seennums = set()
    while len(finalTranslation) < len(potentials):
        
        for key in potentials.keys():
            if key not in finalTranslation:

                pots = potentials[key]
                valids = []
                for i, x in enumerate(pots):
                    if i not in seennums:
                        if x == needed_nums:
                            valids.append(i)
                if len(valids) == 1:
                    finalTranslation[key] = valids[0]
                    seennums.add(valids[0])
                    
    return finalTranslation

    

def potentialClassValidity(number, ranges):
    for l, r in ranges:
        if number >= l and number <= r:
            return True
    return False

def getDepartureMultiplication(translation, ticket):
    needed = ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time']
    out = 1
    for field in needed:
        out *= ticket[translation[field]]
    return out

def main():
    fields, myTicket, ticketList = readFile('input.txt')
    ticketClasses = parseFields(fields)
    otherTickets = parseTickets(ticketList)
    errorcards, errorRate = getCardsAndCalcErrorRate(ticketClasses, otherTickets)
    validTickets = [ticket for i, ticket in enumerate(otherTickets) if i not in errorcards]
    translation = getClassTranslation(ticketClasses, validTickets)
    personalTicket = parseTickets(myTicket)
    print(errorRate)
    print(getDepartureMultiplication(translation, personalTicket[0]))

if __name__ == "__main__":
    main()