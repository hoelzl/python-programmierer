# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
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

# %% pycharm={"name": "#%%\n"}

# %% [markdown] pycharm={"name": "#%% md\n"}
# Testen Sie die Klasse (interaktiv falls Sie die Aufgabe im Notebook bearbeiten,
# sonst mit pytest)

# %% pycharm={"name": "#%%\n"}

# %% pycharm={"name": "#%%\n"}

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Implementieren Sie jetzt eine Klasse `TriviaGame`, die eine Liste von
# `Question`-Instanzen enthält und eine Methode `run(self)` hat, die
#
# - zufällig eine Frage auswählt,
# - den Fragetext auf dem Bildschirm ausgibt,
# - den Benutzer nach seiner Antwort fragt,
# - die Antwort des Benutzers überprüft und
# - einen Text ausgibt, ob die Antwort richtig oder falsch war.
#
# Eine leere Eingabe soll das Spiel abbrechen. Am Ende des Spiels soll die Anzahl
# der beantworteten Fragen und der Prozentsatz der korrekt beantworteten Fragen
# zurückgegeben werden.
#
# *Hinweis:* Es empfiehlt sich einige Hilfsmethoden zu implementieren, die einen
# *Teil der Funktionalität von `run()` übernehmen. Eine Möglichkeit wäre
#
# - `percentage_questions_answered_correctly(self)` gibt den Prozentsatz der
#   richtig beantworteten Fragen zurück. (Achten Sie auf den Fall, dass der
#   Benutzer keine Frage beantwortet hat). Für diese Methode empfiehlt sich eine
#   Implementierueng als Property.
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
# - `print_reply()` gibt eine Antwort basierend auf der Frage und dem "Statuscode"
#   zurück.
#  
#

# %% pycharm={"name": "#%%\n"}

# %% pycharm={"name": "#%%\n"}

# %% pycharm={"name": "#%%\n"}

# %% pycharm={"name": "#%%\n"}

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# ## Packaging
#
# Fügen Sie eine `setup.py` Datei, sowie alle weiteren benötigten Dateien zu Ihrem Projekt hinzu, um daraus eine Wheel-Datei zu generieren.
#
# Erzeugen Sie in der `setup.py`-Datei ein Skript, das Ihre Anwendung startet.

# %%
