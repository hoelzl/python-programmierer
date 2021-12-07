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
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <h1 style="text-align:center;">Python Quickstart</h1>
# <h2 style="text-align:center;">Coding Akademie München GmbH</h2>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] slideshow={"slide_type": "slide"}
# # Python und Jupyter Notebooks
#
# Wir beginnen mit einer kurzen Einführung in die Arbeitsweise von Python und
# Jypyter Notebooks.

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Compiler (C++)
#
# <img src="img/compiler.svg" style="width:60%;margin:auto"/>

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Interpreter (Python)
#
# <img src="img/interpreter.svg" style="width:60%;margin:auto"/>
#

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Jupyter Notebooks
#
# <img src="img/jupyter-notebook.svg" style="width:60%;margin:auto"/>

# %% slideshow={"slide_type": "subslide"}
import numpy as np
import matplotlib.pyplot as plt

page_load_time = np.random.normal(3.0, 1.0, 1000)
purchase_amount = np.random.normal(50.0, 1.5, 1000) - page_load_time

plt.figure(figsize=(12, 8))
plt.scatter(page_load_time, purchase_amount)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## Variablen und Datentypen
#
# Zahlen und Arithmetik:

# %%
17 + 4 + 1

# %%
1.5 + 7.4

# %%
1 + 2 * 3

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Zeichenketten

# %%
"This is a string"

# %%
"This is also a string"

# %%
str(1 + 2)

# %% slideshow={"slide_type": "subslide"}
"3" + "abc"

# %%
"literal strings " "can be concatenated " "by justaposition"

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Variablen

# %%
answer = 42

# %%
my_value = answer + 2


# %% [markdown] slideshow={"slide_type": "slide"}
# ## Jupyter Notebooks: Anzeige von Werten
#
# - Jupyter Notebooks geben den letzten Wert jeder Zelle auf dem Bildschirm aus
# - Das passiert in "normalen" Python-Programmen nicht!
#   - Wenn sie als Programme ausgeführt werden
#   - Der interaktive Interpreter verhält sich ähnlich wie Notebooks

# %% slideshow={"slide_type": "subslide"}
123

# %% [markdown]
# Um die Ausgabe des letzten Wertes einer Zeile in Jupyter zu unterbinden kann man
# die Zeile mit einem Strichpunkt beenden:

# %%
123;

# %% [markdown] slideshow={"slide_type": "subslide"}
# Jupyter zeigt auch den Wert von Variablen an:

# %%
answer

# %%
my_value

# %%
answer
my_value

# %% [markdown] slideshow={"slide_type": "subslide"}
# Um mehrere Werte anzuzeigen kann man die `print()`-Funktion verwenden:
#
# `print(...)` gibt den in Klammern eingeschlossenen Text auf dem Bildschirm aus.

# %%
print(123)

# %%
print(answer)

# %%
print(my_value)

# %%
print(answer)
print(my_value)


# %% slideshow={"slide_type": "subslide"}
print("Hello, world!")


# %% [markdown]
# Vergleichen Sie die Ausgabe mit der folgenden Zelle:

# %%
"Hello, world!"

# %% slideshow={"slide_type": "subslide"}
print("answer =", answer, "my_value =", my_value)

# %%
print("a", "b", "c", sep="-", end="+++")
print("d", "e")

# %%
print("a", end=", ")
print("b", end=", ")
print("c")

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Typen

# %%
type(123)

# %%
type("Foo")

# %%
answer = 42
print(type(answer))
answer = "Hallo!"
print(type(answer))


# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Vordefinierte Funktionen

# %%
print("Hello, world!")

# %%
int("123")

# %%
int(3.8)

# %%
round(4.4)

# %%
round(4.6)

# %%
print(round(0.5), round(1.5), round(2.5), round(3.5))

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Funktionen

# %%
def add_1(n):
    return n + 1


# %%
x = add_1(10)
add_1(20) + x + x

# %%
add_1(5) + add_1(7)

# %%
def my_round(n):
    return int(n + 0.5)


# %%
print(my_round(0.5), my_round(1.5), my_round(2.5), my_round(3.5))

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Micro-Workshop
#
# Schreiben Sie eine Funktion `greeting(name)`, die eine Begrüßung in der Form
# "Hallo *name*!" auf dem Bildschirm ausgibt, z.B.
# ```python
# >>> greeting("Max")
# Hallo Max!
# >>>
# ```

# %%
def greeting(name):
    print("Hallo ", name, "!", sep="")


