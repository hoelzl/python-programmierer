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
# # Todo-Liste Version 3
#
# In diesem Workshop wollen wir eine Todo-Liste implementieren, und dabei sowohl die
# Liste als auch die Einträge durch Instanzen von Klassen darstellen und die
# Implementierung in den Klassen kapseln.
#
# Es empfiehlt sich, diesen Workshop in einer IDE zu bearbeiten, da die
# letzten Teilaufgaben in Notebooks nicht sinnvoll implementiert werden
# können. **Schreiben Sie Tests zu jeder implementierten Methode,** entweder
# indem Sie im TDD-Stil Test-First arbeiten oder indem Sie unmittlebar nach
# der Implementierung einer Methode Unit-Tests dafür schreiben.
#
# Jeder Eintrag in der Todo-Liste soll folgende Information enthalten:
#
# - Titel
# - Priorität
# - Wurde das Item schon erledigt oder nicht?
#
# Definieren Sie eine Klasse `TodoItem`, die diese Daten kapselt.
#
# Implementieren Sie eine `__init__()`-Methode, die Titel als obligatorisches
# Argument bekommt. Priorität und "wurde erledigt" sollen optionale Parameter
# mit Weren 1 bzw. `False` sein.
#
# Implementieren Sie Methoden `__str__(self)` und `__repr__(self)`,
# die Instanzen der Klasse in Strings umwandeln.
#
# *Hinweise:*
# - Falls Sie V2 der Todo Liste bereits implementiert haben, sollten Sie diese Lösung kopieren und anpassen, da große Teile der Aufgaben übereinstimmen.
# - Sie können auch den `@dataclass` Decorator verwenden um sich die Arbeit zu erleichtern.

# %% [markdown] lang="en"
# # Todo list version 3
#
# In this workshop we want to implement a to-do list, where both the
# list itself as well as individual todo items are represented by instances of classes that encapsulate their implementation.
#
# It's a good idea to perform this workshop in an IDE, because the
# last subtasks cannot be meaningfully implemented in notebooks.
# **Write tests for each implemented method,** either
# by working in a TDD-style test-first manner or by writing a unit test immediately after
# implementing a method.
#
# Each entry in the todo list should contain the following information:
#
# - Title
# - Priority
# - Has the item already been completed or not?
#
# Define a class `TodoItem` that encapsulates this data.
#
# Implement a `__init__()` method, that gets the title as mandatory
# argument gets. Priority and "is completed" should be optional parameters
# with default values 1 and `False`, respectively.
#
# Implement methods `__str__(self)` and `__repr__(self)`, that
# convert the instances of the class to strings.
#
# *Notes:*
#
# - If you have already implemented V2 of the todo list workshop, copy your implementation and enhance it for this workshop, since many parts of the workshops are similar.
# - You can also use the `@dataclass` decorator to make your work easier.

# %% tags=["solution"]
class TodoItem:
    def __init__(self, title, priority=1, is_completed=False):
        self.title = title
        self.priority = priority
        self.is_completed = is_completed

    def __str__(self):
        return f"{self.title}, priority {self.priority}" + (
            "" if not self.is_completed else ", done"
        )

    def __repr__(self):
        return f"TodoItem({self.title!r}, {self.priority!r}, {self.is_completed!r})"


# %% [markdown] lang="de"
# Legen Sie eine Liste mit Todo-Items an, die folgende Einträge
#  enthält:
#
# - Titel: Python lernen, Priorität 3, nicht erledigt
# - Titel: Gemüse einkaufen, Priorität 2, nicht erledigt
# - Titel: Hans anrufen, Priorität 5, erledigt


# %% [markdown] lang="en"
# Create a list of todo items containing the following entries:
#
# - Title: Learn Python, priority 3, not done
# - Title: Buy vegetables, priority 2, not done
# - Title: Call Hans, Priority 5, Done

# %% tags=["solution"]
todos = [
    TodoItem("Python lernen", 3),
    TodoItem("Gemüse einkaufen", 2),
    TodoItem("Hans anrufen", 5, True),
]
todos


