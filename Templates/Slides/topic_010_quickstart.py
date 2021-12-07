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
#       jupytext_version: 1.13.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# j2 import 'macros.j2' as doc
# %% [markdown] {{ doc.slide() }}
# {{ doc.header("Quickstart") }}

# %% [markdown] {{ doc.slide() }}
# # Python und Jupyter Notebooks
#
# Wir beginnen mit einer kurzen Einführung in die Arbeitsweise von Python und
# Jupyter Notebooks.

# %% [markdown] {{ doc.subslide() }}
# ## Compiler (C++)
#
# <img src="img/compiler.svg" style="width:60%;margin:auto"/>

# %% [markdown] {{ doc.subslide() }}
# ## Interpreter (Python)
#
# <img src="img/interpreter.svg" style="width:60%;margin:auto"/>
#

# %% [markdown] {{ doc.subslide() }}
# ## Jupyter Notebooks
#
# <img src="img/jupyter-notebook.svg" style="width:60%;margin:auto"/>

# %% {{ doc.subslide() }}
import numpy as np
import matplotlib.pyplot as plt

page_load_time = np.random.normal(3.0, 1.0, 1000)
purchase_amount = np.random.normal(50.0, 1.5, 1000) - page_load_time

plt.figure(figsize=(12, 8))
plt.scatter(page_load_time, purchase_amount)


# %% [markdown] {{ doc.slide() }}
# ## Variablen und Datentypen
#
# Zahlen und Arithmetik:

# %% {{ doc.codealong() }}
17 + 4 + 1

# %% {{ doc.codealong() }}
1.5 + 7.4

# %% {{ doc.codealong() }}
1 + 2 * 3

# %% [markdown] {{ doc.subslide() }}
# ## Zeichenketten

# %% {{ doc.codealong() }}
'This is a string'

# %% {{ doc.codealong() }}
"This is also a string"

# %% {{ doc.codealong() }}
str(1 + 2)

# %% [markdown] {{ doc.subslide() }} {{ doc.codealong() }}
"3" + "abc"

# %% {{ doc.codealong() }}
"literal strings " "can be concatenated " "by juxtaposition"

# %% [markdown] {{ doc.subslide() }}
# ### Variablen

# %% {{ doc.codealong() }}
answer = 42

# %% {{ doc.codealong() }}
my_value = answer + 2


# %% [markdown] {{ doc.slide() }}
# ## Jupyter Notebooks: Anzeige von Werten
#
# - Jupyter Notebooks geben den letzten Wert jeder Zelle auf dem Bildschirm aus
# - Das passiert in "normalen" Python-Programmen nicht!
#   - Wenn sie als Programme ausgeführt werden
#   - Der interaktive Interpreter verhält sich ähnlich wie Notebooks

# %% [markdown] {{ doc.subslide() }} {{ doc.codealong() }}
123

# %% [markdown]
# Um die Ausgabe des letzten Wertes einer Zeile in Jupyter zu unterbinden
# kann man die Zeile mit einem Strichpunkt beenden:

# %% {{ doc.codealong() }}
123;

# %% [markdown] {{ doc.subslide() }}
# Jupyter zeigt auch den Wert von Variablen an:

# %% {{ doc.codealong() }}
answer

# %% {{ doc.codealong() }}
my_value

# %% {{ doc.codealong() }}
answer
my_value

# %% [markdown] {{ doc.subslide() }}
# Um mehrere Werte anzuzeigen kann man die `print()`-Funktion verwenden:
#
# `print(...)` gibt den in Klammern eingeschlossenen Text auf dem Bildschirm
# aus.

# %% {{ doc.codealong() }}
print(123)

# %% {{ doc.codealong() }}
print(answer)

# %% {{ doc.codealong() }}
print(my_value)

# %% {{ doc.codealong() }}
print(answer)
print(my_value)


# %% {{ doc.subslide() }} {{ doc.codealong() }}
print("Hello, world!")


# %% [markdown]
# Vergleichen Sie die Ausgabe mit der folgenden Zelle:

