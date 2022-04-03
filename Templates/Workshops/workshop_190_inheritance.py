# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
# j2 import 'macros.j2' as doc
# %% [markdown]
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

# %% tags=["solution"]
from dataclasses import dataclass

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


# %% [markdown]
#
# Erzeugen Sie einen Arbeiter mit Namen Hans, Personalnummer 123, einem
# Grundgehalt von  36000.0 Euro, der 3.5 Überstunden zu je 40.0 Euro gearbeit
# hat. Drucken Sie das Gehalt aus.

# %% tags=["solution"]
a = Arbeiter("Hans", "123", 36_000, 3.5, 40.0)
print(a.gehalt)
a

# %% [markdown]
#
# Erzeugen Sie einen Manager mit Namen Sepp, Personalnummer 666, der ein
# Grundgehalt von 60000.0 Euro und einen Bonus von 30000.0 Euro hat. Drucken Sie
# das Gehalt aus.

# %% tags=["solution"]
m = Manager("Sepp", "666", 60_000.0, 30_000.0)
print(m.gehalt)
m

# %% [markdown]
#
# Lösung ohne Dataclasses:

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


# %% [markdown]
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


# %% [markdown]
#
# Testen Sie die Funktionalität der Klasse sowohl für erfolgreiche
# Transaktionen, als auch für Transaktionen, die Exceptions auslösen.

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


# %% [markdown]
#
#  # Lesen und Schreiben in Dateien
#
# Schreiben Sie eine Funktion `write_text_to_file(text: str, file_name: str) ->
# None`, die den String `text` in die Datei `file_name` schreibt, sofern diese
# *nicht* existiert und eine Exception vom Typ `FileExistsError` wirft, falls
# die Datei existiert.
#
# *Hinweis:*  Beachten Sie die möglichen Werte für das `mode` Argument von
# `open()`.

# %% tags=["solution"]
def write_text_to_file(text, file_name):
    with open(file_name, "x") as file:
        file.write(text)


# %% [markdown]
#
# Testen Sie die Funktion, indem Sie zweimal hintereinander versuchen den Text
# `Python 3.8` in die Datei `my-private-file.txt` zu schreiben.

# %% tags=["solution"]
write_text_to_file("Python 3.8", "my_private_file.txt")

# %% tags=["solution"]
# write_text_to_file('Python 3.8', 'my_private_file.txt')


# %% [markdown]
#
#  Schreiben Sie eine Funktion `annotate_file(file_name: str) -> None`, die
# - den Inhalt der Datei `file_name` gefolgt von dem Text `(annotated version)`
#   auf dem Bildschirm ausgibt, falls sie existiert
# - den Text `No file found, we will bill the time we spent searching.` ausgibt
#   falls sie nicht existiert
# - in beiden Fällen den Text `Our invoice will be sent by mail.` ausgibt.

# %% tags=["solution"]
def annotate_file(file_name):
    try:
        with open(file_name, "r") as file:
            print(file.read())
            print("(annotated version)")
    except FileNotFoundError:
        print("No file found, we will bill the time we spent searching.")
    finally:
        print("Our invoice will be sent by mail.")


# %% tags=["solution"]
annotate_file("my_private_file.txt")

# %% tags=["solution"]
annotate_file("does-not-exist.txt")


# %%
