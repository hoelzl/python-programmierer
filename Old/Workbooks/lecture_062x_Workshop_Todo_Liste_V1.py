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

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Erzeugen Sie ein Todo-Item mit folgenden Bestandteilen:
# - Titel: Python lernen
# - Priorität 3
# - nicht erledigt

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Die Repräsentation des Items ist nicht sehr aussagekräftig. Definieren Sie
# deshalb eine Funktion `todo_item_as_string(item: TodoItem) -> str`, die ein
# Todo-Item in einen String umwandelt, der Information über die Bestandteile
# enthält.

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Definieren Sie eine Klasse `TodoList`, die eine Todo-Liste repräsentiert.

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Definieren Sie eine Funktion `todo_list_as_string(todo_list: TodoList) -> str`,
# die eine Todo-Liste in einen String umwandelt, der Information über ihre
# Bestandteile enthält.

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Legen Sie eine Todo-Liste `todos` mit Todo-Items an, die folgende Einträge enthält:
#
# - Titel: Python lernen, Priorität 3, nicht erledigt
# - Titel: Gemüse einkaufen, Priorität 2, nicht erledigt
# - Titel: Hans anrufen, Priorität 5, erledigt

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Schreiben Sie eine Funktion `add_todo_item(todo_list, title, priority)`, die ein neues Todo-Item zu `todo_list` hinzufügt.

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Fügen Sie ein neues Todo-Item mit Titel "Schnee schaufeln" und Priorität 5 in die Liste `todos` ein.

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Schreiben Sie eine Funktion `mark_todo_item_done(todo_list, title)`, die das erste in der Liste `todo_list` vorkommende Todo-Item mit Titel `title`, das noch nicht bearbeitet ist, als bearbeitet markiert.

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Markieren Sie das Todo-Item `Schnee schaufeln` als bearbeitet.

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Fügen Sie zwei Todo-Items mit Text "Python lernen" und Priorität 1 und 6 zur Todo-Liste hinzu.

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Markieren Sie ein Todo-Item "Python lernen" als erledigt. Wie sieht jetzt Ihre Liste aus?

# %% pycharm={"name": "#%%\n"}



# %% [markdown]
# Markieren Sie noch zwei Todo-Items `Python lernen` als erledigt. Wie sieht jetzt Ihre Liste aus?

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Schreiben Sie eine Funktion `delete_todo_item(todo_list, title)`, die das erste in der liste `todo_list` vorkommende Todo-Item mit Titel `title` aus der Liste entfernt.
#
# *Vorsicht: Sie sollten während Sie über eine Liste iterieren keine Einträge entfernen oder einfügen!*

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Entfernen Sie eines der Items `Python lernen`.

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Entfernen Sie dreimal ein Item `Python lernen`. Was erwarten Sie als Ergebnis?

# %% pycharm={"name": "#%%\n"}

# %% pycharm={"name": "#%%\n"}



# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Schreiben Sie eine Funktiion `delete_all_completed_todo_items(todo_list)`, die alle erledigten Todo-Items aus `todo_list` löscht.
#
# *Hinweis: Sie benötigen dazu wahrscheinlich zwei aufeinanderfolgende `for`-Schleifen: eine um die Indizes zu bestimmen und eine um sie zu löschen*

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Testen Sie Ihre Implementierung von `delete_all_completed_todo_items()` mit einer Liste der folgenden Form:
# ```
# Todo List:
#   Item 0, priority 1, done
#   Item 1, priority 1
#   Item 2, priority 1, done
#   Item 3, priority 1
#   Item 4, priority 1, done
#   Item 5, priority 1
#   Item 6, priority 1, done
#   Item 7, priority 1
#   Item 8, priority 1, done
#   Item 9, priority 1
#
#
# ```
#
# Eine derartige Liste können Sie folgendermaßen erzeugen falls der Konstruktor Ihrer Todo-Items Titel, Priorität und Bearbeitungsstatus als positionale Argumente akzeptiert: 
#
# ```python
# todo_list_2 = TodoList([TodoItem(f'Item {n}', 1, n % 2 == 0)
#                         for n in range(10)])
# ```

# %% pycharm={"name": "#%%\n"}
