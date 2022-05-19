from .formatter import format_answers, format_question


def questions_to_str(question: dict):
    question_block = "Question:\n" + format_question(question["text"])
    answer_block = "Answers:\n" + format_answers(question["answers"])
    return f"{question_block}\n{answer_block}\n"


def print_question(question: dict):
    print(questions_to_str(question))


def print_questions(questions: list):
    pass


