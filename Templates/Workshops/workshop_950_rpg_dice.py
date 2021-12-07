# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py:percent
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

# j2 import 'macros.j2' as doc
# %% [markdown]
# # RPG-Würfel
#
# In Rollenspielen werden Konflikte zwischen Spielern oft durch Würfeln
# entschieden. Dabei werden oft mehrere Würfel gleichzeitig verwendet. Außerdem
# werden nicht nur die bekannten 6-seitigen Würfel verwendet, sondern auch
# 4-seitige, 8-seitige, 20-seitige Würfel, etc.
#
# Die Anzahl und Art der Würfel wird dabei durch folgende Notation beschrieben:
#
# ```text
# <Anzahl der Würfel> d <Seiten pro Würfel>
# ```
#
# Zum Beispiel wird das Würfeln mit zwei 6-seitigen Würfeln als `2d6`
# beschrieben. Manchmal werden auch komplexere Formeln verwendet: `3d20 + 2d6
# - 4` bedeutet, dass gleichzeitig drei 20-seitige Würfel und zwei 6-seitige
# Würfel geworfen werden und die Gesamtsumme der Augenzahlen dann um 4
# verringert wird.
#
# In manchen Spielen wird das Werfen der niedrigsten oder höchsten Augenzahl
# besonders behandelt ("katastrophale Niederlage", "kritischer Erfolg").
#
#
# In den folgenden Aufgaben sollen Sie derartige RPG-Würfel in Python
# implementieren. Um Ihre Implementierung testen zu können empfiehlt es sich
# sie in einem IDE zu realisieren. Schreiben Sie Tests für jede
# Funktionalität, die Sie implementieren. Wie können Sie beim Testen mit der
# Zufälligkeit beim Würfeln umgehen? Was sind Stärken bzw. Schwächen der von
# Ihnen gewählten Teststrategie?
#
#
#
# ## Generalisierte Würfel: Interface `Dice`
#
# Implementieren Sie eine abstrakte Klasse `Dice`, die das Würfeln mit
# beliebigen Würfeln beschreibt: Die Klasse soll folgende abstrakte Methoden
# anbieten:
#
# - `roll(): int` liefert das Ergebnis eines Wurfes mit den entsprechenden
#   Würfeln zurück.
#
# - properties `max_value: int` und `min_value: int` geben den kleinsten bzw.
#   größten Wert zurück, der mit den entsprechenden Würfeln geworfen werden
#   kann.
#
# Schreiben Sie parametrische Pytest Tests, mit denen (indirekte) Instanzen
# von `Dice` getestet werden können.
#
# ## Klasse `ConstantDice`
#
# Implementieren Sie eine Klasse `ConstantDice`, die das Interface `Dice`
# implementiert und einen Würfel realisiert, der immer einen konstanten, bei der
# Instanziierung des Objekts festgelegten Wert würfelt.
#
# ## Klasse `FairDice`
#
# Implementieren Sie eine Klasse `FairDice`, die das Interface `Dice`
# implementiert und einen der oben beschriebenen Würfe mit mehreren Würfeln
# einer beliebigen (aber für alle Würfel gleichen) Augenzahl realisiert. Z.B.
# sollen Würfe der Form `3d6` oder `4d17` durch Instanzen dieser Klasse
# darstellbar sein (obwohl es in der Realität keinen 17-seitigen (fairen)
# Würfel gibt).
#
# Wie können Sie beim Testen mit der Zufälligkeit beim Würfeln umgehen? Was
# sind Stärken bzw. Schwächen der gewählten Teststrategie?
#
# ## Klasse `SumDice`
#
# Implementieren Sie eine Klasse `SumDice`, die das Interface `Dice`
# implementiert und die Summe des Würfelns mit mehreren verschiedenen Würfeln
# (potentiell der Form `<m>d<n>`) repräsentiert.
#
#
# ## Klasse `SimpleDie`
#
# Implementieren Sie eine Klasse `SimpleDie`, die das Interface `Dice`
# implementiert und das Würfeln mit einem Würfel beliebiger, bei der
# Instanziierung des Würfels festgelegten, Seitenzahl ermöglicht.
#
# ## Klasse `MultipleRollDice`
#
# Implementieren Sie eine Klasse `MultipleRollDice`, die das Interface `Dice`
# implementiert und das wiederholte Würfeln mit einem (generalisierten)
# Würfel realisiert.
#
# Was ist die Beziehung zwischen `FairDice` und der Kombination aus
# `SimpleDie` und `MultipleRollDice`? Wie unterscheiden sich die beiden
# Implementierungsstrategien in ihrer Testbarkeit.
#

# %% [markdown]
# # Factory für RPG-Würfel
#
# Schreiben Sie eine Funktion `create_dice(configuration: str) -> Dice`,
# die eine Konfiguration von RPG-Würfeln als Argument bekommt und eine
# geeignete Konfiguration von Dice-Instanzen zurückgibt.  Zum Beispiel soll
# für "3d8 + 6" ein `SumDice` zurückgegeben werden, der einen `FairDice` (mit
# 3 8-seitigen Würfeln) und einen `ConstantDice` mit dem Wert 6 enthält.

# %%
