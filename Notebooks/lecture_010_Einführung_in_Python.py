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

# %% [markdown] slideshow={"slide_type": "slide"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <h1 style="text-align:center;">Einführung in Python: Grundlagen</h1>
# <h2 style="text-align:center;">Coding Akademie München GmbH</h2>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <div style="text-align:center;">Allaithy Raed</div>

# %% [markdown] slideshow={"slide_type": "slide"}
# # Python und Jupyter Notebooks
#
# Wir beginnen mit einer kurzen Einführung in die Arbeitsweise von Python und Jypyter Notebooks.

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

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
import numpy as np
import matplotlib.pyplot as plt

page_load_time = np.random.normal(3.0, 1.0, 1000)
purchase_amount = np.random.normal(50.0, 1.5, 1000) - page_load_time

plt.figure(figsize=(12, 8))
plt.scatter(page_load_time, purchase_amount)


# %% [markdown] slideshow={"slide_type": "slide"}
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

# %% [markdown] slideshow={"slide_type": "subslide"}
# Was benötigen wir dazu?
#
# - Daten 
#     - den Text `Hello, world!`
# - Anweisungen
#     - *Gib den folgenden Text auf dem Bildschirm aus*
# - Kommentare
#     - Hinweise für den Programmierer, werden von Python ignoriert

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Kommentare
#
# - `#` gefolgt von beliebigem Text
# - bis zum Ende der Zeile

# %% pycharm={"name": "#%%\n"}
# Das ist ein Kommentar.
# Alle Zeilen in dieser Zelle werden
# von Python ignoriert.


# %% [markdown] slideshow={"slide_type": "subslide"}
# # Daten
#
# - Zahlen: `123`, `3.141592`
# - Text (Strings): `'Das ist ein Text'`, `"Hello, world!"`

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
# Die Zahl 123
123


# %% pycharm={"name": "#%%\n"}
# Die Zahl Pi = 3.141592
3.141592


# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
# Der Text 'Das ist ein Text'
"Das ist ein Text"


# %% pycharm={"name": "#%%\n"}
# Der Text 'Hello, world!'
"Hello, world!"


# %% pycharm={"name": "#%%\n"}
"""Auch ein Text.
Der über mehrere Zeilen geht."""


# %% [markdown] slideshow={"slide_type": "slide"}
# ## Anzeige von Werten
#
# - Jupyter Notebooks geben den letzten Wert jeder Zelle auf dem Bildschirm aus
# - Das passiert in "normalen" Python-Programmen nicht!
#   - Wenn sie als Programme ausgeführt werden
#   - Der interaktive Interpreter verhält sich ähnlich wie Notebooks

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
123


# %% [markdown]
# Um die Ausgabe des letzten Wertes einer Zeile in Jupyter zu unterbinden kann man
# die Zeile mit einem Strichpunkt beenden:

# %% pycharm={"name": "#%%\n"}
123


# %% [markdown] slideshow={"slide_type": "slide"}
# ## Mehrere Berechnungen

# %% pycharm={"name": "#%%\n"}
2 * 3 + 4
5 + 6 * 7


# %% pycharm={"name": "#%%\n"}
2 * 3 + 4


# %% pycharm={"name": "#%%\n"}
5 + 6 * 7


# %% [markdown] slideshow={"slide_type": "subslide"}
# Wie kann man die Werte mehrerer Berechnungen in einer Zelle anzeigen?

# %% [markdown] slideshow={"slide_type": "slide"}
# # Anweisungen
#
# `print(...)` gibt den in Klammern eingeschlossenen Text auf dem Bildschirm aus

# %% pycharm={"name": "#%%\n"}
print("Hello, world!")


# %% [markdown]
# Vergleichen Sie die Ausgabe mit der folgenden Zelle:

# %% pycharm={"name": "#%%\n"}
"Hello, world!"


# %% [markdown] slideshow={"slide_type": "subslide"}
# - Den in Klammern eingeschlossenen Text nennt man das *Argument*
# - Man kann auch Zahlen und andere Werte mit `print` ausgeben.