# %% [markdown] lang="de"
# Definieren Sie eine Klasse `TodoList`, die eine Todo-Liste repräsentiert.
#
# Implementieren Sie eine `__init__()` Methode, die eine Liste von
# TodoItems beschreiben, als Argument bekommt.
#
# Fügen Sie folgende Methoden hinzu:
#
# - `add(self, title: str, priority: int, is_completed: bool)`, die ein neues
#   Todo-Item an die Todo-Liste anhängt und geeignete Default-Werte für
#   `priority` und `is_completed` übergibt.
#
# - `mark_done(self, title)`, die das erste in der Liste vorkommende
#   Todo-Item mit Titel `title`, das noch nicht bearbeitet ist, als bearbeitet
#   markiert.
#
# - `delete(self, title)`, die das erste in der Liste vorkommende Todo-Item
#   mit Titel `title` aus der Liste entfernt.
#
# - `delete_all_completed(self)`, die alle beendetend Items aus der Liste
#   entfernt.
#
# - `__str__(self)` und `__repr__(self)`
#
# - `__iter__(self)`, so dass in einer `for`-Schleife über alle in der
#   Todo-Liste enthaltenen TodoItems iteriert werden kann.
#
# <!-- *Hinweis*: Kopieren Sie die Implementierung der Methoden aus
# `062z-Lösung Todo-Liste V1` oder ihrer vorherigen Implementierung und
#  passen Sie den Code an. -->

# %% [markdown] lang="en"
# Define a class `TodoList` that represents a todo list.
#
# Implement an `__init__()` method that gets a list of
# `TodoItem` instances as arguments.
#
# Add the following methods:
#
# - `add(self, title: str, priority: int, is_completed: bool)` which creates a new
#   todo item and adds it to the todo list. Use appropriate default values for
#   `priority` and `is_completed`.
#
# - `mark_done(self, title)`, which finds the first todo item in the list that has a matching title and is not yet marked as done, and marks this item as done.
#
# - `delete(self, title)`, which deletes the first todo item in the list
#   that has `title` as title.
#
# - `delete_all_completed(self)`, which deletes all completed items from the list.
#
# - `__str__(self)` and `__repr__(self)`.
#
# - `__iter__(self)` that returns a generator for all items, so that a `for` loop can
#   iterate over all items in the list.

# %% tags=["solution"]
class TodoList:
    def __init__(self, items: list[TodoItem]):
        self.items = items

    def __iter__(self):
        return iter(self.items)

    def add(self, title: str, priority: int = 1, is_completed: bool = False):
        self.items.append(TodoItem(title, priority, is_completed))

    def mark_done(self, title: str):
        for item in self.items:
            if item.title == title and not item.is_completed:
                item.is_completed = True
                return

    def __str__(self):
        from io import StringIO

        result = StringIO()
        print("Todo List:", file=result)
        for item in self.items:
            print(f"  {item!s}", file=result)
        return result.getvalue()

    def __repr__(self):
        return f"TodoList({self.items!r})"


# %% [markdown] lang="de"
# Legen Sie eine Todo-Liste `todos` mit Todo-Items an, die folgende Einträge
#  enthält:
#
# - Titel: Python lernen, Priorität 3, nicht erledigt
# - Titel: Gemüse einkaufen, Priorität 2, nicht erledigt
# - Titel: Hans anrufen, Priorität 5, erledigt

# %% [markdown] lang="en"
# Create a todo list `todos` with todo items, the following entries
#  contains:
#
# - Title: Learn Python, priority 3, not done
# - Title: Buy vegetables, priority 2, not done
# - Title: Call Hans, Priority 5, Done

# %% tags=["solution"]
todo_list = TodoList(todos)
print(todo_list)
todo_list


# %% [markdown] lang="de"
# Fügen Sie ein neues Todo-Item mit Titel "Schnee schaufeln" und Priorität 5
# in die Liste `todos` ein.

