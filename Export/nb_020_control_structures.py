#!/usr/bin/env python
# coding: utf-8

# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <h1 style="text-align:center;">Python: Kontrollstrukturen<br/><br/>
# Mit Exkursen in Vererbung, Ausnahmebehandlung und Dateien</h1>
# <h2 style="text-align:center;">Coding Akademie München GmbH</h2>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <div style="text-align:center;">Allaithy Raed</div>

# # Namensräume
# 
# Variablen und Funktionsnamen existieren in einem *Namensraum (Namespace)*.
# 
# - Globale Variablen und Funktionsnamen sind im globalen Namensraum.
# - Mit `import` importierte Namen existieren im importierten Namensraum.
# - Namen, die innerhalb einer Funktion definiert werden sind im Namensraum dieser Funktion.
#     - Parameter
#     - lokale Variablen
# 
# Der Namensraum einer Funktion "verschwindet" am Ende des Rumpfs.

# In[1]:


# Ohne Angabe der Namensräume, siehe nächste Folie
a = 1
def f(x):
    # print(a) # Was passiert, wenn diese Zeile einkommentiert wird?
    a = x + 1
    print(a)
f(2)
print(a)
# print(x)


# In[2]:


a = 1                   # Globaler Namespace
def f(x):               # Namespace von f - x ist im globalen Namespace *nicht* sichtbar
    a = x + 1           # Namespace von f - a ist im globalen Namespace *nicht* sichtbar
    print(a)            # Greift auf a aus dem Namespace von f zu
f(2)
print(a)                # Greift auf a aus dem globalen Namespace zu
# print(x)              # Fehler: x ist im Namespace von f


# In[3]:


a = 1
def f2():
    global a
    a = 4
    print(a)
f2()
print(a)
a = 5
print(a)


# # `if`-Anweisung
# 
# Wiederholung:

# In[4]:


def ist_glückszahl(zahl):
    print("Ist", zahl, "eine Glückszahl?")
    if zahl == 7:
        print("Ja!")
    else:
        print("Leider nein.")
    print("Wir wünschen Ihnen alles Gute.")


# ## Mini-Workshop
# 
# - Notebook `020x-Workshop Kontrollstrukturen`
# - Abschnitt "Gerade Zahl"
# 

# ## Mehrere Zweige
# 
# - Wir wollen ein Spiel schreiben, in dem der Spieler eine Zahl zwischen 1 und 100 erraten muss.
# - Nachdem er geraten hat, bekommt er die Information, ob seine Zahl zu hoch, zu niedrig oder richtig war angezeigt.
# - Später wollen wir dem Spieler mehrere Versuche erlauben.

# In[5]:


def klassifiziere_zahl(geratene_zahl, lösung):
    if geratene_zahl < lösung:
        print("Die geratene Zahl ist zu klein!")
    elif geratene_zahl > lösung:
        print("Die geratene Zahl ist zu groß!")
    else:
        print("Sie haben gewonnen!")


# In[6]:


klassifiziere_zahl(10, 12)


# In[7]:


klassifiziere_zahl(14, 12)


# In[8]:


klassifiziere_zahl(12, 12)


# ## Mini-Workshop
# 
# - Notebook `020x-Workshop Kontrollstrukturen`
# - Abschnitt "Positiv/Negativ"
# 

# ## Struktur einer `if`-Anweisung (vollständig):
# 
# ```python
# if <Bedingung 1>:
#     Rumpf, der ausgeführt wird, wenn Bedingung 1 wahr ist
# elif <Bedingung 2>:
#     Rumpf, der ausgeführt wird, wenn Bedingung 2 wahr ist
# ...
# else:
#     Rumpf, der ausgeführt wird, wenn keine der Bedingungen wahr ist
# ```
# - Nur das `if` und der erste Rumpf sind notwendig
# - Falls ein `elif` oder ein `else` vorhanden ist, so darf der entsprechende Rumpf nicht leer sein

# ### Bessere Klassifizierung
# 
# Wir wollem dem Spieler etwas mehr Information geben, wie nahe er an der richtigen Lösung ist:
# 
# - Die geratene Zahl ist viel zu klein/zu groß wenn der Unterschied größer als 10 ist

# In[9]:


def klassifiziere_zahl_2(geratene_zahl, lösung):
    if geratene_zahl < lösung - 10:
        print("Die geratene Zahl ist viel zu klein!")
    elif geratene_zahl < lösung:
        print("Die geratene Zahl ist zu klein!")
    elif geratene_zahl > lösung + 10:
        print("Die geratene Zahl ist viel zu groß!")
    elif geratene_zahl > lösung:
        print("Die geratene Zahl ist zu groß!")
    else:
        print("Sie haben gewonnen!")


