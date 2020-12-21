import itertools
def readFile(input):
    out = []
    with open(input, 'r') as infile:
        out = infile.read().split('\n\n')

    return out


def combine(l, start):
    if len(l) == 1:
        return l[0]
    while len(l) > 1:
        nextcombo = []
        cur = l.pop()
        for x in l[-1]:
            for item in cur:
                nextcombo.append(x + item)
        l.pop()
        if len(l) >= 1:
            l.append(nextcombo)
        else:
            l = nextcombo
            break
    return l

class Language():

    def __init__(self, rules):
        self.rules = {}
        for rule in rules:
            self.parseRule(rule)
        self.constructionHelper = {}

    def parseRule(self, rule):
        l, r = rule.split(': ')
        l = int(l)
        if "|" in r:
            splits = r.split(" | ")
            out = [[int(x) for x in y.split(' ')] for y in splits]
            self.rules[l] = out
        elif "\"" in r:
            self.rules[l] = r[1]
        else:
            new = r.split(" ")
            if len(new) == 1:
                self.rules[l] = [[int(new[0])]]
            else:
                self.rules[l] = [[int(x) for x in new]]

    def constructVocabulary(self, start):
        if len(self.rules[start]) == 1 and len(self.rules[start][0]) == 1 and (self.rules[start][0] == 'a' or self.rules[start][0] ==  'b'):
            return [self.rules[start]]
        elif start in self.constructionHelper:
            return self.constructionHelper[start]
        else:
            out = []
            for rules in self.rules[start]:
                x = []
                for rule in rules:
                    x.append(self.constructVocabulary(rule))
                x = combine(x, start)
                out = out + x

            self.constructionHelper[start] = out
            return out

        

def main():
    rules, messages = readFile('input.txt')
    rules = rules.split('\n')
    messages = messages.split('\n')
    maxlen = max(len(message) for message in messages)
    monsterLanguage = Language(rules)
    
    a = set(monsterLanguage.constructVocabulary(0))
    count = 0
    for x in messages:
        if x.strip() in a:
            count += 1
    print(count)


if __name__ == "__main__":
    main()