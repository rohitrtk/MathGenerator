from MathQ import Expression
from typing import List
from datetime import datetime
import random
import os

FILE_NAME = 'Questions.txt'
HOME_DIRECTORY = os.path.join(os.environ['USERPROFILE'], 'Desktop')


def run():
    difficulty = set_difficulty()

    number_of_questions = set_number_questions()

    questions = generate_questions(number_of_questions, difficulty)

    output_file = os.path.join(HOME_DIRECTORY, generate_file_name(FILE_NAME))
    generate_file(output_file, questions)


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


def set_number_questions(number_of_questions = 20) -> int:
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


def generate_question(difficulty: int) -> str:
    number1 = random.randrange(0, 50)
    number2 = random.randrange(0, 50)

    while number2 > number1:
        number2 = random.randrange(0, 50)

    exp = Expression(number1, number2)

    # Addition and Subtraction
    if difficulty == 1:

        r = random.randrange(0, 2)
        # Addition
        if r == 0:
            return exp.add_expression()

        return exp.sub_expression()

    # Implies difficulty = 0
    return exp.add_expression()


def generate_questions(number_of_questions: int, difficulty: int) -> List[str]:
    questions = []

    for i in range(number_of_questions):

        q = generate_question(difficulty)
        while q in questions:
            q = generate_question(difficulty)

        questions.append('%d) %s' % (i + 1, q))

    if number_of_questions % 2 == 1:
        questions.append(' ')

    return questions


def generate_file(target_file: str, questions: List[str]):
    os.makedirs(os.path.dirname(target_file), exist_ok=True)

    with open(target_file) as file:

        for line in format_questions(questions):
            file.write(line)


def format_questions(questions: List[str]) -> List[str]:
    # Gets the average number of chars per question
    #average_chars = get_average_chars(questions)

    # Gets the max number of chars per question
    max_chars = get_max_chars(questions)

    lines = ['\n']
    char_counter = 0

    for i in range(len(questions)):
        line = check_spacing(questions[i], max_chars)
        lines.append(line)
        char_counter += len(line)

        if i % 2 == 1 and i != 0:
            lines.append('\n%s' % add_pretty_line(char_counter))
            lines.append('\n')

            char_counter = 0

    return lines


def get_average_chars(questions: List[str]) -> int:
    indices = len(questions)

    total_chars = 0
    for question in questions:
        total_chars += len(question)

    return total_chars // indices


def get_max_chars(questions: List[str]) -> int:
    max_char = 0

    for i in range(len(questions)):
        if i > max_char:
            max_char = i

    return max_char


def check_spacing(question: str, chars: int) -> str:
    if len(question) >= chars:
        return question

    return '%s%s' % (question, ' ' * (chars - len(question)))


def add_pretty_line(length_of_previous: int) -> str:
    s = ''

    for i in range(length_of_previous):
        s += '-'

    return s


def generate_file_name(file_name: str) -> str:
    # file_name will be a constant

    t = str(datetime.now())
    #for i in t:
    #    if i == ':' or i == '.':
    #        i = '-'

    return '%s_%s' % (file_name, t)


if __name__ == '__main__':
    run()

