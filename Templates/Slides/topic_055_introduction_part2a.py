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
# <div style="text-align:center; font-size:200%;"><b>Einführung in Python: Grundlagen Teil 2</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Introduction to Python: Part 2</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>


# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# # `if`-Anweisungen
#
# - Wir wollen ein Programm schreiben, das bestimmt ob eine Zahl eine Glückszahl
#   ist oder nicht:
#     - 7 ist eine Glückszahl
#     - Alle anderen Zahlen sind es nicht.
# - Wir benötigen dazu die `if`-Anweisung:

# %% [markdown] {"lang": "en"}
# # `if` statements
#
# - We want to write a program that determines if a number is a lucky number or not:
#     - 7 is a lucky number
#     - all other numbers are not.
# - We need the `if` statement for this:

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"], "lang": "de"}
def ist_glückszahl(zahl):
    if zahl == 7:
        print("Glückszahl")
    else:
        print("Keine Glückszahl")


# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"], "lang": "en"}
def is_lucky_number(number):
    if number == 7:
        print("lucky number")
    else:
        print("not a lucky number")

# %% {"tags": ["code-along"], "lang": "de"}
ist_glückszahl(1)

# %% {"tags": ["code-along"], "lang": "en"}
is_lucky_number(1)

# %% {"tags": ["code-along"], "lang": "de"}
ist_glückszahl(7)

# %% {"tags": ["code-along"], "lang": "en"}
is_lucky_number(7)


# %% {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
def ist_glückszahl_1(zahl):
    print("Ist", zahl, "eine Glückszahl?")

    if zahl == 7:
        print("Ja!")
    else:
        print("Leider nein.")

    print("Wir wünschen Ihnen alles Gute.")


# %% {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
def is_lucky_number_1(number):
    print("Is", number, "a lucky number?")

    if number == 7:
        print("Yes!")
    else:
        print("Unfortunately no.")

    print("We wish you all the best.")

# %% {"lang": "de"}
ist_glückszahl_1(1)

# %% {"lang": "en"}
is_lucky_number_1(1)

# %% {"lang": "de"}
ist_glückszahl_1(7)

# %% {"lang": "en"}
is_lucky_number_1(7)


# %% {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
def ist_glückszahl_2(zahl):
    if zahl == 7:
        print(zahl, "ist eine Glückszahl!")
        print("Sie haben sicher einen super Tag!")
    else:
        print(zahl, "ist leider keine Glückszahl.")
        print("Vielleicht sollten Sie heute lieber im Bett bleiben.")
        print("Wir wünschen Ihnen trotzdem alles Gute.")


# %% {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
def is_lucky_number_2(number):
    if number == 7:
        print(number, "is a lucky number!")
        print("You must be having a great day!")
    else:
        print(number, "is unfortunately not a lucky number.")
        print("Maybe you should stay in bed today.")
        print("We wish you all the best anyway.")


# %% {"tags": ["code-along"], "lang": "de"}
ist_glückszahl_2(1)

# %% {"lang": "en"}
is_lucky_number_2(1)

# %% {"tags": ["code-along"], "lang": "de"}
ist_glückszahl_2(7)

# %% {"lang": "en"}
is_lucky_number_2(7)


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Workshop
#
# - Notebook `workshop_060_introduction_part2`
# - Abschnitt "Volljährig"

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# ## Workshop
#
# - Notebook `workshop_060_introduction_part2`
# - Section "Of legal age"

# %% {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
def einseitiges_if(zahl):
    print("Vorher")

    if zahl == 7:
        print(zahl, "ist eine Glückszahl")
        print("Glückwunsch!")

    print("Nachher")


# %% {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
def one_sided_if(number):
    print("Before")

    if number == 7:
        print(number, "is a lucky number")
        print("Congratulations!")

    print("After")


# %% {"tags": ["code-along"], "lang": "de"}
einseitiges_if(1)

# %% {"tags": ["code-along"], "lang": "en"}
one_sided_if(1)

# %% {"tags": ["code-along"], "lang": "de"}
einseitiges_if(7)

# %% {"tags": ["code-along"], "lang": "en"}
one_sided_if(7)

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# # Listen

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# # Lists

# %% {"lang": "de"}
warenkorb = ["Haferflocken", "Kaffeebohnen", "Orangenmarmelade"]

# %% {"lang": "en"}
shopping_cart = ["oatmeal", "coffee beans", "orange marmalade"]

# %% [markdown] {"lang": "de"}
# Der Typ von Listen ist `list`.

# %% [markdown] {"lang": "en"}
# The type of lists is `list`.

# %% {"tags": ["code-along"], "lang": "de"}
type(warenkorb)

# %% {"tags": ["code-along"], "lang": "en"}
type(shopping_cart)

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Erzeugen von Listen
#
# - Listen werden erzeugt, indem man ihre Elemente in eckige Klammern
#   einschließt.
# - Die Elemente einer Liste können beliebige Python-Werte sein.
# - Eine Liste kann Elemente mit verschiedenen Typen enthalten.

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# ## Creating lists
#
# - Lists are created by enclosing their elements in square brackets.
# - The elements of a list can be any Python values.
# - A list can contain elements of different types.

