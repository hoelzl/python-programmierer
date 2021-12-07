# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
#
#  # Strings
#  ## Vergleich von Strings

# %%
"a" == "a"


# %%
"A" == "a"


# %%
"A" < "B"


# %%
"A" < "a"


# %%
"a" < "A"


# %% [markdown]
#
#  Strings sind wie im Wörterbuch (lexikographisch) geordnet

# %%
"ab" < "abc"


# %%
"ab" < "ac"


# %%
"ab" != "ac"


# %% [markdown]
#
#  # Nochmal String Literale
#
#  - String-Literale werden in einfache oder doppelte Anführungszeichen eingeschlossen
#      - `"Hello, world!"`
#      - `'Hallo Welt!'`
#      - Welche Form man wählt spielt keine Rolle, außer man will Anführungszeichen im String haben
#      - `"Er sagt 'Huh?'"`
#      - `'Sie antwortet: "Genau."'`

# %% [markdown]
#
#  - String-Literale, können Unicode Zeichen enthalten:
#      - `"おはようございます"`
#      - `"😠🙃🙄"`

# %%
print("Er sagt 'Huh?'")
print('Sie antwortet: "Genau."')
print("おはようございます")
print("😠🙃🙄")

# %% [markdown]
#
#  - Sonderzeichen können mit *Escape-Notation* angegeben werden:
#      - `\n`, `\t`, `\\`, `\"`, `\'`, ...
#      - `\u`, `\U` für Unicode code points (16 bzw. 32 bit)
#      - `\N{...}` für Unicode

# %%
print("a\tbc\td\n123\t4\t5")

# %%
print('"Let\'s go crazy", she said.')


# %%
print("C:\\Users\\John")

# %%
print(r"C:\Users\John")

# %%
r"C:\Users\John" == "C:\\Users\\John"

# %%
print("\u0394 \u03b1 \t\U000003b2 \U000003b3")
print("\U0001F62E \U0001f61a \U0001f630")

# %%
print("\N{GREEK CAPITAL LETTER DELTA} \N{GREEK SMALL LETTER ALPHA}")
print("\N{smiling face with open mouth and smiling eyes} \N{winking face}")

# %% [markdown]
#
#  - String Literale können auch in 3-fache Anführungszeichen eingeschlossen werden
#  - Diese Art von Literalen kann über mehrere Zeilen gehen

# %%
"""Das ist
ein String-Literal,
das über mehrere
Zeilen geht."""

# %%
"""Mit Backslash am Ende der Zeile kann der Zeilenvorschub \
unterdrückt werden. \
Allerdings muss der Backslash wirklich das letzte \ 
Zeichen in der Zeile sein."""

# %%
("Mit Backslash am Ende der Zeile kann der Zeilenvorschub "
 "unterdrückt werden.\n"
 "Allerdings muss der Backslash wirklich das letzte "
 "Zeichen in der Zeile sein.")

# %%
"Das ist " "ein String."

# %% [markdown]
#
#  ## Konkatenation von Strings
#
#  Mit `+` können Strings aneinandergehängt (konkateniert) werden:

# %%
"Ein" + " " + "String"

# %%
number = "Ein"
number + " String"

# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `015x-Workshop Mehr zu Strings`
#  - Abschnitt "Begrüßung 1"

# %% [markdown]
#
#  ## Umwandeln eines Strings in Klein-/Großbuchstaben

# %%
text = "Das ist ein Text"
print(text)
print(text.lower())

# %%
"Das ist ein Text".upper()

# %%
text.title()

# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `020x-Workshop Kontrollstrukturen`
#  - Abschnitt "Shout"
#

# %% [markdown]
#
#  # String Interpolation: F-Strings
#
#  Python bietet die Möglichkeit, Werte von Variablen in Strings einzusetzen:

# %%
name = "Hans"
zahl = 12
f"Hallo, {name}, die Zahl ist {zahl + 1}."

# %%
f"Hallo, {name}" == "Hallo, Hans"

# %%
spieler_name = "Hans"
anzahl_spiele = 10
anzahl_gewinne = 2

# %% [markdown]
#
#  Auch bei F-Strings können Zeilenvorschübe durch eine Backslash am Ende der
#  Zeile unterdrückt werden:

# %%
ausgabe = f"""Hallo {spieler_name}!
Sie haben {anzahl_spiele}-mal gespielt \
und dabei {anzahl_gewinne}-mal gewonnen.\
"""
print(ausgabe)

# %%
ausgabe = (
    f"Hallo {spieler_name}!\n"
    f"Sie haben {anzahl_spiele}-mal gespielt "
    f"und dabei {anzahl_gewinne}-mal gewonnen."
)
print(ausgabe)

# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `015x-Workshop Mehr zu Strings`
#  - Abschnitt "Begrüßung 2"

# %% [markdown]
#
#  ## Extra Mini-Workshop
#
#  - Notebook `015x-Workshop Mehr zu Strings`
#  - Abschnitt "Piraten 4"

# %% [markdown]
#
#  ## Umwandlung in Strings
#
#  Python bietet zwei Funktionen an, mit denen beliebige Werte in Strings
#  umgewandelt werden können:
#
#  - `repr` für eine "programmnahe" Darstellung (wie könnte der Wert im Programm
#    erzeugt werden)
#  - `str` für eine "benutzerfreundliche" Darstellung

# %%
str("Hallo!")

# %%
str(123)

# %%
repr("Hallo!")

# %%
print(repr("Hallo!"))

# %% [markdown]
#
#  Für manche Datentypen liefern `str` und `repr` den gleichen String zurück:

# %%
print(str(["a", "b"]))
print(repr(["a", "b"]))

# %% [markdown]
#
#  ## Mehr zu F-Strings
#
#  Ob Werte in F-Strings mit `str()` oder `repr()` umgewandelt werden lässt sich
#  mit den Typkonvertierungen `!s` (der Default) oder `!r` steuern:

# %%
hallo = "Hallo!"
print(f"{hallo}")
print(f"{hallo!s}")
print(f"{hallo!r}")
print(f"{hallo!a}")

# %% [markdown]
#
#  Es gibt auch `!a` (`ascii()`, wie `repr()` mit escapes für nicht-ASCII-Character):

# %%
mood = "Größenwahn 😠"
print(ascii(mood))
print(f"{mood!a}")
print(f"{mood!r}")
print(f"{mood!s}")

# %% [markdown]
#
#  Mit `:n` kann man eine Mindestbreite für ein Element angeben. Mit `:<n` und
#  `:>n` und `:^n` kann man festlegen, wie der Text ausgerichtet werden soll:

# %%
print(f"|{hallo:20}|")
print(f"|{hallo:<20}|")
print(f"|{hallo:^20}|")
print(f"|{hallo:>20}|")

# %%
width = 10
print(f"|{hallo:^{width}}|")
print(f"|{hallo:^{width + len(hallo)}}|")

# %% [markdown]
#
#  Wenn sowohl Typkonvertierung als auch Format-Spezifikation angegeben werden,
#  dann muss die Typkonvertierung zuerst angegeben werden:

# %%
print(f"{hallo!r:^20}")

# %% [markdown]
#
#  Für manche Datentypen gibt es spezielle Formatanweisungen:

# %%
print(f"{2 ** 0.5}")
print(f"{2 ** 0.5:.2f}")
print(f"{2 ** 0.5:>10.2f}")

# %%
