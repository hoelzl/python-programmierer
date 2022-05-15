# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     formats: py:percent
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
# <div style="text-align:center; font-size:200%;"><b>Einführung in Python: Grundlagen Teil 1</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Introduction to Python: Part 1</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# # Woraus besteht ein Programm?
#
# Wir wollen ein Programm schreiben, das
#
# ```
# Hello, world!
# ```
#
# auf dem Bildschirm ausgibt.
#
# Was benötigen wir dazu?

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # Parts of a program
#
# We want to write a program that outputs
#
# ```
# Hello world!
# ```
#
# on the screen.
#
# What do we need for this?

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Was benötigen wir dazu?
#
# - Daten
#     - den Text `Hello, world!`
# - Anweisungen
#     - *Gib den folgenden Text auf dem Bildschirm aus*
# - Kommentare
#     - Hinweise für den Programmierer, werden von Python ignoriert

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# What do we need for this?
#
# - Data
#     - the text `Hello, world!`
# - Instructions
#     - *Output the following text on the screen*
# - Comments
#     - Notes for the programmer, are ignored by Python

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Kommentare
#
# - `#` gefolgt von beliebigem Text
# - bis zum Ende der Zeile

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Comments
#
# - `#` followed by any text
# - to the end of the line

# %%
# Das ist ein Kommentar.
# Alle Zeilen in dieser Zelle werden
# von Python ignoriert.


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# # Daten
#
# - Zahlen: `123`, `3.141592`
# - Text (Strings): `'Das ist ein Text'`, `"Hello, world!"`

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# # Data
#
# - Numbers: `123`, `3.141592`
# - Text (strings): `'This is a text'`, `"Hello, world!"`

# %% {"slideshow": {"slide_type": "subslide"}} tags=["code-along"]
123

# %% {"tags": ["code-along"]}
3.141592

# %% {"slideshow": {"slide_type": "subslide"}} tags=["code-along"]
"Das ist ein Text"

# %% {"tags": ["code-along"]}
'Hello, world!'

# %% {"tags": ["code-along"]}
"""Auch ein Text. (Another text.)
Der über mehrere Zeilen geht. (Spanning multiple lines.)"""

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Anzeige von Werten mit der `print()` Funktion
# Um Werte anzuzeigen kann man die `print()`-Funktion verwenden:
#
# `print(...)` gibt den in Klammern eingeschlossenen Text auf dem Bildschirm
# aus.

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# Displaying values with the `print()` function
# To display values ​​you can use the `print()` function:
#
# `print(...)` prints the values between the trailing parens on the screen.

# %% {"tags": ["code-along"]}
print(123)

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
print("Hello, world!")

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Einschub: Anzeige von Werten in Jupyter Notebooks
#
# - Jupyter Notebooks geben den letzten Wert jeder Zelle auf dem Bildschirm aus
# - Das passiert in "normalen" Python-Programmen nicht!
#   - Wenn sie als Programme ausgeführt werden
#   - Der interaktive Interpreter verhält sich ähnlich wie Notebooks

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# ## Excursion: displaying values in Jupyter notebooks
#
# - Jupyter notebooks print the last value of each cell on the screen
# - That doesn't happen in "normal" Python programs!
#   - At least when they are executed as programs
#   - The interactive interpreter behaves similar to notebooks

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
123

# %% [markdown] {"lang": "de"}
# Um die Ausgabe des letzten Wertes einer Zelle in Jupyter zu unterbinden
# kann man die Zeile mit einem Strichpunkt beenden:

# %% [markdown] {"lang": "en"}
# To prevent the output of the last value of a cell in Jupyter
# you can end the line with a semicolon:

# %% {"tags": ["code-along"]}
123

# %% {"tags": ["code-along"]}
# fmt: off
123;
# fmt: on

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Mini-Workshop
#
# - Notebook `workshop_050_introduction_part1`
# - Abschnitt "Einleitung"

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
# - Notebook `workshop_050_introduction_part1`
# - Section "Introduction"

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Zurück zur `print()` Funktion
#
# Der `print()` Funktion können mehrere Argumente übergeben werden.
# - Die Argumente werden durch Kommata getrennt
# - Alle Argumente werden in einer Zeile ausgegeben, mit Leerzeichen zwischen den Argumenten.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Back to the `print()` function
#
# Multiple arguments can be passed to a `print()` function call:
# - The arguments are separated by commas
# - All arguments are printed on one line, with spaces between arguments.

