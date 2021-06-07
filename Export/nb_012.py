#!/usr/bin/env python
# coding: utf-8

# # Vergleiche, Boole'sche Werte

# Gleichheit von Werten wird mit `==` getestet:

# In[1]:


1 == 1


# In[2]:


1 == 2


# Das Ergebnis eines Vergleichs ist ein Boole'scher Wert (Wahrheitswert)
# 
# - `True`
# - `False`

# In[3]:


type(True)


# ## Gleichheit von Zahlen

# In[4]:


1 == 1.0


# In[5]:


0.000_000_1 * 10_000_000 == 1


# Vorsicht: Rundungsfehler!

# In[6]:


(2 ** 0.5) ** 2 == 2


# In[7]:


(2 ** 0.5) ** 2


# ## Ungleichheit von Zahlen
# 
# Der Operator `!=` testet, ob zwei Zahlen verschieden sind

# In[8]:


1 != 1.0


# In[9]:


1 != 2


# ## Vergleich von Zahlen

# In[10]:


1 < 2


# In[11]:


1 < 1


# In[12]:


1 <= 1


# In[13]:


1 > 2


# In[14]:


2 >= 1


# ## Vergleichsoperatoren auf anderen Typen
# 
# Die Vergleichsoperatoren lassen sich auch auf viele andere Typen anwenden
# (genaueres später).

# ## Operatoren auf Boole'schen Werten
# 

# In[15]:


1 < 2 and 3 < 2


# In[16]:


1 < 2 or 3 < 2


# In[17]:


not (1 < 2)


# ### Wann ist ein logischer Ausdruck wahr?
# 
# | Operator | Operation                      | `True` wenn...                 |
# |:--------:|:-------------------------------|:-------------------------------|
# | and      | logisches "Und" (Konjunktion)  | beide Argumente `True`         |
# | or       | logisches "Oder" (Disjunktion) | mindestens ein Argument `True` |
# | not      | logisches "Nicht" (Negation)   | Argument `False`               |

# ### Verkettung von Vergleichen

# In[18]:


1 < 2 < 3


# In[19]:


1 < 2 and 2 < 3


# In[20]:


1 < 3 <= 2


# In[21]:


1 < 3 and 3 <= 2


# ## Mini-Workshop
# 
# - Notebook `012x-Workshop Einführung in Python (Teil 2)`
# - Abschnitt "Operatoren, Vergleiche"

# # `if`-Anweisungen
# 
# - Wir wollen ein Programm schreiben, das bestimmt ob eine Zahl eine Glückszahl ist oder nicht:
#     - 7 ist eine Glückszahl
#     - Alle anderen Zahlen sind es nicht.
# - Mit den Python-Konstrukten, die wir bis jetzt kennen können wir das nicht machen.
# - Wir benötigen dazu die `if`-Anweisung:

# In[22]:


def ist_glückszahl(zahl):
    print("Ist", zahl, "eine Glückszahl?")
    if zahl == 7:
        print("Ja!")
    else:
        print("Leider nein.")
    print("Wir wünschen Ihnen alles Gute.")


# In[23]:


ist_glückszahl(1)


# In[24]:


ist_glückszahl(7)


# In[25]:


def ist_glückszahl_2(zahl):
    if zahl == 7:
        print(zahl, "ist eine Glückszahl!")
        print("Sie haben sicher einen super Tag!")
    else:
        print(zahl, "ist leider keine Glückszahl.")
        print("Vielleicht sollten Sie heute lieber im Bett bleiben.")
        print("Wir wünschen Ihnen trotzdem alles Gute.")


# In[26]:


ist_glückszahl_2(1)


# In[27]:


ist_glückszahl_2(7)


# In[28]:


def einseitiges_if_1(zahl):
    print("Vorher")

    if zahl == 7:
        print(zahl, "ist eine Glückszahl")
        print("Glückwunsch!")

    print("Nachher")


# In[29]:


einseitiges_if_1(1)


# In[30]:


einseitiges_if_1(7)


# In[31]:


def einseitiges_if_2(zahl):
    if zahl % 2 != 0:
        zahl += 1         # zahl = zahl + 1
    print(zahl)


# In[32]:


einseitiges_if_2(1)


# In[33]:


einseitiges_if_2(6)


