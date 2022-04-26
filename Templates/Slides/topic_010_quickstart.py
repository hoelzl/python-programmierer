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

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# # Introduction
#
# - Executing Python Code
# - Notebooks and development environments (IDEs)
# - Programming paradigms

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


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Entwicklungsumgebungen
#
# - Visual Studio Code
# - PyCharm
# - Vim/Emacs/... + interaktive Shell

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# ## Development Environments
#
# - Visual Studio Code
# - PyCharm
# - Vim/Emacs/... + interactive shell

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# # Programmierparadigmen
# - Prozedural
# - Funktional (?)
# - Objektorientiert

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# # Programming paradigms
# - Procedural
# - Functional (?)
# - Object oriented

# %% {"slideshow": {"slide_type": "slide"}, "tags": ["code-along"]}
def add(x, y):
    return x + y


# %% {"tags": ["code-along"]}
add(2, 3)

# %% {"tags": ["code-along"]}
accu = 0


# %% {"slideshow": {"slide_type": "slide"}, "tags": ["code-along"]}
def inc(x):
    global accu
    accu += x


# %% {"tags": ["code-along"]}
def disp():
    print(f"Accumulator is {accu}.")


# %% {"tags": ["code-along"]}
disp()
inc(2)
inc(3)
disp()


# %% {"slideshow": {"slide_type": "slide"}, "tags": ["code-along"]}
def ntimes(n, f, x):
    if n <= 0:
        return x
    else:
        return ntimes(n - 1, f, f(x))


# %% {"tags": ["code-along"]}
ntimes(10, lambda x: x * 2, 1)

# %% {"slideshow": {"slide_type": "slide"}, "tags": ["code-along"]}
from pathlib import Path

path = Path("./some_file.txt")

# %% {"tags": ["code-along"]}
path.with_suffix(".md").absolute()

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Variablen und Datentypen
#
# Zahlen und Arithmetik:

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
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

# %% [markdown]  {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
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

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
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

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
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

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
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

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
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

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
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


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
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


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
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

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
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


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
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

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# ### Nested function calls

# %% {"tags": ["code-along"]}
add3(add_1(2), add3(1, 2, add3(1, 2)))


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Typannotationen

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# ### Type annotations

# %% {"tags": ["code-along"]}
def mult(a: int, b: float):
    return a * b


# %% {"tags": ["code-along"]}
mult(3, 2.0)

# %% {"tags": ["code-along"]}
# Type annotations are only for documentation purposes:
mult("a", 3)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Listen und Tupel

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
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

# %% {"tags": ["code-along"]}
my_list.insert(1, 9)
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

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Tupel
#
# Tupel sind ähnlich zu Listen, allerdings sind Tupel nach ihrer Konstruktion
# unveränderlich. Funktionen und Methoden für Listen, die die Liste nicht destruktiv
# modifizieren sind in der Regel auch auf Tupel anwendbar.

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# ## Tuples
#
# Tuples are similar to lists but cannot be destructively modified. Functions and
# methods on lists that don't modify the list destructively are generally also available
# for tuples.

# %% {"tags": ["code-along"]}
my_tuple = 1, 2, 3

# %% {"tags": ["code-along"]}
my_tuple[0]

# %% {"tags": ["code-along"]}
# my_tuple[0] = 1


# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Boole'sche Werte und `if`-Anweisungen

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# ## Boolean values and `if` statements

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


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
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


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# ### Micro workshop
#
# Write a function `print_squares(n: int)` that prints the squares of the
# numbers from 1 to n, one element per line:
#
# ```python
# >>>print_squares(3)
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

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
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

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Hinweise für den nächsten Workshop

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# ### Hints for the upcoming workshop

# %%
advice = "Don't worry be happy"

# %%
words = advice.split()

# %%
" ".join(words)

