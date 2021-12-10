# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# j2 import 'macros.j2' as doc
# %% [markdown] {{ doc.slide() }}
# {{ doc.header("Vertiefung zu Strings") }}

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Vergleich von Strings

# %%
"a" == "a"

# %%
"A" == "a"

# %% {"slideshow": {"slide_type": "subslide"}}
"A" < "B"

# %%
"A" < "a"

# %%
"a" < "A"

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Strings sind wie im Wörterbuch (lexikographisch) geordnet

# %%
"ab" < "abc"

# %%
"ab" < "ac"

# %%
"ab" != "ac"

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Einschub: Sortieren von Listen/Iterables
#
# Mit der Funktion `sorted()` können iterables sortiert werden. Mit dem
# benannten Argument `key` kann eine Funktion angegeben werden, die bestimmt,
# wie die Sortierung erfolgt:

# %%
numbers = [3, 8, -7, 1, 0, 2, -3, 3]

# %% {{ doc.codealong() }}
sorted(numbers)

# %% {{ doc.codealong() }}
sorted(numbers, key=abs)

# %% {"slideshow": {"slide_type": "subslide"}}
strings = ["a", "ABC", "xy", "Asdfgh", "foo", "bar", "quux"]

# %% {{ doc.codealong() }}
sorted(strings)


# %% {{ doc.codealong() }}
def lower(my_string):
    return my_string.lower()


# %% {{ doc.codealong() }}
sorted(strings, key=lower)

# %% {{ doc.codealong() }}
sorted(strings, key=len)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
#
# ## Vergleich von Unicode Strings
#
# Die eingebauten Vergleichsfunktionen sind nur für einfache (ASCII) Strings
# sinnvoll. Für Strings, die Unicode-Zeichen enthalten ist Sortieren/Vergleichen
# schwieriger.
#
# Das Standard Modul in Python ist `locale`; das auf die Locale-Settings des
# Betriebssystems zurückgreift:

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
import locale

locale.getlocale()

# %%
my_strings = ["o", "oa", "oe", "ö", "oz", "sa", "s", "ß", "ss", "sz"]

# %% {{ doc.codealong() }}
sorted(my_strings)

# %% {{ doc.codealong() }}
sorted(my_strings, key=locale.strxfrm)

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
locale.setlocale(locale.LC_COLLATE, "de_DE.UTF-8")

# %% {{ doc.codealong() }}
sorted(my_strings, key=locale.strxfrm)

# %% {{ doc.codealong() }}
locale.setlocale(locale.LC_COLLATE, "C")

# %% {{ doc.codealong() }}
sorted(my_strings, key=locale.strxfrm)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
#
# Die Locale Settings sind global pro Prozess und deshalb hauptsächlich geeignet
# um mit dem Benutzer zu interagieren. 
#
# Wenn man mit Strings in verschiedenen Sprachen umgehen muss empfiehlt sich die
# Verwendung von Bibliotheken wie `PyUCA` (in Python geschrieben und daher
# leichter zu installieren) oder `PyICU` (vollständigere Implementierung der
# Unicode Spezifikation, basierend auf einer C++ Bibliothek).


# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Umwandeln eines Strings in Groß-/Kleinbuchstaben

# %% {{ doc.codealong() }}
text = "Das ist ein Text"
print(text.lower())
print(text)

# %% {{ doc.codealong() }}
"Das ist ein Text".upper()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
#
# Die `lower()` Methode führt nicht immer die gewünschten Umwandlungen durch.
# Die `casefold` Methode is dafür manchmal nützlich:

# %% {{ doc.codealong() }}
s1 = "daß er sehe"
s1.upper()

# %% {{ doc.codealong() }}
s1.lower()

# %% {{ doc.codealong() }}
s1.casefold()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Mini-Workshop
#
# - Notebook `workshop_070_more_strings_and_sorting`
# - Abschnitt "Shout"


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Nochmal String Literale
#
# - String-Literale werden in einfache oder doppelte Anführungszeichen
#   eingeschlossen
#     - `"Hello, world!"`
#     - `'Hallo Welt!'`
#     - Welche Form man wählt spielt keine Rolle, außer man will
#       Anführungszeichen im String haben
#     - `"Er sagt 'Huh?'"`
#     - `'Sie antwortet: "Genau."'`

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# - String-Literale, können Unicode Zeichen enthalten:
#     - `"おはようございます"`
#     - `"😠🙃🙄"`

