def readFile(input):
    out = []
    infile = open(input, 'r')
    curline = []
    for line in infile:
        if line == "\n":
            out.append(curline)
            curline = []
        else:
            curline.append(line.strip())
    out.append(curline)
    infile.close()

    return out


def countUniqueQuestions(batchs):
    batch_totals = 0
    for batch in batches:
        seen = set()
        
        for q in batch:
            for letter in q:
                seen.add(letter)
        batch_totals += len(seen)
    
    return batch_totals

def countAllAnswered(batches):
    total_count = 0
    for batch in batches:
        needed = len(batch)
        seen = [0 for x in range(26)]
        for responses in batch:
            for question in responses:
                seen[ord(question) - ord('a')] += 1

        for total_response in range(len(seen)):
            if seen[total_response] == needed:
                total_count += 1

    return total_count

if __name__ == "__main__":
    batches = readFile('input.txt')
    print(countUniqueQuestions(batches))
    print(countAllAnswered(batches))