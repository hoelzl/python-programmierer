# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] lang="de"
# # Grid World
#
# In den folgenden Abschnitten sollen die grundlegenden Komponenten eines
# 2D-Rollenspiels implementiert werden.

# %% [markdown] lang="en"
# # GridWorld
#
# The following sections we want to implement the basic components of a
# 2D role-playing game.

# %% [markdown] lang="de"
# ## Rechteckiges Spielfeld (Level)
# - Größe (w x h) wird beim Erzeugen des Spielfelds festgelegt
# - Das Spielfeld kann seine Breite und Länge (width, height)
#   und die Anzahl der Felder (size) zurückgeben
# - Jedes einzelne "Feld" im Spielfeld ist ein `Location`-Objekt
# - Jede Location kennt ihre Nachbarn in die 4 Himmelsrichtungen
#   (N, O, S, W)
# - Bei Locations, die am Rand liegen verweisen die Nachbarn, die
#   außerhalb des Spielfelds liegen würden, auf das
#   Location-Objekt 
# - Jede Location kennt ihre Cartesischen Koordinaten (w, h)
# - Jede Location kennt die `Level` Instanz, zu der sie gehört

# %% [markdown] lang="en"
# ## Rectangular playing field (`Level`)
# - The size (w x h) is set when creating the playing field
# - The playing field can change its width and length (width, height)
#   and return the number of fields (size).
# - Every single "square" in the playing field is represented by a `Location` object
# - Each location knows its neighbors in the 4 cardinal points
#   (N, E, S, W)
# - In the case of locations that are on the edge, neighbors in directions that
#   would lie outside the playing field, refer to the location itself
# - Each location knows its Cartesian coordinates (w, h)
# - Every location knows the `Level` instance to which it belongs

# %% [markdown] lang="de"
# ## Factory zum Erzeugen eines Spielfelds (`LevelFactory`)
# - Kann Spielfelder für verschiedene Dimensionen und
#   Schwierigkeitsgrade erzeugen
# - Verwendet eine LevelPopulationStrategy um (abhängig vom
#   Schwierigkeitsgrad) Objekte im Level zu verteilen
# - Implementieren Sie im Moment nur das Interface für eine
#   LevelPopulationStrategy, keine wirkliche Strategie
# - Wie können Sie unter diesen Umständen die LevelFactory
#   testen?

# %% [markdown] lang="en"
# ## Factory to create a playing field (`LevelFactory`)
# - Can create levels with different dimensions (and possibly different difficulties)
# - Uses a `LevelPopulationStrategy` to distribute objects in the level (depending on the 
#   desired difficulty) 
# - Implement only the interface for `LevelPopulationStrategy`, no concrete strategy
# - How can you test `LevelFactory` in this situation?

# %% [markdown] lang="de"
# ## Abstrakter Character
# - Erstellen Sie eine Klasse `AbstractCharacter`, die folgende
#   Funktionalität bietet:
#   - Abfrage des Namen des Characters
#   - Abfrage der Location, auf der sich der Character befindet
#   - Bewegen auf dem Spielfeld
#   - Sterben des Characters
# - Alle wesentlichen Ereignisse des AbstractCharacters sollen
#   mit Observern beobachtbar sein (Creation, Move, Death)
# - AbstractCharacter soll außerhalb des Core-Rings liegen.
#   Wie können Sie die Abhängigkeiten korrekt behandeln?

# %% [markdown] lang="en"
# ## Abstract character
# - Create an `AbstractCharacter` class, that provides the following functionality:
#   - Query the name of the character
#   - Query the location where the character is
#   - Move the character around the field
#   - Character death
# - All significant events of the `AbstractCharacter` should
#   be observable with observers (creation, move, death)
# - `AbstractCharacter` should be outside of the core ring.
#   How can you handle the dependencies correctly?

# %% [markdown] lang="de"
# ## LevelPopulationStrategy (1)
# - Schreiben Sie eine `LevelPopulationStrategy`,
#   `LevelPopulationStrategy_LeaveLevelEmpty`, die einen Level ohne zusätzliche
#   Elemente erzeugt

# %% [markdown] lang="en"
# ## LevelPopulationStrategy (1)
# - Write a `LevelPopulationStrategy`,
#   `LevelPopulationStrategy_LeaveLevelEmpty`, that creates a level without any additional
#   elements.

# %% [markdown] lang="de"
# ## Spieler/NPCs
# - Erstellen Sie Unterklassen von `AbstractCharacter` für Spieler
#   und NPCs
# - Jeder Character soll jetzt zusätzlich folgende Funktionen
#   haben:
#   - `getAttitudeTowardsPlayer()` (neutral, freundlich, feindlich)
#   - `tick()` um periodisch das Verhalten voranzutreiben
# - Das Verhalten von NPCs soll über eine Behavior Strategie
#   gesteuert werden.
# - Die "Anweisungen" der Behavior Strategie sollen in der Form
#   des Command Patterns implementiert werden.
# - Implementieren Sie Behaviors und Commands, die eine Bewegung
#   von NPCs in zufälliger Richtung erreichen
# - Implementieren Sie ein Command, das die Bewegung eines Characters
#   in eine bestimmte (bei der Erzeugung des Commands wählbare)
#   Richtung ermöglicht
# - Implementieren Sie einen Builder für NPCs

# %% [markdown] lang="en"
# ## Players/NPCs
# - Subclass `AbstractCharacter` for players
#   and NPCs
# - Each character should now also have the following functions:
#   - `getAttitudeTowardsPlayer()` (neutral, friendly, hostile)
#   - `tick()` to periodically advance the behavior
# - The behavior of NPCs should be controlled by a behavior strategy
# - The "instructions" of the behavior strategy should be implemented
#   in the form of the Command Pattern
# - Implement behaviors and commands that move an NPCs in a random direction
# - Implement a command that moves a character
#   in a specific direction (selectable when creating the command)
# - Implement a builder for NPCs

# %% [markdown] lang="de"
# ## LevelPopulationStrategy (2)
# - Schreiben Sie eine `LevelPopulationStrategy`
#   `LevelPopulationStrategy_DistributeRandomElements`, die das Spielfeld zufällig
#   mit freundlichen und feindlichen NPCs bevölkert. Die Anzahl der NPCs soll
#   dabei in Abhängigkeit von der Anzahl der Felder (`Level.size()`) und des
#   Schwierigkeitsgrads angepasst werden
# - Implementieren Sie eine Funktion `Character.attack(...)`, um einen
#   anderen Character anzugreifen

# %% [markdown] lang="en"
# ## LevelPopulationStrategy (2)
# - Write a `LevelPopulationStrategy`
#   `LevelPopulationStrategy_DistributeRandomElements`, which creates a playing field
#   populated with randomly placed friendly and hostile NPCs. The number of NPCs should
#   depend on the number of fields (`Level.size()`) and the difficulty
# - Implement a function `Character.attack(...)` to attack other characters

# %%