# ## Struktur einer `if`-Anweisung (unvollständig):
# 
# ```python
# if <Bedingung>:
#     Rumpf, der ausgeführt wird, wenn Bedingung 1 wahr ist
# else:
#     Rumpf, der ausgeführt wird, wenn keine der Bedingungen wahr ist
# ```
# - Nur das `if` und der erste Rumpf sind notwendig
# - Falls ein `else` vorhanden ist, so darf der entsprechende Rumpf nicht leer sein
# 

# ## Mini-Workshop
# 
# - Notebook `012x-Workshop Einführung in Python (Teil 2)`
# - Abschnitt "Volljährig"

# # Listen
# 
# - Bisher haben wir nur die Möglichkeit einzelne Werte in Variablen zu speichern:

# In[34]:


produkt_1 = "Haferflocken"
produkt_2 = "Kaffeebohnen"
produkt_3 = "Orangenmarmelade"


# - Probleme damit:
#     - Außer den Variablennamen deutet nichts darauf hin, dass diese Werte z.B. zu einem Warenkorb gehören.
#     - Wir können nur eine fest vorgegebene Anzahl von Werten speichern.
#     - Es ist sehr schwer
#         - die Werte nach verschiedenen Kriterien zu sortieren
#         - Werte hinzuzufügen
#         - Werte zu löschen
#         - die Anzahl der Werte zu bestimmen
#         - ...

# - Wir brauchen einen Datentyp, der es uns erlaubt mehrere "Dinge" zusammenzufassen.
# - In Python verwendet man häufig Listen um das zu erreichen.

# In[35]:


warenkorb = ["Haferflocken", "Kaffeebohnen", "Orangenmarmelade"]


# In[36]:


type(warenkorb)


# ## Erzeugen von Listen
# 
# - Listen werden erzeugt, indem man ihre Elemente in eckige Klammern einschließt.
# - Die Elemente einer Liste können beliebige Python-Werte sein.
# - Eine Liste kann Elemente mit verschiedenen Typen enthalten.

# In[37]:


liste_1 = [1, 2, 3, 4, 5]
liste_2 = ["string1", "another string"]


# In[38]:


print(liste_1)


# In[39]:


print(liste_2)


# In[40]:


liste_3 = []
liste_4 = [1, 0.4, "ein String", True, None]


# In[41]:


print(liste_3)


# In[42]:


print(liste_4)


# Die Elemente einer Liste müssen keine Literale sein, man kann auch Werte von Variablen in einer Liste speichern:

# In[43]:


produkt_1 = "Haferflocken"
produkt_2 = "Kaffeebohnen"
produkt_3 = "Orangenmarmelade"
warenkorb = [produkt_1, produkt_2, produkt_3, "Erdbeermarmelade"]


# In[44]:


warenkorb


# Der Typ von Listen ist `list`.

# In[45]:


type([1, 2, 3])


# Mit der Funktion `list` können manche andere Datentypen in Listen umgewandelt werden.
# 
# Im Moment kennen wir nur Listen und Strings als mögliche Argumenttypen:

# In[46]:


list("abc")


# In[47]:


list([1, 2, 3])


# ## Zugriff auf Listenelemente

# In[48]:


zahlenliste = [0, 1, 2, 3]


# In[49]:


zahlenliste[0]


# In[50]:


zahlenliste[3]


# In[ ]:


zahlenliste[-1]


# ## Länge einer Liste

# In[51]:


zahlenliste


# In[52]:


len(zahlenliste)


# ## Modifikation von Listeneinträgen

# In[53]:


zahlenliste[1] = 10
zahlenliste


# In[ ]:





# ## Anhängen von Elementen an eine Liste

# In[54]:


zahlenliste.append(40)
zahlenliste


# ## Iteration über Listen
# 
# In Python kann man mit der `for`-Schleife über Listen iterieren.
# 
# Die `for`-Schleife entspricht dem range-based for aus C++,
# `for-in`/`for-of` aus JavaScript oder der `for-each`-Schleife
# aus Java, nicht der klassischen `for`-Schleife
# aus C, C++ oder Java.

# In[66]:


zahlenliste


# In[55]:


for zahl in zahlenliste:
    print("Die Zahl ist:", zahl)


# ## Syntax der `for`-Schleife
# 
# ```python
# for <element-var> in <liste>:
#     <rumpf>
# ```