# %% [markdown] lang="en"
# Add a new todo item titled "shovel snow" and priority 5
# to the `todos` list.

# %% tags=["solution"]
todo_list.add("Schnee schaufeln", 5)
print(todo_list)

# %% [markdown] lang="de"
# Fügen Sie zwei Todo-Items mit Text "Python lernen" und Priorität 1 und 6
# zur Todo-Liste hinzu.

# %% [markdown] lang="en"
# Add two todo items with text "Learn Python" and priority 1 and 6
# to the todo list.

# %% tags=["solution"]
todo_list.add("Python lernen", 1)
todo_list.add("Python lernen", 6)
print(todo_list)

# %% [markdown] lang="de"
# Markieren Sie ein Todo-Item "Python lernen" als erledigt.
# Wie sieht jetzt Ihre Liste aus?

# %% [markdown] lang="en"
# Mark a "Learn Python" todo item as done.
# How does your list look now?

# %% tags=["solution"]
todo_list.mark_done("Python lernen")
print(todo_list)

# %% [markdown] lang="de"
# Markieren Sie noch zwei Todo-Items `Python lernen` als erledigt.
# Wie sieht jetzt Ihre Liste aus?

# %% [markdown] lang="en"
# Mark two more todo items `Learn Python` as done.
# How does your list look now?

# %% tags=["solution"]
todo_list.mark_done("Python lernen")
print(todo_list)


# %% [markdown] lang="de"
# Fügen Sie zu Ihrer `TodoList` Klasse eine Methode `delete_todo_item(todo_list, title)`
# hinzu, die das erste in der liste `todo_list` vorkommende Todo-Item mit Titel `title`
# aus der Liste entfernt.
#
# *Vorsicht: Sie sollten während Sie über eine Liste iterieren keine Einträge
# entfernen oder einfügen!*

# %% [markdown] lang="en"
# Add a method `delete_todo_item(todo_list, title)` to your `TodoList` class
# which deletes the first todo item in `todo_list` with title `title`.
#
# *Caution: You should not enter any entries while iterating over a list
# remove or insert!*

# %% tags=["solution"]
class TodoList:
    def __init__(self, items: list[TodoItem]):
        self.items = items

    def add(self, title, priority=1, is_completed=False):
        self.items.append(TodoItem(title, priority, is_completed))

    def mark_done(self, title):
        for item in self.items:
            if item.title == title and not item.is_completed:
                item.is_completed = True
                break

    def delete(self, title):
        index_to_delete = -1
        for index, item in enumerate(self.items):
            if item.title == title:
                index_to_delete = index
                break
        if index_to_delete >= 0:
            del self.items[index_to_delete]

    def delete_all_completed(self):
        indices_to_delete = []
        # To keep PyCharm happy
        assert isinstance(self.items, list)
        for index, item in enumerate(self.items):
            if item.is_completed:
                indices_to_delete.append(index)
        import numpy as np

        self.items = np.delete(self.items, indices_to_delete).tolist()

    def __str__(self):
        from io import StringIO

        result = StringIO()
        print("Todo List:", file=result)
        for item in self.items:
            print(f"  {item!s}", file=result)
        return result.getvalue()

    def __repr__(self):
        return f"TodoList({self.items!r})"

    def __iter__(self):
        return (i for i in self.items)


# %% [markdown] lang="de"
# ## Laden und Speichern
#
# Erweitern Sie die Klasse `TodoList` um eine Methode
#
# ```save_to_file(self, file)```
#
# und eine statische Methode
#
# ```load_from_file(file)```
#
# mit der Todo-Listen gespeichert und geladen werden können.
#
# *Hinweis:* Am Einfachsten ist das mit der `pickle` Bibliothek.

# %% [markdown] lang="en"
# ## Loading and saving
#
# Add a method 
#
# ```save_to_file(self, file)```
#
# to the `TodoList` class, and add a static method
#
# ```load_from_file(file)```
#
# with which to-do lists can be saved and loaded.
#
# *Note:* The easiest way is with the `pickle` library.

