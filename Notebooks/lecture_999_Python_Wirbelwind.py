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
# <h1 style="text-align:center;">Python Wirbelwind</h1>
# <h2 style="text-align:center;">Coding Akademie München GmbH</h2>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <div style="text-align:center;">Allaithy Raed</div>

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Variablen und Datentypen
#
# Zahlen und Arithmetik:

# %%
17 + 4

# %%
1.5 + 7.4

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Zeichenketten

# %%
"This is a string" " with extension"

# %%
'This is also a string'

# %%
str(1 + 2)

# %%
"3" + 'abc'

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Variablen

# %%
answer = 42

# %%
my_value = answer + 2 * 3 - 4 // 3 + 7 % 2

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Evaluierung vs. Drucken von Werten

# %%
answer

# %%
my_value

# %%
answer
my_value

# %% slideshow={"slide_type": "subslide"}
print(answer)

# %%
print(my_value)

# %%
print(answer)
print(my_value)

# %% slideshow={"slide_type": "subslide"}
print("answer =", answer, "my_value =", my_value)

# %%
print('a', 'b', 'c', end='+++')
print('d', 'e')

# %%
print('a', end = ", ")
print('b', end = ", ")
print('c')

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Typen

# %%
type(123)

# %%
type('Foo')

# %%
answer = 42
print(type(answer))
answer = "Hallo!"
print(type(answer))


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

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Vordefinierte Funktionen

# %%
round(4.4)

# %%
round(4.6)

# %%
print(round(0.5), round(1.5), round(2.5), round(3.5))


# %%
def my_round(n):
    return int(n + 0.5)
print(my_round(0.5), my_round(1.5), my_round(2.5), my_round(3.5))

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Methoden

# %%
"Foo".lower()

# %%
number = 5
number.bit_length()


# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Mehrere Parameter, Default Argumente

# %%
def add(a, b=0, c=0):
    return a + b + c


# %%
print(add(2))
print(add(2, 3))
print(add(2, 3, 4))
print(add(1, c=3))

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Verschachtelte Funktionsaufrufe

# %%
add(add_1(2), add(1, 2, add(1, 2)))


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

# %% slideshow={"slide_type": "subslide"}
my_list = [1, 2, 3]
my_list[1] = 5
my_list

# %%
my_list.append(7)
my_list


# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Kontrollstrukturen

# %%
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

# %% slideshow={"slide_type": "subslide"}
for char in "abc":
    print(char, end='|')

# %%
result = 0
for n in [1, 2, 3, 4]:
    result += n
result

# %% slideshow={"slide_type": "subslide"}
for i in range(3):
    print(i, end=", ")

# %%
for i in range(1, 6, 2):
    print(i, end=", ")

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Dictionaries

# %%
translations = {'snake': 'Schlange', 'bat': 'Fledermaus', 'horse': 'Hose'}

# %%
print(translations['snake'])
print(translations.get('bat', '<unbekannt>'))
print(translations.get('monkey', '<unbekannt>'))

# %%
# Fehler:
# translations['monkey']

# %% slideshow={"slide_type": "subslide"}
translations['horse'] = 'Pferd'
translations['horse']

# %%
list = [1, 2, 3]
list[0] = 'one'
list

# %% slideshow={"slide_type": "subslide"}
for key in translations.keys():
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