# %% {"slideshow": {"slide_type": "subslide"}}
list_1 = [1, 2, 3, 4, 5]
list_2 = ["string1", "another string"]

# %% {"tags": ["code-along"]}
print(list_1)

# %% {"tags": ["code-along"]}
print(list_2)

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
list_3 = []
list_4 = [1, 0.4, "ein String", True, None]

# %% {"tags": ["code-along"]}
print(list_3)

# %% {"tags": ["code-along"]}
print(list_4)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
# Die Elemente einer Liste müssen keine Literale sein, man kann auch Werte von
# Variablen in einer Liste speichern:

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# The elements of a list do not have to be literals, it can also contain values of variables or expressions:

# %% {"lang": "de"}
produkt_1 = "Haferflocken"
produkt_2 = "Kaffeebohnen"
produkt_3 = "Orangenmarmelade"
warenkorb = [produkt_1, produkt_2, produkt_3, "Erdbeermarmelade"]
warenkorb

# %% {"lang": "en"}
product_1 = "oatmeal"
product_2 = "coffee beans"
product_3 = "orange marmalade"
shoopping_cart = [product_1, product_2, product_3, "strawberry jam"]
shopping_cart

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
# Nachdem eine Liste erzeugt ist hat sie keine Verbindung zu den Variablen, die
# in ihrer Konstruktion verwendet wurden:

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# Once a list has been created, it has no connection to the variables that were
# used in its construction:

# %% {"tags": ["code-along"], "lang": "de"}
produkt_1 = "Dinkelflocken"
produkt_2 = "Teebeutel"
warenkorb

# %% {"tags": ["code-along"], "lang": "en"}
product_1 = "spelled flakes"
product_2 = "teabag"
shopping_cart

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Mit der Funktion `list()` können manche andere Datentypen in Listen umgewandelt
# werden.
#
# Im Moment kennen wir nur Listen und Strings als mögliche Argumenttypen:

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# The `list()` function can be used to convert some other data types into lists.
#
# At the moment we only know lists and strings as possible argument types:

# %% {"tags": ["code-along"]}
list("abc")

# %% {"tags": ["code-along"]}
list([1, 2, 3])

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Zugriff auf Listenelemente

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# ## Accessing list items

# %%
number_list = [0, 1, 2, 3]

# %% {"tags": ["code-along"]}
number_list[0]

# %% {"tags": ["code-along"]}
number_list[3]

# %% {"tags": ["code-along"]}
number_list[-1]

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Länge einer Liste

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# ## Length of a list

# %%
number_list

# %% {"tags": ["code-along"]}
len(number_list)

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Modifikation von Listeneinträgen

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# ## Modification of list entries

# %% {"tags": ["code-along"]}
number_list[1] = 10
number_list

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Einfügen und Löschen von Elementen
#
# Wenn möglich ist es zweckmäßig Elemente an das Ende einer Liste anzufügen.

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# ## Inserting and deleting items
#
# If possible elements should be inserted at the end of a list

# %% {"tags": ["code-along"]}
number_list.append(40)
number_list

# %% {"tags": ["code-along"]}
number_list.extend([50, 60])
number_list

# %% {"tags": ["code-along"]}
number_list.pop()
number_list

# %% {"tags": ["code-along"]}
number_list.insert(1, 9)
number_list

# %% {"tags": ["code-along"]}
number_list.pop(1)
number_list

# %% {"tags": ["code-along"]}
del number_list[1]
number_list

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
# ## Iteration über Listen
#
# In Python kann man mit der `for`-Schleife über Listen iterieren.
#
# Die `for`-Schleife entspricht dem range-based for aus C++,
# `for-in`/`for-of` aus JavaScript oder der `for-each`-Schleife
# aus Java, nicht der klassischen `for`-Schleife
# aus C, C++ oder Java.

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# ## Iteration over lists
#
# In Python, you can iterate over lists using the `for` loop.
#
# The `for` loop corresponds to the range-based for from C++,
# `for-in`/`for-of` from JavaScript or the `for-each` loop
# from Java, not the classic `for` loop
# from C, C++ or Java.

# %% {"slideshow": {"slide_type": "subslide"}}
number_list = [0, 1, 2, 3, 4]
number_list

# %% {"tags": ["code-along"]}
for number in number_list:
    print("Number is:", number)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Syntax der `for`-Schleife
#
# ```python
# for <element-var> in <liste>:
#     <rumpf>
# ```

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# ## Syntax of `for` loops
#
# ```pythons
# for <element-var> in <liste>:
#     <rumpf>
# ```

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Workshop
#
# - Notebook `workshop_060_introduction_part2`
# - Abschnitt "Einkaufsliste"

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# ## Workshop
#
# - Notebook `workshop_060_introduction_part2`
# - Section "Shopping list"

# %%
