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
# # TODO-Liste Version 0
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

# %% [markdown]
# Legen Sie eine Liste `todos` mit Todo-Items an, die folgende Einträge enthält:
#
# - Titel: Python lernen, Priorität 3, nicht erledigt
# - Titel: Gemüse einkaufen, Priorität 2, nicht erledigt
# - Titel: Hans anrufen, Priorität 5, erledigt

# %%
todos = [dict(title='Python lernen', priority=3, is_completed=False)]
todos

# %%
todos = [{'title': 'Python lernen', 'priority': 3, 'is_completed': False},
         {'title': 'Gemüse einkaufen', 'priority': 2, 'is_completed': False},
         {'title': 'Hans anrufen', 'priority': 5, 'is_completed': True}]

# %%
todos


# %% [markdown]
# Schreiben Sie eine Funktion `add_todo_item(todo_list, title, priority)`, die ein
# neues Todo-Item zu `todo_list` hinzufügt.

# %%
def add_todo_item(todo_list, title, priority):
    todo_list.append({'title': title,
                      'priority': priority,
                      'is_completed': False})


# %% [markdown]
# Fügen Sie ein neues Todo-Item mit Titel "Schnee schaufeln" und Priorität 5 in die Liste `todos` ein.

# %%
add_todo_item(todos, "Schnee schaufeln", 5)

# %%
todos


# %% [markdown]
# Schreiben Sie eine Funktion `mark_todo_item_done(todo_list, title)`, die das erste in der Liste `todo_list` vorkommende Todo-Item mit Titel `title`, das noch nicht bearbeitet ist, als bearbeitet markiert.

# %%
def mark_todo_item_done(todo_list, title):
    for item in todo_list:
        if item['title'] == title and not item['is_completed']:
            item['is_completed'] = True
            break


# %% [markdown]
# Markieren Sie das Todo-Item `Schnee schaufeln` als bearbeitet.

# %%
mark_todo_item_done(todos, "Schnee schaufeln")

# %%
todos

# %% [markdown]
# Fügen Sie zwei Todo-Items mit Text "Python lernen" und Priorität 1 und 6 zur Todo-Liste hinzu.

# %%
add_todo_item(todos, "Python lernen", 1)
add_todo_item(todos, "Python lernen", 6)

# %%
todos

# %% [markdown]
# Markieren Sie ein Todo-Item "Python lernen" als erledigt. Wie sieht jetzt Ihre Liste aus?

# %%
mark_todo_item_done(todos, "Python lernen")

# %%
todos

# %% [markdown]
# Markieren Sie noch ein Todo-Item "Python lernen" als erledigt. Wie sieht jetzt Ihre Liste aus?

# %%
mark_todo_item_done(todos, "Python lernen")
todos


# %% [markdown]
# Schreiben Sie eine Funktion `delete_todo_item(todo_list, title)`, die das erste in der liste `todo_list` vorkommende Todo-Item mit Titel `title` aus der Liste entfernt.
#
# *Vorsicht: Sie sollten während Sie über eine Liste iterieren keine Einträge entfernen oder einfügen!*

# %%
def delete_todo_item(todo_list, title):
    index_to_delete = -1
    for index, item in enumerate(todo_list):
        if item['title'] == title:
            index_to_delete = index
            break
    if index_to_delete >= 0:
        del todo_list[index_to_delete]



# %% [markdown] pycharm={"name": "#%% md\n"}
# Löschen Sie ein item `Python lernen` aus `todo_list`

# %%
delete_todo_item(todos, "Python lernen")
todos


# %% [markdown]
# Schreiben Sie eine Funktiion `delete_all_completed_todo_items(todo_list)`, die alle erledigten Todo-Items aus `todo_list` löscht.
#
# *Hinweis: Eine Möglichkeit diese Aufgabe zu lösen sind zwei aufeinanderfolgende `for`-Schleifen: eine um die Indizes zu bestimmen und eine um sie zu löschen. Beachten Sie die Reihenfolge, in der Sie Items löschen! Eine elegantere Methode ist eine List Comprehension und Zuweisung an ein Slice zu verwenden.*

# %%
def delete_all_completed_todo_items(todo_list):
    indices_to_delete = []
    for index, item in enumerate(todo_list):
        if item['is_completed']:
            indices_to_delete.append(index)
    for index in sorted(indices_to_delete, reverse=True):
        del todo_list[index]


# %%
# delete_all_completed_todo_items(todos)
todos


# %%
def delete_all_completed_todo_items_v2(todo_list):
    todo_list[:] = [item
                    for item in todo_list
                    if not item['is_completed']]


# %%
delete_all_completed_todo_items_v2(todos)
todos

# %%
