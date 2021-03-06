# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] lang="de"
# # Vererbung
#
# Im Folgenden soll eine Klassenhierarchie für Mitarbeiter einer Firma erstellt
# werden:
#
# - Mitarbeiter können entweder Arbeiter oder Manager sein
# - Jeder Mitarbeiter der Firma hat einen Namen, eine Personalnummer und ein
#   Grundgehalt
# - Für jeden Arbeiter werden die angefallenen Überstunden und der Stundenlohn
#   gespeichert.
# - Das Gehalt eines Arbeiters berechnet sich als das 13/12-fache des
#   Grundgehalts plus der Bezahlung für die Überstunden
# - Jeder Manager hat einen individuellen Bonus
# - Das Gehalt eines Managers berechnet sich als das 13/12-fache des
#   Grundgehalts plus Bonus
#
# Implementieren Sie Python Klassen `Mitarbeiter`, `Arbeiter` und `Manager` mit
# geeigneten Attributen und einer Methode `gehalt()`, die das Gehalt berechnet.
#

# %% [markdown] lang="en"
# # Inheritance
#
# In the following we will implement a class hierarchy for employees of a company:
#
# - Employees can be either workers or managers
# - Each employee of the company has a name, a personnel number and a
#   base salary
# - For each worker, the accumulated overtime and the hourly wage
#   are stored in attributes.
# - A worker's salary is calculated as 13/12 times the
#   base salary plus overtime pay
# - Each manager has an individual bonus
# - A manager's salary is calculated as 13/12 times the
#   base salary plus bonus
#
# Implement Python classes `Employee`, `Worker` and `Manager` with
# appropriate attributes and a method `salary()` that calculates the salary.

# %% tags=["solution"]
from dataclasses import dataclass

from numpy import isin

# %% tags=["solution"]
@dataclass
class Mitarbeiter:
    name: str
    pers_nr: str
    grundgehalt: float

    @property
    def gehalt(self):
        return 13 / 12 * self.grundgehalt


# %% tags=["solution"]
@dataclass
class Arbeiter(Mitarbeiter):
    überstunden: float = 0.0
    stundensatz: float = 0.0

    @property
    def gehalt(self):
        return super().gehalt + self.überstunden * self.stundensatz


# %% tags=["solution"]
@dataclass
class Manager(Mitarbeiter):
    bonus: float

    @property
    def gehalt(self):
        return super().gehalt + self.bonus


# %% [markdown] lang="de"
#
# Erzeugen Sie einen Arbeiter mit Namen Hans, Personalnummer 123, einem
# Grundgehalt von  36000.0 Euro, der 3.5 Überstunden zu je 40.0 Euro gearbeit
# hat. Drucken Sie das Gehalt aus.

# %% [markdown] lang="en"
# Create a worker named Hans, personnel number 123, a base salary of 36000.0 Euros, who worked 3.5 hours of overtime at 40.0 euros each. Print out the salary.

# %% tags=["solution"]
a = Arbeiter("Hans", "123", 36_000, 3.5, 40.0)
print(a.gehalt)
a

# %% [markdown] lang="de"
# Schreiben sie Assertions, die die Funktionalität der Klasse `Arbeiter` testen.

# %% [markdown] lang="en"
# Write assertions to test the functionality of the class `Worker`.

# %% tags=["solution"]
# Diese Assertions sind überflüssig! /  These assertions are superfluous!
assert a.name == "Hans"
assert a.pers_nr == "123"
assert a.grundgehalt == 36_000
assert a.überstunden == 3.5
assert a.stundensatz == 40.0

# Diese Assertion sollte vorhanden sein / This is the assertion that should be present
assert a.gehalt == 39_140.0

# %% [markdown] lang="de"
#
# Erzeugen Sie einen Manager mit Namen Sepp, Personalnummer 666, der ein
# Grundgehalt von 60000.0 Euro und einen Bonus von 30000.0 Euro hat. Drucken Sie
# das Gehalt aus.

# %% [markdown] lang="en"
# Create a manager named Sepp, personnel number 666, who is a
# base salary of 60000.0 euros and a bonus of 30000.0 euros. Print out
# the salary.

# %% tags=["solution"]
m = Manager("Sepp", "666", 60_000.0, 30_000.0)
print(m.gehalt)
m

