# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Vertiefung zu Strings</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>More Strings</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# # Vergleich von Strings

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # Comparison of strings

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

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Strings sind wie im Wörterbuch (lexikographisch) geordnet

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# Strings are ordered as in the dictionary (lexicographically).

# %%
"ab" < "abc"

# %%
"ab" < "ac"

# %%
"ab" != "ac"

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Einschub: Sortieren von Listen/Iterables
#
# Mit der Funktion `sorted()` können iterables sortiert werden. Mit dem
# benannten Argument `key` kann eine Funktion angegeben werden, die bestimmt,
# wie die Sortierung erfolgt:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Inset: sorting lists/iterables
#
# Iterables can be sorted with the `sorted()` function. With the
# named argument `key`, a function can be specified that determines
# how the sorting is done:

# %%
numbers = [3, 8, -7, 1, 0, 2, -3, 3]

# %% {"tags": ["code-along"]}
sorted(numbers)

# %% {"tags": ["code-along"]}
sorted(numbers, key=abs)

# %% {"slideshow": {"slide_type": "subslide"}}
strings = ["a", "ABC", "xy", "Asdfgh", "foo", "bar", "quux"]

# %% {"tags": ["code-along"]}
sorted(strings)


# %% {"tags": ["code-along"]}
def lower(my_string):
    return my_string.lower()


# %% {"tags": ["code-along"]}
sorted(strings, key=lower)

# %% {"tags": ["code-along"]}
sorted(strings, key=len)

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
#
# ## Vergleich von Unicode Strings
#
# Die eingebauten Vergleichsfunktionen sind nur für einfache (ASCII) Strings
# sinnvoll. Für Strings, die Unicode-Zeichen enthalten ist Sortieren/Vergleichen
# schwieriger.
#
# Das Standard Modul in Python ist `locale`; das auf die Locale-Settings des
# Betriebssystems zurückgreift:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Comparison of Unicode strings
#
# The built-in comparison functions work only for simple (ASCII) strings. For strings containing Unicode characters, sorting/comparison is more difficult.
#
# The default module for dealing with Unicode in Python is `locale`; it relies on the locale settings of the
# operating system:

# %% {"tags": ["code-along"]}
import locale

locale.getlocale()

# %%
my_strings = ["o", "oa", "oe", "ö", "oz", "sa", "s", "ß", "ss", "sz"]

# %% {"tags": ["code-along"]}
sorted(my_strings)

# %% {"tags": ["code-along"]}
sorted(my_strings, key=locale.strxfrm)

# %% {"incorrectly_encoded_metadata": "{\"slideshow\": {\"slide_type\": \"subslide\"}} tags=[\"code-along\"]"}
locale.setlocale(locale.LC_COLLATE, "de_DE.UTF-8")

# %% {"tags": ["code-along"]}
sorted(my_strings, key=locale.strxfrm)

# %% {"tags": ["code-along"]}
locale.setlocale(locale.LC_COLLATE, "C")

# %% {"tags": ["code-along"]}
sorted(my_strings, key=locale.strxfrm)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
# Die Locale Settings sind global pro Prozess und deshalb hauptsächlich geeignet
# um mit dem Benutzer zu interagieren.
#
# Wenn man mit Strings in verschiedenen Sprachen umgehen muss empfiehlt sich die
# Verwendung von Bibliotheken wie `PyUCA` (in Python geschrieben und daher
# leichter zu installieren) oder `PyICU` (vollständigere Implementierung der
# Unicode Spezifikation, basierend auf einer C++ Bibliothek).


# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# The locale settings are global per process and therefore mainly suitable
# to interact with the user.
#
# If you have to deal with strings in different languages, 
# using libraries like `PyUCA` (written in Python and therefore
# easier to install) or `PyICU` (more complete implementation of the
# Unicode specification based on a C++ library) might be a good idea.

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Umwandeln eines Strings in Groß-/Kleinbuchstaben

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Converting a string to uppercase/lowercase

# %% {"tags": ["code-along"]}
text = "Das ist ein Text"
print(text.lower())
print(text)

# %% {"tags": ["code-along"]}
"Das ist ein Text".upper()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
# Die `lower()` Methode führt nicht immer die gewünschten Umwandlungen durch.
# Die `casefold` Methode is dafür manchmal nützlich:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# The `lower()` method does not always perform the desired conversions.
# The `casefold` method is sometimes useful for this:

# %% {"tags": ["code-along"]}
s1 = "daß er sehe"
s1.upper()

# %% {"tags": ["code-along"]}
s1.lower()

# %% {"tags": ["code-along"]}
s1.casefold()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Mini-Workshop
#
# - Notebook `workshop_070_more_strings_and_sorting`
# - Abschnitt "Shout"


# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
# - Notebook `workshop_070_more_strings_and_sorting`
# - "Shout" section

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
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

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # String literals (again)
#
# - String literals are enclosed in single or double quotes
#     - `"Hello, world!"`
#     - `'Hello world!'`
#     - It doesn't matter which form you choose, unless you want to
#       have double quotes in the string
#     - `"He says 'Huh?'"`
#     - `'She replies: "Exactly."'`

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# - String-Literale, können Unicode Zeichen enthalten:
#     - `"おはようございます"`
#     - `"😠🙃🙄"`

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# - String literals, can contain Unicode characters:
#     - `"おはようございます"`
#     - `"😠🙃🙄"`

# %%
print("Er sagt 'Huh?'")
print('Sie antwortet: "Genau."')
print("おはようございます")
print("😠🙃🙄")

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# - Sonderzeichen können mit *Escape-Notation* angegeben werden:
#     - `\n`, `\t`, `\\`, `\"`, `\'`, ...
#     - `\u`, `\U` für Unicode code points (16 bzw. 32 bit)
#     - `\N{...}` für Unicode

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# - Special characters can be specified with *escape notation*:
#     - `
# `, `\t`, `\`, `"`, `\'`, ...
#     - `\u`, `\U` for Unicode code points (16 or 32 bit)
#     - `\N{...}` for Unicode

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

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# - String Literale können auch in 3-fache Anführungszeichen eingeschlossen
#   werden
# - Diese Art von Literalen kann über mehrere Zeilen gehen

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# - String literals can also be enclosed in triple quotes
# - This type of literal can span multiple lines

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

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Konkatenation von Strings
#
# Mit `+` können Strings aneinandergehängt (konkateniert) werden:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Concatenation of strings
#
# Strings can be concatenated with `+`:

# %%
"Ein" + " " + "String"

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Mit der `join()` Methode können mehrere Strings mit einem Trennzeichen (oder Trenn-String) zusammengefügt werden:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# The `join()` method can be used to join multiple strings with a delimiter:

# %%
" ".join(["das", "sind", "mehrere", "strings"])

# %%
", ".join(["Pferd", "Katze", "Hund"])

# %%
"".join(["ab", "cde", "f"])

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Mini-Workshop
#
# - Notebook `workshop_070_more_strings_and_sorting`
# - Abschnitt "Begrüßung 1"

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
# - Notebook `workshop_070_more_strings_and_sorting`
# - Section "Welcome 1"

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
# ## Nochmal Vergleich von Strings
#
# Um Strings mit Unicode-Zeichen zu vergleichen ist es zweckmäßig sie in
# Unicode-Normalform zu bringen.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## String comparison (again)
#
# To compare strings with Unicode characters, it is convenient to use them in
# bring Unicode normal form.

# %%
s1 = "café"
s2 = "cafe\u0301"

# %% {"tags": ["code-along"]}
print(s1, s2)
s1 == s2

# %% {"incorrectly_encoded_metadata": "{\"slideshow\": {\"slide_type\": \"subslide\"}} tags=[\"code-along\"]"}
import unicodedata

unicodedata.normalize("NFC", s1) == s1

# %% {"tags": ["code-along"]}
unicodedata.normalize("NFC", s2) == s1

# %% {"tags": ["code-along"]}
unicodedata.normalize("NFD", s1) == s2


# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# # String Interpolation: F-Strings
#
# Python bietet die Möglichkeit, Werte von Variablen in Strings einzusetzen:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # String interpolation: F strings
#
# Python offers the possibility to insert values ​​of variables into strings:

# %% {"tags": ["code-along"]}
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

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Mini-Workshop
#
# - Notebook `workshop_070_more_strings_and_sorting`
# - Abschnitt "Begrüßung 2"

# %% [markdown] {"lang": "en"}
# ## Mini workshop
#
# - Notebook `workshop_070_more_strings_and_sorting`
# - Section "Welcome 2"

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Mini-Workshop
#
# - Notebook `workshop_070_more_strings_and_sorting`
# - Abschnitt "Piraten 4"

# %% [markdown] {"lang": "en"}
# ## Mini workshop
#
# - Notebook `workshop_070_more_strings_and_sorting`
# - Section "Pirates 4"

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Finden in Strings
#
# Der `in` Operator funktioniert auch mit Strings als Argument. Um den Index
# eines Substrings in einem String zu finden kann man die `index()`-Methode
# verwenden.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Finding substrings in strings
#
# The `in` operator also works with strings as arguments. To find the index
# of a substring in a string you can use the `index()` method.

# %% {"tags": ["code-along"]}
"a" in "abc"

# %% {"tags": ["code-along"]}
"x" not in "abc"

# %% {"tags": ["code-along"]}
"bc" in "abc"

# %% {"tags": ["code-along"]}
"cb" in "abc"

# %% {"tags": ["code-along"]}
"Halloween".index("Hallo")

# %% {"tags": ["code-along"]}
"Halloween".index("we")

# %% {"tags": ["code-along"]}
# "Team".index("I")

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Workshop
#
# - Notebook `lecture_920x_Workshop_Cäsar_Verschlüsselung`

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Workshop
#
# - Notebook `lecture_920x_Workshop_Caesar_Encryption`

# %%
