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
# ## Grundlegende Funktionalität
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

# %% [markdown]
# Definieren Sie eine Klasse `TodoList`, die eine Todo-Liste repräsentiert.
#
# Implementieren Sie eine `__init__()` Methode, die eine Liste von TodoItems als Argument bekommt und speichert.
#
# Fügen Sie folgende Methoden hinzu:
#
# - `add(self, title: str, priority: int, is_completed: bool)`, die ein neues Todo-Item an die Todo-Liste anhängt und 
#   geeignete Default-Werte für `priority` und `is_completed` übergibt.
# - `mark_done(self, title)`, die das erste in der Liste vorkommende Todo-Item mit Titel `title`, das noch nicht bearbeitet ist, als bearbeitet markiert.
# - NO! `delete(self, title)`, die das erste in der Liste vorkommende Todo-Item mit Titel `title` aus der Liste entfernt.
# - NO! `delete_all_completed(self)`, die alle beendeten Items aus der Liste entfernt.
# - `__str__(self)` und `__repr__(self)`
# - NO! `__iter__(self)`, so dass in einer `for`-Schleife über alle in der Todo-Liste enthaltenen TodoItems iteriert werden kann.
#
# <!--
# *Hinweis*: Kopieren Sie die Implementierung der Methoden aus `062z-Lösung Todo-Liste V1` oder ihrer vorherigen Implementierung und passen Sie den Code an.
# -->

# %% pycharm={"name": "#%%\n"}

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
# Fügen Sie eine Datei `__main__.py` zu Ihrer Implementierung hinzu, die einen `ArgumentParser` instanziiert, der folgendes Interface bereitstellt:
#
# ```[shell]
# usage: Manage a TODO list.
#     [-h]
#     (--create 
#       | --add title priority 
#       | --delete title
#       | --mark-completed title 
#       | --delete-all-completed 
#       | --list)
#     file
#
# positional arguments:
#   file
#
# optional arguments:
#   -h, --help            show this help message and exit
#   --create
#   --add title priority
#   --delete title
#   --mark-completed title
#   --delete-all-completed
#   --list
# ```

# %%

# %% [markdown]
# ## Packaging
#
# Fügen Sie eine `setup.py` Datei, sowie alle weiteren benötigten Dateien zu Ihrem Projekt hinzu, um daraus eine Wheel-Datei zu generieren.
#
# Erzeugen Sie in der `setup.py`-Datei ein Skript, das Ihre Anwendung startet.

# %%