# %% {{ doc.codealong() }}
"Hello, world!"

# %% {{ doc.subslide() }} {{ doc.codealong() }}
print("answer =", answer, "my_value =", my_value)

# %% {{ doc.codealong() }}
print("a", "b", "c", sep="-", end="+++")
print("d", "e")

# %% {{ doc.codealong() }}
print("a", end=", ")
print("b", end=", ")
print("c")

# %% [markdown] {{ doc.subslide() }} {{ doc.codealong() }}
# ## Typen

# %% {{ doc.codealong() }}
type(123)

# %% {{ doc.codealong() }}
type("Foo")

# %% {{ doc.codealong() }}
answer = 42
print(type(answer))
answer = "Hallo!"
print(type(answer))


# %% [markdown] {{ doc.subslide() }}
# ### Vordefinierte Funktionen

# %% {{ doc.codealong() }}
print("Hello, world!")

# %% {{ doc.codealong() }}
int("123")

# %% {{ doc.codealong() }}
int(3.8)

# %% {{ doc.codealong() }}
round(4.4)

# %% {{ doc.codealong() }}
round(4.6)

# %%
print(round(0.5), round(1.5), round(2.5), round(3.5))

# %% [markdown] {{ doc.subslide() }}
# ## Funktionen


# %% {{ doc.codealong() }}
def add_1(n):
    return n + 1


# %% {{ doc.codealong() }}
x = add_1(10)
add_1(20) + x + x

# %% {{ doc.codealong() }}
add_1(5) + add_1(7)


# %% {{ doc.codealong() }}
def my_round(n):
    return int(n + 0.5)


# %%
print(my_round(0.5), my_round(1.5), my_round(2.5), my_round(3.5))

# %% [markdown] {{ doc.subslide() }}
# ### Micro-Workshop
#
# Schreiben Sie eine Funktion `greeting(name)`, die eine Begrüßung in der Form
# "Hallo *name*!" auf dem Bildschirm ausgibt, z.B.
# ```python
# >>> greeting("Max")
# Hallo Max!
# >>>
# ```


# %% {{ doc.codealong() }}
def greeting(name):
    print("Hallo ", name, "!", sep="")


# %% {{ doc.codealong() }}
greeting("Max")

# %% [markdown] {{ doc.subslide() }}
# ### Methoden

# %% {{ doc.codealong() }}
"Foo".lower()

# %% {{ doc.codealong() }}
# 5.bit_length()

# %% {{ doc.codealong() }}
number = 5
number.bit_length()

# %% [markdown] {{ doc.subslide() }}
# ### Mehrere Parameter, Default Argumente


# %% {{ doc.codealong() }}
def add2(a, b):
    return a + b


# %% {{ doc.codealong() }}
def add3(a, b=0, c=0):
    return a + b + c


# %% {{ doc.codealong() }}
print(add3(2))
print(add3(2, 3))
print(add3(2, 3, 4))
print(add3(1, c=3))

# %% [markdown] {{ doc.subslide() }}
# ### Verschachtelte Funktionsaufrufe

# %% {{ doc.codealong() }}
add3(add_1(2), add3(1, 2, add3(1, 2)))


# %% [markdown] {{ doc.subslide() }}
# ### Typannotationen

# %% {{ doc.codealong() }}
def mult(a: int, b: float):
    return a * b


# %% {{ doc.codealong() }}
mult(3, 2.0)

# %% {{ doc.codealong() }}
# Typannotationen dienen lediglich zur Dokumentation und werden von Python
# ignoriert:
mult("a", 3)

# %% [markdown] {{ doc.subslide() }}
# ## Listen und Tupel

# %% {{ doc.codealong() }}
numbers = [1, 2, 3, 4]

# %% {{ doc.codealong() }}
print(numbers)
print(numbers[0], numbers[3])
print("Länge:", len(numbers))

# %% {{ doc.subslide() }}
numbers + numbers

# %% {{ doc.codealong() }}
[1] * 3

# %% {{ doc.codealong() }}
5 in [5, 6, 7]

