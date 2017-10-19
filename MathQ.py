import random


class Expression:

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

        # 'Assume 2'
        for i in range(self.number_of_numbers):
            if i > 0:
                print(i)
                n = random.randrange(0, nie[i] - 1 // 2)
            else:
                n = random.randrange(0, self.maximum_number // 2)
            nie.append(n)

        s += '%d ' % nie[0]
        for i in range(len(nie)):
            if i == 0:
                continue

            s += '+ %d ' % nie[i]
        s += '= '

        return s


    def mul_expression(self) -> str:
        return '%d x %d = ' % (self.number1, self.number2)

    def div_expression(self) -> str:
        return '%d \u00F7 %d = ' % (self.number1, self.number2)


class QuestionType:
    ADDITION = 0
    SUBTRACTION = 1
    MULTIPLICATION = 2
    DIVISION = 3
    EXPONENTS = 4
    BRACKETS = 5