# %% pycharm={"name": "#%%\n"}
print(234)


# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "-"}
print(1.1)


# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
print(2 * 3 + 4)
print(5 + 6 * 7)


# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
print(1 + 1)
2 + 2
print(3 + 3)
4 + 4
print(5 + 5)
6 + 6


# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
print("Hello, world!")


# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `010x-Workshop Einführung in Python`
# - Abschnitt "Einleitung"

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Ausdrucken mehrerer Werte in einer Zeile
#
# Einer `print()`-Anweisung können mehrere Argumente übergeben werden.
# - Die Argumente werden durch Kommata getrennt
# - Alle Argumente werden in einer Zeile ausgegeben, mit Leerzeichen zwischen den Argumenten.

# %% pycharm={"name": "#%%\n"}
print("Der Wert von 1 + 1 ist", 1 + 1, ".")


# %% [markdown] slideshow={"slide_type": "subslide"}
# Durch Angabe eines *benannten Arguments* `sep=''` kann die Ausgabe der Leerzeichen unterdrückt werden:

# %% pycharm={"name": "#%%\n"}
print("Der Wert von 1 + 1 ist", 1 + 1, ".", sep="")


# %% pycharm={"name": "#%%\n"}
print("Der Wert von 1 + 1 ist ", 1 + 1, ".", sep="")


# %% [markdown] slideshow={"slide_type": "subslide"}
# Es sind auch beliebige andere Strings als Wert des Arguments `sep` zulässig:

# %% pycharm={"name": "#%%\n"}
# CSV (nicht empfehlenswert)
print(1, 3, 7.5, 2, sep=",")


# %% pycharm={"name": "#%%\n"}
# Uh, oh
print(1, 3, 7.5, 2, "who, me?", sep=",")


# %% [markdown] slideshow={"slide_type": "slide"}
# # Zahlen und Mathematik
#
# - Ganze Zahlen: `1`, `837`, `-12`
# - Gleitkommazahlen: `0.5`, `123.4`, `-0.01`
# - Rechenoperationen: 
#     - Addition: `+`
#     - Subtraktion: `-`
#     - Multiplikation: `*`
#     - Division: `/`

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Python als Taschenrechner

# %% pycharm={"name": "#%%\n"}
17 + 4


# %% pycharm={"name": "#%%\n"}
1 + 4 * 4 + (3 - 1) * (1 + 1)


# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Arten von Zahlen
#
# - Python unterscheidet ganze Zahlen und Gleitkommazahlen:
#     - `1` ist eine ganze Zahl (`int`)
#     - `1.0` ist eine Gleitkommazahl (`float`)
# - Mit `type(...)` kann man den Typ des Arguments erfahren:

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
type(1)


# %% pycharm={"name": "#%%\n"}
type(1.0)


# %% pycharm={"name": "#%%\n"}
type("1")


# %% [markdown] slideshow={"slide_type": "subslide"}
# Ganze Zahlen in Python haben keine (praktisch relevante) Obergrenze:

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": ""}
10000000000000000000000000000000000000000000000000 + 500


# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": ""}
type(10000000000000000000000000000000000000000000000000)


# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `010x-Workshop Einführung in Python`
# - Abschnitt "Zahlen und Mathematik"

# %% [markdown] slideshow={"slide_type": "slide"}
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

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Division

# %% pycharm={"name": "#%%\n"}
4 / 2


# %% pycharm={"name": "#%%\n"}
20 / 7


# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
# // und % können zur Division mit Rest verwendet werden:
20 // 7  # Wie oft geht 7 in 20?


# %% pycharm={"name": "#%%\n"}
20 % 7  # Welcher Rest bleibt dabei?