# %% [markdown] lang="de"
# Testen Sie die Funktionalität der `Manager` Klasse.

# %% [markdown] lang="en"
# Test the functionality of the class `Manager`.

# %% tags=["solution"]
assert m.gehalt == 95_000.0


# %% [markdown] lang="de"
# ## Lösung ohne Dataclasses:

# %% [markdown] lang="en"
# ## Solution without dataclasses:

# %% tags=["solution"]
class Mitarbeiter:
    def __init__(self, name, pers_nr, grundgehalt):
        self.name = name
        self.pers_nr = pers_nr
        self.grundgehalt = grundgehalt

    @property
    def gehalt(self):
        return 13 / 12 * self.grundgehalt


# %% tags=["solution"]
class Arbeiter(Mitarbeiter):
    def __init__(self, name, pers_nr, grundgehalt, überstunden, stundensatz):
        super().__init__(name, pers_nr, grundgehalt)
        self.überstunden = überstunden
        self.stundensatz = stundensatz

    def __repr__(self):
        return (
            f"Arbeiter({self.name!r}, {self.pers_nr!r}, {self.grundgehalt}, "
            f"{self.überstunden}, {self.stundensatz})"
        )

    @property
    def gehalt(self):
        return super().gehalt + self.überstunden * self.stundensatz


# %% tags=["solution"]
class Manager(Mitarbeiter):
    def __init__(self, name, pers_nr, grundgehalt, bonus):
        super().__init__(name, pers_nr, grundgehalt)
        self.bonus = bonus

    def __repr__(self):
        return (
            f"Manager({self.name!r}, {self.pers_nr!r}, {self.grundgehalt}, "
            f"{self.bonus})"
        )

    @property
    def gehalt(self):
        return super().gehalt + self.bonus


# %% tags=["solution"]
a = Arbeiter("Hans", 123, 36_000, 3, 40)
print(a.gehalt)
a

# %% tags=["solution"]
m = Manager("Sepp", 666, 60_000, 30_000)
print(m.gehalt)
m


# %% [markdown] lang="de"
#
# # Bank Account
#
# Definieren Sie eine Klasse `BankAccount` mit einem Attribut `balance: float`
# und Methoden `deposit(amount: float)` und `withdraw(amount: float)`.
#
# *Hinweis: Für eine realistischere Implementierung sollte `decimal.Decimal`
# statt `float` verwendet werden.*
#
# Die Klasse soll in folgenden Fällen eine Exception vom Typ `ValueError`
# auslösen:
#
# - Wenn ein neuer `BankAccount` mit negativer `balance` angelegt werden soll.
# - Wenn `deposit` mit einem negativen Wert aufgerufen wird.
# - Wenn `withdraw` mit einem negativen Wert aufgerufen wird oder durch das
#   Abheben des Betrags die `balance` des Kontos negativ werden würde.

# %% [markdown] lang="en"
# # Bank accounts
#
# Define a class `BankAccount` with an attribute `balance: float`
# and methods `deposit(amount: float)` and `withdraw(amount: float)`.
#
# *Note: For a more realistic implementation, `decimal.Decimal`
# can be used instead of `float`.*
#
# The class should throw an exception of type `ValueError` in the following cases:
#
# - If a new `BankAccount` with a negative `balance` is created.
# - If `deposit` is called with a negative value.
# - When `withdraw` is called with a negative value if by withdrawing the desired amount the `balance` attribute of the account would become negative.

# %% tags=["solution"]
from dataclasses import dataclass


@dataclass
class BankAccount:
    balance: float

    def __post_init__(self):
        if self.balance < 0:
            raise ValueError(
                f"Cannot create an account with negative balance: {self.balance}."
            )

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError(f"Cannot deposit a negative amount: {amount}")

    def withdraw(self, amount: float):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                raise ValueError(
                    f"Cannot withdraw {amount} because it exceeds "
                    f"the current balance of {self.balance}."
                )
        else:
            raise ValueError(f"Cannot withdraw a negative amount: {amount}")


# %% [markdown] lang="de"
#
# Testen Sie die Funktionalität der Klasse sowohl für erfolgreiche
# Transaktionen, als auch für Transaktionen, die Exceptions auslösen.

