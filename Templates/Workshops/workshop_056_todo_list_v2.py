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
# In diesem Workshop wollen wir die eine Todo-Liste implementieren, aber dabei
# sowohl die Liste als auch die Einträge durch Instanzen von Klassen darstellen.
#
# Jeder Eintrag in der Todo-Liste soll wieder folgende Information enthalten:
#
# - Titel
# - Priorität
# - Wurde das Item schon erledigt oder nicht?
#
# Definieren Sie eine Klasse `TodoItem`, die diese Daten kapselt.

# %%  {{ solution() }}
class TodoItem:
    def __init__(self, title, priority, is_completed):
        self.title = title
        self.priority = priority
        self.is_completed = is_completed


# %% [markdown]
# Erzeugen Sie ein Todo-Item mit folgenden Bestandteilen:
# - Titel: Python lernen
# - Priorität 3
# - nicht erledigt

# %%  {{ solution() }}
todo_item = TodoItem('Python lernen', 3, False)
todo_item


# %% [markdown]
# Die Repräsentation des Items ist nicht sehr aussagekräftig. Definieren Sie
# deshalb eine Funktion `todo_item_as_string(item: TodoItem) -> str`, die ein
# Todo-Item in einen String umwandelt, der Information über die Bestandteile
# enthält.

# %%  {{ solution() }}
def todo_item_as_string(item):
    return f"{item.title}, priority {item.priority}" \
           + ("" if not item.is_completed else ", done")


# %%  {{ solution() }}
print(todo_item_as_string(todo_item))
print(todo_item_as_string(TodoItem("Buy food", 2, True)))


# %% [markdown]
# Definieren Sie eine Klasse `TodoList`, die eine Todo-Liste repräsentiert.

# %%  {{ solution() }}
class TodoList:
    def __init__(self, items):
        self.items = items


# %% [markdown]
# Definieren Sie eine Funktion
#
# `todo_list_as_string(todo_list: TodoList) -> str`,
#
# die eine Todo-Liste in einen String umwandelt, der Information über ihre
# Bestandteile enthält.

# %%  {{ solution() }}
def todo_list_as_string(todo_list):
    from io import StringIO
    result = StringIO()
    print("Todo List:", file=result)
    for item in todo_list.items:
        print("  " + todo_item_as_string(item), file=result)
    return result.getvalue()


# %% [markdown]
# Legen Sie eine Todo-Liste `todos` mit Todo-Items an, die folgende Einträge
#  enthält:
#
# - Titel: Python lernen, Priorität 3, nicht erledigt
# - Titel: Gemüse einkaufen, Priorität 2, nicht erledigt
# - Titel: Hans anrufen, Priorität 5, erledigt

# %%  {{ solution() }}
todos = TodoList([TodoItem('Python lernen', 3, False),
                  TodoItem('Gemüse einkaufen', 2, False),
                  TodoItem('Hans anrufen', 5, True)])

# %%  {{ solution() }}
print(todo_list_as_string(todos))


# %% [markdown]
# Schreiben Sie eine Funktion `add_todo_item(todo_list, title, priority)`,
# die ein neues Todo-Item zu `todo_list` hinzufügt.

# %%  {{ solution() }}
def add_todo_item(todo_list, title, priority):
    todo_list.items.append(TodoItem(title, priority, False))


# %% [markdown]
# Fügen Sie ein neues Todo-Item mit Titel "Schnee schaufeln" und Priorität 5
# in die Liste `todos` ein.

# %%  {{ solution() }}
add_todo_item(todos, "Schnee schaufeln", 5)

# %%  {{ solution() }}
print(todo_list_as_string(todos))


# %% [markdown]
#
# Schreiben Sie eine Funktion `mark_todo_item_done(todo_list, title)`,
# die das erste in der Liste `todo_list` vorkommende Todo-Item mit Titel
# `title`, das noch nicht bearbeitet ist, als bearbeitet markiert.

# %%  {{ solution() }}
def mark_todo_item_done(todo_list, title):
    for item in todo_list.items:
        if item.title == title and not item.is_completed:
            item.is_completed = True
            break


