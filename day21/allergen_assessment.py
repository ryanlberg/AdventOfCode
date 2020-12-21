from collections import defaultdict

def readFile(input):
    out = []
    with open(input, 'r') as inFile:
        out = inFile.read().split("\n")
    return out

def getAllergyIngredList(recipe):
    ingredients, allergens = recipe.split(" (contains ")
    return ingredients.split(" "), allergens[:-1].split(", ")

class AllergenDistinguisher():
    def __init__(self):
        self.allergyLists = defaultdict(lambda: defaultdict(int))
        self.allergyRecipeCounts = defaultdict(int)
        self.allergens = set()
        self.causers = {}
        self.allergyout = []

    def addAllergenCounts(self, allergens, ingredients):
        for allergen in allergens:
            self.allergens.add(allergen)
            self.allergyRecipeCounts[allergen] += 1
            for ingredient in ingredients:
                self.allergyLists[allergen][ingredient] += 1

    def findCausers(self):
        while len(self.causers) < len(self.allergens) * 2:
            for allergen in self.allergens:
                if allergen not in self.causers:
                    needed = self.allergyRecipeCounts[allergen]
                    needed_match = []
                    for ingredient in self.allergyLists[allergen].keys():
                        if self.allergyLists[allergen][ingredient] == needed and ingredient not in self.causers:
                            needed_match.append(ingredient)
                    if len(needed_match) == 1:
                        self.allergyout.append([needed_match[0], allergen])
                        self.causers[needed_match[0]] = allergen
                        self.causers[allergen] = needed_match[0]

def main():
    ingredients = readFile("input.txt")
    finder = AllergenDistinguisher()
    recipes = []
    for recipe in ingredients:
        a, b = getAllergyIngredList(recipe)
        finder.addAllergenCounts(b, a)
        recipes.append(a)
    finder.findCausers()
    
    count = 0
    for recipe in recipes:
        for ingredient in recipe:
            if ingredient not in finder.causers:
                count += 1
    print(count)
    print(','.join([x[0] for x in sorted(finder.allergyout, key = lambda x: x[1])]))
    
if __name__ == "__main__":
    main()