# %% {{ doc.codealong() }}
3 in [5, 6, 7]

# %% {{ doc.subslide() }}
my_list = [1, 2, 3]
my_list[1] = 5
my_list

# %% {{ doc.codealong() }}
my_list.append(7)
my_list


# %% [markdown] {{ doc.subslide() }}
# ## Boole'sche Werte und `if`-Anweisungen

# %% {{ doc.codealong() }}
True

# %% {{ doc.codealong() }}
False

# %% {{ doc.codealong() }}
value = False

# %% {{ doc.codealong() }}
if value:
    print("Wahr")
else:
    print("Falsch")


# %% {{ doc.subslide() }}
def print_size(n):
    if n < 10:
        print("Very small")
    elif n < 15:
        print("Pretty small")
    elif n < 30:
        print("Average")
    else:
        print("Large")


# %% {{ doc.subslide() }}
print_size(1)
print_size(10)
print_size(20)
print_size(100)

# %% [markdown] {{ doc.subslide() }}
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
# ```python
# >>> print_line("Hallo")
# Hallo
# >>> print_line("Hallo", 3)
# ...
# >>>
# ```


# %% {{ doc.codealong() }}
def fits_in_line(text: str, line_length: int = 72):
    return len(text) <= line_length


# %% {{ doc.codealong() }}
fits_in_line("Hallo")

# %% {{ doc.codealong() }}
fits_in_line("Hallo", 3)


# %% {{ doc.codealong() }}
def print_line(text: str, line_length: int = 72):
    if fits_in_line(text, line_length=line_length):
        print(text)
    else:
        print("...")


# %% {{ doc.codealong() }}
print_line("Hallo")

# %% {{ doc.codealong() }}
print_line("Hallo", 3)


# %% [markdown] {{ doc.subslide() }}
# ## `for`-Schleifen

# %% {{ doc.subslide() }} {{ doc.codealong() }}
for char in "abc":
    print(char, end="|")

# %% {{ doc.codealong() }}
result = 0
for n in [1, 2, 3, 4]:
    result += n
result

# %% [markdown] {{ doc.subslide() }}
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


# %% {{ doc.codealong() }}
def print_all(items: list):
    for item in items:
        print(item)


# %% {{ doc.codealong() }}
print_all([1, 2, 3])

# %% {{ doc.codealong() }}
print_all("abc")

# %% {{ doc.subslide() }} {{ doc.codealong() }}
for i in range(3):
    print(i, end=", ")

# %% {{ doc.codealong() }}
for i in range(1, 6, 2):
    print(i, end=", ")

# %% [markdown] {{ doc.subslide() }}
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


# %% {{ doc.codealong() }}
def print_squares(n: int):
    for i in range(1, n+1):
        print(i, "**2 = ", i*i, sep="")


# %% {{ doc.codealong() }}
print_squares(3)

# %% [markdown] {{ doc.subslide() }}
# ## Dictionaries

# %%
translations = {"snake": "Schlange", "bat": "Fledermaus", "horse": "Hose"}

# %% {{ doc.codealong() }}
print(translations["snake"])
print(translations.get("bat", "<unbekannt>"))
print(translations.get("monkey", "<unbekannt>"))

# %% {{ doc.codealong() }}
# Fehler:
# translations['monkey']

# %% {{ doc.subslide() }} {{ doc.codealong() }}
translations["horse"] = "Pferd"
translations["horse"]

# %% {{ doc.subslide() }} {{ doc.codealong() }}
for key in translations.keys():
    print(key, end=" ")

# %% {{ doc.subslide() }} {{ doc.codealong() }}
for key in translations:
    print(key, end=" ")

# %% {{ doc.codealong() }}
for val in translations.values():
    print(val, end=" ")

# %% {{ doc.subslide() }} {{ doc.codealong() }}
for item in translations.items():
    print(item, end=" ")

# %% {{ doc.codealong() }}
for key, val in translations.items():
    print("Key:", key, "\tValue:", val)

# %%