# In[10]:


klassifiziere_zahl_2(1, 12)


# In[11]:


klassifiziere_zahl_2(10, 12)


# In[12]:


klassifiziere_zahl_2(14, 12)


# In[13]:


klassifiziere_zahl_2(24, 12)


# In[14]:


klassifiziere_zahl_2(12, 12)


# Die Reihenfolge der `if`- und `elif`-Zweige ist wichtig:

# In[15]:


def klassifiziere_zahl_3(geratene_zahl, lösung):
    if geratene_zahl < lösung:
        print("Die geratene Zahl ist zu klein!")  
    elif geratene_zahl < lösung - 10:
        print("Die geratene Zahl ist viel zu klein!")
    elif geratene_zahl > lösung:
        print("Die geratene Zahl ist zu groß!")
    elif geratene_zahl > lösung + 10:
        print("Die geratene Zahl ist viel zu groß!")
    else:
        print("Sie haben gewonnen!")


# In[16]:


klassifiziere_zahl_3(1, 12)


# In[17]:


klassifiziere_zahl_3(100, 12)


# ## Return aus einem `if`-Statement
# 
# Die Zweige eines `if`-Statements können `return` Anweisungen enthalten um einen Wert aus einer Funktion zurückzugeben:

# In[18]:


def ist_große_zahl(zahl):
    if zahl > 10:
        return True
    else:
        return False


# Es können auch mehrere Werte aus einem `if`-Statement zurückgegeben werden:

# In[19]:


def klassifiziere_zahl_4(geratene_zahl, lösung):
    if geratene_zahl < lösung:
        return False, "Die geratene Zahl ist zu klein!"
    elif geratene_zahl > lösung:
        return False, "Die geratene Zahl ist zu groß!"
    else:
        return True, "Sie haben gewonnen!"


# In[20]:


gewonnen, text = klassifiziere_zahl_4(1, 10)
print(gewonnen)
print(text)


# In[21]:


gewonnen, text = klassifiziere_zahl_4(15, 10)
print(gewonnen)
print(text)


# In[22]:


gewonnen, text = klassifiziere_zahl_4(10, 10)
print(gewonnen)
print(text)


# ## Mini-Workshop
# 
# - Notebook `020x-Workshop Kontrollstrukturen`
# - Abschnitt "Signum"
# 

# # Benutzereingaben
# 
# - Die Funktion `input()` erlaubt es dem Benutzer einen Text einzugeben.
# - Optional kann sie einen Eingabeprompt ausgeben.
# - Die Funktion gibt den vom Benutzer eingegebenen Text als String zurück.

# In[23]:


# input("What is your name? ")


# In[24]:


def query_name():
    name = input("What is your name? ")
    print(f"You entered {name}")


# In[25]:


# query_name()


# ## Beispiel: Konvertierung von Temperaturen
# 
# Wir wollen eine Anwendung schreiben, die den Benutzer nach einer Temperatur in Fahrenheit fragt und die entsprechende Temperatur in Grad Celsius zurückgibt.

# In[26]:


def konvertiere_fahrenheit_nach_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# In[27]:


konvertiere_fahrenheit_nach_celsius(32)


# In[28]:


konvertiere_fahrenheit_nach_celsius(90)


# In[29]:


def temperaturkonverter_1():
    fahrenheit = input("Bitte geben Sie die Temperatur in Fahrenheit ein: ")
    celsius = konvertiere_fahrenheit_nach_celsius(float(fahrenheit))
    print(f"{fahrenheit}F sind {celsius}°C")


# In[30]:


float('1.23')


# In[31]:


# temperaturkonverter_1()


# In[32]:


def temperaturkonverter_2():
    fahrenheit = input("Bitte geben Sie die Temperatur in Fahrenheit ein: ")
    if fahrenheit != "":
        celsius = konvertiere_fahrenheit_nach_celsius(float(fahrenheit))
        print(f"{fahrenheit}F sind {celsius}°C")
    else:
        print("Bitte geben Sie eine gültige Temperatur ein.")


# In[33]:


# temperaturkonverter_2()


# ## Mini-Workshop
# 
# - Notebook `020x-Workshop Kontrollstrukturen`
# - Abschnitt "Umrechnung in Meilen"
# 

# In[34]:


def temperaturkonverter_3():
    fahrenheit = input("Bitte geben Sie die Temperatur in Fahrenheit ein: ")
    if fahrenheit:
        celsius = konvertiere_fahrenheit_nach_celsius(float(fahrenheit))
        print(f"{fahrenheit}F sind {celsius}°C")
    else:
        print("Bitte geben Sie eine gültige Temperatur ein.")


