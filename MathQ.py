import random


class Expression:

    MAX_MULTIPLY = 20

    def __init__(self, maximum_number=50, number_of_numbers=2):
        self.maximum_number = maximum_number
        self.number_of_numbers = number_of_numbers

    def add_expression(self) -> str:
        s = ''

        for i in range(self.number_of_numbers + 1):
            n = random.randrange(0, self.maximum_number // 2)

            if i == 0:
                s += '%d ' % n
                continue
            elif i < self.number_of_numbers:
                s += '+ %d ' % n
                continue
            s += '= '

        return s

    def sub_expression(self) -> str:
        s = ''

        # Numbers in expression
        nie = []

        for i in range(self.number_of_numbers):
            if i > 0:
                n = random.randrange(0, nie[i - 1])
            else:
                # Using a random number for the min value to prevent an empty range error
                n = random.randrange(random.randrange(1, 5), self.maximum_number)
            nie.append(n)

        s += '%d ' % nie[0]
        for i in range(len(nie)):
            if i == 0:
                continue

            s += '- %d ' % nie[i]
        s += '= '

        return s

    def mul_expression(self) -> str:
        s = ''

        nie = []

        for i in range(self.number_of_numbers):
            # Check that multiplication of two numbers <= max number
            n = random.randrange(0, self.MAX_MULTIPLY)

            if i > 0:

            nie.append(n)
        return s

    def div_expression(self) -> str:
        s = ''

        return s


class QuestionType:
    ADDITION = 0
    SUBTRACTION = 1
    MULTIPLICATION = 2
    DIVISION = 3
    EXPONENTS = 4
    BRACKETS = 5
