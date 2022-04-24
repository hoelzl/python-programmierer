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
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Quickstart</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Quickstart</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# # Einführung
#
# - Ausführung von Python Code
# - Notebooks und Entwicklungsumgebungen
# - Programmierparadigmen

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Python Interpreter und Jupyter Notebooks
#
# Wir beginnen mit einer kurzen Einführung in die Arbeitsweise von Python und
# Jupyter Notebooks.

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# # Python and Jupyter notebooks
#
# We'll start with a brief introduction:
# - How does Python work?
# - What are Jupyter notebooks?

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Compiler (C++)
#
# <img src="img/compiler.svg" style="width:60%;margin:auto"/>

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# ## Compiler (C++)
#
# <img src="img/compiler.svg" style="width:60%;margin:auto"/>

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Interpreter (Python)
#
# <img src="img/interpreter.svg" style="width:60%;margin:auto"/>
#

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# ## Interpreter (Python)
#
# <img src="img/interpreter.svg" style="width:60%;margin:auto"/>

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Jupyter Notebooks
#
# <img src="img/jupyter-notebook.svg" style="width:60%;margin:auto"/>

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# ## Jupyter Notebooks
#
# <img src="img/jupyter-notebook.svg" style="width:60%;margin:auto"/>

# %% {"slideshow": {"slide_type": "subslide"}}
import numpy as np
import matplotlib.pyplot as plt

page_load_time = np.random.normal(3.0, 1.0, 1000)
purchase_amount = np.random.normal(50.0, 1.5, 1000) - page_load_time

plt.figure(figsize=(12, 8))
plt.scatter(page_load_time, purchase_amount)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# ## Entwicklungsumgebungen
#
# - Visual Studio Code
# - PyCharm
# - Vim/Emacs/... + interaktive Shell


# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Variablen und Datentypen
#
# Zahlen und Arithmetik:

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# ## Variables and data types
#
# Numbers and arithmetic:

# %% {"tags": ["code-along"]}
17 + 4 + 1

# %% {"tags": ["code-along"]}
1.5 + 7.4

# %% {"tags": ["code-along"]}
1 + 2 * 3

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Zeichenketten

# %% [markdown] {"lang": "en"}
# ## Strings

# %% {"tags": ["code-along"]}
"This is a string"

# %% {"tags": ["code-along"]}
# fmt: off
'This is also a string'
# fmt: on

# %% {"tags": ["code-along"]}
str(1 + 2)

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
"3" + "abc"

# %% {"tags": ["code-along"]}
"literal strings " "can be concatenated " "by juxtaposition"

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Variablen

# %% [markdown] {"lang": "en"}
# ### Variables

# %% {"tags": ["code-along"]}
answer = 42

# %% {"tags": ["code-along"]}
my_value = answer + 2


# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Jupyter Notebooks: Anzeige von Werten
#
# - Jupyter Notebooks geben den letzten Wert jeder Zelle auf dem Bildschirm aus
# - Das passiert in "normalen" Python-Programmen nicht!
#   - Wenn sie als Programme ausgeführt werden
#   - Der interaktive Interpreter verhält sich ähnlich wie Notebooks

# %% [markdown] {"lang": "en"}
# ## Jupyter notebooks: displaying values
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
# Jupyter zeigt auch den Wert von Variablen an:

# %% [markdown] {"lang": "en"}
# Jupyter also displays the value of variables:

# %% {"tags": ["code-along"]}
answer

# %% {"tags": ["code-along"]}
my_value

# %% {"tags": ["code-along"]}
answer
my_value

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Um mehrere Werte anzuzeigen kann man die `print()`-Funktion verwenden:
#
# `print(...)` gibt den in Klammern eingeschlossenen Text auf dem Bildschirm
# aus.

# %% [markdown] {"lang": "en"}
# To display multiple values ​​you can use the `print()` function:
#
# `print(...)` prints the values between the trailing parens on the screen.

