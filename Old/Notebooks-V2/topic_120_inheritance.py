# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
#
#  # Objektorientierung Teil 2
#
#  - Wir haben im vorherigen Kapitel Klassen kennengelernt, einen der grundlegenden Baustein der objektorientierten Programmierung
#  - In diesem Kapitel werden wir Vererbung betrachten.

# %% [markdown]
#  ## Vererbung

# %%
import random
from typing import Tuple


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



# %%
p = Point(0, 0)
p


# %%
p.move(2, 3)
p


# %%
p.randomize()
p


# %%
class ColorPoint(Point):
    def __init__(self, x=0, y=0, color="black"):
        super().__init__(x, y)
        self.color = color

    def __repr__(self):
        return f"ColorPoint({self.x:.1f}, {self.y:.1f}, {self.color!r})"

    def randomize(self):
        super().randomize()
        self.color = random.choice(["black", "red", "green", "blue", "yellow", "white"])



# %%
cp = ColorPoint(2, 3, "red")
# cp


# %%
cp.move(2, 3)
# cp


# %%
cp.randomize()
# cp


# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `020x-Workshop Kontrollstrukturen`
#  - Abschnitt "Vererbung"
#

# %% [markdown]
#
#  ## Abstrakte Klassen
#
#  - Die Klasse `abc.ABC` als Basisklasse
#  - (Eigentlich ist eine Metaklasse verantwortlich)
#  - `@abstractmethod` Dekorator

# %%
from abc import ABC, abstractmethod


class MyBase(ABC):
    @abstractmethod
    def my_method(self):
        print("HI!")



# %%
class MyClass(MyBase):
    pass


# mc = MyClass()


# %%
class YourClass(MyBase):
    def my_method(self):
        super().my_method()
        print("Hello!")


yc = YourClass()
yc.my_method()


# %% [markdown]
#
#  # Workshop
#
#  Siehe `070x-Workshop RPG-Würfel` bis `Factory für RPG-Würfel`.

# %% [markdown]
#
#  ## Attribute von Klassen

# %%
class CountedAdder:
    num_counters = 0

    def __init__(self, value):
        CountedAdder.num_counters += 1
        self.value = value

    def describe(self):
        print(
            f"One of {CountedAdder.num_counters} adders. "
            f"This one adds {self.value} to its argument."
        )

    def add(self, n):
        return self.value + n



# %%
print(CountedAdder.num_counters)
a1 = CountedAdder(10)
print(CountedAdder.num_counters)
a2 = CountedAdder(20)
print(CountedAdder.num_counters)


# %%
print(a1.add(1))
print(a2.add(2))


# %%
a1.describe()
a2.describe()


# %%
print(CountedAdder.num_counters)
print(a1.num_counters)
print(a2.num_counters)


# %%
print(CountedAdder.add)
print(a1.add)
print(a2.add)

# ## Vererbung


# %%
class LoggingAdder(CountedAdder):
    def add(self, n):
        print(f"Adding {self.value} to {n}")
        return self.value + n



# %%
a3 = LoggingAdder(30)
print(a3.add(3))
print(a3.num_counters)


# %%
a1.describe()
a2.describe()
a3.describe()


# %%
# Method Resolution Order:
LoggingAdder.mro()


# %%
print(CountedAdder.add)
print(a1.add)
print(a2.add)
print(LoggingAdder.add)
print(a3.add)


# %%
print(CountedAdder.add)
print(a1.add.__func__)
print(a2.add.__func__)
print(LoggingAdder.add)
print(a3.add.__func__)


# %%
a1.__dict__["value"] = 15


# %%
a1.add(0)


# %%
LoggingAdder.__dict__


# %% [markdown]
#
#  ## Zugriff auf Attribute
#
#  Python ermöglicht es uns als Programmierer, an mehreren Stellen in den Zugriff auf Attribute einzugreifen und das Verhalten zu modifizieren.

