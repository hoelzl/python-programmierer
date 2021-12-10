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
# {{ doc.header("Einführung in Python: Grundlagen Teil 3 - Gelöscht") }}



# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # `if`-Anweisungen
#
# - Wir wollen ein Programm schreiben, das bestimmt ob eine Zahl eine Glückszahl
#   ist oder nicht:
#     - 7 ist eine Glückszahl
#     - Alle anderen Zahlen sind es nicht.
# - Wir benötigen dazu die `if`-Anweisung:

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
def ist_glückszahl(zahl):
    print("Ist", zahl, "eine Glückszahl?")

    if zahl == 7:
        print("Ja!")
    else:
        print("Leider nein.")

    print("Wir wünschen Ihnen alles Gute.")


# %% {{ doc.codealong() }}
ist_glückszahl(1)

# %% {{ doc.codealong() }}
ist_glückszahl(7)


# %% {"slideshow": {"slide_type": "subslide"}}
def ist_glückszahl_2(zahl):
    if zahl == 7:
        print(zahl, "ist eine Glückszahl!")
        print("Sie haben sicher einen super Tag!")
    else:
        print(zahl, "ist leider keine Glückszahl.")
        print("Vielleicht sollten Sie heute lieber im Bett bleiben.")
        print("Wir wünschen Ihnen trotzdem alles Gute.")


# %% {{ doc.codealong() }}
ist_glückszahl_2(1)

# %% {{ doc.codealong() }}
ist_glückszahl_2(7)


# %% {"slideshow": {"slide_type": "subslide"}}
def einseitiges_if_1(zahl):
    print("Vorher")

    if zahl == 7:
        print(zahl, "ist eine Glückszahl")
        print("Glückwunsch!")

    print("Nachher")


# %% {{ doc.codealong() }}
einseitiges_if_1(1)

# %% {{ doc.codealong() }}
einseitiges_if_1(7)


# %% {"slideshow": {"slide_type": "subslide"}}
def einseitiges_if_2(zahl):
    if zahl % 2 != 0:
        zahl += 1  # zahl = zahl + 1
    print(zahl)


# %% {{ doc.codealong() }}
einseitiges_if_2(1)

# %% {{ doc.codealong() }}
einseitiges_if_2(6)



# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Listen

# %%
warenkorb = ["Haferflocken", "Kaffeebohnen", "Orangenmarmelade"]

# %% [markdown]
# Der Typ von Listen ist `list`.

# %% {{ doc.codealong() }}
type(warenkorb)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Erzeugen von Listen
#
# - Listen werden erzeugt, indem man ihre Elemente in eckige Klammern
#   einschließt.
# - Die Elemente einer Liste können beliebige Python-Werte sein.
# - Eine Liste kann Elemente mit verschiedenen Typen enthalten.

# %% {"slideshow": {"slide_type": "subslide"}}
liste_1 = [1, 2, 3, 4, 5]
liste_2 = ["string1", "another string"]

# %% {{ doc.codealong() }}
print(liste_1)

# %% {{ doc.codealong() }}
print(liste_2)

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
liste_3 = []
liste_4 = [1, 0.4, "ein String", True, None]

# %% {{ doc.codealong() }}
print(liste_3)

# %% {{ doc.codealong() }}
print(liste_4)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
#
# Die Elemente einer Liste müssen keine Literale sein, man kann auch Werte von
# Variablen in einer Liste speichern:

# %%
produkt_1 = "Haferflocken"
produkt_2 = "Kaffeebohnen"
produkt_3 = "Orangenmarmelade"
warenkorb = [produkt_1, produkt_2, produkt_3, "Erdbeermarmelade"]
warenkorb

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
#
# Nachdem eine Liste erzeugt ist hat sie keine Verbindung zu den Variablen, die
# in ihrer Konstruktion verwendet wurden:

# %% {{ doc.codealong() }}
produkt_1 = "Dinkelflocken"
produkt_2 = "Teebeutel"
warenkorb

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
#
# Mit der Funktion `list` können manche andere Datentypen in Listen umgewandelt
# werden.
#
# Im Moment kennen wir nur Listen, Strings und Dictionaries als mögliche
# Argumenttypen:

# %% {{ doc.codealong() }}
list("abc")

# %% {{ doc.codealong() }}
list([1, 2, 3])

# %% {{ doc.codealong() }}
list({"a": 1, "b": 2})

# %% [markdown] {"pycharm": {"name": "#%% md\n"}, "slideshow": {"slide_type": ""}}
# ## Zugriff auf Listenelemente

# %%
zahlenliste = [0, 1, 2, 3]

# %% {{ doc.codealong() }}
zahlenliste[0]

# %% {{ doc.codealong() }}
zahlenliste[3]

# %% {{ doc.codealong() }}
zahlenliste[-1]

# %% [markdown] {"pycharm": {"name": "#%% md\n"}, "slideshow": {"slide_type": "slide"}}
# ## Länge einer Liste

# %%
zahlenliste

# %% {{ doc.codealong() }}
len(zahlenliste)

# %% [markdown] {"pycharm": {"name": "#%% md\n"}, "slideshow": {"slide_type": "slide"}}
# ## Modifikation von Listeneinträgen

# %% {{ doc.codealong() }}
zahlenliste[1] = 10
zahlenliste

# %% [markdown] {"pycharm": {"name": "#%% md\n"}, "slideshow": {"slide_type": "slide"}}
# ## Anhängen von Elementen an eine Liste

# %% {{ doc.codealong() }}
zahlenliste.append(40)
zahlenliste

# %% {{ doc.codealong() }}
zahlenliste.extend([50, 60])
zahlenliste

# %% [markdown] {"pycharm": {"name": "#%% md\n"}, "slideshow": {"slide_type": "slide"}}
# ## Iteration über Listen
#
# In Python kann man mit der `for`-Schleife über Listen iterieren.
#
# Die `for`-Schleife entspricht dem range-based for aus C++,
# `for-in`/`for-of` aus JavaScript oder der `for-each`-Schleife
# aus Java, nicht der klassischen `for`-Schleife
# aus C, C++ oder Java.

# %% {"slideshow": {"slide_type": "subslide"}}
zahlenliste = [0, 1, 2, 3, 4]
zahlenliste

# %% {{ doc.codealong() }}
for zahl in zahlenliste:
    print("Die Zahl ist:", zahl)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Syntax der `for`-Schleife
#
# ```python
# for <element-var> in <liste>:
#     <rumpf>
# ```

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Workshop
#
# - Notebook `workshop_060_introduction_part2`
# - Abschnitt "Einkaufsliste"