# %% {"tags": ["code-along"]}
print(123)

# %% {"tags": ["code-along"]}
print(answer)

# %% {"tags": ["code-along"]}
print(my_value)

# %% {"tags": ["code-along"]}
print(answer)
print(my_value)


# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
print("Hello, world!")


# %% [markdown] {"lang": "de"}
# Vergleichen Sie die Ausgabe mit der folgenden Zelle:

# %% [markdown] {"lang": "en"}
# Compare the output to the following cell:

# %% {"tags": ["code-along"]}
"Hello, world!"

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
print("answer =", answer, "my_value =", my_value)

# %% {"tags": ["code-along"]}
print("a", "b", "c", sep="-", end="+++")
print("d", "e")

# %% {"tags": ["code-along"]}
print("a", end=", ")
print("b", end=", ")
print("c")

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
# ## Typen

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# ## Types

# %% {"tags": ["code-along"]}
type(123)

# %% {"tags": ["code-along"]}
type("Foo")

# %% {"tags": ["code-along"]}
answer = 42
print(type(answer))
answer = "Hallo!"
print(type(answer))


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Vordefinierte Funktionen

# %% [markdown] {"lang": "en"}
# ### Predefined functions

# %% {"tags": ["code-along"]}
print("Hello, world!")

# %% {"tags": ["code-along"]}
int("123")

# %% {"tags": ["code-along"]}
int(3.8)

# %% {"tags": ["code-along"]}
round(4.4)

# %% {"tags": ["code-along"]}
round(4.6)

# %%
print(round(0.5), round(1.5), round(2.5), round(3.5))

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Funktionen


# %% [markdown] {"lang": "en"}
# ## Functions

# %% {"tags": ["code-along"]}
def add_1(n):
    return n + 1


# %% {"tags": ["code-along"]}
x = add_1(10)
add_1(20) + x + x

# %% {"tags": ["code-along"]}
add_1(5) + add_1(7)


# %% {"tags": ["code-along"]}
def my_round(n):
    return int(n + 0.5)


# %%
print(my_round(0.5), my_round(1.5), my_round(2.5), my_round(3.5))

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Micro-Workshop
#
# Schreiben Sie eine Funktion `greeting(name)`, die eine Begrüßung in der Form
# "Hallo *name*!" auf dem Bildschirm ausgibt, z.B.
# ```python
# >>> greeting("Max")
# Hallo Max!
# >>>
# ```


# %% [markdown] {"lang": "en"}
# ### Micro workshop
#
# Write a function `greeting(name)` that prints a greeting in the form
# "Hello *name*!" to the screen, e.g.
# ```python
# >>> greeting("Max")
# Hi Max!
# >>>
# ```

# %% {"tags": ["code-along"]}
def greeting(name):
    print("Hallo ", name, "!", sep="")


# %% {"tags": ["code-along"]}
greeting("Max")

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Methoden

# %% [markdown] {"lang": "en"}
# ### Methods

# %% {"tags": ["code-along"]}
"Foo".lower()

# %% {"tags": ["code-along"]}
# 5.bit_length()

# %% {"tags": ["code-along"]}
number = 5
number.bit_length()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Mehrere Parameter, Default Argumente


# %% [markdown] {"lang": "en"}
# ### Multiple parameters, default arguments

# %% {"tags": ["code-along"]}
def add2(a, b):
    return a + b


# %% {"tags": ["code-along"]}
def add3(a, b=0, c=0):
    return a + b + c


# %% {"tags": ["code-along"]}
print(add3(2))
print(add3(2, 3))
print(add3(2, 3, 4))
print(add3(1, c=3))

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Verschachtelte Funktionsaufrufe

# %% [markdown] {"lang": "en"}
# ### Nested function calls

# %% {"tags": ["code-along"]}
add3(add_1(2), add3(1, 2, add3(1, 2)))


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Typannotationen

