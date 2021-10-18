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
# <h1 style="text-align:center;">Python: Objektorientierung</h1>
# <h2 style="text-align:center;">Coding Akademie München GmbH</h2>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <div style="text-align:center;">Allaithy Raed</div>

# %% [markdown] slideshow={"slide_type": "slide"}
# # Objektorientierung Teil 2
#
# - Wir haben im vorherigen Kapitel Klassen kennengelernt, einen der grundlegenden Baustein der objektorientierten Programmierung
# - In diesem Kapitel werden wir Vererbung betrachten.

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Attribute von Klassen

# %%
class CountedAdder:
    num_counters = 0
    
    def __init__(self, value):
        CountedAdder.num_counters += 1
        self.value = value
    
    def describe(self):
        print(f"One of {CountedAdder.num_counters} adders. "
              f"This one adds {self.value} to its argument.")
    
    def add(self, n):
        return self.value + n


# %% slideshow={"slide_type": "subslide"}
print(CountedAdder.num_counters)
a1 = CountedAdder(10)
print(CountedAdder.num_counters)
a2 = CountedAdder(20)
print(CountedAdder.num_counters)

# %% slideshow={"slide_type": "subslide"}
print(a1.add(1))
print(a2.add(2))

# %% slideshow={"slide_type": "-"}
a1.describe()
a2.describe()

# %% slideshow={"slide_type": "subslide"}
print(CountedAdder.num_counters)
print(a1.num_counters)
print(a2.num_counters)

# %%
print(CountedAdder.add)
print(a1.add)
print(a2.add)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## Vererbung

# %% slideshow={"slide_type": "-"}
class LoggingAdder(CountedAdder):
    def add(self, n):
        print(f"Adding {self.value} to {n}")
        return self.value + n


# %%
a3 = LoggingAdder(30)
print(a3.add(3))
print(a3.num_counters)

# %% slideshow={"slide_type": "subslide"}
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

# %% slideshow={"slide_type": "subslide"}
print(CountedAdder.add)
print(a1.add.__func__)
print(a2.add.__func__)
print(LoggingAdder.add)
print(a3.add.__func__)

# %% slideshow={"slide_type": "subslide"}
a1.__dict__['value'] = 15

# %%
a1.add(0)

# %%
LoggingAdder.__dict__


# %% [markdown] slideshow={"slide_type": "slide"}
# # Zugriff auf Attribute
#
# Python ermöglicht es uns als Programmierer, an mehreren Stellen in den Zugriff auf Attribute einzugreifen und das Verhalten zu modifizieren.

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Attribute von Klassen
#
# Beim Zugriff auf `C.name` verfährt Python folgendermaßen:
#
# - Falls `name` ein Key in `C.__dict__` ist:
#   - `v = C.__dict__['name']`
#   - Falls `v` ein Deskriptor ist (i.e., `type(v).__get__` definiert ist:
#     - Resultat ist `type(v).__get__(v, None, C)`
#   - Falls `v` kein Deskriptor ist:
#     - Resultat ist `v`
# - Falls `name` kein Key in `C.__dict__` ist:
#   - Die Baisklassen von `C` werden in Method Resolution Order durchlaufen und diese Verfahren wird für jede Klasse ausgeführt

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Attribute von Instanzen
#
# Beim Zugriff auf `object.name` verfährt Python folgendermaßen:
#
# - Falls `name` ein Overriding Descriptor `v` in `C` oder einer der Basisklassen von `C` ist (`type(v)` hat Methoden `__get__()` und `__set__()`:
#   - Das Resultat ist `type(v).__get__(v, object, C)`
# - Andernfalls, falls `name` ein Schlüssel in `object.__dict__` ist:
#   - Das Resultat ist `object.__dict__['name']`
# - Andernfalls delegiert `object.name` die Suche an die Klasse, wie oben beschrieben
#   - Falls dadurch ein Deskriptor `v` gefunden wird, so ist das Ergebnis `type(v).__get__(v, object, C)`
#   - Wenn ein Wert `v` gefunden wird, der kein Deskriptor ist, dann wird `v` zurückgegeben
# - Wenn kein Wert gefunden wird und `C.__getattr__` definiert ist, dann wird `C.__getattr__(object, 'name')` aufgerufen um den Wert zu erhalten
# - Andernfalls wird eine `AttributeError` Exception ausgelöst
#
# Dieser Prozess kann durch die `__getattribute__` Methode überschrieben werden.

