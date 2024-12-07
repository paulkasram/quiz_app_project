from django.core.management.base import BaseCommand
from quiz.models import Question

class Command(BaseCommand):
    help = 'Populate the database with 20 Python Beginner questions'

    def handle(self, *args, **kwargs):
        questions = [
            {
                "question_text": "What is the output of `print(2 * 3)`?",
                "option_1": "5",
                "option_2": "6",
                "option_3": "7",
                "option_4": "8",
                "correct_option": "6"
            },
            {
                "question_text": "How do you start a comment in Python?",
                "option_1": "//",
                "option_2": "#",
                "option_3": "/* */",
                "option_4": "--",
                "correct_option": "#"
            },
            {
                "question_text": "Which keyword is used to define a function in Python?",
                "option_1": "define",
                "option_2": "def",
                "option_3": "func",
                "option_4": "function",
                "correct_option": "def"
            },
            {
                "question_text": "What data type is the result of `2.0 + 3`?",
                "option_1": "int",
                "option_2": "float",
                "option_3": "string",
                "option_4": "bool",
                "correct_option": "float"
            },
            {
                "question_text": "Python is a case-sensitive programming language.",
                "option_1": "True",
                "option_2": "False",
                "option_3": None,
                "option_4": None,
                "correct_option": "True"
            },
            {
                "question_text": "How do you print 'Hello, World!' in Python?",
                "option_1": "print(\"Hello\")",
                "option_2": "echo(\"Hello\")",
                "option_3": "print(\"Hello, World!\")",
                "option_4": "printf(\"Hello\")",
                "correct_option": "print(\"Hello, World!\")"
            },
            {
                "question_text": "What will `len(\"Python\")` return?",
                "option_1": "5",
                "option_2": "6",
                "option_3": "7",
                "option_4": "8",
                "correct_option": "6"
            },
            {
                "question_text": "Which operator is used for exponentiation in Python?",
                "option_1": "^",
                "option_2": "**",
                "option_3": "//",
                "option_4": "%",
                "correct_option": "**"
            },
            {
                "question_text": "Strings in Python are immutable.",
                "option_1": "True",
                "option_2": "False",
                "option_3": None,
                "option_4": None,
                "correct_option": "True"
            },
            {
                "question_text": "Which keyword is used to exit a loop prematurely?",
                "option_1": "exit",
                "option_2": "break",
                "option_3": "stop",
                "option_4": "return",
                "correct_option": "break"
            },
            {
                "question_text": "What is the output of `print(10 // 3)`?",
                "option_1": "3.3",
                "option_2": "3",
                "option_3": "4",
                "option_4": None,
                "correct_option": "3"
            },
            {
                "question_text": "How do you create a list in Python?",
                "option_1": "[]",
                "option_2": "{}",
                "option_3": "()",
                "option_4": "<>",
                "correct_option": "[]"
            },
            {
                "question_text": "In Python, `x = 5` assigns a value to the variable `x`.",
                "option_1": "True",
                "option_2": "False",
                "option_3": None,
                "option_4": None,
                "correct_option": "True"
            },
            {
                "question_text": "Which method is used to add an element to a list?",
                "option_1": ".insert()",
                "option_2": ".append()",
                "option_3": ".add()",
                "option_4": ".push()",
                "correct_option": ".append()"
            },
            {
                "question_text": "What is the output of `bool(\"\")`?",
                "option_1": "True",
                "option_2": "False",
                "option_3": None,
                "option_4": None,
                "correct_option": "False"
            },
            {
                "question_text": "What will `range(3)` produce?",
                "option_1": "0, 1, 2",
                "option_2": "1, 2, 3",
                "option_3": "0, 1, 2, 3",
                "option_4": "3, 2, 1",
                "correct_option": "0, 1, 2"
            },
            {
                "question_text": "What does `type(\"Hello\")` return?",
                "option_1": "str",
                "option_2": "int",
                "option_3": "list",
                "option_4": "bool",
                "correct_option": "str"
            },
            {
                "question_text": "Python allows multiple inheritance.",
                "option_1": "True",
                "option_2": "False",
                "option_3": None,
                "option_4": None,
                "correct_option": "True"
            },
            {
                "question_text": "What is the output of `print(2 > 3)`?",
                "option_1": "True",
                "option_2": "False",
                "option_3": None,
                "option_4": None,
                "correct_option": "False"
            },
            {
                "question_text": "How do you declare a variable in Python?",
                "option_1": "var x = 5",
                "option_2": "x = 5",
                "option_3": "let x = 5",
                "option_4": "declare x = 5",
                "correct_option": "x = 5"
            }
        ]

        for question in questions:
            Question.objects.create(**question)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with initial 20 questions!'))
