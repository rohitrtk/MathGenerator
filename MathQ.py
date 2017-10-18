class Expression:

    def __init__(self, number1: int, number2: int):
        self.number1 = number1
        self.number2 = number2

    def add_expression(self) -> str:
        return '%d + %d = ' % (self.number1, self.number2)

    def sub_expression(self):
        return '%d - %d = ' % (self.number1, self.number2)

    def mul_expression(self):
        return '%d x %d = ' % (self.number1, self.number2)

    def div_expression(self):
        return '%d \u00F7 %d = ' % (self.number1, self.number2)


class QuestionType():
    ADDITION = 0
    SUBTRACTION = 1
    MULTIPLICATION = 2
    DIVISION = 3
    EXPONENTS = 4
    BRACKETS = 5
