from ..questions import questions_to_str, print_question


def test_question_to_str():
    question = {
        "text":    "Question",
        "answers": ["Answer 1", "Answer 2"]
    }
    expected = ("Question:\n"
                "  Question\n"
                "Answers:\n"
                "  1. Answer 1\n"
                "  2. Answer 2\n")
    assert questions_to_str(question) == expected


def test_print_question(capsys):
    question = {
        "text":    "Question",
        "answers": ["Answer 1", "Answer 2"]
    }
    expected = ("Question:\n"
                "  Question\n"
                "Answers:\n"
                "  1. Answer 1\n"
                "  2. Answer 2\n")
    print_question(question)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected.strip()


def test_print_questions(capsys):
    questions = [{
        "text":    "Question",
        "answers": ["Answer 1", "Answer 2"]
    },
        {
            "text":    "Question 2",
            "answers": ["Answer 2.1"]
        }]
    expected = ""
    ...
