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

# %% [markdown]
# Schreiben Sie eine Funktion `add_todo_item(todo_list, title, priority)`, die ein
# neues Todo-Item zu `todo_list` hinzufügt.

# %%

# %% [markdown]
# Fügen Sie ein neues Todo-Item mit Titel "Schnee schaufeln" und Priorität 5 in die Liste `todos` ein.

# %%

# %% [markdown]
# Schreiben Sie eine Funktion `mark_todo_item_done(todo_list, title)`, die das erste in der Liste `todo_list` vorkommende Todo-Item mit Titel `title`, das noch nicht bearbeitet ist, als bearbeitet markiert.

# %%

# %% [markdown]
# Markieren Sie das Todo-Item `Schnee schaufeln` als bearbeitet.

# %%

# %% [markdown]
# Fügen Sie zwei Todo-Items mit Text "Python lernen" und Priorität 1 und 6 zur Todo-Liste hinzu.

# %%

# %% [markdown]
# Markieren Sie ein Todo-Item "Python lernen" als erledigt. Wie sieht jetzt Ihre Liste aus?

# %%

# %% [markdown]
# Markieren Sie noch ein Todo-Item "Python lernen" als erledigt. Wie sieht jetzt Ihre Liste aus?

# %%

# %% [markdown]
# Schreiben Sie eine Funktion `delete_todo_item(todo_list, title)`, die das erste in der liste `todo_list` vorkommende Todo-Item mit Titel `title` aus der Liste entfernt.
#
# *Vorsicht: Sie sollten während Sie über eine Liste iterieren keine Einträge entfernen oder einfügen!*

# %%

# %% [markdown] pycharm={"name": "#%% md\n"}
# Löschen Sie ein item `Python lernen` aus `todo_list`

# %%

# %% [markdown]
# Schreiben Sie eine Funktiion `delete_all_completed_todo_items(todo_list)`, die alle erledigten Todo-Items aus `todo_list` löscht.
#
# *Hinweis: Sie benötigen dazu wahrscheinlich zwei aufeinanderfolgende `for`-Schleifen: eine um die Indizes zu bestimmen und eine um sie zu löschen*

# %%

# %%
