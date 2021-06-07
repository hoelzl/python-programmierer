#!/usr/bin/env python
# coding: utf-8

# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <h1 style="text-align:center;">Python: Listen und For-Schleifen</h1>
# <h2 style="text-align:center;">Coding Akademie München GmbH</h2>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <div style="text-align:center;">Allaithy Raed</div>
# 

# # Listen
# 
# Wiederholung:
# 
# - Listen-Literale werden in eckige Klammern eingeschlossen
# - Andere Sequenzen können mittels `list` in Listen umgewandelt werden

# In[1]:


['a', 'b', 'c']


# In[2]:


list(range(3))


# ## Eigenschaften von Listen
# 
# - Listen können beliebige Python-Werte speichern
# - Elemente in einer Liste haben eine feste Reihenfolge
# - Auf Elemente einer Liste kann mit einem Index zugegriffen werden
# - Listen können modifiziert werden
# 
# Listen können Elemente mit verschiedenen Typen enthalten, die meisten Listen
# enthalten aber Elemente eines einzigen Typs.

# In[ ]:


stringliste = ["a", "b", "c"]


# In[ ]:


stringliste[0]


# In[ ]:


stringliste[-1]


# ### Überprüfen, ob ein Element in einer Liste enthalten ist

# In[ ]:


2 in [1, 2, 3]


# In[ ]:


not (2 in [1, 3, 5])


# In[ ]:


2 not in [1, 3, 5]


# ### Finden der Position eines Elements

# In[ ]:


[1, 2, 3, 2, 4].index(2)


# In[ ]:


my_list = ['a', 'b', 'c', 'd', 'b', 'd', 'b']
my_index = my_list.index('b')
print(my_index)
my_list[my_index]


# In[ ]:


# Fehler
# [1, 3, 5].index(2)


# Die Methode `index` wirft eine Exception, wenn das gesuchte Objekt nicht in der Liste vorkommt. Wie können wir eine Funktion
# ```
# find(element, a_list)
# ```
# schreiben, die uns 
# 
# - einen Index zurückgibt, falls das Element `element` in der Liste vorkommt, und die
# - `None` zurückgibt, falls es nicht vorkommt?

# In[ ]:


def find(element, a_list):
    if element in a_list:
        return a_list.index(element)
    else:
        return None


# In[ ]:


my_list = ['a', 'b', 'c', 'd', 'e']


# In[ ]:


find('a', my_list)


# In[ ]:


find('d', my_list)


# In[ ]:


print(find('x', my_list))


# ### Modifikation von Elementen

# In[ ]:


stringliste


# In[ ]:


stringliste[0] = "A"


# In[ ]:


stringliste


# ### Einfügen und Anhängen von Elementen

# In[ ]:


stringliste


# In[ ]:


stringliste.append("D")


# In[ ]:


stringliste


# In[ ]:


stringliste + ["E", "F"]


# In[ ]:


stringliste


# In[ ]:


stringliste.extend(["E", "F"])


# In[ ]:


stringliste


# In[ ]:


stringliste


# In[ ]:


stringliste.insert(1, "Y")


# In[ ]:


stringliste


# In[ ]:


stringliste.insert(0, "ANFANG")


# In[ ]:


stringliste


# In[ ]:


# Vorsicht!
stringliste.insert(-1, "ENDE")


# In[ ]:


stringliste


# ### Entfernen von Elementen

# In[ ]:


stringliste


# In[ ]:


stringliste[7]


# In[ ]:


del stringliste[7]


# In[ ]:


stringliste


# ### Länge einer Liste

# In[ ]:


stringliste


# In[ ]:


len(stringliste)


# In[ ]:


stringliste.insert(len(stringliste), "WIRKLICH DAS ENDE")


# In[ ]:


stringliste


# In[ ]:


# Vorsicht
# stringliste[len(stringliste)]


# ## Mini-Workshop
# 
# - Notebook `030x-Workshop Listen und For-Schleifen`
# - Abschnitt "Farben"
# 