# %%
smilies = {"worry": "\U0001f61f", "happy": "\U0001f600"}


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Micro-Workshop
#
# Schreiben Sie eine Funktion `replace_words(text: str, replacements: dict)`, die alle
# Wörter, die in `dict` als Key vorkommen durch ihren Wert in `dict` ersetzen.
#
# ```python
# >>> replace_words(advice, smilies)
# "Don't 😟 be 😀"
# ```
# #### Hinweise
#
# - Splitten Sie `text` in eine Liste `words` aus einzelnen Wörtern
#
# - Erzeugen Sie eine neue leere Liste `new_words`
#
# - Iterieren Sie über `words` und fügen Sie jedes Wort, das nicht im Wörterbuch
#   vorkommt unverändert an `new_words` an; fügen Sie für jedes Wort, das im Wörterbuch
#   vorkommt seine Übersetzung an
#
# - Fügen Sie `new_words` mit der `join()`-Methode zu einem String zusammen

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# ### Micro workshop
#
# Write a function `replace_words(text: str, replacements: dict)` that replaces all
# words occurring as key in `dict` with their values in `dict`.
#
# ```python
# >>> replace_words(advice, smilies)
# "Don't 😟 be 😀"
# ```
# #### Hints
#
# - Split `text` into a list of individual words
#
# - Create an empty list called `new_words`
#
# - Iterate over `words`; add each word that does not appear in `replacements` to
# `new_words`; for every word that appears in `replacements`, add its value
#
# - Use the `join()` method to turn `new_words` into a single string

# %% {"tags": ["code-along"]}
def replace_words(text: str, replacements: dict):
    new_words = []
    for word in text.lower().split():
        replacement = replacements.get(word)
        if replacement is not None:
            new_words.append(replacement)
        else:
            new_words.append(word)
    return " ".join(new_words)


# %% {"tags": ["code-along"]}
replace_words(advice, smilies)

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Mengen

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# ## Sets

# %% {"tags": ["code-along"]}
numbers = {3, 5, 4, 9, 4, 1, 5, 4, 3}
numbers

# %% {"tags": ["code-along"]}
type(numbers)

# %% {"tags": ["code-along"]}
numbers.add(3)

# %% {"tags": ["code-along"]}
numbers

# %% {"tags": ["code-along"]}
numbers.union({42})

# %% {"tags": ["code-along"]}
numbers

# %% {"tags": ["code-along"]}
numbers | {42}

# %% {"tags": ["code-along"]}
numbers

# %% {"tags": ["code-along"]}
numbers & {2, 3, 4}

# %% {"tags": ["code-along"]}
numbers - {2, 3, 4}

# %% {"tags": ["code-along"]}
numbers.add(5)

# %% {"tags": ["code-along"]}
numbers

# %% {"tags": ["code-along"]}
numbers.remove(5)

# %% {"tags": ["code-along"]}
numbers

# %% {"tags": ["code-along"]}
numbers.discard(5)

# %% {"tags": ["code-along"]}
numbers

# %% {"tags": ["code-along"]}
3 in numbers

# %% {"tags": ["code-along"]}
2 not in numbers

# %% {"tags": ["code-along"]}
{2, 3} <= {1, 2, 3, 4}

# %% {"tags": ["code-along"]}
{2, 5} <= {1, 2}

# %% {"tags": ["code-along"]}
type({})  # Empty dictionary!

# %% {"tags": ["code-along"]}
set()

# %% {"tags": ["code-along"]}
type(set())

# %%
philosophy = ("Half a bee , philosophically , must ipso facto half not be . "
              "But can it be an entire bee , if half of it is not a bee , "
              "due to some ancient injury .")
philosophy

# %% {"tags": ["code-along"]}
words = philosophy.lower().split()
words

# %% {"tags": ["code-along"]}
len(words)

# %% {"tags": ["code-along"]}
word_set = set(words)

# %% {"tags": ["code-along"]}
len(word_set)

# %% {"tags": ["code-along"]}
word_set - {".", ","}

# %%
dickens = "It was the best of times , it was the worst of times"


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Micro-Workshop
#
# Schreiben Sie eine Funktion `count_unique_words(text: str)`, die die Anzahle der in
# einem Text vorkommenden Wörter (ohne Wiederholungen und Satzzeichen) zählt. Testen Sie
# die Funktion mit dem in `dickens` gespeicherten String.
#
# ```python
# >>> count_unique_words(dickens)
# 8
# >>>
# ```


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# ### Micro workshop
#
# Write a function `count_unique_words(text: str)` that prints the number of unique
# words in `text` (i.e., without repetitions, without punctuation).
#
# ```python
# >>> count_unique_words(dickens)
# 7
# >>>
# ```

# %% {"tags": ["code-along"]}
def count_unique_words(text: str):
    word_set = set(text.lower().split()) - {",", "."}
    return len(word_set)


# %% {"tags": ["code-along"]}
count_unique_words(dickens)