# %% [markdown] {"lang": "en"}
# ### Type annotations

# %% {"tags": ["code-along"]}
def mult(a: int, b: float):
    return a * b


# %% {"tags": ["code-along"]}
mult(3, 2.0)

# %% {"tags": ["code-along"]}
# Typannotationen are only for documentation purposes:
mult("a", 3)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Listen und Tupel

# %% [markdown] {"lang": "en"}
# ## Lists and tuples

# %% {"tags": ["code-along"]}
numbers = [1, 2, 3, 4]

# %% {"tags": ["code-along"]}
print(numbers)
print(numbers[0], numbers[3])
print("Länge:", len(numbers))

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
numbers + numbers

# %% {"tags": ["code-along"]}
[1] * 3

# %% {"tags": ["code-along"]}
5 in [5, 6, 7]

# %% {"tags": ["code-along"]}
3 in [5, 6, 7]

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
my_list = [1, 2, 3]
my_list[1] = 5
my_list

# %% {"tags": ["code-along"]}
my_list.append(7)
my_list

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Mini-Workshop
#
# - Notebook `workshop_100_lists_part2`
# - Abschnitt "Farben"
#

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
# - Notebook `workshop_100_lists_part2`
# - Section Colors

# %% {"tags": ["code-along"]}
my_tuple = 1, 2, 3

# %% {"tags": ["code-along"]}
my_tuple[0]

# %% {"tags": ["code-along"]}
# my_tuple[0] = 1


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Boole'sche Werte und `if`-Anweisungen

# %% [markdown] {"lang": "en"}
# ## Boolean values ​​and `if` statements

# %% {"tags": ["code-along"]}
True

# %% {"tags": ["code-along"]}
False

# %% {"tags": ["code-along"]}
value = False

# %% {"tags": ["code-along"]}
if value:
    print("Wahr")
else:
    print("Falsch")


# %% {"slideshow": {"slide_type": "subslide"}}
def print_size(n):
    if n < 10:
        print("Very small")
    elif n < 15:
        print("Pretty small")
    elif n < 30:
        print("Average")
    else:
        print("Large")


# %% {"slideshow": {"slide_type": "subslide"}}
print_size(1)
print_size(10)
print_size(20)
print_size(100)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Micro-Workshop
#
# Schreiben Sie eine Funktion `fits_in_line(text: str, line_length: int = 72)`,
# die `True` oder `False` zurückgibt, je nachdem ob `text` in einer Zeile der
# Länge `line_length` ausgegeben werden kann oder nicht:
# ```python
# >>> fits_in_line("Hallo")
# True
# >>> fits_in_line("Hallo", 3)
# False
# >>>
# ```
#
# Schreiben Sie eine Funktion `print_line(text: str, line_length:int = 72)`,
# die
# * `text` auf dem Bildschirm ausgibt, falls das in einer Zeile der Länge
#   `line_length` möglich ist
# * `...` ausgibt, falls das nicht möglich ist.
#
# ```python
# >>> print_line("Hallo")
# Hallo
# >>> print_line("Hallo", 3)
# ...
# >>>
# ```


# %% [markdown] {"lang": "en"}
# ### Micro workshop
#
# Write a function `fits_in_line(text: str, line_length: int = 72)`,
# which returns `True` or `False` depending on whether `text` fits into a line of
# length `line_length`:
# ```python
# >>> fits_in_line("Hello")
# True
# >>> fits_in_line("Hello", 3)
# False
# >>>
# ```
#
# Write a function `print_line(text: str, line_length:int = 72)`,
# that
# * prints `text` to the screen if that is possible in a line of length
#   `line_length`
# * prints `...` if that is not possible.
#
# ```python
# >>> print_line("Hello")
# Hello
# >>> print_line("Hello", 3)
# ...
# >>>
# ```