# %% [markdown] lang="en"
# Test the functionality of the class for both successful transactions, as well as for transactions that throw exceptions.

# %% tags=["solution"]
BankAccount(100.0)

# %% tags=["solution"]
try:
    BankAccount(-100)
except ValueError as err:
    print("ERROR:", err)

# %% tags=["solution"]
b = BankAccount(100.0)
b

# %% tags=["solution"]
b.deposit(200.0)
b

# %% tags=["solution"]
try:
    b.deposit(-100.0)
except ValueError as err:
    print("ERROR:", err)

# %% tags=["solution"]
b.withdraw(50.0)
b

# %% tags=["solution"]
try:
    b.withdraw(-200.0)
except ValueError as err:
    print("ERROR:", err)

# %% tags=["solution"]
try:
    b.withdraw(1000.0)
except ValueError as err:
    print("ERROR:", err)


# %% [markdown] lang="de"
# ## Lösung ohne Dataclasses:

# %% [markdown] lang="en"
# ## Solution without dataclasses:

# %% tags=["solution"]
class BankAccount:
    def __init__(self, balance):
        if balance < 0:
            raise ValueError(
                f"Cannot create an account with negative balance: {balance}."
            )
        self.balance = balance

    def __repr__(self):
        return f"BankAccount({self.balance:.2f})"

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError(f"Cannot deposit a negative amount: {amount}")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError(f"Cannot withdraw a negative amount: {amount}")
        if amount > self.balance:
            raise ValueError(
                f"Cannot withdraw {amount} because it exceeds "
                f"the current balance of {self.balance}."
            )
        self.balance -= amount


# %% tags=["solution"]
BankAccount(100.0)

# %% tags=["solution"]
try:
    BankAccount(-100)
except ValueError as err:
    print("ERROR:", err)

# %% tags=["solution"]
b = BankAccount(100.0)
b

# %% tags=["solution"]
b.deposit(200.0)
b

# %% tags=["solution"]
try:
    b.deposit(-100.0)
except ValueError as err:
    print("ERROR:", err)

# %% tags=["solution"]
b.withdraw(50.0)
b

# %% tags=["solution"]
try:
    b.withdraw(-200.0)
except ValueError as err:
    print("ERROR:", err)

# %% tags=["solution"]
try:
    b.withdraw(1000.0)
except ValueError as err:
    print("ERROR:", err)

# %% [markdown] lang="de"
# # Protokolle
#
# Implementieren Sie ein zur Laufzeit überprüfbares Protokoll `SupportsConnect`,
# das Instanzen von Klassen beschreibt, die eine Methode `connect(self, device)`
# haben.

# %% [markdown] lang="en"
# # Protocols
#
# Implement a runtime checkable protocol `SupportsConnect`,
# which describes instances of classes that have a method `connect(self, device)`.

# %% tags=["solution"]
from typing import Protocol, runtime_checkable

# %% tags=["solution"]
@runtime_checkable
class SupportsConnect(Protocol):
    def connect(self, device):
        ...


# %% [markdown] lang="de"
#
# Implementieren Sie Klassen `Plugboard` und `PatchCord`, die das
# `SupportsConnect` Protokoll unterstützen.

# %% [markdown] lang="en"
# Implement classes `Plugboard` and `PatchCord` that support the `SupportsConnect` protocol.

# %% tags=["solution"]
class Plugboard:
    def connect(self, device):
        print("Connecting plugboard to device.")

# %% tags=["solution"]
issubclass(Plugboard, SupportsConnect)

# %% tags=["solution"]
class PatchCord:
    def connect(self, device):
        print("Connecting patch cord to device.")

# %% tags=["solution"]
issubclass(PatchCord, SupportsConnect)

# %% [markdown] lang="de"
# Erfüllt die folgende Klasse das Protokoll `SupportsConnect`? Lässt sich das
# zur Laufzeit feststellen?

# %% [markdown] lang="en"
# Does the following class comply with the `SupportsConnect` protocol? Is it possible to determine this at runtime?

# %% 
class SelfConnector:
    def connect(self):
        print("Connecting to self!")

# %% tags=["solution"]
issubclass(SelfConnector, SupportsConnect)

# %%
