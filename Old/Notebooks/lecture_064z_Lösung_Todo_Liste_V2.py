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
# # Todo-Liste
#
# In diesem Workshop wollen wir zum dritten Mal eine Todo-Liste implementieren, aber dabei sowohl die Liste als auch die Einträge durch Instanzen von Klassen darstellen und die Implementierung in den Klassen kapseln.
#
# Es empfiehlt sich, diesen Workshop in einer IDE zu bearbeiten, da die letzten Teilaufgaben in Notebooks nicht sinnvoll implementiert werden können. Schreiben Sie Tests zu jeder implementierten Methode, entweder indem Sie im TDD-Stil Test-First arbeiten oder indem Sie unmittlebar nach der Implementierung einer Methode Unit-Tests dafür schreiben.
#
# Jeder Eintrag in der Todo-Liste soll wieder folgende Information enthalten:
#
# - Titel
# - Priorität
# - Wurde das Item schon erledigt oder nicht?
#
# Definieren Sie eine Klasse `TodoItem`, die diese Daten kapselt. 
#
# Implementieren Sie eine `__init__()`-Methode, die Titel als obligatorisches Argument bekommt. Priorität und "wurde erledigt" sollen optionale Parameter mit Weren 1 bzw. `False` sein.
#
# Implementieren Sie Methoden `__str__(self)` und `__repr__(self)`, die Instanzen der Klasse in Strings umwandeln.

# %% pycharm={"name": "#%%\n"}
class TodoItem:
    def __init__(self, title, priority=1, is_completed=False):
        self.title = title
        self.priority = priority
        self.is_completed = is_completed

    def __str__(self):
        return f"{self.title}, priority {self.priority}" + ("" if not self.is_completed else ", done")
    
    def __repr__(self):
        return f"TodoItem({self.title!r}, {self.priority!r}, {self.is_completed!r})"


# %%
todos = [TodoItem('Python lernen', 3),
         TodoItem('Gemüse einkaufen', 2),
         TodoItem('Hans anrufen', 5,  True)]
todos

# %% [markdown]
# Definieren Sie eine Klasse `TodoList`, die eine Todo-Liste repräsentiert.
#
# Implementieren Sie eine `__init__()` Methode, die eine Liste von Dictionaries, die TodoItems beschreiben, als Argument bekommt und daraus eine Liste von `TodoItem`-Instanzen erzeugt und speichert.
#
# Fügen Sie folgende Methoden hinzu:
#
# - `add(self, title: str, priority: int, is_completed: bool)`, die ein neues Todo-Item an die Todo-Liste anhängt und 
#   geeignete Default-Werte für `priority` und `is_completed` übergibt.
# - `mark_done(self, title)`, die das erste in der Liste vorkommende Todo-Item mit Titel `title`, das noch nicht bearbeitet ist, als bearbeitet markiert.
# - `delete(self, title)`, die das erste in der Liste vorkommende Todo-Item mit Titel `title` aus der Liste entfernt.
# - `delete_all_completed(self)`, die alle beendetend Items aus der Liste entfernt.
# - `__str__(self)` und `__repr__(self)`
# - `__iter__(self)`, so dass in einer `for`-Schleife über alle in der Todo-Liste enthaltenen TodoItems iteriert werden kann.
#
# <!--
# *Hinweis*: Kopieren Sie die Implementierung der Methoden aus `062z-Lösung Todo-Liste V1` oder ihrer vorherigen Implementierung und passen Sie den Code an.
# -->

# %% pycharm={"name": "#%%\n"}
from typing import List

class TodoList:
    def __init__(self, items: List[TodoItem]):
        self.items = items

    def add(self, title, priority=1, is_completed=False):
        self.items.append(TodoItem(title, priority, is_completed))

    def mark_done(self, title):
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


# %%
todo_list = TodoList(todos)
print(str(todo_list))
todo_list

# %%
todo_list.add("Schnee schaufeln", 5)

# %%
print(str(todo_list))

# %%
todo_list.add("Python lernen", 1)
todo_list.add("Python lernen", 6)

# %%
print(str(todo_list))

# %%
todo_list.mark_done("Python lernen")

# %%
print(str(todo_list))

# %%
todo_list.mark_done("Python lernen")

# %%
print(str(todo_list))

# %% pycharm={"name": "#%%\n"}
from typing import List

class TodoList:
    def __init__(self, items):
        self.items: List[TodoItem] = [TodoItem(**spec) for spec in items]

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

# %%

# %% [markdown]
# ## Kommandozeilenargumente
#
# Fügen Sie eine Datei `main.py` zu Ihrer Implementierung hinzu, die einen `ArgumentParser` instanziieren, der folgende Subkommandos verarbeiten kann:
#
# - `create file`: erstellt `file` neu mit Größe 0
# - `add file title --priority priority` fügt ein neues Todo-Item zu `file` hinzu
# - `delete file title` löscht das erste Todo-Item mit Titel `title` aus der Todo-Liste
# - `mark-completed file title` markiert das erste Todo-Item mit Titel `title` als erledigt
# - `delete-all-completed file` entfernt alle erledigten Items aus `file`
# - `list file` gibt die TODO-Liste aus
#
# - Das positionales Argument `file`, das in allen Subkommandos vorkommt, bennennt eine Datei, in der eine TODO-Liste gespeichert ist bzw. gespeichert werden kann. Dieses Argument muss angegeben werden. Der Inhalt von `file` ist eine   Todo-Liste im `pickle` Format.
#
# Beispielaufrufe:
#
# ```shell
# $ python -m todos.main add .\my-todos.json 'Kaufe Äpfel' 1
# $ python -m todos.main add .\my-todos.json list
# ```
#
# Die vorgenommenen Änderungen sollen in `file` gespeichert werden.

# %%

# %% [markdown]
# ## Packaging
#
# Fügen Sie eine `setup.py` Datei, sowie alle weiteren benötigten Dateien zu Ihrem Projekt hinzu, um daraus eine Wheel-Datei zu generieren.
#
# Erzeugen Sie in der `setup.py`-Datei ein Skript, das Ihre Anwendung startet.

# %%