# In[35]:


# temperaturkonverter_3()


# # Wahrheitswerte: Truthiness
# 
# Die `if`-Anweisung kann als Argument beliebige Python-Werte bekommen, nicht nur Boole'sche Werte.
# 
# Folgende Werte gelten als *nicht wahr*
# 
# - `None` und `False`
# - `0` und `0.0` (und Null-Werte von anderen Zahlentypen)
# - Leere Strings, Sequences und Collections: ``
# 
# Alle anderen Werte gelten als wahr.

# In[36]:


if -1:
    print("-1 ist wahr")
elif 0:
    print("0 ist wahr")
else:
    print("Alles ist falsch")


# In[37]:


if 0:
    print("0 ist wahr")
else:
    print("0 ist falsch")


# In[38]:


if '':
    print("'' ist wahr")
else:
    print("'' falsch")


# In[39]:


if print("Hallo"):
    print("None ist wahr")
else:
    print("None ist falsch")


# ## Mini-Workshop
# 
# - Notebook `020x-Workshop Kontrollstrukturen`
# - Abschnitt "Umrechnung in Meilen mit Truthiness"
# 

# ## Mini-Workshop
# 
# - Notebook `020x-Workshop Kontrollstrukturen`
# - Abschnitt "Kino-Preis"
# 

# ## Hinweis: Umwandeln eines Strings in Kleinbuchstaben

# In[40]:


text = "Das ist ein Text"
print(text.lower())
print(text)


# In[41]:


"Das ist ein Text".upper()


# ## Mini-Workshop
# 
# - Notebook `020x-Workshop Kontrollstrukturen`
# - Abschnitt "Shout"
# 

# # While-Schleifen
# 
# Manchmal wollen wir einen Teil eines Programms immer wieder ausführen:
# 
# - Zahlenraten bis die richtige Zahl gefunden wurde
# - Physik-Simulation bis das Ergebnis genau genug ist
# - Verarbeitung von Benutzereingaben in interaktiven Programmen
# 
# Wenn wir die Anzahl der Wiederholungen nicht von vornherein wissen, verwenden wir dafür in der Regel eine While-Schleife.

# In[42]:


number = 0
while number < 3:
    print(f"Durchlauf {number}")
    number += 1 # <==


# In[43]:


def führe_ein_experiment_aus(versuch_nr):
    """Führt ein Experiment aus
    Gibt True zurück wenn das Experiment erfolgreich war, andernfalls False.
    """
    print(f"Versuch Nr. {versuch_nr} gestartet...", end='')
    from random import random
    if random() > 0.8:
        print("Erfolg!")
        return True
    else:
        print("Fehlschlag.")
        return False


# In[44]:


versuch_nr = 0

while not führe_ein_experiment_aus(versuch_nr):
    versuch_nr += 1

print("Wir haben einen erfolgreichen Versuch ausgeführt.")


# ## Beenden von Schleifen
# 
# Manchmal ist es leichter, die Abbruchbedingung einer Schleife im Rumpf zu bestimmen, statt am Anfang. Mit der Anweisung `break` kann man eine Schleife vorzeitig beenden:

# In[45]:


i = 1
while i < 10:
    print(i)
    if i % 3 == 0:
        break
    i += 1
print("Nach der Schleife:", i)


# In[46]:


def annoy_user():
    while True:
        text = input("Say hi! ")
        if text.lower() == "hi":
            break
        else:
            print("You chose", text)


# In[47]:


# annoy_user()


# ## Mini-Workshop
# 
# - Notebook `020x-Workshop Kontrollstrukturen`
# - Abschnitt "Ratespiele"
# 

# # Vererbung

# In[48]:


import random
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x:.1f}, {self.y:.1f})"

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
    
    def randomize(self):
        self.x = random.gauss(2, 4)
        self.y = random.gauss(3, 2)


# In[49]:


p = Point(0, 0)
p


# In[50]:


p.move(2, 3)
p


# In[51]:


p.randomize()
p


# In[52]:


class ColorPoint(Point):
    def __init__(self, x=0, y=0, color='black'):
        super().__init__(x, y)
        self.color = color
    
    def __repr__(self):
        return f"ColorPoint({self.x:.1f}, {self.y:.1f}, {self.color!r})"

    def randomize(self):
        super().randomize()
        self.color = random.choice(["black", "red", "green", "blue", "yellow", "white"])


# In[53]:


cp = ColorPoint(2, 3, 'red')
cp


# In[54]:


cp.move(2, 3)
cp


# In[55]:


cp.randomize()
cp


