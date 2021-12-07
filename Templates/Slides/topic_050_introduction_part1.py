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
# {{ doc.header("Einführung in Python: Grundlagen (Teil 1)") }}

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
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

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Was benötigen wir dazu?
#
# - Daten 
#     - den Text `Hello, world!`
# - Anweisungen
#     - *Gib den folgenden Text auf dem Bildschirm aus*
# - Kommentare
#     - Hinweise für den Programmierer, werden von Python ignoriert

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Kommentare
#
# - `#` gefolgt von beliebigem Text
# - bis zum Ende der Zeile

# %%
# Das ist ein Kommentar.
# Alle Zeilen in dieser Zelle werden
# von Python ignoriert.


# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# # Daten
#
# - Zahlen: `123`, `3.141592`
# - Text (Strings): `'Das ist ein Text'`, `"Hello, world!"`

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
# Die Zahl 123
123

# %% {{ doc.codealong() }}
# Die Zahl Pi = 3.141592
3.141592

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
# Der Text 'Das ist ein Text'
"Das ist ein Text"

# %% {{ doc.codealong() }}
# Der Text 'Hello, world!'
"Hello, world!"

# %% {{ doc.codealong() }}
"""Auch ein Text.
Der über mehrere Zeilen geht."""

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Mini-Workshop
#
# - Notebook `lecture_010x_Workshop_Einführung_in_Python`
# - Abschnitt "Einleitung"

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Wiederholung: `print()`-Funktion
#
# Einer `print()`-Anweisung können mehrere Argumente übergeben werden.
# - Die Argumente werden durch Kommata getrennt
# - Alle Argumente werden in einer Zeile ausgegeben, mit Leerzeichen zwischen den Argumenten.

# %% {{ doc.codealong() }}
print("Der Wert von 1 + 1 ist", 1 + 1, ".")

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Durch Angabe eines *benannten Arguments* `sep=''` kann die Ausgabe der
# Leerzeichen unterdrückt werden:

# %% {{ doc.codealong() }}
print("Der Wert von 1 + 1 ist", 1 + 1, ".", sep="")

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Es sind auch beliebige andere Strings als Wert des Arguments `sep` zulässig:

# %% {{ doc.codealong() }}
# CSV (nicht empfehlenswert)
print(1, 3, 7.5, 2, sep=",")

# %% {{ doc.codealong() }}
# Uh, oh
print(1, 3, 7.5, 2, "who, me?", sep=",")

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Zahlen und Mathematik
#
# - Ganze Zahlen: `1`, `837`, `-12`
# - Gleitkommazahlen: `0.5`, `123.4`, `-0.01`
# - Rechenoperationen: 
#     - Addition: `+`
#     - Subtraktion: `-`
#     - Multiplikation: `*`
#     - Division: `/`

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Python als Taschenrechner

# %% {{ doc.codealong() }}
17 + 4

# %% {{ doc.codealong() }}
1 + 4 * 4 + (3 - 1) * (1 + 1)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Arten von Zahlen
#
# - Python unterscheidet ganze Zahlen und Gleitkommazahlen:
#     - `1` ist eine ganze Zahl (`int`)
#     - `1.0` ist eine Gleitkommazahl (`float`)
# - Mit `type(...)` kann man den Typ des Arguments erfahren:

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
type(1)

# %% {{ doc.codealong() }}
type(1.0)

# %% {{ doc.codealong() }}
type("1")

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Ganze Zahlen in Python haben keine (praktisch relevante) Obergrenze:

# %% {"slideshow": {"slide_type": ""}} {{ doc.codealong() }}
10000000000000000000000000000000000000000000000000 + 500

# %% {"slideshow": {"slide_type": ""}} {{ doc.codealong() }}
type(10000000000000000000000000000000000000000000000000)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Mini-Workshop
#
# - Notebook `lecture_010x_Workshop_Einführung_in_Python`
# - Abschnitt "Zahlen und Mathematik"

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
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

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ### Division

# %% {{ doc.codealong() }}
4 / 2

# %% {{ doc.codealong() }}
20 / 7

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
# // und % können zur Division mit Rest verwendet werden:
20 // 7  # Wie oft geht 7 in 20?

