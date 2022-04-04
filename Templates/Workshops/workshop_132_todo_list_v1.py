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
# # TODO-Liste Version 1
#
# Im Folgenden soll eine einfache Anwendung zur Verwaltung einer TODO-Liste
# erstellt werden.
#
# Jeder Eintrag in der TODO-Liste soll folgende Information enthalten:
#
# - Titel
# - Priorität
# - Wurde das Item schon erledigt oder nicht?
#
# Verwenden Sie im Folgenden ein Dictionary um einen Eintrag in der TODO-Liste
# darzustellen und eine Liste um die TODO-Liste zu repräsentieren:

# %% [markdown] lang="en"
# # TODO list version 1
#
# The this workshop a simple application for managing a TODO list
# should to be created.
#
# Each entry in the TODO list should contain the following information:
#
# - Title
# - Priority
# - Has the item already been completed or not?
#
# In the following, use a dictionary for each entry in the TODO list
# and a list to represent the TODO list:

# %% [markdown] lang="de"
# Legen Sie eine Liste `todos` mit Todo-Items an, die folgende Einträge enthält:
#
# - Titel: Python lernen, Priorität 3, nicht erledigt
# - Titel: Gemüse einkaufen, Priorität 2, nicht erledigt
# - Titel: Hans anrufen, Priorität 5, erledigt

# %% [markdown] lang="en"
# Create a list `todos` with todo items that contains the following entries:
#
# - Title: Learn Python, priority 3, not done
# - Title: Buy vegetables, priority 2, not done
# - Title: Call Hans, Priority 5, Done

# %% tags=["solution"]
todos = [dict(title="Python lernen", priority=3, is_completed=False)]
todos

# %% tags=["solution"]
todos = [
    {"title": "Python lernen", "priority": 3, "is_completed": False},
    {"title": "Gemüse einkaufen", "priority": 2, "is_completed": False},
    {"title": "Hans anrufen", "priority": 5, "is_completed": True},
]

# %% tags=["solution"]
todos


# %% [markdown] lang="de"
# Schreiben Sie eine Funktion `add_todo_item(todo_list, title, priority)`,
# die ein neues Todo-Item zu `todo_list` hinzufügt.

# %% [markdown] lang="en"
# Write a function `add_todo_item(todo_list, title, priority)`,
# which adds a new todo item to `todo_list`.

# %% tags=["solution"]
def add_todo_item(todo_list, title, priority):
    todo_list.append({"title": title, "priority": priority, "is_completed": False})


# %% [markdown] lang="de"
# Fügen Sie ein neues Todo-Item mit Titel "Schnee schaufeln" und Priorität 5
#  in die Liste `todos` ein.

# %% [markdown] lang="en"
# Add a new todo item titled "shovel snow" with priority 5 to the `todos` list.

# %% tags=["solution"]
add_todo_item(todos, "Schnee schaufeln", 5)

# %% tags=["solution"]
todos


# %% [markdown] lang="de"
# Schreiben Sie eine Funktion `mark_todo_item_done(todo_list, title)`,
# die das erste in der Liste `todo_list` vorkommende Todo-Item mit Titel
#  `title`, das noch nicht bearbeitet ist, als bearbeitet markiert.

# %% [markdown] lang="en"
# Write a function `mark_todo_item_done(todo_list, title)`, that marks as done
# the first todo item in `todo_list` list that has title `title` and is not yet marked as done.

# %% tags=["solution"]
def mark_todo_item_done(todo_list, title):
    for item in todo_list:
        if item["title"] == title and not item["is_completed"]:
            item["is_completed"] = True
            break


# %% [markdown] lang="de"
# Markieren Sie das Todo-Item `Schnee schaufeln` als bearbeitet.

# %% [markdown] lang="en"
# Mark the to-do item `shovel snow` as edited.

# %% tags=["solution"]
mark_todo_item_done(todos, "Schnee schaufeln")

# %% tags=["solution"]
todos

# %% [markdown] lang="de"
# Fügen Sie zwei Todo-Items mit Text "Python lernen" und Priorität 1 und 6
#  zur Todo-Liste hinzu.

# %% [markdown] lang="en"
# Add two todo items with text "Learn Python" and priority 1 and 6 to the todo list.

# %% tags=["solution"]
add_todo_item(todos, "Python lernen", 1)
add_todo_item(todos, "Python lernen", 6)

# %% tags=["solution"]
todos

# %% [markdown] lang="de"
# Markieren Sie ein Todo-Item "Python lernen" als erledigt. Wie sieht jetzt
#  Ihre Liste aus?

# %% [markdown] lang="en"
# Mark a "Learn Python" todo item as done. How does your list look now?

# %% tags=["solution"]
mark_todo_item_done(todos, "Python lernen")

# %% tags=["solution"]
todos

# %% [markdown] lang="de"
# Markieren Sie noch ein Todo-Item "Python lernen" als erledigt. Wie sieht
#  jetzt Ihre Liste aus?

# %% [markdown] lang="en"
# Mark another todo item "Learn Python" as done. What is the contents of your list?

# %% tags=["solution"]
mark_todo_item_done(todos, "Python lernen")
todos


# %% [markdown] lang="de"
#
# Schreiben Sie eine Funktion `delete_todo_item(todo_list, title)`, die das
# erste in der liste `todo_list` vorkommende Todo-Item mit Titel `title` aus
#  der Liste entfernt.
#
# *Vorsicht: Sie sollten während Sie über eine Liste iterieren keine Einträge
# entfernen oder einfügen!*

# %% [markdown] lang="en"
# Write a function `delete_todo_item(todo_list, title)` that removes the
# first todo item in the `todo_list` with the title `title`.
#
# *Caution: You should not add or remove any entries while iterating over a list!*

# %% tags=["solution"]
def delete_todo_item(todo_list, title):
    index_to_delete = -1
    for index, item in enumerate(todo_list):
        if item["title"] == title:
            index_to_delete = index
            break
    if index_to_delete >= 0:
        del todo_list[index_to_delete]


# %% [markdown] pycharm={"name": "#%% md\n"} lang="de"
# Löschen Sie ein item `Python lernen` aus `todo_list`

# %% [markdown] lang="en"
# Delete an item `Learn Python` from `todo_list`

# %% tags=["solution"]
delete_todo_item(todos, "Python lernen")
todos


# %% [markdown] lang="de"
# Schreiben Sie eine Funktiion `delete_all_completed_todo_items(todo_list)`,
# die alle erledigten Todo-Items aus `todo_list` löscht.
#
# *Hinweis: Eine Möglichkeit diese Aufgabe zu lösen sind zwei
# aufeinanderfolgende `for`-Schleifen: eine um die Indizes zu bestimmen und
# eine um sie zu löschen. Beachten Sie die Reihenfolge, in der Sie Items
# löschen! Eine elegantere Methode ist eine List Comprehension und Zuweisung
# an ein Slice zu verwenden.*

# %% [markdown] lang="en"
# Write a function `delete_all_completed_todo_items(todo_list)`,
# which deletes all completed todo items from `todo_list`.
#
# *Note: One possibility to solve this task consists of two
# consecutive `for` loops: one to determine the indices and
# one to erase them. Does the order in which you delete items matter? (Hint: It does!)
#
# A more elegant method is to use a list comprehension and assign to a slice containing the complete original list.*

# %% tags=["solution"]
def delete_all_completed_todo_items(todo_list):
    indices_to_delete = []
    for index, item in enumerate(todo_list):
        if item["is_completed"]:
            indices_to_delete.append(index)
    for index in sorted(indices_to_delete, reverse=True):
        del todo_list[index]


# %% tags=["solution"]
# delete_all_completed_todo_items(todos)
todos


# %% tags=["solution"]
def delete_all_completed_todo_items_v2(todo_list):
    todo_list[:] = [item for item in todo_list if not item["is_completed"]]


# %% tags=["solution"]
delete_all_completed_todo_items_v2(todos)
todos

# %%
