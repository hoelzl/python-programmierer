# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
# j2 import 'macros.j2' as doc
# %% [markdown]
# # Todo-Liste Version 3
#
# In diesem Workshop wollen wir eine Todo-Liste implementieren, und dabei sowohl die
# Liste als auch die Einträge durch Instanzen von Klassen darstellen und die
# Implementierung in den Klassen kapseln.
#
# Es empfiehlt sich, diesen Workshop in einer IDE zu bearbeiten, da die
# letzten Teilaufgaben in Notebooks nicht sinnvoll implementiert werden
# können. Schreiben Sie Tests zu jeder implementierten Methode, entweder
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
# Sie können auch den `@dataclass` Decorator verwenden um sich die Arbeit zu erleichtern.

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


# %% [markdown]
# Legen Sie eine Liste mit Todo-Items an, die folgende Einträge
#  enthält:
#
# - Titel: Python lernen, Priorität 3, nicht erledigt
# - Titel: Gemüse einkaufen, Priorität 2, nicht erledigt
# - Titel: Hans anrufen, Priorität 5, erledigt


# %% tags=["solution"]
todos = [
    TodoItem("Python lernen", 3),
    TodoItem("Gemüse einkaufen", 2),
    TodoItem("Hans anrufen", 5, True),
]
todos


# %% [markdown]
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


# %% [markdown]
# Legen Sie eine Todo-Liste `todos` mit Todo-Items an, die folgende Einträge
#  enthält:
#
# - Titel: Python lernen, Priorität 3, nicht erledigt
# - Titel: Gemüse einkaufen, Priorität 2, nicht erledigt
# - Titel: Hans anrufen, Priorität 5, erledigt

# %% tags=["solution"]
todo_list = TodoList(todos)
print(todo_list)
todo_list


# %% [markdown]
# Fügen Sie ein neues Todo-Item mit Titel "Schnee schaufeln" und Priorität 5
# in die Liste `todos` ein.

# %% tags=["solution"]
todo_list.add("Schnee schaufeln", 5)
print(todo_list)

# %% [markdown]
# Fügen Sie zwei Todo-Items mit Text "Python lernen" und Priorität 1 und 6
# zur Todo-Liste hinzu.

# %% tags=["solution"]
todo_list.add("Python lernen", 1)
todo_list.add("Python lernen", 6)
print(todo_list)

# %% [markdown]
# Markieren Sie ein Todo-Item "Python lernen" als erledigt.
# Wie sieht jetzt Ihre Liste aus?

# %% tags=["solution"]
todo_list.mark_done("Python lernen")
print(todo_list)

# %% [markdown]
# Markieren Sie noch zwei Todo-Items `Python lernen` als erledigt.
# Wie sieht jetzt Ihre Liste aus?

# %% tags=["solution"]
todo_list.mark_done("Python lernen")
print(todo_list)


# %% [markdown]
# Fügen Sie zu Ihrer `TodoList` Klasse eine Methode `delete_todo_item(todo_list, title)`
# hinzu, die das erste in der liste `todo_list` vorkommende Todo-Item mit Titel `title`
# aus der Liste entfernt.
#
# *Vorsicht: Sie sollten während Sie über eine Liste iterieren keine Einträge
# entfernen oder einfügen!*

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


# %% [markdown]
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

# %% [markdown]
# ## Kommandozeilenargumente
#
# Fügen Sie eine Datei `__main__.py` zu Ihrer Implementierung hinzu, und bearbeiten Sie
# mit der Typer die folgenden Kommandozeilen-Argumente:
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
# Beispielaufrufe:
#
# ```shell
# $ python -m todos add .\my-todos.json 'Kaufe Äpfel' 1
# $ python -m todos add .\my-todos.json list
# ```
#
# Die vorgenommenen Änderungen sollen von jedem Kommando in `file` gespeichert werden.

# %%

# %% [markdown]
# ## Packaging
#
# Fügen Sie eine `setup.cfg` Datei, sowie alle weiteren benötigten Dateien zu
# Ihrem Projekt hinzu, um daraus eine Wheel-Datei zu generieren.
#
# Erzeugen Sie in der `setup.cfg`-Datei ein Skript, das Ihre Anwendung startet.

# %%