# %% {{ doc.codealong() }}
20 % 7  # Welcher Rest bleibt dabei?

# %% {{ doc.codealong() }}
(20 // 7) * 7 + (20 % 7)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# `/` ist links-assoziativ (genau wie `//`, `%`, `+`, `-`, `*`)

# %% {{ doc.codealong() }}
20 / 5 / 2

# %% {{ doc.codealong() }}
# Besser:
(20 / 5) / 2

# %% {{ doc.codealong() }}
20 / (5 / 2)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ### Exponentiation (Potenz)

# %% {{ doc.codealong() }}
2 ** 3

# %% {{ doc.codealong() }}
2 * 2 * 2

# %% {{ doc.codealong() }}
2 ** 4

# %% {{ doc.codealong() }}
2 * 2 * 2 * 2

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# `**` ist rechts-assoziativ
#
# $2^{(2^3)} = 2^8 = 256 \qquad$
# $(2^2)^3 = 4^3 = 64$

# %% {{ doc.codealong() }}
2 ** 2 ** 3

# %% {{ doc.codealong() }}
2 ** (2 ** 3)

# %% {{ doc.codealong() }}
(2 ** 2) ** 3

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Der `**` Operator kann auch zum Wurzelziehen verwendet werden:
#
# $\sqrt{4} = 4^{1/2} = 2\qquad$
# $\sqrt{9} = 9^{1/2} = 3\qquad$
# $\sqrt{2} = 2^{1/2} \approx 1.4142\qquad$

# %% {{ doc.codealong() }}
4 ** 0.5

# %% {{ doc.codealong() }}
9 ** 0.5

# %% {{ doc.codealong() }}
2 ** 0.5

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Variablen
#
# Wir wollen einen Zaun um unser neues Grundstück bauen.
#
# <img src="img/fence.svg" style="display:block;margin:auto;width:50%"/>

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# <img src="img/fence.svg" style="vertical-align:top;overflow:auto;float:right;width:25%"/>
#
# Die gemessenen Längen sind:
# - Birkenweg: 20m
# - Fichtengasse: 30m
#
# Wie lange muss unser Zaun sein?

# %% {{ doc.codealong() }}
20 + 30 + (20 ** 2 + 30 ** 2) ** 0.5

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# <img src="img/fence.svg" style="vertical-align:top;overflow:auto;float:right;width:25%"/>
#
# Die gemessenen Längen sind:
# - Birkenweg: 20m
# - Fichtengasse: 30m
#
# Wie lange muss unser Zaun sein?

# %% {{ doc.codealong() }}
länge_birkenweg = 20
länge_fichtengasse = 30
länge_hauptstr = (länge_birkenweg ** 2 + länge_fichtengasse ** 2) ** 0.5
länge_gesamt = länge_birkenweg + länge_fichtengasse + länge_hauptstr
ergebniss = länge_gesamt

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
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

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# <img src="img/variables-01.svg" style="float:right;margin:auto;width:50%"/>
#
# Einve Variable wird
# - erzeugt durch `name = wert`
# - gelesen durch `name`
# - geändert durch `name = wert`
#
# Erzeugen und Ändern von Variablen<br/>
# sind *Anweisungen*.

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
länge_birkenweg = 20
print(länge_birkenweg)
länge_birkenweg = 25
print(länge_birkenweg)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Eigenschaften von Variablen in Python
#
# - Eine Variable kann Werte mit beliebigem Datentyp speichern
#     - Es gibt keine `int`-Variablen, etc.
#     - Man sagt: Python ist dynamisch getypt
# - Variablen müssen erzeugt worden sein, bevor sie verwendet werden
# - Man kann Variablen neue Werte zuweisen
#     - Dabei kann der *alte Wert* der Variablen auf der rechten Seite verwendet werden:<br/> `jobs = jobs + 1`

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
x = "Hallo!"
print(x)
x = 123
print(x)
x = x + 1
print(x)
x += 1
print(x)

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
# print(diese_variable_gibt_es_nicht)


# %% {{ doc.codealong() }}
# nonono = nonono + 1


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
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

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
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

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
print(__name__)
print(type(__name__))

# %% {{ doc.codealong() }}
# Bitte nicht nachmachen, obwohl es möglich ist:
__my_var__ = 123

# %% {{ doc.codealong() }}
__my_var__

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# - Manchmal werden "private" Variablen mit einem führenden Unterstrich
#   geschrieben: `_my_var`
#     - Das ist (für globale Variablen) besonders in älterem Code verbreitet
#     - In Klassen gibt es weitere Konventionen
# - Die meisten Python-Projekte folgen den Konventionen in
#   [PEP 8](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

# %% {{ doc.codealong() }}
_my_var = 234

# %% {{ doc.codealong() }}
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

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
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
γ = α ** 2 + 3 * β ** 2
print(γ)
αβγ = α * β * γ
print(αβγ)
Σ = 1 + 2 + 3
print(Σ)
# ∑ = 1 + 2 + 3 # Unzulässig!


# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Mini-Workshop
#
# - Notebook `lecture_010x_Workshop_Einführung_in_Python`
# - Abschnitt "Piraten"

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Zuweisung an mehrere Variablen
#
# In Python können mehrere Variablen gleichzeitig definiert bzw. mit neuen
# Werten versehen werden:

# %% {{ doc.codealong() }}
a, b = 1, 2
print(a)
print(b)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Funktionen
#
# Wir haben eine Firma zum Einzäunen dreieckiger Grundstücke gegründet.
#
# Für jedes von Straßen $A$, $B$ und $C$ begrenze Grundstück berechnen wir:

# %%
länge_a = 10  # Beispielwert
länge_b = 40  # Beispielwert
länge_c = (länge_a ** 2 + länge_b ** 2) ** 0.5
länge_gesamt = länge_a + länge_b + länge_c
print(länge_gesamt)


# %% [markdown]
# Können wir das etwas eleganter gestalten?

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Satz von Pythagoras
#
# Wir berechnen die Länge von $C$ aus $A$ und $B$ immer nach dem Satz von
# Pythagoras: $C = \sqrt{A^2 + B^2}$.
#
# Das können wir in Python durch eine *Funktion* ausdrücken:

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
def pythagoras(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c


# %% {{ doc.codealong() }}
pythagoras(3, 4)

# %% {{ doc.codealong() }}
pythagoras(1, 1)


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Funktionsdefinition
# - Schlüsselwort `def`
# - Name der Funktion
# - Parameter der Funktion, in Klammern; Doppelpunkt
# - Rumpf der Funktion, einen Tabulator eingerückt
# - Im Rumpf können die Parameter wie Variablen verwendet werden
# - Schlüsselwort `return`
#     - Beendet die Funktion
#     - Bestimmt welcher Wert zurückgegeben wird

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
def pythagoras(a, b):
    quadratsumme = a ** 2 + b ** 2
    return quadratsumme ** 0.5


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Funktionsaufruf
#
# - Name der Funktion
# - Argumente des Aufrufs, in Klammern
# - Ein Argument für jeden Parameter

# %% {{ doc.codealong() }}
pythagoras(3, 4)


# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Zurück zur Zaunlänge
#
# - Wir haben bis jetzt die Länge der dritten Seite unseres Grundstücks berechnet.
# - Wir brauchen noch eine Funktion, die die Gesamtlänge ausrechnet:

# %% {{ doc.codealong() }}
def gesamtlänge(x, y):
    z = pythagoras(x, y)
    länge = x + y + z
    return länge


# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Damit können wir unser Problem vereinfachen:

# %% {{ doc.codealong() }}
länge_a = 10  # Beispielwert
länge_b = 40  # Beispielwert
print(gesamtlänge(länge_a, länge_b))

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Mini-Workshop
#
# - Notebook `lecture_010x_Workshop_Einführung_in_Python`
# - Abschnitt "Spenden"
#

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Import von Modulen
#
# Ein Großteil der Funktionalität von Python ist nicht direkt im Interpreter
# verfügbar sonder in Module (und Packages) ausgelagert. Mit der `import`
# Anweisung kann man dises Funktionalität verfügbar machen:

# %% {{ doc.codealong() }}
# Zusätzliche mathematische Funktionen:
import math

# %% [markdown] {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
# Auf die Funktionen aus dem `math` Modul kann man dann mit der Syntax
# `math.floor` zugreifen:

# %% {{ doc.codealong() }}
math.floor(2.5)

# %% {{ doc.codealong() }}
math.floor(2.9)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
# Die Funktion `pythagoras` steht im `math`-Modul unter dem Namen `hypot`
# zur Verfügung:

# %% {{ doc.codealong() }}
math.hypot(3, 4)


# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Damit können wir die Funktion `gesamtlänge` ohne die Hilfsfunktion
# `pythagoras` schreiben:

# %% {{ doc.codealong() }}
def gesamtlänge(x, y):
    z = math.hypot(x, y)
    länge = x + y + z
    return länge


# %% {{ doc.codealong() }}
gesamtlänge(3, 4)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Andere Arten von Zahlen
#
# Python bietet noch weitere Arten von Zahlen für spezielle Anwendungen
#
# - Dezimalzahlen mit beliebiger Genauigkeit
# - Komplexe Zahlen
# - Ganze Zahlen mit fixer Größe (z.B. mit `numpy`)
# - Gleitkommazahlen mit unterschiedlicher Größe (`numpy`)

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
1.1 * 100

# %% {{ doc.codealong() }}
import decimal

decimal.Decimal("1.1") * 100

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
(1 + 1j) * (1 + 1j)

# %% {{ doc.codealong() }}
1j * 1j


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Funktionen ohne Argumente
#
# - Eine Funktion kann auch ohne formale Parameter definiert werden.
# - Sowohl bei der Definition, als auch beim Aufruf müssen die Klammern
#   trotzdem angegeben werden.

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
def null():
    return 0


# %% {{ doc.codealong() }}
null()

# %% {{ doc.codealong() }}
# Fehler: 'Aufruf' ohne Klammern
null

# %% {{ doc.codealong() }}
# Fehler: 'Aufruf' ohne Klammern
# plus_eins(null)


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Funktionen mit Seiteneffekten
#
# Funktionene können
#
# - Werte berechnen: `quadratsumme(3, 4)`
# - Seiteneffekte haben: `print("Hans")`

# %% {{ doc.codealong() }}
type(print("Hans"))

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ### Der Wert `None`
#
# Der Rückgabewert der Funktion `print()` ist der spezielle Wert `None`.
# - Jupyter druckt `None` nicht als Wert einer Zelle aus:

# %% {{ doc.codealong() }}
None

# %% {{ doc.codealong() }}
print(None)

# %% {{ doc.codealong() }}
print(print("Hans"))


# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# - Funktionen können Seiteneffekte haben
#     - Z.B. durch Aufruf von `print`
# - Diese werden ausgeführt, wenn ein Funktionsaufruf ausgewertet wird
# - Auch Funktionen mit Seiteneffekten geben einen Wert zurück
#     - Oft ist das der spezielle Wert `None`
#     - Wenn eine Funktion `None` zurückgibt brauchen wir keine explizite `return`-Anweisung

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
def say_hello():
    print("Hello, world!")
    print("Today is a great day!")


# %% {{ doc.codealong() }}
say_hello()


# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Mini-Workshop
#
# - Notebook `lecture_010x_Workshop_Einführung_in_Python`
# - Abschnitt "Piraten, Teil 2"
#

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Default-Argumente
#
# Funktionsparameter können einen Default-Wert haben.
# - Der Default-Wert wird mit der Syntax `parameter=wert` angegeben
# - Wird das entsprechende Argument nicht übergeben so wird der Default-Wert eingesetzt
# - Hat ein Parameter einen Default-Wert, so müssen alle rechts davon stehenden Werte ebenfalls einen haben

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
def add_weighted(a, b=0, c=0):
    return a + 2 * b + 3 * c


# %% {{ doc.codealong() }}
print(add_weighted(2))
print(add_weighted(2, 3))
print(add_weighted(2, 3, 4))


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Vorsicht mit veränderlichen Default-Argumenten

# %% {{ doc.codealong() }}
def append_value(value, my_list=[]):
    my_list.append(value)
    return my_list


# %% {{ doc.codealong() }}
append_value(1)

# %% {{ doc.codealong() }}
append_value(2)


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
#
# Lösung: verwende `Null` als Argument, erzeuge in jedem Aufruf eine neue Liste

# %% {{ doc.codealong() }}
def append_value(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list


# %% {{ doc.codealong() }}
append_value(1)

# %% {{ doc.codealong() }}
append_value(2)


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Aufruf mit benannten Argumenten
#
# Beim Aufruf einer Funktion kann der Parametername in der Form `parameter=wert`
# angegeben werden.
# - Der entsprechende Wert wird dann für den benannten Parameter eingesetzt
# - Werden alle Parameter benannt, so wird der Aufruf unabhängig von der
#   Parameterreihenfolge

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
def say_hi(person, greeting="Hi"):
    print(greeting, " ", person, "!", sep="")


# %% {{ doc.codealong() }}
say_hi("Jill")
say_hi("Jack", "Good morning")

# %% {{ doc.codealong() }}
say_hi(greeting="Heya", person="Betty")


# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
def add_weighted(a, b=0, c=0):
    return a + 2 * b + 3 * c


# %% {"slideshow": {"slide_type": ""}} {{ doc.codealong() }}
add_weighted(c=2, a=1)

# %% {{ doc.codealong() }}
add_weighted(5, c=7)


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Typannotationen
#
# Python erlaubt es die Typen von Funktionsargumenten und den Rückgabetyp einer
# Funktion anzugeben:

# %% {{ doc.codealong() }}
def mult(a: int, b: float) -> float:
    return a * b


# %% {{ doc.codealong() }}
mult(3, 2.0)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Typannotationen dienen lediglich zur Dokumentation und werden von Python ignoriert:

# %% {{ doc.codealong() }}
mult("a", 3)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Typannotationen können parametrische Typen, optionale Typen, etc. enthalten.
# (*Hinweis:* in älteren Python Versionen kann `list` keine Typparameter
# erhalten.)

# %% {{ doc.codealong() }}
from typing import Optional


def my_append(lhs: list[int], rhs: Optional[int]):
    # What exactly does this mean?
    if rhs:
        lhs.append(rhs)


# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
my_list = [1, 2, 3]
my_append(my_list, None)
my_list

# %% {{ doc.codealong() }}
my_append(my_list, 4)
my_list


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Docstrings
#
# Jede Funktion in Python kann dokumentiert werden, indem ein String-Literal als
# erstes Element im Rumpf angegeben wird. Meistens wird dafür ein `"""`-String
# verwendet:

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
def my_fun(x):
    """
    Zeigt dem Benutzer den Wert von x an

    Verwendung:
    >>> my_fun(123)
    """
    print("Das Argument x hat den Wert", x)


# %% {{ doc.codealong() }}
my_fun(123)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Konventionen für Docstrings finden sich in
# [PEP 257](https://www.python.org/dev/peps/pep-0257/).

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Der Docstring einer Funktion kann mit `help()` ausgegeben werden:

# %% {{ doc.codealong() }}
help(my_fun)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# In Jupyter kann man den Docstring einer Funktion durch ein vorangestelltes
# oder nachgestelltes Fragezeichen anzeigen lassen:

# %% {{ doc.codealong() }}
# # ?my_fun


# %% {{ doc.codealong() }}
# # my_fun?


# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Oft verwendet man statt dessen Shift-Tab:

# %% {{ doc.codealong() }}
my_fun

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Bei Funktionen mit langen Docstrings kann man durch zweimaliges Drücken von `Shift-Tab` auf die ausführliche Anzeigeform umschalten:

# %% {{ doc.codealong() }}
my_fun

# %% {{ doc.codealong() }}
print

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Signatur
#
# Die Anzahl, Namen, Default-Werte (und evtl. Typen) einer Funktion nennt man
# ihre *Signatur*.
#
# Jupyter zeigt u.a. die Signatur einer Funktion an, wenn man `Shift-Tab`
# eingibt:

# %% {{ doc.codealong() }}
# Shift-Tab zum Anzeigen der Signatur:
say_hi


# %% {{ doc.codealong() }}
def add_ints(m: int, n: int) -> int:
    return m + n


# %% {{ doc.codealong() }}
add_ints


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Beliebig viele Argumente:
#
# Man kann Funktionen definieren, die beliebig viele Argumente bekommen können:

# %% {{ doc.codealong() }}
def my_add(*args):
    result = 0
    for i in args:
        result += i
    return result


# %% {{ doc.codealong() }}
my_add(1, 2, 3, 4, 5, 6)


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# Das kann auch mit anderen Argumenten kombiniert werden:

# %% {{ doc.codealong() }}
def add_more_than_two(x, y, *more_args):
    result = x + y
    for i in more_args:
        result += i
    return result


# %% {"slideshow": {"slide_type": "slide"}} {{ doc.codealong() }}
add_more_than_two(1, 2, 3, 4, 5, 6)

# %% {{ doc.codealong() }}
add_more_than_two(1, 2)


# %% {{ doc.codealong() }}
# add_more_than_two(1)

# %% [markdown]
# ## Beliebig viele benannte Argumente:
#
# Ebenso kann eine Funktion beliebig viele benannte Argumente haben:

# %% {{ doc.codealong() }}
def my_keys(**kwargs):
    print("Keyword arguments:", kwargs)


# %% {{ doc.codealong() }}
my_keys(x=1, y=2)


# %% [markdown]
# Es ist möglich diese beiden Features zu kombinieren:

# %% {{ doc.codealong() }}
def takes_arbitrary_args(*args, **kwargs):
    print("Positional argsuments:", args)
    print("Keyword arguments:    ", kwargs)


# %% {{ doc.codealong() }}
takes_arbitrary_args(1, "foo", a="alpha", b="beta")


# %% [markdown]
# ## "Splicing" von Argumenten
#
# - Wenn man eine Liste `args` hat, kann man die darin enthaltenen Werte mit
#   der Syntax `*args` als positionale Argumente übergeben.
# - Wenn man ein Dictionary `kwargs` hat, kann man die Key/Value-Paare mit der
#   Syntax `**kwargs` als benannte Argumente übergeben:

# %% {{ doc.codealong() }}
def add(x, y):
    return x + y


# %% {{ doc.codealong() }}
my_list = [3, 4]

# %% {{ doc.codealong() }}
# add(my_list)

# %% {{ doc.codealong() }}
add(my_list[0], my_list[1])

# %% {{ doc.codealong() }}
add(*my_list)

# %% {{ doc.codealong() }}
my_dict = {"a": "alpha", "b": "beta"}

# %% {{ doc.codealong() }}
takes_arbitrary_args(my_list, my_dict)

# %% {{ doc.codealong() }}
takes_arbitrary_args(*my_list, **my_dict)

# %% {{ doc.codealong() }}
takes_arbitrary_args(3, 4, a="alpha", b="beta")

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Mehrere Rückgabewerte
#
# Wie oben gezeigt kann man mehrere Variablen in einem Schritt definieren:

# %% {{ doc.codealong() }}
ergebnis, rest = 10, 2

# %% {{ doc.codealong() }}
print(ergebnis)
print(rest)


# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# - Besonders hilfreich ist das für Funktionen die mehrere eng zusammenhängende
#   Werte berechnen.
# - Man kann mit `return wert1, wert2` mehrere Werte zurückgeben

# %% {{ doc.codealong() }}
def zwei_werte(a, b):
    return a + 1, b + 2


# %% {{ doc.codealong() }}
erster_wert, zweiter_wert = zwei_werte(1, 2)
print(erster_wert)
print(zweiter_wert)


# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
def division_mit_rest(m, n):
    ergebnis = m // n
    rest = m % n
    return ergebnis, rest


# %% {{ doc.codealong() }}
e, r = division_mit_rest(17, 7)
print(e)
print(r)


# %% {"slideshow": {"slide_type": ""}} {{ doc.codealong() }}
# Kürzer
def division_mit_rest_2(m, n):
    return m // n, m % n


# %% {{ doc.codealong() }}
e, r = division_mit_rest_2(17, 7)
print(e)
print(r)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# (In Python gibt es die eingebaute Funktion `divmod`, die diese Berechnung
# ausführt:)

# %% {{ doc.codealong() }}
e, r = divmod(17, 7)
print(e)
print(r)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Mini-Workshop
#
# - Notebook `lecture_010x_Workshop_Einführung_in_Python`
# - Abschnitt "Piraten, Teil 3"