# %% {"tags": ["code-along"]}
print("Der Wert von 1 + 1 ist", 1 + 1, ".")

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Durch Angabe eines *benannten Arguments* `sep=''` kann die Ausgabe der
# Leerzeichen unterdrückt werden:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# By supplying a *named argument* `sep=''`, the spaces in the output are suppressed:

# %% {"tags": ["code-along"]}
print("Der Wert von 1 + 1 ist", 1 + 1, ".", sep="")

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Es sind auch beliebige andere Strings als Wert des Arguments `sep` zulässig:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# Any other strings are also allowed as the value of the `sep` argument:

# %% {"tags": ["code-along"]}
# CSV (don't do this!)
print(1, 3, 7.5, 2, sep=",")

# %% {"tags": ["code-along"]}
# Uh, oh
print(1, 3, 7.5, 2, "who, me?", sep=",")

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# # Zahlen und Mathematik
#
# - Ganze Zahlen: `1`, `837`, `-12`
# - Gleitkommazahlen: `0.5`, `123.4`, `-0.01`
# - Rechenoperationen:
#     - Addition: `+`
#     - Subtraktion: `-`
#     - Multiplikation: `*`
#     - Division: `/`

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # Numbers and maths
#
# - Integers: `1`, `837`, `-12`
# - Floating point numbers: `0.5`, `123.4`, `-0.01`
# - Arithmetic operations:
#     - Addition: `+`
#     - Subtraction: `-`
#     - Multiplication: `*`
#     - Division: `/`

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Python als Taschenrechner

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Python as pocket calculator

# %% {"tags": ["code-along"]}
17 + 4

# %% {"tags": ["code-along"]}
1 + 4 * 4 + (3 - 1) * (1 + 1)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Arten von Zahlen
#
# - Python unterscheidet ganze Zahlen und Gleitkommazahlen:
#     - `1` ist eine ganze Zahl (`int`)
#     - `1.0` ist eine Gleitkommazahl (`float`)
# - Mit `type(...)` kann man den Typ des Arguments erfahren:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Different types of numbers
#
# - Python distinguishes integers and floating point numbers:
#     - `1` is an integer (`int`)
#     - `1.0` is a floating point number (`float`)
# - With `type(...)` you can get the type of the argument:

# %% {"slideshow": {"slide_type": "subslide"}} tags=["code-along"]
type(1)

# %% {"tags": ["code-along"]}
type(1.0)

# %% {"tags": ["code-along"]}
type("1")

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Ganze Zahlen in Python haben keine (praktisch relevante) Obergrenze:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# Integers in Python have no (practically relevant) upper limit:

# %% {"tags": ["code-along"]}
10000000000000000000000000000000000000000000000000 + 500

# %% {"tags": ["code-along"]}
type(10000000000000000000000000000000000000000000000000)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Mini-Workshop
#
# - Notebook `workshop_050_introduction_part1`
# - Abschnitt "Zahlen und Mathematik"

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
# - Notebook `workshop_050_introduction_part1`
# - Section "Numbers and mathematics"

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Rechenoperationen
#
# | Operator | Operation            |
# |:--------:|:---------------------|
# | +        | Summe                |
# | -        | Differenz            |
# | *        | Multiplikation       |
# | /        | Division             |
# | **       | Potenz               |
# | %        | Modulo, Rest         |
# | //       | ganzzahlige Division |

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Arithmetic operations
#
# | Operator | Operation            |
# |:--------:|:---------------------|
# | +        | Sum                  |
# | -        | Difference           |
# | *        | Multiplication       |
# | /        | Division             |
# | **       | Power                |
# | %        | Modulo, Remainder    |
# | //       | Integer division     |

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Division

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ### Division

# %% {"tags": ["code-along"]}
4 / 2

# %% {"tags": ["code-along"]}
20 / 7

# %% {"slideshow": {"slide_type": "subslide"}} tags=["code-along"]
# // und % können zur Division mit Rest verwendet werden:
20 // 7  # Wie oft geht 7 in 20?

# %% {"tags": ["code-along"]}
20 % 7  # Welcher Rest bleibt dabei?

