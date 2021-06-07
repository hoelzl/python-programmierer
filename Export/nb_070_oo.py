#!/usr/bin/env python
# coding: utf-8

# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <h1 style="text-align:center;">Python: Objektorientierung</h1>
# <h2 style="text-align:center;">Coding Akademie München GmbH</h2>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <div style="text-align:center;">Allaithy Raed</div>

# # Objektorientierung Teil 2
# 
# - Wir haben im vorherigen Kapitel Klassen kennengelernt, einen der grundlegenden Baustein der objektorientierten Programmierung
# - In diesem Kapitel werden wir Vererbung betrachten.

# ## Attribute von Klassen

# In[ ]:


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


# In[ ]:


print(CountedAdder.num_counters)
a1 = CountedAdder(10)
print(CountedAdder.num_counters)
a2 = CountedAdder(20)
print(CountedAdder.num_counters)


# In[ ]:


print(a1.add(1))
print(a2.add(2))


# In[ ]:


a1.describe()
a2.describe()


# In[ ]:


print(CountedAdder.num_counters)
print(a1.num_counters)
print(a2.num_counters)


# In[ ]:


print(CountedAdder.add)
print(a1.add)
print(a2.add)


# ## Vererbung

# In[ ]:


class LoggingAdder(CountedAdder):
    def add(self, n):
        print(f"Adding {self.value} to {n}")
        return self.value + n


# In[ ]:


a3 = LoggingAdder(30)
print(a3.add(3))
print(a3.num_counters)


# In[ ]:


a1.describe()
a2.describe()
a3.describe()


# In[ ]:


# Method Resolution Order:
LoggingAdder.mro()


# In[ ]:


print(CountedAdder.add)
print(a1.add)
print(a2.add)
print(LoggingAdder.add)
print(a3.add)


# In[ ]:


print(CountedAdder.add)
print(a1.add.__func__)
print(a2.add.__func__)
print(LoggingAdder.add)
print(a3.add.__func__)


# In[ ]:


a1.__dict__['value'] = 15


# In[ ]:


a1.add(0)


# In[ ]:


LoggingAdder.__dict__


# # Zugriff auf Attribute
# 
# Python ermöglicht es uns als Programmierer, an mehreren Stellen in den Zugriff auf Attribute einzugreifen und das Verhalten zu modifizieren.

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

# In[ ]:


class LoggingDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print(f'__get__({self}, {instance}, {owner})')
        print(f'  __dict__ == {instance.__dict__}')
        return instance.__dict__.get(self.name, 'nothing')


# In[ ]:


class OverridingLoggingDescriptor(LoggingDescriptor):
    def __set__(self, instance, value):
        print(f'__set__({self}, {instance}, {value}')
        instance.__dict__[self.name] = value


# In[ ]:


class YourClass:
    f = LoggingDescriptor('f')
    g = OverridingLoggingDescriptor('g')


# In[ ]:


yc = YourClass()
print(yc.f, yc.g)


# In[ ]:


yc.f = 234
yc.g = 345


# In[ ]:


print(yc.f, yc.g)


# In[ ]:


class MyClass:
    def g(self, x):
        print(self, x)
def f(x, y):
    print(x, y)


# In[ ]:


mc = MyClass()
print(mc.__class__)


# In[ ]:


print(MyClass.g)
print(mc.g.__qualname__)
print(mc.g.__get__)


# In[ ]:


print(f.__get__)


# In[ ]:


bound_f = f.__get__(mc, MyClass)
bound_g = mc.g
print(bound_f)
print(bound_g)


# In[ ]:


bound_f(3)
bound_g(3)
mc.g(3)


# ## Mehrfachvererbung

# In[ ]:


class A:
    """Superclass of everything"""

    def f(self):
        print(f'f(A) on {self!r}')

    def g(self):
        print(f'g(A) on {self!r}')


# In[ ]:


class B(A):
    def f(self):
        print(f'f(B) on {self!r}')
        super().f()

    def g(self):
        print(f'g(B) on {self!r}')
        A.g(self)


# In[ ]:


class C(A):
    def f(self):
        print(f'f(C) on {self!r}')
        super().f()

    def g(self):
        print(f'g(C) on {self!r}')
        A.g(self)


# In[ ]:


class D(B, C):
    def f(self):
        print(f'f(D) on {self!r}')
        super().f()

    def g(self):
        print(f'g(D) on {self!r}')
        B.g(self)
        C.g(self)


# In[ ]:


d = D()
d.f()


# In[ ]:


d.g()


# ## Abstrakte Klassen
# 
# - Die Klasse `abc.ABC` als Basisklasse
# - (Eigentlich ist eine Metaklasse verantwortlich)
# - `@abstractmethod` Dekorator

# In[ ]:


from abc import ABC, abstractmethod

class MyBase(ABC):
    @abstractmethod
    def my_method(self):
        print("HI!")


# In[ ]:


class MyClass(MyBase):
    pass

# mc = MyClass()


# In[ ]:


class YourClass(MyBase):
    def my_method(self):
        super().my_method()
        print("Hello!")

yc = YourClass()
yc.my_method()


# # Workshop
# 
# Siehe `070x-Workshop RPG-Würfel` bis `Factory für RPG-Würfel`.

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

# In[ ]:





# In[ ]:





# In[ ]:





# # Workshop
# 
# Siehe `070x-Workshop RPG-Würfel` bis `Factory für RPG-Würfel`.

# # Workshop
# 
# Siehe Verzeichnis `Examples/NameGenerator`.

# In[ ]:




