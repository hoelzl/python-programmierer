# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] lang="de"
# # Quiz
#
# Wir wollen ein Quiz in Python implementieren.
#
# Obwohl es möglich ist, die Implementierung in einem Notebook zu beginnen wäre es
# besser, dieses Projekt in einem IDE zu starten und das Notebook nur als
# Anleitung herzunehmen, da die späteren Teile im IDE besser zu realisieren sind.
#
# Definieren Sie eine Klasse `Question`, die einzelne Fragen und korrekte
# Antworten repräsentiert. Der Zustand der Klasse ist
#
# - Ein String `text`, der den Text der Frage darstellt.
# - Eine Liste von Strings `answers`, die die richtigen Antworten darstellen.
#
# `Question` hat die folgende Methoden:
#
# - `is_answer_correct(self, answer: str)`: überprüft, ob der String  `answer`
#   eine korrekte Antwort auf die Frage ist.
# - `correct_answer(self)`: Gibt eine der korrekten Antworten zurück.

# %% [markdown] lang="en"
# # Quiz
#
# We want to implement a quiz in Python.
#
# Although it is possible to start implementing it in a notebook it would be
# better to start this project in an IDE and use the notebook only for
# instructions, since the later parts are easier to implement in an IDE.
#
# Define a class `Question` representing a single questions and multiple correct
# answers. The attributes of the class are:
#
# - A string `text` representing the text of the question.
# - A list of strings `answers` representing the correct answers.
#
# `Question` has the following methods:
#
# - `is_answer_correct(self, answer: str)`: checks whether the string `answer`
#   is a correct answer to the question.
# - `correct_answer(self)`: Returns one of the correct answers.

# %% tags=["solution"]
class Question:
    def __init__(self, text, answers):
        self.text = text
        self.answers = answers

    def __str__(self):
        return f"{self.text!s}"

    def __repr__(self):
        return f"Question({self.text!r}, {self.answers!r})"

    def is_answer_correct(self, answer):
        return answer in self.answers

    def correct_answer(self):
        return self.answers[0]


# %% [markdown] lang="de"
#
# Testen Sie die Klasse (interaktiv, falls Sie die Aufgabe im Notebook
# bearbeiten, sonst mit pytest)

# %% [markdown] lang="en"
# Test the class (interactively if you did the assignment in the notebook, else with
# pytest)

# %% tags=["solution"]
questions = [
    Question("Wann wurde Napoleon geboren?", ["15. August 1769", "1769"]),
    Question("Wann wurde Python erfunden?", ["1991"]),
    Question(
        "Wer ist Pythons Benevolent Dictator For Life?",
        ["Guido van Rossum", "Guido v. Rossum"],
    ),
]
questions

# %% tags=["solution"]
questions[0].is_answer_correct("15. August 1769")

# %% tags=["solution"]
questions[0].correct_answer()

# %% [markdown] lang="de"
# Implementieren Sie jetzt eine Klasse `TriviaGame`, die eine Liste von
# `Question`-Instanzen enthält und eine Methode `run(self)` hat, die
#
# - zufällig eine Frage auswählt,
# - den Fragetext auf dem Bildschirm ausgibt,
# - den Benutzer nach seiner Antwort fragt,
# - die Antwort des Benutzers überprüft und
# - einen Text ausgibt, ob die Antwort richtig oder falsch war.
#
# Eine leere Eingabe soll das Spiel abbrechen. Am Ende des Spiels soll die
# Anzahl der beantworteten Fragen und der Prozentsatz der korrekt
# beantworteten Fragen zurückgegeben werden.
#
# *Hinweis:* Es empfiehlt sich einige Hilfsmethoden zu implementieren, die einen
# *Teil der Funktionalität von `run()` übernehmen. Eine Möglichkeit wäre
#
# - `percentage_questions_answered_correctly(self)` gibt den Prozentsatz der
#   richtig beantworteten Fragen zurück. (Achten Sie auf den Fall, dass der
#   Benutzer keine Frage beantwortet hat). Für diese Methode empfiehlt sich eine
#   Implementierung als Property.
#
# - `pick_random_question(self)` wählt zufällig eine der Fragen aus. Hierfür
#   leistet die Funktion `random.choice()` gute Dienste
#
# - `query_user_for_answer(self, question: Question)` und gibt diese zurück
#
# - `process_answer(self, question: Question, answer: str)` , wertet die Antwort
#   aus und gibt einen "Statuscode" zurück, der eine der folgende Möglichkeiten
#   beschreibt:
#
#   - Die Frage wurde korrekt beantwortet.
#   - Die Frage wurde falsch beantwortet.
#   - Der Spieler möchte das Spiel beenden.
#
# - `print_reply()` gibt eine Antwort basierend auf der Frage und dem
#   "Statuscode" zurück.