# %% {"tags": ["code-along"]}
(20 // 7) * 7 + (20 % 7)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# `/` ist links-assoziativ (genau wie `//`, `%`, `+`, `-`, `*`)

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# `/` is left-associative (just like `//`, `%`, `+`, `-`, `*`)

# %% {"tags": ["code-along"]}
20 / 5 / 2

# %% {"tags": ["code-along"]}
# Besser:
(20 / 5) / 2

# %% {"tags": ["code-along"]}
20 / (5 / 2)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Exponentiation (Potenz)

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ### Exponentiation (power)

# %% {"tags": ["code-along"]}
2**3

# %% {"tags": ["code-along"]}
2 * 2 * 2

# %% {"tags": ["code-along"]}
2**4

# %% {"tags": ["code-along"]}
2 * 2 * 2 * 2

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# `**` ist rechts-assoziativ
#
# $2^{(2^3)} = 2^8 = 256 \qquad$
# $(2^2)^3 = 4^3 = 64$

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# `**` is right-associative
#
# $2^{(2^3)} = 2^8 = 256 \qquad$
# $(2^2)^3 = 4^3 = 64$

# %% {"tags": ["code-along"]}
2**2**3

# %% {"tags": ["code-along"]}
2 ** (2**3)

# %% {"tags": ["code-along"]}
(2**2) ** 3

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Der `**` Operator kann auch zum Wurzelziehen verwendet werden:
#
# $\sqrt{4} = 4^{1/2} = 2$
# $\sqrt{9} = 9^{1/2} = 3$
# $\sqrt{2} = 2^{1/2} \approx 1.4142$

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# The `**` operator can also be used to extract roots:
#
# $\sqrt{4} = 4^{1/2} = 2$
# $\sqrt{9} = 9^{1/2} = 3$
# $\sqrt{2} = 2^{1/2} \approx 1.4142$

# %% {"tags": ["code-along"]}
4**0.5

# %% {"tags": ["code-along"]}
9**0.5

# %% {"tags": ["code-along"]}
2**0.5

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# # Variablen
#
# Wir wollen einen Zaun um unser neues Grundstück bauen.
#
# <img src="img/fence.svg" style="display:block;margin:auto;width:50%"/>

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # Variables
#
# We want to build a fence around our new property.
#
# <img src="img/fence.svg" style="display:block;margin:auto;width:50%"/>

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# <img src="img/fence.svg" style="vertical-align:top;overflow:auto;float:right;width:25%"/>
#
# Die gemessenen Längen sind:
# - Birkenweg: 20m
# - Fichtengasse: 30m
#
# Wie lange muss unser Zaun sein?

# %% [markdown] {"lang": "en"}
# <img src="img/fence.svg" style="vertical-align:top;overflow:auto;float:right;width:25%"/>
#
# The measured lengths are:
# - Birkenweg: 20m
# - Fichtengasse: 30m
#
# How long does our fence have to be?

# %% {"tags": ["code-along"]}
20 + 30 + (20**2 + 30**2) ** 0.5

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# <img src="img/fence.svg" style="vertical-align:top;overflow:auto;float:right;width:25%"/>
#
# Es ist nicht klar, was die Zahlen in dem vorhergehenden Ausdruck bedeuten. Können wir das besser machen?

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# <img src="img/fence.svg" style="vertical-align:top;overflow:auto;float:right;width:25%"/>
#
# It is not clear what the numbers in the preceding expression mean. Can we do better?

# %% {"tags": ["code-along"]}
länge_birkenweg = 20
länge_fichtengasse = 30
länge_hauptstr = (länge_birkenweg**2 + länge_fichtengasse**2) ** 0.5
länge_gesamt = länge_birkenweg + länge_fichtengasse + länge_hauptstr
ergebniss = länge_gesamt

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Genauere Beschreibung von Variablen
#
# <img src="img/variables-01.svg" style="float:right;margin:auto;width:50%"/>
#
# Eine *Variable* ist
# - ein <span style="color:red;">"Verweis"</span> auf ein "Objekt"
# - der einen <span style="color:red;">Namen</span> hat.
#
# <span style="color:blue;">Ein Objekt</span> kann von <span style="color:blue;">mehreren Variablen</span><br/>
# referenziert werden!

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## More detailed description of variables
#
# <img src="img/variables-01.svg" style="float:right;margin:auto;width:50%"/>
#
# A *variable* is
# - a <span style="color:red;">"reference"</span> to an "object"
# - which has a <span style="color:red;">name</span>.
#
# <span style="color:blue;">An object </span> can be referenced by<span style="color:blue;"> several variables </span>!

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# <img src="img/variables-01.svg" style="float:right;margin:auto;width:50%"/>
#
# Einve Variable wird
# - erzeugt durch `name = wert`
# - gelesen durch `name`
# - geändert durch `name = wert`
#
# Erzeugen und Ändern von Variablen<br/>
# sind *Anweisungen*.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# <img src="img/variables-01.svg" style="float:right;margin:auto;width:50%"/>
#
# A variable is
# - generated by `name = value`
# - read by `name`
# - changed by `name=value`
#
# Creating and changing variable <br/>
# are *statements*.

# %% {"slideshow": {"slide_type": "subslide"}} tags=["code-along"]
länge_birkenweg = 20
print(länge_birkenweg)
länge_birkenweg = 25
print(länge_birkenweg)

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Eigenschaften von Variablen in Python
#
# - Eine Variable kann Werte mit beliebigem Datentyp speichern
#     - Es gibt keine `int`-Variablen, etc.
#     - Man sagt: Python ist dynamisch getypt
# - Variablen müssen erzeugt worden sein, bevor sie verwendet werden
# - Man kann Variablen neue Werte zuweisen
#     - Dabei kann der *alte Wert* der Variablen auf der rechten Seite verwendet werden:<br/> `jobs = jobs + 1`

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Properties of variables in Python
#
# - A variable can store values of any data type
#     - There are no `int` variables, etc.
#     - Anather way of saying this: Python is dynamically typed
# - Variables must be created before they are used
# - You can assign new values to variables
#     - The *old value* of the variable can be used on the right hand side:<br/> `jobs = jobs + 1`

# %% {"slideshow": {"slide_type": "subslide"}} tags=["code-along"]
x = "Hallo!"
print(x)
x = 123
print(x)
x = x + 1
print(x)
x += 1
print(x)

# %% {"slideshow": {"slide_type": "subslide"}} tags=["code-along"]
# print(diese_variable_gibt_es_nicht)


# %% {"tags": ["code-along"]}
# nonono = nonono + 1


# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Variablennamen in Python
#
# - Fangen mit einem Buchstaben oder Unterstrich `_` an
#     - Umlaute gelten auch als Buchstaben
# - Können Ziffern, Buchstaben und Unterstriche `_` enthalten
# - Können viele andere Unicode-Zeichen enthalten
#     - Es ist aber meist besser, das zu vermeiden...
# - Groß- und Kleinschreibung wird unterschieden
#     - `A` ist eine andere Variable als `a`
#

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Variable names in Python
#
# - Begin with a letter or underscore `_`
#     - Umlauts also count as letters
# - Can contain digits, letters and underscores `_`
# - May contain many other Unicode characters
#     - But it's usually better to avoid them...
# - A distinction is made between upper and lower case
#     - `A` is a different variable than `a`

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Stil
#
# - Variablennamen werden klein geschrieben
#     - Außer konstanten Variablen: `CONSTANT_VAR`
# - Bestandteile werden durch Unterstriche `_` getrennt
#     - Dieser Stil nennt sich Snake-Case
# - Variablen, die mit zwei Unterstrichen anfangen und aufhören haben
#   typischerweise eine spezielle Bedeutung (*Dunders*):
#     - `__class__`, `__name__`
#     - Normale benutzerdefinierte Variablen sollten nicht als Dunders benannt
#       werden

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ### Style
#
# - Variable names are written in lower case
#     - Except constant variables: `CONSTANT_VAR`
# - Components are separated by underscores `_`
#     - This style is called snake case
# - Variables that start and end with two underscores
#   typically have a special meaning (*dunders*):
#     - `__class__`, `__name__`
#     - Normal user-defined variables should not be dunders

# %% {"slideshow": {"slide_type": "subslide"}} tags=["code-along"]
print(__name__)
print(type(__name__))

# %% {"tags": ["code-along"]}
# Bitte nicht nachmachen, obwohl es möglich ist/ Don't do this:
__my_var__ = 123

# %% {"tags": ["code-along"]}
__my_var__

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# - Manchmal werden "private" Variablen mit einem führenden Unterstrich
#   geschrieben: `_my_var`
#     - Das ist (für globale Variablen) besonders in älterem Code verbreitet
#     - In Klassen gibt es weitere Konventionen
# - Die meisten Python-Projekte folgen den Konventionen in
#   [PEP 8](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# - Sometimes "private" variables are written with a leading underscore: `_my_var`
#     - This is particularly common in older code (for global variables)
#     - There are more conventions for classes
# - Most Python projects follow the conventions in
#   [PEP 8](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

# %% {"tags": ["code-along"]}
_my_var = 234

# %% {"tags": ["code-along"]}
_my_var

# %% {"slideshow": {"slide_type": "subslide"}}
variable_1 = 123
VARIABLE_1 = 234
Variable_1 = 345
variablE_1 = 456

# %%
print(variable_1)
print(VARIABLE_1)
print(Variable_1)
print(variablE_1)

# %% {"slideshow": {"slide_type": "subslide"}} tags=["code-along"]
_my_var = 1
print(_my_var)
_my_var = _my_var + 5
print(_my_var)

# %% {"slideshow": {"slide_type": "subslide"}}
größenmaßstäbe_der_fußgängerübergänge = 0.3
größenmaßstäbe_der_fußgängerübergänge

# %%
# me@foo = 1


# %% {"slideshow": {"slide_type": "subslide"}}
α = 0.2
β = 0.7
γ = α**2 + 3 * β**2
print(γ)
αβγ = α * β * γ
print(αβγ)
Σ = 1 + 2 + 3
print(Σ)
# ∑ = 1 + 2 + 3 # Unzulässig!


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Mini-Workshop
#
# - Notebook `workshop_050_introduction_part1`
# - Abschnitt "Piraten"

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
# - Notebook `workshop_050_introduction_part1`
# - Section "Pirates"

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Zuweisung an mehrere Variablen
#
# In Python können mehrere Variablen gleichzeitig definiert bzw. mit neuen
# Werten versehen werden:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Assignment to multiple variables
#
# In Python, multiple variables can be defined (or assigned values) at the same time:

# %% {"tags": ["code-along"]}
a, b = 1, 2
print(a)
print(b)

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# # Funktionen
#
# Wir haben eine Firma zum Einzäunen dreieckiger Grundstücke gegründet.
#
# Für jedes von Straßen $A$, $B$ und $C$ begrenze Grundstück berechnen wir:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # Functions
#
# We want to start a company for fencing triangular plots of land.
#
# For each property bordered by streets $A$, $B$ and $C$ we calculate:

# %%
länge_a = 10  # Beispielwert
länge_b = 40  # Beispielwert
länge_c = (länge_a**2 + länge_b**2) ** 0.5
länge_gesamt = länge_a + länge_b + länge_c
print(länge_gesamt)


# %% [markdown] {"lang": "de"}
# Können wir das etwas eleganter gestalten?

# %% [markdown] {"lang": "en"}
# Can we make this a little more elegant?

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Satz von Pythagoras
#
# Wir berechnen die Länge von $C$ aus $A$ und $B$ immer nach dem Satz von
# Pythagoras: $C = \sqrt{A^2 + B^2}$.
#
# Das können wir in Python durch eine *Funktion* ausdrücken:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Pythagorean theorem
#
# We always calculate the length of $C$ from $A$ and $B$ according to the theorem of
# Pythagoras: $C = \sqrt{A^2 + B^2}$.
#
# We can express this in Python using a *function*:

# %% {"slideshow": {"slide_type": "subslide"}} tags=["code-along"]
def pythagoras(a, b):
    c = (a**2 + b**2) ** 0.5
    return c


# %% {"tags": ["code-along"]}
pythagoras(3, 4)

# %% {"tags": ["code-along"]}
pythagoras(1, 1)


# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Funktionsdefinition
# - Schlüsselwort `def`
# - Name der Funktion
# - Parameter der Funktion, in Klammern; Doppelpunkt
# - Rumpf der Funktion, einen Tabulator eingerückt
# - Im Rumpf können die Parameter wie Variablen verwendet werden
# - Schlüsselwort `return`
#     - Beendet die Funktion
#     - Bestimmt welcher Wert zurückgegeben wird

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Function definition
# - Keyword `def`
# - Function name
# - Function parameters, in brackets; colon
# - Body of the function, indented one tab
# - In the body, the parameters can be used like variables
# - Keyword `return`
#     - Exits the function
#     - Determines which value is returned

# %% {"slideshow": {"slide_type": "subslide"}} tags=["code-along"]
def pythagoras(a, b):
    quadratsumme = a**2 + b**2
    # We can compute (part of) the return value here
    return quadratsumme**0.5


# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Funktionsaufruf
#
# - Name der Funktion
# - Argumente des Aufrufs, in Klammern
# - Ein Argument für jeden Parameter

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Function call
#
# - Function name
# - Arguments of the call, in brackets
# - One argument for each parameter

# %% {"tags": ["code-along"]}
pythagoras(3, 4)


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Zurück zur Zaunlänge
#
# - Wir haben bis jetzt die Länge der dritten Seite unseres Grundstücks berechnet.
# - Wir brauchen noch eine Funktion, die die Gesamtlänge ausrechnet:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Back to fences
#
# - So far we have calculated the length of the third side of our property.
# - We still need a function that calculates the total length:

# %% {"tags": ["code-along"]}
def gesamtlänge(x, y):
    z = pythagoras(x, y)
    länge = x + y + z
    return länge


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Damit können wir unser Problem vereinfachen:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# With this we can simplify our problem:

# %% {"tags": ["code-along"]}
länge_a = 10  # Beispielwert
länge_b = 40  # Beispielwert
print(gesamtlänge(länge_a, länge_b))

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Mini-Workshop
#
# - Notebook `workshop_050_introduction_part1`
# - Abschnitt "Spenden"
#

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
# - Notebook `workshop_050_introduction_part1`
# - Section "Donations"

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Import von Modulen
#
# Ein Großteil der Funktionalität von Python ist nicht direkt im Interpreter
# verfügbar sonder in Module (und Packages) ausgelagert. Mit der `import`
# Anweisung kann man dises Funktionalität verfügbar machen:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Importing modules
#
# Much of Python's functionality is not implemented in the interpreter itself
# but rather provided by external modules (and packages). With the `import`
# statement you can make this functionality available:

# %% {"tags": ["code-along"]}
import math

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Auf die Funktionen aus dem `math` Modul kann man dann mit der Syntax
# `math.floor` zugreifen:

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# The functions from the `math` module can then be accessed with the syntax `math.floor`:

# %% {"tags": ["code-along"]}
math.floor(2.5)

# %% {"tags": ["code-along"]}
math.floor(2.9)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Die Funktion `pythagoras` steht im `math`-Modul unter dem Namen `hypot`
# zur Verfügung:

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# The `pythagoras` function is available from the `math` module under the name `hypot`:

# %% {"tags": ["code-along"]}
math.hypot(3, 4)


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Damit können wir die Funktion `gesamtlänge` ohne die Hilfsfunktion
# `pythagoras` schreiben:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# This allows us to write the `total_length` function without the helper function `pythagoras`:

# %% {"tags": ["code-along"]}
def gesamtlänge(x, y):
    z = math.hypot(x, y)
    länge = x + y + z
    return länge


# %% {"tags": ["code-along"]}
gesamtlänge(3, 4)

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Andere Arten von Zahlen
#
# Python bietet noch weitere Arten von Zahlen für spezielle Anwendungen
#
# - Dezimalzahlen mit beliebiger Genauigkeit
# - Komplexe Zahlen
# - Ganze Zahlen mit fixer Größe (z.B. mit `numpy`)
# - Gleitkommazahlen mit unterschiedlicher Größe (`numpy`)

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Other types of numbers
#
# Python offers other kinds of numbers for special applications
#
# - Decimal numbers with any precision
# - Complex numbers
# - Fixed size integers (e.g. with `numpy`)
# - Floating point numbers with different sizes (`numpy`)

# %% {"slideshow": {"slide_type": "subslide"}} tags=["code-along"]
1.1 * 100

# %% {"tags": ["code-along"]}
import decimal

decimal.Decimal("1.1") * 100

# %% {"slideshow": {"slide_type": "subslide"}} tags=["code-along"]
(1 + 1j) * (1 + 1j)

# %% {"tags": ["code-along"]}
1j * 1j


# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Funktionen ohne Argumente
#
# - Eine Funktion kann auch ohne formale Parameter definiert werden.
# - Sowohl bei der Definition, als auch beim Aufruf müssen die Klammern
#   trotzdem angegeben werden.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Functions without arguments
#
# - A function can also be defined without formal parameters.
# - The parentheses must be used in the definition and in calls.

# %% {"slideshow": {"slide_type": "subslide"}} tags=["code-along"]
def null():
    return 0


# %% {"tags": ["code-along"]}
null()

# %% {"tags": ["code-along"]}
# Fehler: 'Aufruf' ohne Klammern
null

# %% {"tags": ["code-along"]}
# Fehler: 'Aufruf' ohne Klammern
# plus_eins(null)


# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# # Funktionen mit Seiteneffekten
#
# Funktionene können
#
# - Werte berechnen: `quadratsumme(3, 4)`
# - Seiteneffekte haben: `print("Hans")`

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # Functions with side effects
#
# Functions can
#
# - Calculate values: `sumofsquares(3, 4)`
# - Have side effects: `print("Hans")`

# %% {"tags": ["code-along"]}
type(print("Hans"))

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Der Wert `None`
#
# Der Rückgabewert der Funktion `print()` ist der spezielle Wert `None`.
# - Jupyter druckt `None` nicht als Wert einer Zelle aus:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ### The value `None`
#
# The return value of the `print()` function is the special value `None`.
# - Jupyter doesn't print `None` as a cell's value:

# %% {"tags": ["code-along"]}
None

# %% {"tags": ["code-along"]}
print(None)

# %% {"tags": ["code-along"]}
print(print("Hans"))


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# - Funktionen können Seiteneffekte haben
#     - Z.B. durch Aufruf von `print`
# - Diese werden ausgeführt, wenn ein Funktionsaufruf ausgewertet wird
# - Auch Funktionen mit Seiteneffekten geben einen Wert zurück
#     - Oft ist das der spezielle Wert `None`
#     - Wenn eine Funktion `None` zurückgibt brauchen wir keine explizite `return`-Anweisung

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# - Functions can have side effects
#     - E.g. by calling `print`
# - These are executed when a function call is evaluated
# - Even functions with side effects return a value
#     - Often this is the special value `None`
#     - If a function returns `None` we don't need an explicit `return` statement

# %% {"slideshow": {"slide_type": "subslide"}} tags=["code-along"]
def say_hello():
    print("Hello, world!")
    print("Today is a great day!")


# %% {"tags": ["code-along"]}
say_hello()


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Mini-Workshop
#
# - Notebook `workshop_050_introduction_part1`
# - Abschnitt "Piraten, Teil 2"
#

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
# - Notebook `workshop_050_introduction_part1`
# - Section "Pirates, Part 2"

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Default-Argumente
#
# Funktionsparameter können einen Default-Wert haben.
# - Der Default-Wert wird mit der Syntax `parameter=wert` angegeben
# - Wird das entsprechende Argument nicht übergeben so wird der Default-Wert eingesetzt
# - Hat ein Parameter einen Default-Wert, so müssen alle rechts davon stehenden Werte ebenfalls einen haben

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Default arguments
#
# Function parameters can have a default value.
# - The default value is given with the syntax `parameter=value`
# - If the corresponding argument is not passed, the default value is used
# - If a parameter has a default value, all values ​​to the right of it must also have one

# %% {"slideshow": {"slide_type": "subslide"}} tags=["code-along"]
def add_weighted(a, b=0, c=0):
    return a + 2 * b + 3 * c


# %% {"tags": ["code-along"]}
print(add_weighted(2))
print(add_weighted(2, 3))
print(add_weighted(2, 3, 4))


# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Vorsicht mit veränderlichen Default-Argumenten

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Be careful with variable default arguments

# %% {"tags": ["code-along"]}
def append_value(value, my_list=[]):
    my_list.append(value)
    return my_list


# %% {"tags": ["code-along"]}
append_value(1)

# %% {"tags": ["code-along"]}
append_value(2)


# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
#
# Lösung: verwende `Null` als Argument, erzeuge in jedem Aufruf eine neue Liste

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# Solution: use `Null` as argument, create a new list in each call

# %% {"tags": ["code-along"]}
def append_value(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list


# %% {"tags": ["code-along"]}
append_value(1)

# %% {"tags": ["code-along"]}
append_value(2)


# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Aufruf mit benannten Argumenten
#
# Beim Aufruf einer Funktion kann der Parametername in der Form `parameter=wert`
# angegeben werden.
# - Der entsprechende Wert wird dann für den benannten Parameter eingesetzt
# - Werden alle Parameter benannt, so wird der Aufruf unabhängig von der
#   Parameterreihenfolge

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Calls with named arguments
#
# When calling a function, the parameter name can be specified in the form `parameter=value`.
# - The appropriate value is then substituted for the named parameter
# - If all parameters are named, the call becomes independent of the parameter order

# %% {"slideshow": {"slide_type": "subslide"}} tags=["code-along"]
def say_hi(person, greeting="Hi"):
    print(greeting, " ", person, "!", sep="")


# %% {"tags": ["code-along"]}
say_hi("Jill")
say_hi("Jack", "Good morning")

# %% {"tags": ["code-along"]}
say_hi(greeting="Heya", person="Betty")


# %% {"slideshow": {"slide_type": "subslide"}} tags=["code-along"]
def add_weighted(a, b=0, c=0):
    return a + 2 * b + 3 * c


# %% {"slideshow": {"slide_type": "subslide"}} tags=["code-along"]
add_weighted(c=2, a=1)

# %% {"tags": ["code-along"]}
add_weighted(5, c=7)


# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Typannotationen
#
# Python erlaubt es die Typen von Funktionsargumenten und den Rückgabetyp einer
# Funktion anzugeben:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Type annotations
#
# Python allows the types of function arguments and the return type to be specified:

# %% {"tags": ["code-along"]}
def mult(a: int, b: float) -> float:
    return a * b


# %% {"tags": ["code-along"]}
mult(3, 2.0)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Typannotationen dienen lediglich zur Dokumentation und werden von Python ignoriert:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# Type annotations are for documentation only and are ignored by Python:

# %% {"tags": ["code-along"]}
mult("a", 3)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Typannotationen können parametrische Typen, optionale Typen, etc. enthalten.
# (*Hinweis:* in älteren Python Versionen kann `list` keine Typparameter
# erhalten.)

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# Type annotations can contain parametric types, optional types, etc.
# (*Note:* in older Python versions, `list` cannot take type parameters.)

# %% {"tags": ["code-along"]}
from typing import Optional


def my_append(lhs: list[int], rhs: Optional[int]):
    # What exactly does this mean?
    if rhs:
        lhs.append(rhs)


# %% {"slideshow": {"slide_type": "subslide"}} tags=["code-along"]
my_list = [1, 2, 3]
my_append(my_list, None)
my_list

# %% {"tags": ["code-along"]}
my_append(my_list, 4)
my_list


# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Docstrings
#
# Jede Funktion in Python kann dokumentiert werden, indem ein String-Literal als
# erstes Element im Rumpf angegeben wird. Meistens wird dafür ein `"""`-String
# verwendet:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Docstrings
#
# Any function in Python can be documented using a string literal as a
# first element in the body. Most often, a `"""` string is used for this:

# %% {"slideshow": {"slide_type": "subslide"}} tags=["code-along"]
def my_fun(x):
    """
    Zeigt dem Benutzer den Wert von x an

    Verwendung:
    >>> my_fun(123)
    """
    print("Das Argument x hat den Wert", x)


# %% {"tags": ["code-along"]}
my_fun(123)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Konventionen für Docstrings finden sich in
# [PEP 257](https://www.python.org/dev/peps/pep-0257/).

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# Conventions for docstrings can be found in
# [PEP 257](https://www.python.org/dev/peps/pep-0257/).

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Der Docstring einer Funktion kann mit `help()` ausgegeben werden:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# The docstring of a function can be output with `help()`:

# %% {"tags": ["code-along"]}
help(my_fun)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# In Jupyter kann man den Docstring einer Funktion durch ein vorangestelltes
# oder nachgestelltes Fragezeichen anzeigen lassen:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# In Jupyter, a function's docstring can be displayed by preceeding or following it with a question mark:

# %% {"tags": ["code-along"]}
# # ?my_fun


# %% {"tags": ["code-along"]}
# # my_fun?


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Oft verwendet man statt dessen Shift-Tab:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# Shift-Tab is often used instead:

# %% {"tags": ["code-along"]}
my_fun

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Bei Funktionen mit langen Docstrings kann man durch zweimaliges Drücken von `Shift-Tab` auf die ausführliche Anzeigeform umschalten:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# For functions with long docstrings, you can switch to the detailed display form by pressing `Shift-Tab` twice:

# %% {"tags": ["code-along"]}
my_fun

# %% {"tags": ["code-along"]}
print

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Signatur
#
# Die Anzahl, Namen, Default-Werte (und evtl. Typen) einer Funktion sowie ihren Rückgabetyp nennt man
# ihre *Signatur*.
#
# Jupyter zeigt u.a. die Signatur einer Funktion an, wenn man `Shift-Tab`
# eingibt:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Signature
#
# The number, names, default values (and possibly types) of a function's arguments and its return type are called its *signature*.
#
# Among other things, Jupyter displays the signature of a function when you type `Shift-Tab`:

# %% {"tags": ["code-along"]}
# Shift-Tab zum Anzeigen der Signatur:
say_hi


# %% {"tags": ["code-along"]}
def add_ints(m: int, n: int) -> int:
    return m + n


# %% {"tags": ["code-along"]}
add_ints