# %% {"tags": ["code-along"]}
def fits_in_line(text: str, line_length: int = 72):
    return len(text) <= line_length


# %% {"tags": ["code-along"]}
fits_in_line("Hallo")

# %% {"tags": ["code-along"]}
fits_in_line("Hallo", 3)


# %% {"tags": ["code-along"]}
def print_line(text: str, line_length: int = 72):
    if fits_in_line(text, line_length=line_length):
        print(text)
    else:
        print("...")


# %% {"tags": ["code-along"]}
print_line("Hallo")

# %% {"tags": ["code-along"]}
print_line("Hallo", 3)


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## `for`-Schleifen

# %% [markdown] {"lang": "en"}
# ## `for` loops

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
for char in "abc":
    print(char, end="|")

# %% {"tags": ["code-along"]}
result = 0
for n in [1, 2, 3, 4]:
    result += n
result

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Micro-Workshop
#
# Schreiben Sie eine Funktion `print_all(items: list)`, die die Elemente der
# Liste `items` auf dem Bildschirm ausgibt, jeweils ein Element pro Zeile:
#
# ```python
# >>> print_all([1, 2, 3])
# 1
# 2
# 3
# >>>
# ```
# Was passiert, wenn Sie die Funktion mit einem String als Argument aufrufen,
# z.B. `print_all("abc")`


# %% [markdown] {"lang": "en"}
# ### Micro workshop
#
# Write a function `print_all(items: list)` that prints the elements of a
# list `items` to the screen, one item per line:
#
# ```python
# >>> print_all([1, 2, 3])
# 1
# 2
# 3
# >>>
# ```
# What happens if you call the function with a string as an argument,
# e.g. `print_all("abc")`

# %% {"tags": ["code-along"]}
def print_all(items: list):
    for item in items:
        print(item)


# %% {"tags": ["code-along"]}
print_all([1, 2, 3])

# %% {"tags": ["code-along"]}
print_all("abc")

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Ranges

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ### Ranges

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
for i in range(3):
    print(i, end=", ")

# %% {"tags": ["code-along"]}
for i in range(1, 6, 2):
    print(i, end=", ")

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Micro-Workshop
#
# Schreiben Sie eine Funktion `print_squares(n: int)`, die die Quadrate der
# Zahlen von 1 bis n ausgibt, jeweils ein Element pro Zeile:
#
# ```python
# >>> print_square(3)
# 1**2 = 1
# 2**2 = 4
# 3**2 = 9
# >>>
# ```


# %% [markdown] {"lang": "en"}
# ### Micro workshop
#
# Write a function `print_squares(n: int)` that prints the squares of the
# numbers from 1 to n, one element per line:
#
# ```python
# >>>print_square(3)
# 1**2 = 1
# 2**2 = 4
# 3**2 = 9
# >>>
# ```

# %% {"tags": ["code-along"]}
def print_squares(n: int):
    for i in range(1, n + 1):
        print(i, "**2 = ", i * i, sep="")


# %% {"tags": ["code-along"]}
print_squares(3)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Dictionaries

# %% [markdown] {"lang": "en"}
# ## Dictionaries

# %%
translations = {"snake": "Schlange", "bat": "Fledermaus", "horse": "Hose"}

# %% {"tags": ["code-along"]}
print(translations["snake"])
print(translations.get("bat", "<unbekannt>"))
print(translations.get("monkey", "<unbekannt>"))

# %% {"tags": ["code-along"]}
# Error:
# translations['monkey']

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
translations["horse"] = "Pferd"
translations["horse"]

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
for key in translations.keys():
    print(key, end=" ")

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
for key in translations:
    print(key, end=" ")

# %% {"tags": ["code-along"]}
for val in translations.values():
    print(val, end=" ")

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
for item in translations.items():
    print(item, end=" ")

# %% {"tags": ["code-along"]}
for key, val in translations.items():
    print("Key:", key, "\tValue:", val)

# %%