# ## Mini-Workshop
# 
# - Notebook `020x-Workshop Kontrollstrukturen`
# - Abschnitt "Vererbung"
# 

# # Fehlerbehandlung
# 
# Wir wollen eine Funktion `int_sqrt(n: int) -> int` schreiben, die die "Ganzzahlige Wurzel" berechnet:
# - Wenn `n` eine Quadratzahl ist, also die Form `m * m` hat, dann soll `m` zurückgegeben werden.
# - Was machen wir, falls `n` keine Quadratzahl ist?
# 
# Einige Lösungsversuche:

# In[56]:


def int_sqrt_with_pair(n: int) -> (int, bool):
    for m in range(n + 1):
        if m * m == n:
            return m, True
    return 0, False


# In[57]:


int_sqrt_with_pair(9)


# In[58]:


int_sqrt_with_pair(8)


# In[59]:


int_sqrt_with_pair(0)


# In[60]:


int_sqrt_with_pair(1)


# In[61]:


def print_int_sqrt_1(n):
    root, is_valid = int_sqrt_with_pair(8)
    print(f"The root of {n} is {root}.")

print_int_sqrt_1(8)


# In[62]:


def int_sqrt_with_negative_value(n: int) -> int:
    for m in range(n + 1):
        if m * m == n:
            return m
    return -1


# In[63]:


int_sqrt_with_negative_value(9)


# In[64]:


int_sqrt_with_negative_value(8)


# In[65]:


def print_int_sqrt_2(n):
    root = int_sqrt_with_negative_value(8)
    print(f"The root of {n} is {root}.")

print_int_sqrt_2(8)


# In[66]:


def print_int_sqrt_2_better(n):
    root = int_sqrt_with_negative_value(8)
    if root < 0:
        print(f"{n} does not have a root!")
    else:
        print(f"The root of {n} is {root}.")

print_int_sqrt_2_better(8)


# Beide Ansätze haben mehrere Probleme:
# - Die Fehlerbehandlung ist optional. Wird sie nicht durchgeführt, so wird mit einem falschen Wert weitergerechnet.
# - Kann der Aufrufer den Fehler nicht selber behandeln, so muss der Fehler über mehrere Ebenen von Funktionsaufrufen "durchgereicht" werden. Das führt zu unübersichtlichem Code, da der "interessante" Pfad nicht vom Code zur Fehlerbehandlung getrennt ist.
# 
# Eine bessere Lösung:

# In[67]:


def int_sqrt(n: int) -> int:
    for m in range(n + 1):
        if m * m == n:
            return m
    raise ValueError(f"{n} is not a square number.")


# In[68]:


int_sqrt(9)


# In[69]:


int_sqrt(0)


# In[70]:


int_sqrt(1)


# In[71]:


# int_sqrt(8)


# In[ ]:


def print_int_sqrt(n):
    root = int_sqrt(n)
    print(f"The root of {n} is {root}.")


# In[73]:


# print_int_sqrt(8)


# In[74]:


def print_int_sqrt_no_error(n):
    try:
        root = int_sqrt(n)
        print(f"The root of {n} is {root}.")
    except ValueError as error:
        print(str(error))


# In[75]:


print_int_sqrt_no_error(9)


# In[76]:


print_int_sqrt_no_error(8)


# In[77]:


def print_int_sqrt_no_error_2(n):
    try:
        root = int_sqrt(n)
        print(f"The root of {n} is {root}.")
    except ValueError:
        print(f"{n} does not have a root!")
    finally:
        print("And that's all there is to say about this topic.")


# In[78]:


print_int_sqrt_no_error_2(9)


# In[79]:


print_int_sqrt_no_error_2(8)


# ## Fehlerklassen
# 
# In Python gibt es viele vordefinierte Fehlerklassen, mit denen verschiedene Fehlerarten signalisiert werden können:
# - `Exception`: Basisklasse aller behandelbaren Exceptions
# - `ArithmeticError`: Basisklasse aller Fehler bei Rechenoperationen:
#   - OverflowError
#   - ZeroDivisionError
# - `LookupError`: Basisklasse wenn ein ungültiger Index für eine Datenstruktur verwendet wurde
# - `AssertionError`: Fehlerklasse, die von `assert` verwendet wird
# - `EOFError`: Fehler wenn `intput()` unerwartet das Ende einer Datei erreicht
# - ...
# 
# Die Liste der in der Standardbibliothek definierten Fehlerklassen ist [hier](https://docs.python.org/3/library/exceptions.html).

# In[80]:


class NoRootError(ValueError):
    pass


# In[81]:


try:
    raise ValueError("ValueError")
    # raise NoRootError("This is a NoRootError.")