# %%
print("Er sagt 'Huh?'")
print('Sie antwortet: "Genau."')
print("おはようございます")
print("😠🙃🙄")

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# - Sonderzeichen können mit *Escape-Notation* angegeben werden:
#     - `\n`, `\t`, `\\`, `\"`, `\'`, ...
#     - `\u`, `\U` für Unicode code points (16 bzw. 32 bit)
#     - `\N{...}` für Unicode

# %%
print("a\tbc\td\n123\t4\t5")

# %%
print('"Let\'s go crazy", she said')

# %%
print("C:\\Users\\John")

# %% {"slideshow": {"slide_type": "subslide"}}
print("\u0394 \u03b1 \t\U000003b2 \U000003b3")
print("\U0001F62E \U0001f61a \U0001f630")

# %%
print("\N{GREEK CAPITAL LETTER DELTA} \N{GREEK SMALL LETTER ALPHA}")
print("\N{smiling face with open mouth and smiling eyes} \N{winking face}")

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# - String Literale können auch in 3-fache Anführungszeichen eingeschlossen
#   werden
# - Diese Art von Literalen kann über mehrere Zeilen gehen

# %%
"""Das ist
ein String-Literal,
das über mehrere
Zeilen geht."""

# %%
print(
    """Mit Backslash am Ende der Zeile \
kann der Zeilenvorschub unterdrückt werden."""
)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Konkatenation von Strings
#
# Mit `+` können Strings aneinandergehängt (konkateniert) werden:

# %%
"Ein" + " " + "String"

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Mit der `join()` Methode können mehrere Strings mit einem Trennzeichen (oder Trenn-String) zusammengefügt werden:

# %%
" ".join(["das", "sind", "mehrere", "strings"])

# %%
", ".join(["Pferd", "Katze", "Hund"])

# %%
"".join(["ab", "cde", "f"])

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Mini-Workshop
#
# - Notebook `workshop_070_more_strings_and_sorting`
# - Abschnitt "Begrüßung 1"

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
#
# ## Nochmal Vergleich von Strings
#
# Um Strings mit Unicode-Zeichen zu vergleichen ist es zweckmäßig sie in
# Unicode-Normalform zu bringen.

# %%
s1 = "café"
s2 = "cafe\u0301"

# %% {{ doc.codealong() }}
print(s1, s2)
s1 == s2

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
import unicodedata
unicodedata.normalize("NFC", s1) == s1

# %% {{ doc.codealong() }}
unicodedata.normalize("NFC", s2) == s1

# %% {{ doc.codealong() }}
unicodedata.normalize("NFD", s1) == s2


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # String Interpolation: F-Strings
#
# Python bietet die Möglichkeit, Werte von Variablen in Strings einzusetzen:

# %% {{ doc.codealong() }}
name = "Hans"
zahl = 12
f"Hallo, {name}, die Zahl ist {zahl + 1}"

# %% {"slideshow": {"slide_type": "subslide"}}
spieler_name = "Hans"
anzahl_spiele = 10
anzahl_gewinne = 2

ausgabe = f"Hallo {spieler_name}!\nSie haben {anzahl_spiele}-mal gespielt und dabei {anzahl_gewinne}-mal gewonnen."
print(ausgabe)

# %% {"slideshow": {"slide_type": "subslide"}}
ausgabe = f"""\
Hallo {spieler_name}!
Sie haben {anzahl_spiele}-mal gespielt \
und dabei {anzahl_gewinne}-mal gewonnen.\
"""
print(ausgabe)

# %% {"slideshow": {"slide_type": "subslide"}}
ausgabe = (
    f"Hallo {spieler_name}!\n"
    f"Sie haben {anzahl_spiele}-mal gespielt "
    f"und dabei {anzahl_gewinne}-mal gewonnen."
)
print(ausgabe)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Mini-Workshop
#
# - Notebook `workshop_070_more_strings_and_sorting`
# - Abschnitt "Begrüßung 2"

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Mini-Workshop
#
# - Notebook `workshop_070_more_strings_and_sorting`
# - Abschnitt "Piraten 4"

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Finden in Strings
#
# Der `in` Operator funktioniert auch mit Strings als Argument. Um den Index eines Substrings in einem String zu finden kann man die `index()`-Methode verwenden.

# %% {{ doc.codealong() }}
"a" in "abc"

# %% {{ doc.codealong() }}
"x" not in "abc"

# %% {{ doc.codealong() }}
"bc" in "abc"

# %% {{ doc.codealong() }}
"cb" in "abc"

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
"Halloween".index("Hallo")

# %% {{ doc.codealong() }}
"Halloween".index("we")

# %%
# "Team".index("I")

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Workshop
#
# - Notebook `lecture_920x_Workshop_Cäsar_Verschlüsselung`

# %%
