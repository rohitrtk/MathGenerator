from MathQ import Expression, QuestionType
from typing import List
from enum import Enum
from datetime import datetime
import random
import os

FILE_NAME = 'Questions'
FILE_EXTENSION = '.txt'
HOME_DIRECTORY = os.path.join(os.environ['USERPROFILE'], 'Desktop')

USE_TEST_FILE = True


def run():

    # Set the type of questions
    question_type = set_question_type()

    # Set the difficulty
    #difficulty = set_difficulty()

    # Set the number of questions
    number_of_questions = set_number_questions()

    questions = generate_questions(number_of_questions, question_type)

    output_directory = os.path.join(HOME_DIRECTORY, generate_file_name(FILE_NAME))
    generate_file(output_directory, questions)


def set_question_type() -> List[int]:
    pretty_question_types = \
        """
        0. Addition
        1. Subtraction
        2. Multiplication
        3. Division
        4. Exponents
        5. Brackets
        """

    i = input('%s\n%s' % ('Enter the questions you\'d like seperated '
        'with a space.\nHere are your options:', pretty_question_types))

    question_types = []
    user_input = i.split()

    for index in range(len(user_input)):
        if user_input[index] in question_types:
            continue

        question_types.append(int(user_input[index]))

    return question_types


def set_difficulty() -> int:
    difficulty = -1

    while True:
        d = input('Enter difficulty level between 0 and 3. (The default is 1, enter a blank line to use default): ')

        if not d:
            return 1

        try:
            difficulty = int(d)
        except ValueError:
            print('Invalid input.')

        if 0 <= difficulty < 4:
            break

    return difficulty


def set_number_questions(number_of_questions=20) -> int:
    while True:
        s = input('Please set number of questions. (The default is 20, enter a blank line to use default): ')

        if not s:
            return number_of_questions

        try:
            number_of_questions = int(s)
            break
        except ValueError:
            print('Invalid input.')

    return number_of_questions


def generate_question(maximum_number: int, question_types: List[int]) -> str:
    exp = Expression(maximum_number=maximum_number)

    question_type = question_types[0]
    if len(question_types) > 1:
        question_type = random.randrange(question_type, question_types[len(question_types) - 1] + 1)

    return get_question_type(question_type, exp)


def get_question_type(question_type: str, exp: Expression) -> str:
    if question_type == QuestionType.ADDITION:
        return exp.add_expression()

    elif question_type == QuestionType.SUBTRACTION:
        return exp.sub_expression()

    elif question_type == QuestionType.MULTIPLICATION:
        return exp.mul_expression()

    elif question_type == QuestionType.DIVISION:
        return exp.div_expression()

    return 'NOT IMPLEMENTED YET!'


def generate_questions(number_of_questions: int, question_types: List[int]) -> List[str]:
    questions = []

    while True:
        s_maximum_number = input(
            'Enter the maximum number you\'d like. (The default is 50, enter a blank line to user default): ')

        if not s_maximum_number:
            maximum_number = 50
            break

        try:
            maximum_number = int(s_maximum_number)
            break
        except ValueError:
            print('Invalid Input')

    for i in range(number_of_questions):

        q = generate_question(maximum_number, question_types)
        while q in questions:
            q = generate_question(maximum_number, question_types)

        questions.append('%d) %s' % (i + 1, q))

    if number_of_questions % 2 == 1:
        questions.append(' ')

    return questions


def generate_file(target_file: str, questions: List[str]):
    if USE_TEST_FILE:
        with open('Questions.txt', 'w') as file:

            for line in format_questions(questions):
                file.write(line)
        return

    create_file(target_file)

    with open(target_file, 'w') as file:

        for line in format_questions(questions):
            file.write(line)


def format_questions(questions: List[str]) -> List[str]:
    # Gets the max number of chars per question
    max_chars = get_max_chars(questions)

    lines = ['\n']
    char_counter = 0

    for i in range(len(questions)):
        line = check_spacing(questions[i], max_chars)
        lines.append(line)
        char_counter += len(line)

        if i % 2 == 1 and i != 0:
            lines.append('\n%s\n' % add_pretty_line(char_counter))

            char_counter = 0

    return lines


def get_max_chars(questions: List[str]) -> int:
    # Get the maximum number of characters from the list
    # of questions
    max_char = 0

    for i in range(len(questions)):
        if len(questions[i]) > max_char:
            max_char = i

    return max_char


def check_spacing(question: str, chars: int) -> str:
    # Compares the length of the question to some number chars
    # and adds spacing if the length of the question
    # is less than number of chars
    if len(question) >= chars + 50:  # Added more spacing
        return question

    return '%s%s' % (question, ' ' * (chars - len(question)))


def add_pretty_line(length_of_previous: int) -> str:
    s = ''

    # Sets string s to a some pretty -'s
    for i in range(length_of_previous):
        s += '-'

    return s


def generate_file_name(directory_name: str) -> str:
    # File file_name will be a constant
    t = '%s_%s-%s-%s' % (str(datetime.now().date()), str(datetime.now().hour), str(datetime.now().minute), str(datetime.now().second))

    return '%s_%s%s' % (directory_name, t, FILE_EXTENSION)


def create_file(file: str):
    f = open(file, 'w')
    f.close()


if __name__ == '__main__':
    run()