# %% [markdown]
# Markieren Sie das Todo-Item `Schnee schaufeln` als bearbeitet.

# %%  {{ solution() }}
mark_todo_item_done(todos, "Schnee schaufeln")

# %%  {{ solution() }}
print(todo_list_as_string(todos))

# %% [markdown]
# Fügen Sie zwei Todo-Items mit Text "Python lernen" und Priorität 1 und 6
# zur Todo-Liste hinzu.

# %%  {{ solution() }}
add_todo_item(todos, "Python lernen", 1)
add_todo_item(todos, "Python lernen", 6)

# %%  {{ solution() }}
print(todo_list_as_string(todos))

# %% [markdown]
# Markieren Sie ein Todo-Item "Python lernen" als erledigt.
# Wie sieht jetzt Ihre Liste aus?

# %%  {{ solution() }}
mark_todo_item_done(todos, "Python lernen")

# %%  {{ solution() }}
print(todo_list_as_string(todos))

# %% [markdown]
# Markieren Sie noch zwei Todo-Items `Python lernen` als erledigt.
# Wie sieht jetzt Ihre Liste aus?

# %%  {{ solution() }}
mark_todo_item_done(todos, "Python lernen")
print(todo_list_as_string(todos))

# %%  {{ solution() }}
mark_todo_item_done(todos, "Python lernen")
print(todo_list_as_string(todos))


# %% [markdown]
# Schreiben Sie eine Funktion `delete_todo_item(todo_list, title)`, die das
# erste in der liste `todo_list` vorkommende Todo-Item mit Titel `title` aus
#  der Liste entfernt.
#
# *Vorsicht: Sie sollten während Sie über eine Liste iterieren keine Einträge
# entfernen oder einfügen!*

# %%  {{ solution() }}
def delete_todo_item(todo_list, title):
    index_to_delete = -1
    for index, item in enumerate(todo_list.items):
        if item.title == title:
            index_to_delete = index
            break
    if index_to_delete >= 0:
        del todo_list.items[index_to_delete]


# %% [markdown]
# Entfernen Sie eines der Items `Python lernen`.

# %%  {{ solution() }}
delete_todo_item(todos, "Python lernen")
print(todo_list_as_string(todos))

# %% [markdown]
# Entfernen Sie dreimal ein Item `Python lernen`. Was erwarten Sie als Ergebnis?

# %%  {{ solution() }}
delete_todo_item(todos, "Python lernen")
print(todo_list_as_string(todos))

# %%  {{ solution() }}
delete_todo_item(todos, "Python lernen")
print(todo_list_as_string(todos))

# %%  {{ solution() }}
delete_todo_item(todos, "Python lernen")
print(todo_list_as_string(todos))


# %% [markdown]
# Schreiben Sie eine Funktiion `delete_all_completed_todo_items(todo_list)`,
# die alle erledigten Todo-Items aus `todo_list` löscht.
#
# *Hinweis: Sie benötigen dazu wahrscheinlich zwei aufeinanderfolgende
# `for`-Schleifen: eine um die Indizes zu bestimmen und eine um sie zu löschen*

# %%  {{ solution() }}
def delete_all_completed_todo_items(todo_list):
    indices_to_delete = []
    for index, item in enumerate(todo_list.items):
        if item.is_completed:
            indices_to_delete.append(index)
    for index in sorted(indices_to_delete, reverse=True):
        del todo_list.items[index]


# %%  {{ solution() }}
delete_all_completed_todo_items(todos)
print(todo_list_as_string(todos))

# %% [markdown]
# Testen Sie Ihre Implementierung von `delete_all_completed_todo_items()` mit
# der folgenden Liste:

# %%  {{ solution() }}
todo_list_2 = TodoList([TodoItem(f'Item {n}', 1, n % 2 == 0)
                        for n in range(10)])
print(todo_list_as_string(todo_list_2))

# %%  {{ solution() }}
delete_all_completed_todo_items(todo_list_2)
print(todo_list_as_string(todo_list_2))

# %%