# ## Slicing
# 
# Mit der Notation `liste[m:n]` kann man eine "Teilliste" von `liste` extrahieren.
# 
# - Das erste Element ist `liste[m]`
# - Das letzte Element ist `liste[n-1]`

# In[ ]:


stringliste = ['a', 'b', 'c', 'd', 'e']


# In[ ]:


stringliste[1:3]


# In[ ]:


stringliste[1:1]


# In[ ]:


stringliste[0:len(stringliste)]


# In[ ]:


stringliste[:3]


# In[ ]:


stringliste[1:]


# In[ ]:


stringliste[:]


# ## Mini-Workshop
# 
# - Notebook `030x-Workshop Listen und For-Schleifen`
# - Abschnitt "Slicing"
# 

# ## Erzeugen von Listen
# 
# Durch den Multiplikationsoperator `*` können die Elemente einer Liste wiederholt werden:

# In[ ]:


[1, 2] * 3


# In[ ]:


3 * ["a", "b"]


# In[ ]:


[0] * 10


# ## Zuweisung an Slices
# 
# Man kann Werte an Slices zuweisen:

# In[ ]:


liste = [1, 2, 3, 4]
liste[1:3]


# In[ ]:


liste[1:3] = ['a', 'b', 'c']
liste


# In[ ]:


liste[2:2]


# In[ ]:


liste[2:2] = ['x']
liste


# In[ ]:


liste[:] = [11, 22, 33]
liste


# ## Identität von Objekten

# In[ ]:


a = [1, 2, 3]
b = [1, 2, 3]
c = b


# In[ ]:


print(f"a = {a}, b = {b}, c = {c}")


# In[ ]:


a[0] = 10


# In[ ]:


print(f"a = {a}, b = {b}, c = {c}")


# In[ ]:


b[0] = 20


# In[ ]:


c[1] = 30


# In[ ]:


print(f"a = {a}, b = {b}, c = {c}")


# <img src="img/identity.svg" style="display:block;width:70%;margin:auto;"/>

# ## Test der Identität von Objekten

# In[ ]:


a = [1, 2, 3]
b = a
c = [1, 2, 3]
d = c[:]


# In[ ]:


a == b


# In[ ]:


b == c


# In[ ]:


c == d


# In[ ]:


a = [1, 2, 3]
b = a
c = [1, 2, 3]
d = c[:]


# In[ ]:


a is b


# In[ ]:


b is c


# In[ ]:


c is d


# In[ ]:


hex(id([1, 2, 3]))


# In[ ]:


def modify_list(lst):
    print("modify_list: before", lst)
    lst.append("abc")
    print("modify_list: after", lst)


# In[ ]:


my_list = [1, 2, 3]
modify_list(my_list)


# In[ ]:


my_list


# # Iteration über Listen
# 
# Zur Iteration über Listen (und andere Datenstrukturen) bietet Python die bereits besprochene`for`-Schleife:

# In[ ]:


my_list = [1, 2, 3, 4]
for n in my_list:
    print(f"Item {n}")


# In[ ]:


index = 0
while index < len(my_list):
    n = my_list[index]
    print(f"Item {n}")
    index += 1


# ## Iteration über Listen von Listen

# In[1]:


a, b = [1, 2]
print(a)
print(b)


# In[2]:


my_list = [[1, 2], [3, 4], [5, 6]]


# In[4]:


index = 0
while index < len(my_list):
    m, n = my_list[index]
    print(f"Items {m} and {n}")
    index += 1


# In[5]:


for m, n in my_list:
    print(f"Items {m} and {n}")


# # Nochmal Finden von Elementen
# 
# Bei unserer bisherigen Version von `find` muss die Liste zweimal durchlaufen werden:
# 
# - Einmal von `in` um zu testen, ob das gesuchte Element in der Liste vorkommt
# - Einmal von `index` um den Index zu finden.
# 
# Schöner wäre es, wenn wir das in einem Durchlauf erledigen könnten.

# In[ ]:


my_list = ['a', 'b', 'c', 'd', 'e']
enumerate(my_list)


# In[ ]:


list(enumerate(my_list))


# In[ ]:


for index, element in enumerate(my_list):
    print(f"index = {index}, element = {element}")