# %% [markdown] lang="en"
# Now implement a class `TriviaGame` that has a list of
# `Question` instances and has a `run(self)` method that
#
# - randomly selects a question,
# - outputs the question text on the screen,
# - asks the user for their answer,
# - checks the user's answer and
# - outputs a text whether the answer was right or wrong.
#
# An empty input should abort the game. At the end of the game the
# number of questions answered and the percentage of correct
# answers are printed out.
#
# *Note:* It's a good idea to implement some helper methods that
# *Take over part of the functionality of `run()`. An option would be
#
# - `percentage_questions_answered_correctly(self)` returns the percentage of
#   correctly answered questions. (Pay attention to the case that the
#   user did not answer a question). For this method, an implementation as property
#   might be appropriate.
#
# - `pick_random_question(self)` randomly selects one of the questions. The
#   `random.choice()` function is very helpful for this
#
# - `query_user_for_answer(self, question: Question)` asks the user for an answer and
#   returns it
#
# - `process_answer(self, question: Question, answer: str)` , evaluates the answer
#   and returns a "status code" with one of the following meanings:
#
#   - The question was answered correctly.
#   - The question was answered incorrectly.
#   - The player wants to end the game.
#
# - `print_reply()` prints out a reply based on the question and the
#   "Status Code".

# %% tags=["solution"]
from random import choice


class TriviaGame:
    EXIT = "EXIT"
    CORRECT_ANSWER = "CORRECT_ANSWER"
    FALSE_ANSWER = "FALSE_ANSWER"

    def __init__(self, questions):
        self.questions = questions
        self.total_questions_answered = 0
        self.questions_answered_correctly = 0

    @property
    def percentage_questions_answered_correctly(self):
        total = self.total_questions_answered
        if total == 0:
            return 0.0
        return self.questions_answered_correctly / total

    def pick_random_question(self):
        """Pick a random question from all available ones."""
        return choice(self.questions)

    @staticmethod
    def query_user_for_answer(question):
        """Ask the user for an answer to the question.

        :param question: the question
        :return: the user's answer to the question
        """
        print(question.text)
        return input("Ihre Antwort: ")

    def process_answer(self, question):
        """Processes an answer to a question.

        Returns True if the game should continue, false otherwise
        :param question: the question we asked the user
        :return: status code indicating whether the answer was correct or not,
                 or whether the user wants to quit the game
        """
        answer = self.query_user_for_answer(question)
        if answer == "":
            return self.EXIT
        elif question.is_answer_correct(answer):
            self.total_questions_answered += 1
            self.questions_answered_correctly += 1
            return self.CORRECT_ANSWER
        else:
            self.total_questions_answered += 1
            return self.FALSE_ANSWER

    def print_reply(self, question, answer_status):
        """
        Print a reply to the user's input.

        :param question: the question we asked the user
        :param answer_status: the status code returned by process_answer()
        :return: nothing
        """
        if answer_status == self.EXIT:
            print("Auf Wiedersehen!")
            print(
                f"Sie haben {self.percentage_questions_answered_correctly}% "
                f"von {self.total_questions_answered} Fragen richtig "
                "beantwortet."
            )
        elif answer_status == self.CORRECT_ANSWER:
            print("Hervorragend!")
        else:
            print(
                f"Leider nein. Die richtige Antwort ist '{question.correct_answer()}''"
            )

    def run(self):
        while True:
            question = self.pick_random_question()
            result = self.process_answer(question)
            self.print_reply(question, result)
            if result == self.EXIT:
                break


# %% tags=["solution"]
my_game = TriviaGame(questions)

# %% tags=["solution"]
my_game.pick_random_question()

# %% tags=["solution"]
# my_game.process_answer(my_game.pick_random_question())

# %% tags=["solution"]
# my_game.run()
