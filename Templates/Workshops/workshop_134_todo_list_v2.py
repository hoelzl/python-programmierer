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
# # Todo-Liste Version 2
#
# In diesem Workshop wollen wir wieder eine Todo-Liste implementieren, aber dabei
# sowohl die Liste als auch die Einträge durch Instanzen von Klassen darstellen.
#
# Jeder Eintrag in der Todo-Liste soll wieder folgende Information enthalten:
#
# - Titel
# - Priorität
# - Wurde das Item schon erledigt oder nicht?
#
# Definieren Sie eine Klasse `TodoItem`, die diese Daten kapselt.

# %% [markdown] lang="en"
# # Todo list version 2
#
# In this workshop we want to implement a to-do list, but now we want to
# represent both the list and the entries by instances of classes.
#
# Each entry in the todo list should contain the following information:
#
# - Title
# - Priority
# - Has the item already been completed or not?
#
# Define a class `TodoItem` that encapsulates this data.

# %% tags=["solution"]
class TodoItem:
    def __init__(self, title, priority, is_completed):
        self.title = title
        self.priority = priority
        self.is_completed = is_completed


# %% [markdown] lang="de"
# Erzeugen Sie ein Todo-Item mit folgenden Bestandteilen:
# - Titel: Python lernen
# - Priorität 3
# - nicht erledigt

# %% [markdown] lang="en"
# Create a todo item with the following components:
# - Title: Learn Python
# - Priority 3
# - not done

# %% tags=["solution"]
todo_item = TodoItem("Python lernen", 3, False)
todo_item


# %% [markdown] lang="de"
# Die Repräsentation des Items ist nicht sehr aussagekräftig. Definieren Sie
# deshalb eine Funktion `todo_item_as_string(item: TodoItem) -> str`, die ein
# Todo-Item in einen String umwandelt, der Information über die Bestandteile
# enthält.

# %% [markdown] lang="en"
# The representation of the item is not very meaningful. Define
# therefore a function `todo_item_as_string(item: TodoItem) -> str` which converts a
# todo item into a string that provides information about the item's attributes.

# %% tags=["solution"]
def todo_item_as_string(item):
    return f"{item.title}, priority {item.priority}" + (
        "" if not item.is_completed else ", done"
    )


# %% tags=["solution"]
print(todo_item_as_string(todo_item))
print(todo_item_as_string(TodoItem("Buy food", 2, True)))


# %% [markdown] lang="de"
# Definieren Sie eine Klasse `TodoList`, die eine Todo-Liste repräsentiert.

# %% [markdown] lang="en"
# Define a class `TodoList` that represents a todo list.

# %% tags=["solution"]
class TodoList:
    def __init__(self, items):
        self.items = items


# %% [markdown] lang="de"
# Definieren Sie eine Funktion
#
# `todo_list_as_string(todo_list: TodoList) -> str`,
#
# die eine Todo-Liste in einen String umwandelt, der Information über ihre
# Bestandteile enthält.

# %% [markdown] lang="en"
# Define a function
#
# `todo_list_as_string(todo_list: TodoList) -> str`,
#
# which converts a todo list into a string containing information about its items.

# %% tags=["solution"]
def todo_list_as_string(todo_list):
    from io import StringIO

    result = StringIO()
    print("Todo List:", file=result)
    for item in todo_list.items:
        print("  " + todo_item_as_string(item), file=result)
    return result.getvalue()


# %% [markdown] lang="de"
# Legen Sie eine Todo-Liste `todos` mit Todo-Items an, die folgende Einträge
#  enthält:
#
# - Titel: Python lernen, Priorität 3, nicht erledigt
# - Titel: Gemüse einkaufen, Priorität 2, nicht erledigt
# - Titel: Hans anrufen, Priorität 5, erledigt

# %% [markdown] lang="en"
# Create a todo list `todos` containing the following items:
#
# - Title: Learn Python, priority 3, not done
# - Title: Buy vegetables, priority 2, not done
# - Title: Call Hans, Priority 5, Done

# %% tags=["solution"]
todos = TodoList(
    [
        TodoItem("Python lernen", 3, False),
        TodoItem("Gemüse einkaufen", 2, False),
        TodoItem("Hans anrufen", 5, True),
    ]
)

# %% tags=["solution"]
print(todo_list_as_string(todos))


# %% [markdown] lang="de"
# Schreiben Sie eine Funktion `add_todo_item(todo_list, title, priority)`,
# die ein neues Todo-Item zu `todo_list` hinzufügt.

# %% [markdown] lang="en"
# Write a function `add_todo_item(todo_list, title, priority)`,
# which adds a new todo item to `todo_list`.

# %% tags=["solution"]
def add_todo_item(todo_list, title, priority):
    todo_list.items.append(TodoItem(title, priority, False))


# %% [markdown] lang="de"
# Fügen Sie ein neues Todo-Item mit Titel "Schnee schaufeln" und Priorität 5
# in die Liste `todos` ein.

# %% [markdown] lang="en"
# Add a new todo item titled "shovel snow" with priority 5 to the `todos` list.

# %% tags=["solution"]
add_todo_item(todos, "Schnee schaufeln", 5)

# %% tags=["solution"]
print(todo_list_as_string(todos))


# %% [markdown] lang="de"
#
# Schreiben Sie eine Funktion `mark_todo_item_done(todo_list, title)`,
# die das erste in der Liste `todo_list` vorkommende Todo-Item mit Titel
# `title`, das noch nicht bearbeitet ist, als bearbeitet markiert.

