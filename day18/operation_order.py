from collections import deque
def readFile(input):
    out = []
    with open(input, 'r') as infile:
        out = list(infile.read().split('\n'))
    return out

def consumeDigit(numstring, i):
    dig = ""
    numlen = len(numstring)
    while i < numlen and numstring[i].isdigit():
        dig += numstring[i]
        i += 1
    return int(dig), i

class Solver():
    def __init__(self, order):
        self.order = order

    def solve(self, equation):
        return self.order.solve(equation)


class LeftToRight():

    def solve(self, equation):
        return self.solveHelper(equation, 0)
    
    def resolve(self, numbers, operators):
        while len(numbers) >= 2 and len(operators) >= 1:
            one = numbers.popleft()
            two = numbers.popleft()
            operator = operators.popleft()
            if operator == "+":
                numbers.appendleft(one + two)
            else:
                numbers.appendleft(one * two)
        if not numbers:
            return 0
        return numbers.pop()

    def solveHelper(self, equation, i):
        numbers = deque([])
        operators = deque([])
        while i < len(equation):
            if equation[i] == '(':
                number, i = self.solveHelper(equation, i+1)
                numbers.append(number)
            elif equation[i] == ')':
                return self.resolve(numbers, operators), i+1
            elif equation[i].isdigit():
                number, i = consumeDigit(equation, i)
                numbers.append(number)
            elif equation[i] == '*' or equation[i] == "+":
                operators.append(equation[i])
                i += 1
            else:
                i += 1
        return self.resolve(numbers, operators), i

class PlusPrecedence():
    def solve(self, equation):
        return self.solveHelper(equation, 0)
   
    def resolve(self, numbers, operators):
        leftovers = []
        for operator in operators:
           
            if operator == "+":
                if leftovers:
                    leftovers.append(leftovers.pop() + numbers.popleft())
                else:
                    leftovers.append(numbers.popleft() + numbers.popleft())
            else:
                if not leftovers:
                    leftovers.append(numbers.popleft())
                    leftovers.append(numbers.popleft())
                else:
                    leftovers.append(numbers.popleft())
       
        out = 1
        for number in leftovers:
            out *= number
        return out

    def solveHelper(self, equation, i):
        numbers = deque([])
        operators = deque([])
        while i < len(equation):
            if equation[i] == '(':
                number, i = self.solveHelper(equation, i+1)
                numbers.append(number)
            elif equation[i] == ')':
                return self.resolve(numbers, operators), i+1
            elif equation[i].isdigit():
                number, i = consumeDigit(equation, i)
                numbers.append(number)
            elif equation[i] == '*' or equation[i] == "+":
                operators.append(equation[i])
                i += 1
            else:
                i += 1
        
        return self.resolve(numbers, operators), i
        
def main():
    equations = readFile('input.txt')
    ltrSolver = Solver(LeftToRight())
    plusSolver = Solver(PlusPrecedence())
    ltrsum = 0
    plussum = 0
    for equation in equations:
        num = ltrSolver.solve(equation)[0]
        ltrsum += num
        plus = plusSolver.solve(equation)[0]
        plussum += plus
    print(ltrsum)
    print(plussum)

if __name__ == "__main__":
    main()