# %%
greeting("Max")

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Methoden

# %%
"Foo".lower()

# %%
# 5.bit_length()

# %%
number = 5
number.bit_length()

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Mehrere Parameter, Default Argumente

# %%
def add2(a, b):
    return a + b


# %%
def add3(a, b=0, c=0):
    return a + b + c


# %%
print(add3(2))
print(add3(2, 3))
print(add3(2, 3, 4))
print(add3(1, c=3))

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Verschachtelte Funktionsaufrufe

# %%
add3(add_1(2), add3(1, 2, add3(1, 2)))


# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Typannotationen

# %%
def mult(a: int, b: float):
    return a * b


# %%
mult(3, 2.0)

# %%
# Typannotationen dienen lediglich zur Dokumentation und werden von Python
# ignoriert:
mult("a", 3)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Listen und Tupel

# %%
numbers = [1, 2, 3, 4]

# %%
print(numbers)
print(numbers[0], numbers[3])
print("Länge:", len(numbers))

# %% slideshow={"slide_type": "subslide"}
numbers + numbers

# %%
[1] * 3

# %%
5 in [5, 6, 7]

# %%
3 in [5, 6, 7]

# %% slideshow={"slide_type": "subslide"}
my_list = [1, 2, 3]
my_list[1] = 5
my_list

# %%
my_list.append(7)
my_list


# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Boole'sche Werte und `if`-Anweisungen

# %%
True

# %%
False

# %%
value = False

# %%
if value:
    print("Wahr")
else:
    print("Falsch")

# %% slideshow={"slide_type": "subslide"}
def print_size(n):
    if n < 10:
        print("Very small")
    elif n < 15:
        print("Pretty small")
    elif n < 30:
        print("Average")
    else:
        print("Large")


# %% slideshow={"slide_type": "subslide"}
print_size(1)
print_size(10)
print_size(20)
print_size(100)

# %% [markdown] slideshow={"slide_type": "subslide"}
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
# * `text` auf dem Bildschirm ausgibt, falls das in einer Zeile der Länge `line_length` möglich ist
# * `...` ausgibt, falls das nicht möglich ist.
# ```python
# >>> print_line("Hallo")
# Hallo
# >>> print_line("Hallo", 3)
# ...
# >>>
# ```

# %%
def fits_in_line(text: str, line_length: int = 72):
    return len(text) <= line_length


# %%
fits_in_line("Hallo")

# %%
fits_in_line("Hallo", 3)

# %%
def print_line(text: str, line_length: int = 72):
    if fits_in_line(text, line_length=line_length):
        print(text)
    else:
        print("...")


# %%
print_line("Hallo")

# %%
print_line("Hallo", 3)


# %% [markdown] slideshow={"slide_type": "subslide"}
# ## `for`-Schleifen

# %% slideshow={"slide_type": "subslide"}
for char in "abc":
    print(char, end="|")

# %%
result = 0
for n in [1, 2, 3, 4]:
    result += n
result

# %% [markdown] slideshow={"slide_type": "subslide"}
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

# %%
def print_all(items: list):
    for item in items:
        print(item)

# %%
print_all([1, 2, 3])

# %%
print_all("abc")

# %% slideshow={"slide_type": "subslide"}
for i in range(3):
    print(i, end=", ")

# %%
for i in range(1, 6, 2):
    print(i, end=", ")

# %% [markdown] slideshow={"slide_type": "subslide"}
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

# %%
def print_squares(n: int):
    for i in range(1, n+1):
        print(i, "**2 = ", i*i, sep="")

# %%
print_squares(3)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Dictionaries

# %%
translations = {"snake": "Schlange", "bat": "Fledermaus", "horse": "Hose"}

# %%
print(translations["snake"])
print(translations.get("bat", "<unbekannt>"))
print(translations.get("monkey", "<unbekannt>"))

# %%
# Fehler:
# translations['monkey']

# %% slideshow={"slide_type": "subslide"}
translations["horse"] = "Pferd"
translations["horse"]

# %% slideshow={"slide_type": "subslide"}
for key in translations.keys():
    print(key, end=" ")

# %% slideshow={"slide_type": "subslide"}
for key in translations:
    print(key, end=" ")

# %%
for val in translations.values():
    print(val, end=" ")

# %% slideshow={"slide_type": "subslide"}
for item in translations.items():
    print(item, end=" ")

# %%
for key, val in translations.items():
    print("Key:", key, "\tValue:", val)

# %%