# %% slideshow={"slide_type": "subslide"}
class LoggingDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print(f'__get__({self}, {instance}, {owner})')
        print(f'  __dict__ == {instance.__dict__}')
        return instance.__dict__.get(self.name, 'nothing')


# %% slideshow={"slide_type": "subslide"}
class OverridingLoggingDescriptor(LoggingDescriptor):
    def __set__(self, instance, value):
        print(f'__set__({self}, {instance}, {value}')
        instance.__dict__[self.name] = value


# %% slideshow={"slide_type": "subslide"}
class YourClass:
    f = LoggingDescriptor('f')
    g = OverridingLoggingDescriptor('g')


# %%
yc = YourClass()
print(yc.f, yc.g)

# %% slideshow={"slide_type": "subslide"}
yc.f = 234
yc.g = 345

# %%
print(yc.f, yc.g)


# %% slideshow={"slide_type": "subslide"}
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

# %% slideshow={"slide_type": "subslide"}
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


# %% [markdown] slideshow={"slide_type": "slide"}
# ## Mehrfachvererbung

# %%
class A:
    """Superclass of everything"""

    def f(self):
        print(f'f(A) on {self!r}')

    def g(self):
        print(f'g(A) on {self!r}')


# %% slideshow={"slide_type": "subslide"}
class B(A):
    def f(self):
        print(f'f(B) on {self!r}')
        super().f()

    def g(self):
        print(f'g(B) on {self!r}')
        A.g(self)


# %% slideshow={"slide_type": "subslide"}
class C(A):
    def f(self):
        print(f'f(C) on {self!r}')
        super().f()

    def g(self):
        print(f'g(C) on {self!r}')
        A.g(self)


# %% slideshow={"slide_type": "subslide"}
class D(B, C):
    def f(self):
        print(f'f(D) on {self!r}')
        super().f()

    def g(self):
        print(f'g(D) on {self!r}')
        B.g(self)
        C.g(self)


# %% slideshow={"slide_type": "subslide"}
d = D()
d.f()

# %%
d.g()

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Abstrakte Klassen
#
# - Die Klasse `abc.ABC` als Basisklasse
# - (Eigentlich ist eine Metaklasse verantwortlich)
# - `@abstractmethod` Dekorator

# %% slideshow={"slide_type": "subslide"}
from abc import ABC, abstractmethod

class MyBase(ABC):
    @abstractmethod
    def my_method(self):
        print("HI!")


# %%
class MyClass(MyBase):
    pass

# mc = MyClass()


# %% slideshow={"slide_type": "subslide"}
class YourClass(MyBase):
    def my_method(self):
        super().my_method()
        print("Hello!")

yc = YourClass()
yc.my_method()

# %% [markdown] slideshow={"slide_type": "slide"}
# # Workshop
#
# Siehe `070x-Workshop RPG-Würfel` bis `Factory für RPG-Würfel`.

# %% [markdown] slideshow={"slide_type": "slide"}
# # Reguläre Ausdrücke
#
# Reguläre Ausdrücke stellen "Muster" dar, mit denen in Strings gesucht und ersetzt werden kann:
# - `x..x`: zwei Vorkommen von `x`, die durch (genau) zwei beliebige andere Zeichen getrennt sind
# - `a[0-9]?[0-9]`: der Buchstabe `a` gefolgt von ein oder zwei Ziffern.
#
# Es gibt dabei verschiedene Operationen und Abkürzungen für Zeichenklassen:
#
# - `.`: Ein beliebiges Zeichen außer `\n`.
# - `*`: Der vorhergehende Ausdruck (ein Zeichen oder eine geklammerte Gruppe von Zeichn) kann beliebig oft (auch 0-mal) wiederholt werden.
# - `+`: Der vorhergehende Ausdruck kann ein oder mehrmals wiederholt werden.
# - `\s`: Whitespace
# - `\w`: Alphanumerische Zeichen und Unterstrich `_`

# %% slideshow={"slide_type": "subslide"}

# %%

# %%

# %% [markdown] slideshow={"slide_type": "subslide"}
# # Workshop
#
# Siehe `070x-Workshop RPG-Würfel` bis `Factory für RPG-Würfel`.

# %% [markdown] slideshow={"slide_type": "subslide"}
# # Workshop
#
# Siehe Verzeichnis `Examples/NameGenerator`.

# %%