# ## Workshop
# 
# - Notebook `012x-Workshop Einführung in Python (Teil 2)`
# - Abschnitt "Einkaufsliste"

# ## Simulation der klassischen `for`-Schleife
# 
# Iteration mit einer `for`-Schleife ist auch über andere Datenstrukturen als Listen möglich.
# 
# In Python stellt der Typ `range` eine Folge von ganzen Zahlen dar:
# 
# - `range(n)` erzeugt das ganzzahlige Interval von $0$ bis $n-1$
# - `range(m, n)` erzeugt das ganzzahlige Interval von $m$ bis $n-1$
# - `range(m, n, k)` erzeugt die ganzzahlige Sequenz $m, m+k, m+2k, ..., p$, wobei $p$ die größte Zahl der Form $m + jk$ mit $j \geq 0$ und $p < n$ ist

# In[56]:


range(3)


# In[57]:


list(range(3))


# In[58]:


list(range(3, 23, 5))


# In[59]:


for i in range(3):
    print(i)


# ## Mini-Workshop
# 
# - Notebook `012x-Workshop Einführung in Python (Teil 2)`
# - Abschnitt "Ausgabe von Quadratzahlen"

# # Umwandlung in Strings
# 
# Python bietet zwei Funktionen an, mit denen beliebige Werte in Strings umgewandelt
# werden können:
# 
# - `repr` für eine "programmnahe" Darstellung (wie könnte der Wert im Programm erzeugt werden)
# - `str` für eine "benutzerfreundliche" Darstellung

# In[60]:


print(str("Hallo!"))


# In[61]:


print(repr("Hallo!"))


# Für manche Datentypen liefern `str` und `repr` den gleichen String zurück:

# In[62]:


print(str(['a', 'b', 'c']))
print(repr(['a', 'b', 'c']))


# # Benutzerdefinierte Datentypen
# 
# In Python können benutzerdefinierte Datentypen definiert werden:

# In[63]:


class PointV0:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# In[64]:


p = PointV0(2, 3)
p


# In[65]:


print("x =", p.x)
print("y =", p.y)


# ## Methoden
# 
# Klassen können Methoden enthalten. Im Gegensatz zu vielen anderen Sprachen hat
# Python bei der Definition keinen impliziten `this` Parameter; das Objekt auf dem
# die Methode aufgerufen wird muss als erster Parameter angegeben werden.
# 
# Per Konvention hat dieser Parameter den Namen `self`.

# In[66]:


class PointV1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


# In[67]:


p = PointV1(2, 3)
print("x =", p.x)
print("y =", p.y)


# In[68]:


p.move(3, 5)
print("x =", p.x)
print("y =", p.y)


# ## Das Python-Objektmodell
# 
# Mit Dunder-Methoden können benutzerdefinierten Datentypen benutzerfreundlicher
# gestaltet werden:

# In[69]:


print(str(p))
print(repr(p))


# Durch Definition der Methode `__repr__(self)` kann der von `repr` zurückgegebene
# String für benutzerdefinierte Klassen angepasst werden: Der Funktionsaufruf
# `repr(x)` überprüft, ob `x` eine Methode `__repr__` hat und ruft diese auf,
# falls sie existiert.

# In[70]:


class PointV2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "PointV2(" + repr(self.x) + ", " + repr(self.y) + ")"

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


# In[71]:


p = PointV2(2, 5)
print(repr(p))


# Standardmäßig delegiert die Funktion `str` an `repr`, falls keine `__str__`-Methode
# definiert ist:
# 

# In[72]:


print(str(p))


# Python bietet viele Dunder-Methoden an: siehe das
# [Python Datenmodell](https://docs.python.org/3/reference/datamodel.html)
# in der Dokumentation

# In[73]:


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(" + repr(self.x) + ", " + repr(self.y) + ")"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


# In[74]:


p1 = Point(1, 2)
p2 = Point(2, 4)
p = p1 + p2
p


# In[75]:


p += p1
p


# In[76]:


p3 = p - Point(3, 2)
p3


# ## Workshop
# 
# - Notebook `012x-Workshop Einführung in Python (Teil 2)`
# - Abschnitt "Verbesserte Einkaufsliste"

# In[ ]:




