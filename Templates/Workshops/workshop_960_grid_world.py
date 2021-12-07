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
# # Grid World
#
# In den folgenden Abschnitten sollen die grundlegenden Komponenten eines
# 2D-Rollenspiels implementeiert werden.

# %% [markdown]
# ## Rechteckiges Spielfeld (Level)
# - Größe (w x h) wird beim Erzeugen des Spielfelds festgelegt
# - Das Spielfeld kann seine Breite und Länge (width, height)
#   und die Anzahl der Felder (size) zurückgeben
# - Jedes einzelne "Feld" im Spielfeld ist ein Location-Objekt
# - Jede Location kennt ihre Nachbarn in die 4 Himmelsrichtungen
#   (N, O, S, W)
# - Bei Locations, die am Rand liegen verweisen die Nachbarn, die
#   außerhalb des Spielfelds liegen würden, auf das
#   Location-Objekt 
# - Jede Location kennt ihre Cartesischen Koordinaten (w, h)
# - Jede Location kennt ihren Level 

# %% [markdown]
# ## Factory zum Erzeugen eines Spielfelds (LevelFactory)
# - Kann Spielfelder für verschiedene Dimensionen und
#   Schwierigkeitsgrade erzeugen
# - Verwendet eine LevelPopulationStrategy um (abhängig vom
#   Schwierigkeitsgrad) Objekte im Level zu verteilen
# - Implementieren Sie im Moment nur das Interface für eine
#   LevelPopulationStrategy, keine wirkliche Strategie
# - Wie können Sie unter diesen Umständen die LevelFactory
#   testen?

# %% [markdown]
# ## Abstrakter Character
# - Erstellen Sie eine Klasse AbstractCharacter, die folgende
#   Funktionalität bietet:
#   - Abfrage des Namen des Characters
#   - Abfrage der Location, auf der sich der Character befindet
#   - Bewegen auf dem Spielfeld
#   - Sterben des Characters
# - Alle wesentlichen Ereignisse des AbstractCharacters sollen
#   mit Observern beobachtbar sein (Creation, Move, Death)
# - AbstractCharacter soll außerhalb des Core-Rings liegen.
#   Wie können Sie die Abhängigkeiten korrekt behandeln?

# %% [markdown]
# ## LevelPopulationStrategy (1)
# - Schreiben Sie eine LevelPopulationStrategy
#   LevelPopulationStrategy_LeaveLevelEmpty, die einen Level ohne zusätzliche
#   Elemente erzeugt

# %% [markdown]
# ## Spieler/NPCs
# - Erstellen Sie Unterklassen von AbstractCharacter für Spieler
#   und NPCs
# - Jeder Character soll jetzt zusätzlich folgende Funktionen
#   haben:
#   - getAttitudeTowardsPlayer() (neutral, freundlich, feindlich)
#   - tick() um periodisch das Verhalten voranzutreiben
# - Das Verhalten von NPCs soll über eine Behavior Strategie
#   gesteuert werden.
# - Die "Anweisungen" der Behavior Strategie sollen in der Form
#   des Command Patterns implementiert werden.
# - Implementieren Sie Behaviors und Commands, die eine Bewegung
#   von NPCs in zufälliger Richtung erreichen
# - Implementieren Sie ein Command, das die Bewegung eines Characters
#   in eine bestimmte (bei der Erzeugung des Commands wählbare)
#   Richtung ermöglicht
#   
# - Implementieren Sie einen Builder für NPCs

# %% [markdown]
# ## LevelPopulationStrategy (2)
# - Schreiben Sie eine LevelPopulationStrategy
#   LevelPopulationStrategy_DistributeRandomElements, die das Spielfeld zufällig
#   mit freundlichen und feindlichen NPCs bevölkert. Die Anzahl der NPCs soll
#   dabei in Abhängigkeit von der Anzahl der Felder (Level.size()) und des
#   Schwierigkeitsgrads angepasst werden
#
# - Implementieren Sie eine Funktion Character::attack(...), um einen
#   anderen Character anzugreifen

# %%