# %% [markdown] lang="de"
# ## Kommandozeilenargumente
#
# Fügen Sie eine Datei `__main__.py` zu Ihrer Implementierung hinzu, und verarbeiten Sie
# die folgenden Kommandozeilen-Argumente:
#
# - `create file`: erstellt `file` als leere Datei
#
# - `add file title --priority priority` fügt ein neues Todo-Item zu `file`
#   hinzu. `title` ist ein verpflichtendes Argument für den Titel, `prioprity` ist
#   optional
#
# - `delete file title` löscht das erste Todo-Item mit Titel `title` aus der
#   Todo-Liste
#
# - `mark-completed file title` markiert das erste Todo-Item mit Titel `title`
#   als erledigt
#
# - `delete-all-completed file` entfernt alle erledigten Items aus `file`
#
# - `list file` gibt die TODO-Liste aus
#
# - Das positionales Argument `file`, das in allen Subkommandos vorkommt,
#   bennennt eine Datei, in der eine TODO-Liste gespeichert ist bzw.
#   gespeichert werden kann. Dieses Argument muss angegeben werden. Der Inhalt
#   von `file` ist eine   Todo-Liste im `pickle` Format.
#
# Verwenden Sie Typer zur Implementierung des Command-Line Interfaces.
#
# Beispielaufrufe:
#
# ```shell
# $ python -m todos create my-todos.pkl
# $ python -m todos add my-todos.pkl 'Kaufe Äpfel' --priority 1
# $ python -m todos list my-todos.pkl
# Todo List:
#   Kaufe Äpfel, priority 1
# $ python -m todos add my-todos.pkl 'Lese Zeitung' --priority 2
# $ python -m todos mark-completed my-todos.pkl 'Lese Zeitung'
# $ python -m todos list my-todos.pkl
# ```
#
# Die vorgenommenen Änderungen sollen von jedem Kommando in `file` gespeichert werden.

# %% [markdown] lang="en"
# ## Command line arguments
#
# Add a `__main__.py` file to your implementation and edit
# create the following command line arguments using the Typer library:
#
# - `create file`: creates `file` as an empty file
#
# - `add file title --priority priority` adds a new todo item to `file`. `title` is a mandatory argument, `prioprity` is
#   optional
#
# - `delete file title` deletes the first todo item with title `title` from the
#   todo list
#
# - `mark-completed file title` marks the first todo item with title `title`
#   as done
#
# - `delete-all-completed file` removes all completed items from `file`
#
# - `list file` prints the TODO list
#
# - The positional argument `file`, which occurs in all subcommands,
#   names a file in which a TODO list is stored or
#   can be saved. This argument must be specified. The content
#   from `file` is a todo list in `pickle` format.
#
# - Each command should (if applicable) first load the contents of `file`, perform the 
#   necessary changes, and then save the changes back to `file`.
#
# Example calls:
#
# ```shell
# $ python -m todos create my-todos.pkl
# $ python -m todos add my-todos.pkl 'Buy apples' --priority 1
# $ python -m todos list my-todos.pkl
# Todo List:
#   Buy apples, priority 1
# $ python -m todos add my-todos.pkl 'Read newspaper' --priority 2
# $ python -m todos mark-completed my-todos.pkl 'Read newspaper'
# $ python -m todos list my-todos.pkl
# ```

# %%

# %% [markdown] lang="de"
# ## Packaging
#
# Fügen Sie eine `setup.cfg` Datei, sowie alle weiteren benötigten Dateien zu
# Ihrem Projekt hinzu, um daraus eine Wheel-Datei zu generieren.
#
# Erzeugen Sie in der `setup.cfg`-Datei ein Skript, das Ihre Anwendung startet.

# %% [markdown] lang="en"
# ## Packaging
#
# Add a `setup.cfg` file and any other required files
# to your project to generate a wheel file.
#
# In the `setup.cfg` file, create a script that starts your application.

# %%
