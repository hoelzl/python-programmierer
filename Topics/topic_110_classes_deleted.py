
# %% [markdown]
#
# # Benutzerdefinierte Datentypen
#
# In Python können benutzerdefinierte Datentypen definiert werden:

# %%
class PointV0:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# %%
p = PointV0(2, 3)
p

# %%
print("x =", p.x)
print("y =", p.y)

# %% [markdown]
#
# ## Methoden
#
# Klassen können Methoden enthalten. Im Gegensatz zu vielen anderen Sprachen hat
# Python bei der Definition keinen impliziten `this` Parameter; das Objekt auf dem
# die Methode aufgerufen wird muss als erster Parameter angegeben werden.
#
# Per Konvention hat dieser Parameter den Namen `self`.

# %%
class PointV1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


# %%
p = PointV1(2, 3)
print("x =", p.x)
print("y =", p.y)

# %%
p.move(3, 5)
print("x =", p.x)
print("y =", p.y)

# %% [markdown]
#
# ## Das Python-Objektmodell
#
# Mit Dunder-Methoden können benutzerdefinierten Datentypen benutzerfreundlicher
# gestaltet werden:

# %%
print(str(p))
print(repr(p))

# %% [markdown]
#
# Durch Definition der Methode `__repr__(self)` kann der von `repr` zurückgegebene
# String für benutzerdefinierte Klassen angepasst werden: Der Funktionsaufruf
# `repr(x)` überprüft, ob `x` eine Methode `__repr__` hat und ruft diese auf,
# falls sie existiert.

# %%
class PointV2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "PointV2(" + repr(self.x) + ", " + repr(self.y) + ")"

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


# %%
p = PointV2(2, 5)
print(repr(p))

# %% [markdown]
#
# Standardmäßig delegiert die Funktion `str` an `repr`, falls keine `__str__`-Methode
# definiert ist:
#

# %%
print(str(p))

# %% [markdown]
#
# Python bietet viele Dunder-Methoden an: siehe das
# [Python Datenmodell](https://docs.python.org/3/reference/datamodel.html)
# in der Dokumentation

# %%
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


# %%
p1 = Point(1, 2)
p2 = Point(2, 4)
p = p1 + p2
p

# %%
p += p1
p

# %%
p3 = p - Point(3, 2)
p3

# %% [markdown]
#
# ## Workshop
#
# - Notebook `012x-Workshop Einführung in Python (Teil 2)`
# - Abschnitt "Verbesserte Einkaufsliste"