# %% pycharm={"name": "#%%\n"}
(20 // 7) * 7 + (20 % 7)


# %% [markdown] slideshow={"slide_type": "subslide"}
# `/` ist links-assoziativ (genau wie `//`, `%`, `+`, `-`, `*`)

# %% pycharm={"name": "#%%\n"}
20 / 5 / 2


# %% pycharm={"name": "#%%\n"}
# Besser:
(20 / 5) / 2


# %% pycharm={"name": "#%%\n"}
20 / (5 / 2)


# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Exponentiation (Potenz)

# %% pycharm={"name": "#%%\n"}
2 ** 3


# %% pycharm={"name": "#%%\n"}
2 * 2 * 2


# %% pycharm={"name": "#%%\n"}
2 ** 4


# %% pycharm={"name": "#%%\n"}
2 * 2 * 2 * 2


# %% [markdown] slideshow={"slide_type": "subslide"}
# `**` ist rechts-assoziativ
#
# $2^{(2^3)} = 2^8 = 256 \qquad$
# $(2^2)^3 = 4^3 = 64$

# %% pycharm={"name": "#%%\n"}
2 ** 2 ** 3


# %% pycharm={"name": "#%%\n"}
2 ** (2 ** 3)


# %% pycharm={"name": "#%%\n"}
(2 ** 2) ** 3


# %% [markdown] slideshow={"slide_type": "subslide"}
# Der `**` Operator kann auch zum Wurzelziehen verwendet werden:
#
# $\sqrt{4} = 4^{1/2} = 2\qquad$
# $\sqrt{9} = 9^{1/2} = 3\qquad$
# $\sqrt{2} = 2^{1/2} \approx 1.4142\qquad$

# %% pycharm={"name": "#%%\n"}
4 ** 0.5


# %% pycharm={"name": "#%%\n"}
9 ** 0.5


# %% pycharm={"name": "#%%\n"}
2 ** 0.5


# %% [markdown] slideshow={"slide_type": "slide"}
# # Variablen
#
# Wir wollen einen Zaun um unser neues Grundstück bauen.
#
# <img src="img/fence.svg" style="display:block;margin:auto;width:50%"/>

# %% [markdown] slideshow={"slide_type": "subslide"}
# <img src="img/fence.svg" style="vertical-align:top;overflow:auto;float:right;width:25%"/>
#
# Die gemessenen Längen sind:
# - Birkenweg: 20m
# - Fichtengasse: 30m
#
# Wie lange muss unser Zaun sein?

# %% pycharm={"name": "#%%\n"}
20 + 30 + (20 ** 2 + 30 ** 2) ** 0.5


# %% [markdown] slideshow={"slide_type": "subslide"}
# <img src="img/fence.svg" style="vertical-align:top;overflow:auto;float:right;width:25%"/>
#
# Die gemessenen Längen sind:
# - Birkenweg: 20m
# - Fichtengasse: 30m
#
# Wie lange muss unser Zaun sein?

# %% pycharm={"name": "#%%\n"}
länge_birkenweg = 20
länge_fichtengasse = 30
länge_hauptstr = (länge_birkenweg ** 2 + länge_fichtengasse ** 2) ** 0.5
länge_gesamt = länge_birkenweg + länge_fichtengasse + länge_hauptstr
ergebniss = länge_gesamt

# %% [markdown] slideshow={"slide_type": "slide"}
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

# %% [markdown] slideshow={"slide_type": "subslide"}
# <img src="img/variables-01.svg" style="float:right;margin:auto;width:50%"/>
#
# Einve Variable wird
# - erzeugt durch `name = wert`
# - gelesen durch `name`
# - geändert durch `name = wert`
#
# Erzeugen und Ändern von Variablen<br/>
# sind *Anweisungen*.

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
länge_birkenweg = 20
print(länge_birkenweg)
länge_birkenweg = 25
print(länge_birkenweg)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## Eigenschaften von Variablen in Python
#
# - Eine Variable kann Werte mit beliebigem Datentyp speichern
#     - Es gibt keine `int`-Variablen, etc.
#     - Man sagt: Python ist dynamisch getypt
# - Variablen müssen erzeugt worden sein, bevor sie verwendet werden
# - Man kann Variablen neue Werte zuweisen
#     - Dabei kann der *alte Wert* der Variablen auf der rechten Seite verwendet werden:<br/> `jobs = jobs + 1`

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
x = "Hallo!"
print(x)
x = 123
print(x)
x = x + 1
print(x)
x += 1
print(x)


# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
# print(diese_variable_gibt_es_nicht)


# %% pycharm={"name": "#%%\n"}
# nonono = nonono + 1


# %% [markdown] slideshow={"slide_type": "slide"}
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

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Stil
#
# - Variablennamen werden klein geschrieben
#     - Außer konstanten Variablen: `CONSTANT_VAR`
# - Bestandteile werden durch Unterstriche `_` getrennt
#     - Dieser Stil nennt sich Snake-Case
# - Variablen, die mit zwei Unterstrichen anfangen und aufhören haben typischerweise eine spezielle Bedeutung (*Dunders*):
#     - `__class__`, `__name__`
#     - Normale benutzerdefinierte Variablen sollten nicht als Dunders benannt werden

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
print(__name__)
print(type(__name__))


# %% pycharm={"name": "#%%\n"}
# Bitte nicht nachmachen, obwohl es möglich ist:
__my_var__ = 123


# %% pycharm={"name": "#%%\n"}
__my_var__


# %% [markdown] slideshow={"slide_type": "subslide"}
# - Manchmal werden "private" Variablen mit einem führenden Unterstrich geschrieben: `_my_var`
#     - Das ist (für globale Variablen) besonders in älterem Code verbreitet
#     - In Klassen gibt es weitere Konventionen
# - Die meisten Python-Projekte folgen den Konventionen in [PEP 8](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

# %% pycharm={"name": "#%%\n"}
_my_var = 234


# %% pycharm={"name": "#%%\n"}
_my_var


# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
variable_1 = 123
VARIABLE_1 = 234
Variable_1 = 345
variablE_1 = 456


# %% pycharm={"name": "#%%\n"}
print(variable_1)
print(VARIABLE_1)
print(Variable_1)
print(variablE_1)


# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
_my_var = 1
print(_my_var)
_my_var = _my_var + 5
print(_my_var)


# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
größenmaßstäbe_der_fußgängerübergänge = 0.3
größenmaßstäbe_der_fußgängerübergänge


# %% pycharm={"name": "#%%\n"}
# me@foo = 1


# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
α = 0.2
β = 0.7
γ = α ** 2 + 3 * β ** 2
print(γ)
αβγ = α * β * γ
print(αβγ)
Σ = 1 + 2 + 3
print(Σ)
# ∑ = 1 + 2 + 3 # Unzulässig!


# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `010x-Workshop Einführung in Python`
# - Abschnitt "Piraten"

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Zuweisung an mehrere Variablen
#
# In Python können mehrere Variablen gleichzeitig definiert bzw. mit neuen Werten versehen werden:

# %% pycharm={"name": "#%%\n"}
a, b = 1, 2
print(a)
print(b)


# %% [markdown] slideshow={"slide_type": "slide"}
# # Funktionen
#
# Wir haben eine Firma zum Einzäunen dreieckiger Grundstücke gegründet.
#
# Für jedes von Straßen $A$, $B$ und $C$ begrenze Grundstück berechnen wir:

# %% pycharm={"name": "#%%\n"}
länge_a = 10  # Beispielwert
länge_b = 40  # Beispielwert
länge_c = (länge_a ** 2 + länge_b ** 2) ** 0.5
länge_gesamt = länge_a + länge_b + länge_c
print(länge_gesamt)


# %% [markdown]
# Können wir das etwas eleganter gestalten?

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Satz von Pythagoras
#
# Wir berechnen die Länge von $C$ aus $A$ und $B$ immer nach dem Satz von Pythagoras: $C = \sqrt{A^2 + B^2}$.
#
# Das können wir in Python durch eine *Funktion* ausdrücken:

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
def pythagoras(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c



# %% pycharm={"name": "#%%\n"}
pythagoras(3, 4)


# %% pycharm={"name": "#%%\n"}
pythagoras(1, 1)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## Funktionsdefinition
# - Schlüsselwort `def`
# - Name der Funktion
# - Parameter der Funktion, in Klammern; Doppelpunkt
# - Rumpf der Funktion, einen Tabulator eingerückt
# - Im Rumpf können die Parameter wie Variablen verwendet werden
# - Schlüsselwort `return`
#     - Beendet die Funktion
#     - Bestimmt welcher Wert zurückgegeben wird

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
def pythagoras(a, b):
    quadratsumme = a ** 2 + b ** 2
    return quadratsumme ** 0.5



# %% [markdown] slideshow={"slide_type": "slide"}
# ## Funktionsaufruf
#
# - Name der Funktion
# - Argumente des Aufrufs, in Klammern
# - Ein Argument für jeden Parameter

# %% pycharm={"name": "#%%\n"}
pythagoras(3, 4)


# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Zurück zur Zaunlänge
#
# - Wir haben bis jetzt die Länge der dritten Seite unseres Grundstücks berechnet.
# - Wir brauchen noch eine Funktion, die die Gesamtlänge ausrechnet:

# %% pycharm={"name": "#%%\n"}
def gesamtlänge(x, y):
    z = pythagoras(x, y)
    länge = x + y + z
    return länge



# %% [markdown] slideshow={"slide_type": "subslide"}
# Damit können wir unser Problem vereinfachen:

# %% pycharm={"name": "#%%\n"}
länge_a = 10  # Beispielwert
länge_b = 40  # Beispielwert
print(gesamtlänge(länge_a, länge_b))


# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `010x-Workshop Einführung in Python`
# - Abschnitt "Spenden"
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Import von Modulen
#
# Ein Großteil der Funktionalität von Python ist nicht direkt im Interpreter verfügbar sonder in Module (und Packages) ausgelagert. Mit der `import` Anweisung kann man dises Funktionalität verfügbar machen:

# %% pycharm={"name": "#%%\n"}
# Zusätzliche mathematische Funktionen:
import math


# %% [markdown] slideshow={"slide_type": "subslide"}
# Auf die Funktionen aus dem `math` Modul kann man dann mit der Syntax `math.floor` zugreifen:

# %% pycharm={"name": "#%%\n"}
math.floor(2.5)


# %% pycharm={"name": "#%%\n"}
math.floor(2.9)


# %% [markdown] slideshow={"slide_type": "subslide"}
# Die Funktion `pythagoras` steht im `math`-Modul unter dem Namen `hypot` zur Verfügung:

# %% pycharm={"name": "#%%\n"}
math.hypot(3, 4)


# %% [markdown] slideshow={"slide_type": "subslide"}
# Damit können wir die Funktion `gesamtlänge` ohne die Hilfsfunktion `pythagoras` schreiben:

# %% pycharm={"name": "#%%\n"}
def gesamtlänge(x, y):
    z = math.hypot(x, y)
    länge = x + y + z
    return länge



# %% pycharm={"name": "#%%\n"}
gesamtlänge(3, 4)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## Andere Arten von Zahlen
#
# Python bietet noch weitere Arten von Zahlen für spezielle Anwendungen
#
# - Dezimalzahlen mit beliebiger Genauigkeit
# - Komplexe Zahlen
# - Ganze Zahlen mit fixer Größe (z.B. mit `numpy`)
# - Gleitkommazahlen mit unterschiedlicher Größe (`numpy`)

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
1.1 * 100


# %% pycharm={"name": "#%%\n"}
import decimal

decimal.Decimal("1.1") * 100


# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
(1 + 1j) * (1 + 1j)


# %% pycharm={"name": "#%%\n"}
1j * 1j


# %% [markdown] slideshow={"slide_type": "slide"}
# ## Funktionen ohne Argumente
#
# - Eine Funktion kann auch ohne formale Parameter definiert werden.
# - Sowohl bei der Definition, als auch beim Aufruf müssen die Klammern trotzdem angegeben werden.

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
def null():
    return 0



# %% pycharm={"name": "#%%\n"}
null()


# %% pycharm={"name": "#%%\n"}
# Fehler: 'Aufruf' ohne Klammern
null
# plus_eins(null)


# %% [markdown] slideshow={"slide_type": "slide"}
# # Funktionen mit Seiteneffekten
#
# Funktionene können
#
# - Werte berechnen: `quadratsumme(3, 4)`
# - Seiteneffekte haben: `print("Hans")`

# %% pycharm={"name": "#%%\n"}
type(print("Hans"))


# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Der Wert `None`
#
# Der Rückgabewert der Funktion `print()` ist der spezielle Wert `None`.
# - Jupyter druckt `None` nicht als Wert einer Zelle aus:

# %% pycharm={"name": "#%%\n"}
None


# %% pycharm={"name": "#%%\n"}
print(None)


# %% pycharm={"name": "#%%\n"}
print(print("Hans"))


# %% [markdown] slideshow={"slide_type": "subslide"}
# - Funktionen können Seiteneffekte haben
#     - Z.B. durch Aufruf von `print`
# - Diese werden ausgeführt, wenn ein Funktionsaufruf ausgewertet wird
# - Auch Funktionen mit Seiteneffekten geben einen Wert zurück
#     - Oft ist das der spezielle Wert `None`
#     - Wenn eine Funktion `None` zurückgibt brauchen wir keine explizite `return`-Anweisung

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
def say_hello():
    print("Hello, world!")
    print("Today is a great day!")



# %% pycharm={"name": "#%%\n"}
say_hello()


# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `010x-Workshop Einführung in Python`
# - Abschnitt "Piraten, Teil 2"
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Default-Argumente
#
# Funktionsparameter können einen Default-Wert haben.
# - Der Default-Wert wird mit der Syntax `parameter=wert` angegeben
# - Wird das entsprechende Argument nicht übergeben so wird der Default-Wert eingesetzt
# - Hat ein Parameter einen Default-Wert, so müssen alle rechts davon stehenden Werte ebenfalls einen haben

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
def add_weighted(a, b=0, c=0):
    return a + 2 * b + 3 * c



# %% pycharm={"name": "#%%\n"}
print(add_weighted(2))
print(add_weighted(2, 3))
print(add_weighted(2, 3, 4))


# %% [markdown] slideshow={"slide_type": "slide"}
# ## Aufruf mit benannten Argumenten
#
# Beim Aufruf einer Funktion kann der Parametername in der Form `parameter=wert` angegeben werden.
# - Der entsprechende Wert wird dann für den benannten Parameter eingesetzt
# - Werden alle Parameter benannt, so wird der Aufruf unabhängig von der Parameterreihenfolge

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
def say_hi(person, greeting="Hi"):
    print(greeting, " ", person, "!", sep="")



# %% pycharm={"name": "#%%\n"}
say_hi("Jill")
say_hi("Jack", "Good morning")


# %% pycharm={"name": "#%%\n"}
say_hi(greeting="Heya", person="Betty")


# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
def add_weighted(a, b=0, c=0):
    return a + 2 * b + 3 * c



# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": ""}
add_weighted(c=2, a=1)


# %% pycharm={"name": "#%%\n"}
add_weighted(5, c=7)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## Typannotationen
#
# Python erlaubt es die Typen von Funktionsargumenten und den Rückgabetyp einer Funktion anzugeben:

# %% pycharm={"name": "#%%\n"}
def mult(a: int, b: float) -> float:
    return a * b



# %% pycharm={"name": "#%%\n"}
mult(3, 2.0)


# %% [markdown] slideshow={"slide_type": "subslide"}
# Typannotationen dienen lediglich zur Dokumentation und werden von Python ignoriert:

# %% pycharm={"name": "#%%\n"}
mult("a", 3)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## Docstrings
#
# Jede Funktion in Python kann dokumentiert werden, indem ein String-Literal als erstes Element im Rumpf angegeben wird. Meistens wird dafür ein `"""`-String verwendet:

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
def my_fun(x):
    """
    Zeigt dem Benutzer den Wert von x an

    Verwendung:
    > my_fun(123)
    """
    print("Das Argument x hat den Wert", x)



# %% pycharm={"name": "#%%\n"}
my_fun(123)


# %% [markdown] slideshow={"slide_type": "subslide"}
# Konventionen für Docstrings finden sich in [PEP 257](https://www.python.org/dev/peps/pep-0257/).

# %% [markdown] slideshow={"slide_type": "subslide"}
# Der Docstring einer Funktion kann mit `help()` ausgegeben werden:

# %% pycharm={"name": "#%%\n"}
help(my_fun)


# %% [markdown] slideshow={"slide_type": "subslide"}
# In Jupyter kann man den Docstring einer Funktion durch ein vorangestelltes oder nachgestelltes Fragezeichen anzeigen lassen:

# %% pycharm={"name": "#%%\n"}
# # ?my_fun


# %% pycharm={"name": "#%%\n"}
# # my_fun?


# %% [markdown] slideshow={"slide_type": "subslide"}
# Oft verwendet man statt dessen Shift-Tab:

# %% pycharm={"name": "#%%\n"}
my_fun


# %% [markdown] slideshow={"slide_type": "subslide"}
# Bei Funktionen mit langen Docstrings kann man durch zweimaliges Drücken von `Shift-Tab` auf die ausführliche Anzeigeform umschalten:

# %% pycharm={"name": "#%%\n"}
my_fun


# %% pycharm={"name": "#%%\n"}
print


# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Signatur
#
# Die Anzahl, Namen, Default-Werte (und evtl. Typen) einer Funktion nennt man ihre *Signatur*.
#
# Jupyter zeigt u.a. die Signatur einer Funktion an, wenn man `Shift-Tab` eingibt:

# %% pycharm={"name": "#%%\n"}
# Shift-Tab zum Anzeigen der Signatur:
say_hi


# %% pycharm={"name": "#%%\n"}
def add_ints(m: int, n: int) -> int:
    return m + n



# %% pycharm={"name": "#%%\n"}
add_ints


# %% [markdown] slideshow={"slide_type": "slide"}
# ## Mehrere Rückgabewerte
#
# Wie oben gezeigt kann man mehrere Variablen in einem Schritt definieren:

# %% pycharm={"name": "#%%\n"}
ergebnis, rest = 10, 2


# %% pycharm={"name": "#%%\n"}
print(ergebnis)
print(rest)


# %% [markdown] slideshow={"slide_type": "subslide"}
# - Besonders hilfreich ist das für Funktionen die mehrere eng zusammenhängende Werte berechnen.
# - Man kann mit `return wert1, wert2` mehrere Werte zurückgeben

# %% pycharm={"name": "#%%\n"}
def zwei_werte(a, b):
    return a + 1, b + 2



# %% pycharm={"name": "#%%\n"}
erster_wert, zweiter_wert = zwei_werte(1, 2)
print(erster_wert)
print(zweiter_wert)


# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
def division_mit_rest(m, n):
    ergebnis = m // n
    rest = m % n
    return ergebnis, rest



# %% pycharm={"name": "#%%\n"}
e, r = division_mit_rest(17, 7)
print(e)
print(r)


# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": ""}
# Kürzer
def division_mit_rest_2(m, n):
    return m // n, m % n



# %% pycharm={"name": "#%%\n"}
e, r = division_mit_rest_2(17, 7)
print(e)
print(r)


# %% [markdown] slideshow={"slide_type": "subslide"}
# (In Python gibt es die eingebaute Funktion `divmod`, die diese Berechnung ausführt:)

# %% pycharm={"name": "#%%\n"}
e, r = divmod(17, 7)
print(e)
print(r)


# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `010x-Workshop Einführung in Python`
# - Abschnitt "Piraten, Teil 3"