# In[6]:


for index, element, other in [[1, 2, 3], ['a', 'b', 'c']]:
    print(index, element, other)


# In[ ]:


def find(element, a_list):
    result = None
    for index, list_entry in enumerate(a_list):
        if list_entry == element:
            result = index
            break
    return result


# In[ ]:


my_list = ['a', 'b', 'c', 'd', 'a']
find('a', my_list)


# In[ ]:


find('d', my_list)


# In[ ]:


assert find('x', my_list) == None


# In[ ]:


# Alternative Implementierung:
def find_return(element, a_list):
    for index, list_entry in enumerate(a_list):
        if list_entry == element:
            return index
    return None


# In[ ]:


# Mit assert können Invarianten dokumentiert werden:
assert find('a', my_list) == find_return('a', my_list)
assert find('d', my_list) == find_return('d', my_list)
assert find('x', my_list) == find_return('x', my_list)


# ## Mini-Workshop
# 
# - Notebook `030x-Workshop Listen und For-Schleifen`
# - Abschnitt "Finden in Listen"
# 

# ## Aggregation von Listenelementen

# In[ ]:


def summe(zahlen):
    ergebnis = 0
    for n in zahlen:
        ergebnis += n
    return ergebnis


# In[ ]:


summe([1, 2, 3])


# ## Mini-Workshop
# 
# - Notebook `030x-Workshop Listen und For-Schleifen`
# - Abschnitt "Mittelwert einer Liste"
# 

# ## Transformation von Listen

# In[ ]:


result = []
for item in [1, 2, 3, 4]:
    result.append(item + 1)
result


# In[ ]:


result = []
for n in [1, 2, 3, 4]:
    result.append(f"Item {n}")
result


# ## Mini-Workshop
# 
# - Notebook `030x-Workshop Listen und For-Schleifen`
# - Abschnitt "Quadratzahlen"
# 

# # Filtern von Listen

# In[ ]:


result = []
for item in [1, 2, 3, 4, 5, 6]:
    if item % 2 == 0:
        result.append(item)
result


# In[ ]:


result = []
for item in ["abc", "def", "asd", "qwe", "bab"]:
    if 'ab' in item:
        result.append(item)
result


# ## Mini-Workshop
# 
# - Notebook `030x-Workshop Listen und For-Schleifen`
# - Abschnitt "Filtern"
# 

# ## Eleganter: Listen-Komprehension

# In[ ]:


result = []
for item in [1, 2, 3, 4]:
    result.append(item + 1)
result


# In[ ]:


my_list = [item + 1 for item in [1, 2, 3, 4]] 
my_list


# In[ ]:


result = []
for n in [1, 2, 3, 4]:
    result.append(f"Item {n}")
result


# In[ ]:


[f"Item {n}" for n in [1, 2, 3, 4]]


# ## Mini-Workshop
# 
# - Notebook `030x-Workshop Listen und For-Schleifen`
# - Abschnitte "Quadratzahlen mit Listen-Komprehension"
# 

# In[ ]:


result = []
for item in [1, 2, 3, 4, 5, 6]:
    if item % 2 == 0:
        result.append(item)
result


# In[ ]:


[item for item in [1, 2, 3, 4, 5, 6] if item % 2 == 0]


# In[ ]:


result = []
for item in ["abc", "def", "asd", "qwe", "bab"]:
    if item[0] == "a":
        result.append(item)
result


# In[ ]:


[item for item in ["abc", "def", "asd", "qwe"] if item[0] == "a"]


# In[ ]:


result = []
for list_1 in [[1, 2], ["a", "b", "c"]]:
    for item in list_1:
        result.append(f"Item {item} in {list_1}")
result


# In[ ]:


[f"Item {item} in {list_1}" for list_1 in [[1, 2], ["a", "b", "c"]] for item in list_1]


# ## Mini-Workshop
# 
# - Notebook `030x-Workshop Listen und For-Schleifen`
# - Abschnitte "Filtern mit Listen-Komprehension"
# 