# %% [markdown] lang="en"
# Write a function `mark_todo_item_done(todo_list, title)`,
# that marks as done the first todo item with title 
# `title` that is not yet marked as done.

# %% tags=["solution"]
def mark_todo_item_done(todo_list, title):
    for item in todo_list.items:
        if item.title == title and not item.is_completed:
            item.is_completed = True
            break


# %% [markdown] lang="de"
# Markieren Sie das Todo-Item `Schnee schaufeln` als bearbeitet.

# %% [markdown] lang="en"
# Mark the to-do item `Shovel snow` as done.

# %% tags=["solution"]
mark_todo_item_done(todos, "Schnee schaufeln")

# %% tags=["solution"]
print(todo_list_as_string(todos))

# %% [markdown] lang="de"
# Fügen Sie zwei Todo-Items mit Text "Python lernen" und Priorität 1 und 6
# zur Todo-Liste hinzu.

# %% [markdown] lang="en"
# Add two todo items with text "Learn Python" and priority 1 and 6
# added to the todo list.

# %% tags=["solution"]
add_todo_item(todos, "Python lernen", 1)
add_todo_item(todos, "Python lernen", 6)

# %% tags=["solution"]
print(todo_list_as_string(todos))

# %% [markdown] lang="de"
# Markieren Sie ein Todo-Item "Python lernen" als erledigt.
# Wie sieht jetzt Ihre Liste aus?

# %% [markdown] lang="en"
# Mark a "Learn Python" todo item as done.
# How does your list look now?

# %% tags=["solution"]
mark_todo_item_done(todos, "Python lernen")

# %% tags=["solution"]
print(todo_list_as_string(todos))

# %% [markdown] lang="de"
# Markieren Sie noch zwei Todo-Items `Python lernen` als erledigt.
# Wie sieht jetzt Ihre Liste aus?

# %% [markdown] lang="en"
# Mark two more todo items `Learn Python` as done.
# How does your list look now?

# %% tags=["solution"]
mark_todo_item_done(todos, "Python lernen")
print(todo_list_as_string(todos))

# %% tags=["solution"]
mark_todo_item_done(todos, "Python lernen")
print(todo_list_as_string(todos))


# %% [markdown] lang="de"
# Schreiben Sie eine Funktion `delete_todo_item(todo_list, title)`, die das
# erste in der liste `todo_list` vorkommende Todo-Item mit Titel `title` aus
#  der Liste entfernt.
#
# *Vorsicht: Sie sollten während Sie über eine Liste iterieren keine Einträge
# entfernen oder einfügen!*

# %% [markdown] lang="en"
# Write a function `delete_todo_item(todo_list, title)` that removes the
# first todo item in `todo_list` with title `title`.
#
# *Caution: You should not add or remove any entries while iterating over a list!

# %% tags=["solution"]
def delete_todo_item(todo_list, title):
    index_to_delete = -1
    for index, item in enumerate(todo_list.items):
        if item.title == title:
            index_to_delete = index
            break
    if index_to_delete >= 0:
        del todo_list.items[index_to_delete]


# %% [markdown] lang="de"
# Entfernen Sie eines der Items `Python lernen`.

# %% [markdown] lang="en"
# Remove one of the items `Learn Python`.

# %% tags=["solution"]
delete_todo_item(todos, "Python lernen")
print(todo_list_as_string(todos))

# %% [markdown] lang="de"
# Entfernen Sie dreimal ein Item `Python lernen`. Was erwarten Sie als Ergebnis?

# %% [markdown] lang="en"
# Remove an item `Learn Python` three times. What do you expect as a result?

# %% tags=["solution"]
delete_todo_item(todos, "Python lernen")
print(todo_list_as_string(todos))

# %% tags=["solution"]
delete_todo_item(todos, "Python lernen")
print(todo_list_as_string(todos))

# %% tags=["solution"]
delete_todo_item(todos, "Python lernen")
print(todo_list_as_string(todos))


# %% [markdown] lang="de"
# Schreiben Sie eine Funktiion `delete_all_completed_todo_items(todo_list)`,
# die alle erledigten Todo-Items aus `todo_list` löscht.
#
# *Hinweis: Sie benötigen dazu wahrscheinlich zwei aufeinanderfolgende
# `for`-Schleifen: eine um die Indizes zu bestimmen und eine um sie zu löschen*

# %% [markdown] lang="en"
# Write a function `delete_all_completed_todo_items(todo_list)`,
# which deletes all completed todo items from `todo_list`.
#
# *Note: You will probably need two consecutive `for` loops to do this: one to collect the indices and one to clear them*

# %% tags=["solution"]
def delete_all_completed_todo_items(todo_list):
    indices_to_delete = []
    for index, item in enumerate(todo_list.items):
        if item.is_completed:
            indices_to_delete.append(index)
    for index in sorted(indices_to_delete, reverse=True):
        del todo_list.items[index]


# %% tags=["solution"]
delete_all_completed_todo_items(todos)
print(todo_list_as_string(todos))

# %% [markdown] lang="de"
# Testen Sie Ihre Implementierung von `delete_all_completed_todo_items()` mit
# der folgenden Liste:

# %% [markdown] lang="en"
# Test your implementation of `delete_all_completed_todo_items()` with
# the following list:

# %% tags=["solution"]
todo_list_2 = TodoList([TodoItem(f"Item {n}", 1, n % 2 == 0) for n in range(10)])
print(todo_list_as_string(todo_list_2))

# %% tags=["solution"]
delete_all_completed_todo_items(todo_list_2)
print(todo_list_as_string(todo_list_2))

# %%
