# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.2
# ---

# j2 import 'macros.j2' as doc
# %% [markdown] {{ doc.slide() }}
# {{ doc.header("Iteration") }}


# %% [markdown]
#
# # Iteration über Listen
#
# Zur Iteration über Listen (und andere Datenstrukturen) bietet Python die
# bereits besprochene`for`-Schleife:


# %% {{ doc.codealong() }}
my_list = [1, 2, 3, 4]
for n in my_list:
    print(f"Item {n}")


# %% {{ doc.codealong() }}
index = 0
while index < len(my_list):
    n = my_list[index]
    print(f"Item {n}")
    index += 1


# %% [markdown]
#
#  ## Iteration über Listen von Listen

# %% {{ doc.codealong() }}
a, b = [1, 2]
print(a)
print(b)


# %%
my_list = [[1, 2], [3, 4], [5, 6]]


# %% {{ doc.codealong() }}
for m, n in my_list:
    print(f"Items {m} and {n}")


# %% {{ doc.codealong() }}
index = 0
while index < len(my_list):
    m, n = my_list[index]
    print(f"Items {m} and {n}")
    index += 1


# %% [markdown]
#
#  # Nochmal Finden von Elementen
#
#  Bei unserer bisherigen Version von `find` muss die Liste zweimal durchlaufen
#  werden:
#
#  - Einmal von `in` um zu testen, ob das gesuchte Element in der Liste vorkommt
#  - Einmal von `index` um den Index zu finden.
#
#  Schöner wäre es, wenn wir das in einem Durchlauf erledigen könnten.

# %%
my_list = ["a", "b", "c", "d", "e"]

# %% {{ doc.codealong() }}
enumerate(my_list)


# %% {{ doc.codealong() }}
list(enumerate(my_list))


# %% {{ doc.codealong() }}
for index, element in enumerate(my_list):
    print(f"index = {index}, element = {element}")


# %% {{ doc.codealong() }}
def find(element, a_list):
    result = None
    for index, list_entry in enumerate(a_list):
        if list_entry == element:
            result = index
            break
    return result



# %%
my_list = ["a", "b", "c", "d", "a"]

# %% {{ doc.codealong() }}
find("a", my_list)


# %% {{ doc.codealong() }}
find("d", my_list)


# %% {{ doc.codealong() }}
assert find("x", my_list) == None


# %% {{ doc.codealong() }}
# Alternative Implementierung:
def find_return(element, a_list):
    for index, list_entry in enumerate(a_list):
        if list_entry == element:
            return index
    return None



# %% {{ doc.codealong() }}
# Mit assert können Invarianten dokumentiert werden:
assert find("a", my_list) == find_return("a", my_list)
assert find("d", my_list) == find_return("d", my_list)
assert find("x", my_list) == find_return("x", my_list)


# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `030x-Workshop Listen und For-Schleifen`
#  - Abschnitt "Finden in Listen"
#

# %% [markdown]
#
#  ## Aggregation von Listenelementen

# %% {{ doc.codealong() }}
def summe(zahlen):
    ergebnis = 0
    for n in zahlen:
        ergebnis += n
    return ergebnis



# %% {{ doc.codealong() }}
summe([1, 2, 3])


# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `030x-Workshop Listen und For-Schleifen`
#  - Abschnitt "Mittelwert einer Liste"

# %% [markdown]
#
#  ## Transformation von Listen

# %% {{ doc.codealong() }}
result = []
for item in [1, 2, 3, 4]:
    result.append(item + 1)
result


# %% {{ doc.codealong() }}
result = []
for n in [1, 2, 3, 4]:
    result.append(f"Item {n}")
result


# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `030x-Workshop Listen und For-Schleifen`
#  - Abschnitt "Quadratzahlen"
#
#  # Filtern von Listen

# %% {{ doc.codealong() }}
result = []
for item in [1, 2, 3, 4, 5, 6]:
    if item % 2 == 0:
        result.append(item)
result


# %% {{ doc.codealong() }}
result = []
for item in ["abc", "def", "asd", "qwe", "bab"]:
    if "ab" in item:
        result.append(item)
result


# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `030x-Workshop Listen und For-Schleifen`
#  - Abschnitt "Filtern"
#