# # Tupel
# 
# Tupel sind eine Datenstruktur, die sehr ähnlich zu Listen ist.
# 
# Syntax:
# 
# - Elemente durch Kommata getrennt: `1, 2, 3, 4`
# - In vielen Fällen müssen Tupel eingeklammert werden: `(1, 2, 3)`

# In[ ]:


1, 2, 3


# In[ ]:


(1,)


# In[ ]:


x = "a", 1, True


# In[ ]:


type(x) 


# ## Eigenschaften von Tupeln
# 
# - Tupel können beliebige Python-Werte speichern
# - Elemente in einem Tupel haben eine feste Reihenfolge
# - Auf Elemente eines Tupels kann mit einem Index zugegriffen werden
# - Tupel können *nicht* modifiziert werden
# 
# Oft werden Tupel zum Speichern *heterogener* Daten verwendet.

# ## Operationen auf Tupeln
# 
# - Viele der Operationen auf Listen lassen sich auf Tupel anwenden.
# - Die Operationen, die Listen verändern sind nicht anwendbar.

# In[ ]:


values = 1, 2, 3
print(values + ('a', 'b'))
print(values[1])
print("Length:", len(values))
values


# In[ ]:


for x in 1, 2, 3:
    print(x)


# In[ ]:


x, y = 1, 2


# In[ ]:


print(x, y)


# In[ ]:


(1, 2, 3).index(2)


# In[ ]:


(1, 2, 3, 1, 2, 1, 2).count(1)


# In[ ]:


[f"Item {item} in {tuple_1}"
 for tuple_1 in ((1, 2), ("a", "b", "c"))
 for item in tuple_1]


# # Generatoren
# 
# - Es ist nicht effizient eine Liste zu konstruieren, wenn wir sie nur zum Iterieren über ihre Elemente verwenden wollen
# - Python bietet die Möglichkeit Generatoren zu definieren, die iterierbar sind, aber nicht den Overhead einer Liste haben
# - Die einfachste Form ist mit Generator Expressions:

# In[ ]:


gen = (n * n for n in range(10))
gen


# In[ ]:


for i in gen:
    print(i, end=' ')


# In[ ]:


for i, j, k in ((n, m, n * m) for n in range(2, 5) for m in range(n, 5)):
    print(f'{i}, {j}, {k}')


# In[ ]:


r = range(3)
repr(r)


# In[ ]:


it = iter(r)
repr(it)


# In[ ]:


next(it)


# In[ ]:


next(it)


# In[ ]:


next(it)


# In[ ]:


next(it)


# In[ ]:


for x in range(3):
    print(x, end=' ')


# In[ ]:


_r = range(3)
_temp_iter = iter(_r)
while True:
    try: x = next(_temp_iter)
    except StopIteration: break
    print(x, end=' ')


# In[ ]:


gen = (n * n for n in range(3))
repr(gen)


# In[ ]:


it = iter(gen)
repr(it)


# In[ ]:


next(it)


# In[ ]:


next(it)


# In[ ]:


next(it)


# In[ ]:


next(it)


# In[ ]:


# `it` ist "erschöpft," man kann keine neuen Werte bekommen
next(it)


# ## Generator Funktionen
# 
# Komplexere Fälle können von Generator Expressions nicht mehr abgedeckt werden.
# 
# - Generator, der alle Zahlen erzeugt (ohne Obergrenze)
# - Generator, der ein Iterable modifiziert (z.B. mehrfach ausführt, eine fixe Anzahl an Elementen nimmt)
# 
# Für diese Fälle gibt es Generator-Funktionen

# In[ ]:


def integers(start=0):
    n = start
    while True:
        yield n
        n += 1


# In[ ]:


for i in integers():
    if i > 3:
        break
    print(i, end=" ")


# In[ ]:


gen = integers()
print(repr(gen))
print(repr(iter(gen)))


# In[ ]:


gen = integers()


# In[ ]:


next(gen)


# In[ ]:





# In[ ]:


def repeat_n_times(n, it):
    for _ in range(n):
        for elt in it:
            yield elt


# In[ ]:


for num in repeat_n_times(3, range(5)):
    print(num, end=' ')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