except NoRootError as error:
    print(f"Case 1: {error}")
except ValueError as error:
    print(f"Case 2: {error}")


# In[82]:


my_var = 1
assert my_var == 1


# ## Mini-Workshop
# 
# - Notebook `020x-Workshop Kontrollstrukturen`
# - Abschnitt "Knobeln"
# 

# # Dateien
# 
# Bislang gehen am Ende der Programmausführung alle Daten, die wir berechnet haben verloren.
# 
# Die einfachste Varianten Daten zu persistieren ist sie in einer Datei zu speichern:

# In[83]:


import os


# In[84]:


os.getcwd()


# - Mit `open()` kann eine Datei zum Lesen oder Schreiben geöffnet werden.
# - Der `mode` Parameter gibt an, ob die Datei zum Lesen oder Schreiben geöffnet wird:
#   - `r`: Lesen
#   - `w`: Schreiben. Der Inhalt der Datei wird gelöscht
#   - `a`: Schreiben. Die neuen Daten werden ans Ende der Datei geschrieben.
#   - `x`: Schreiben. Die Datei darf nicht existieren.
#   - `r+`: Lesen und Schreiben.
# - Wird ans Ende von `mode` der Buchstabe `b` angehängt, so wird die Datei als Binärdatei behandelt.
# - Mit den Methoden `tell()` und `seek()` kann die Position in der Datei abgefragt oder verändert werden.

# In[85]:


file = open('my-data-file.txt', 'w')
file.write("The first line.\n")
file.write("The second line.\n")
file.close()


# In[86]:


file = open('my-data-file.txt', 'r')
contents = file.read()
print(contents)
file.close()
contents


# In[87]:


file = open('my-data-file.txt', mode='w')
file.write("Another line.\n")
file.write("Yet another line.\n")
file.close()


# In[88]:


file = open('my-data-file.txt', mode='r')
contents = file.read()
print(contents)
file.close()


# In[89]:


file = open('my-data-file.txt', mode='a')
file.write("Let's try this again.\n")
file.write("Until we succeed.\n")
file.close()


# In[90]:


file = open('my-data-file.txt', 'r')
contents = file.read()
print(contents)
file.close()


# Dateien müssen immer mit `close` geschlossen werden, auch wenn der Programmteil, in dem die Datei verwendet wird durch eine Exception verlassen wird. Das könnte mit `try ... finally` erfolgen.
# 
# Python bietet dafür ein eleganteres Konstrukt:

# In[91]:


with open('my-data-file.txt', 'r') as file:
    contents = file.read()
print(contents)


# In[92]:


with open('my-data-file.txt', 'r+') as file:
    print(f"File position before reading: {file.tell()}")
    contents = file.read()
    print(f"File position after reading: {file.tell()}")
    file.write('Another line.\nAnd another.')
    print(f"File position after writing: {file.tell()}")   


# In[93]:


with open('my-data-file.txt', 'r+') as file:
    print(f"File has {len(file.readlines())} lines.")
    file.seek(40)
    file.write('overwrite a part of the file, yes?')
    file.seek(0)
    print(file.read())


# ## Mini-Workshop
# 
# - Notebook `020x-Workshop Kontrollstrukturen`
# - Abschnitt "# Lesen und Schreiben in Dateien"
# 

# # Context Managers
# 
# Context Manager sind Objekte, die häufig verwendete `try-except-finally` Patterns für `with`-Blöcke kapseln.

# In[262]:


from contextlib import AbstractContextManager
import sys

class ProgressNotifier(AbstractContextManager):
    def __init__(self, entry_message, width=72):
        self.entry_message = entry_message
        self.width = width
        self.num_completed_items = 0

    def __enter__(self):
        print(f"{self.entry_message}")
        sys.stdout.flush()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print("failed!")
        else:
            print("done.")

    def item_completed(self):
        self.num_completed_items += 1
        print(".", end='\n' if self.num_completed_items % self.width == 0 else '')
        sys.stdout.flush()

    def item_skipped(self):
        self.num_completed_items += 1
        print("-", end='\n' if self.num_completed_items % self.width == 0 else '')
        sys.stdout.flush()


def progress(entry_message):
    return ProgressNotifier(entry_message)


# In[283]:


import random

def download_items(n):
    with progress("Downloading articles") as p:
        for i in range(n):
            r = random.random()
            if r < 0.001:
                raise IOError("Download failed")
            elif r < 0.1:
                p.item_skipped()
            else:
                p.item_completed()


# In[315]:


try:
    download_items(500)
    print("Finished successfully")
except IOError:
    print("Caught IOError")