# %% [markdown]
#
#  ## Attribute von Klassen
#
#  Beim Zugriff auf `C.name` verfährt Python folgendermaßen:
#
#  - Falls `name` ein Key in `C.__dict__` ist:
#    - `v = C.__dict__['name']`
#    - Falls `v` ein Deskriptor ist (i.e., `type(v).__get__` definiert ist:
#      - Resultat ist `type(v).__get__(v, None, C)`
#    - Falls `v` kein Deskriptor ist:
#      - Resultat ist `v`
#  - Falls `name` kein Key in `C.__dict__` ist:
#    - Die Baisklassen von `C` werden in Method Resolution Order durchlaufen und
#      diese Verfahren wird für jede Klasse ausgeführt

# %% [markdown]
#
#  ## Attribute von Instanzen
#
#  Beim Zugriff auf `object.name` verfährt Python folgendermaßen:
#
#  - Falls `name` ein Overriding Descriptor `v` in `C` oder einer der
#    Basisklassen von `C` ist (`type(v)` hat Methoden `__get__()` und
#    `__set__()`:
#    - Das Resultat ist `type(v).__get__(v, object, C)`
#  - Andernfalls, falls `name` ein Schlüssel in `object.__dict__` ist:
#    - Das Resultat ist `object.__dict__['name']`
#  - Andernfalls delegiert `object.name` die Suche an die Klasse, wie oben
#    beschrieben
#    - Falls dadurch ein Deskriptor `v` gefunden wird, so ist das Ergebnis
#      `type(v).__get__(v, object, C)`
#    - Wenn ein Wert `v` gefunden wird, der kein Deskriptor ist, dann wird `v`
#      zurückgegeben
#  - Wenn kein Wert gefunden wird und `C.__getattr__` definiert ist, dann wird
#    `C.__getattr__(object, 'name')` aufgerufen um den Wert zu erhalten
#  - Andernfalls wird eine `AttributeError` Exception ausgelöst
#
#  Dieser Prozess kann durch die `__getattribute__` Methode überschrieben werden.

# %%
class LoggingDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print(f"__get__({self}, {instance}, {owner})")
        print(f"  __dict__ == {instance.__dict__}")
        return instance.__dict__.get(self.name, "nothing")



# %%
class OverridingLoggingDescriptor(LoggingDescriptor):
    def __set__(self, instance, value):
        print(f"__set__({self}, {instance}, {value}")
        instance.__dict__[self.name] = value



# %%
class YourClass:
    f = LoggingDescriptor("f")
    g = OverridingLoggingDescriptor("g")



# %%
yc = YourClass()
print(yc.f, yc.g)


# %%
yc.f = 234
yc.g = 345


# %%
print(yc.f, yc.g)


# %%
class MyClass:
    def g(self, x):
        print(self, x)


def f(x, y):
    print(x, y)



# %%
mc = MyClass()
print(mc.__class__)


# %%
print(MyClass.g)
print(mc.g.__qualname__)
print(mc.g.__get__)


# %%
print(f.__get__)


# %%
bound_f = f.__get__(mc, MyClass)
bound_g = mc.g
print(bound_f)
print(bound_g)


# %%
bound_f(3)
bound_g(3)
mc.g(3)

# ## Mehrfachvererbung


# %%
class A:
    """Superclass of everything"""

    def f(self):
        print(f"f(A) on {self!r}")

    def g(self):
        print(f"g(A) on {self!r}")



# %%
class B(A):
    def f(self):
        print(f"f(B) on {self!r}")
        super().f()

    def g(self):
        print(f"g(B) on {self!r}")
        A.g(self)



# %%
class C(A):
    def f(self):
        print(f"f(C) on {self!r}")
        super().f()

    def g(self):
        print(f"g(C) on {self!r}")
        A.g(self)



# %%
class D(B, C):
    def f(self):
        print(f"f(D) on {self!r}")
        super().f()

    def g(self):
        print(f"g(D) on {self!r}")
        B.g(self)
        C.g(self)



# %%
d = D()
d.f()


# %%
d.g()

