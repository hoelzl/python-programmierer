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

# %% [markdown] slideshow={"slide_type": "slide"}
# # Vergleich von Strings

# %% pycharm={"name": "#%%\n"}
"a" == 'a'

# %% pycharm={"name": "#%%\n"}
"A" == "a"

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
"A" < "B"

# %% pycharm={"name": "#%%\n"}
"A" < "a"

# %% pycharm={"name": "#%%\n"}
"a" < "A"

# %% [markdown] slideshow={"slide_type": "subslide"}
# Strings sind wie im Wörterbuch (lexikographisch) geordnet

# %% pycharm={"name": "#%%\n"}
"ab" < "abc"

# %% pycharm={"name": "#%%\n"}
"ab" < "ac"

# %% pycharm={"name": "#%%\n"}
"ab" != "ac"

# %% [markdown] slideshow={"slide_type": "slide"}
# # Nochmal String Literale
#
# - String-Literale werden in einfache oder doppelte Anführungszeichen eingeschlossen
#     - `"Hello, world!"`
#     - `'Hallo Welt!'`
#     - Welche Form man wählt spielt keine Rolle, außer man will Anführungszeichen im String haben
#     - `"Er sagt 'Huh?'"`
#     - `'Sie antwortet: "Genau."'`

# %% [markdown] slideshow={"slide_type": "subslide"}
# - String-Literale, können Unicode Zeichen enthalten:
#     - `"おはようございます"`
#     - `"😠🙃🙄"`

# %% pycharm={"name": "#%%\n"}
print("Er sagt 'Huh?'")
print('Sie antwortet: "Genau."')
print("おはようございます")
print("😠🙃🙄")

# %% [markdown] slideshow={"slide_type": "subslide"}
# - Sonderzeichen können mit *Escape-Notation* angegeben werden:
#     - `\n`, `\t`, `\\`, `\"`, `\'`, ...
#     - `\u`, `\U` für Unicode code points (16 bzw. 32 bit)
#     - `\N{...}` für Unicode

# %% pycharm={"name": "#%%\n"}
print("a\tbc\td\n123\t4\t5")

# %% pycharm={"name": "#%%\n"}
print("\"Let\'s go crazy\", she said")

# %% pycharm={"name": "#%%\n"}
print("C:\\Users\\John")

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
print("\u0394 \u03b1 \t\U000003b2 \U000003b3")
print("\U0001F62E \U0001f61a \U0001f630")

# %% pycharm={"name": "#%%\n"}
print("\N{GREEK CAPITAL LETTER DELTA} \N{GREEK SMALL LETTER ALPHA}")
print("\N{smiling face with open mouth and smiling eyes} \N{winking face}")

# %% [markdown] slideshow={"slide_type": "subslide"}
# - String Literale können auch in 3-fache Anführungszeichen eingeschlossen werden
# - Diese Art von Literalen kann über mehrere Zeilen gehen

# %% pycharm={"name": "#%%\n"}
"""Das ist
ein String-Literal,
das über mehrere
Zeilen geht."""

# %% pycharm={"name": "#%%\n"}
print('''Mit Backslash am Ende der Zeile \
kann der Zeilenvorschub unterdrückt werden.''')

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Konkatenation von Strings
#
# Mit `+` können Strings aneinandergehängt (konkateniert) werden:

# %% pycharm={"name": "#%%\n"}
"Ein" + " " + "String"

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `015x-Workshop Mehr zu Strings`
# - Abschnitt "Begrüßung 1"

# %% [markdown] slideshow={"slide_type": "slide"}
# # String Interpolation: F-Strings
#
# Python bietet die Möglichkeit, Werte von Variablen in Strings einzusetzen:

# %% pycharm={"name": "#%%\n"}
name = "Hans"
zahl = 12
f"Hallo, {name}, die Zahl ist {zahl + 1}"

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
spieler_name = "Hans"
anzahl_spiele = 10
anzahl_gewinne = 2

ausgabe = f"Hallo {spieler_name}!\nSie haben {anzahl_spiele}-mal gespielt und dabei {anzahl_gewinne}-mal gewonnen."
print(ausgabe)

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
ausgabe = f"""\
Hallo {spieler_name}!
Sie haben {anzahl_spiele}-mal gespielt \
und dabei {anzahl_gewinne}-mal gewonnen.\
"""
print(ausgabe)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `015x-Workshop Mehr zu Strings`
# - Abschnitt "Begrüßung 2"

# %% [markdown]
# ## Mini-Workshop
#
# - Notebook `015x-Workshop Mehr zu Strings`
# - Abschnitt "Piraten 4"
