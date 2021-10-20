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

# %%
from dataclasses import dataclass

# %%
@dataclass
class Mitarbeiter:
    name: str
    pers_nr: str
    grundgehalt: float

    def gehalt(self):
        return 13 / 12 * self.grundgehalt


# %%
@dataclass
class Arbeiter(Mitarbeiter):
    überstunden: float = 0.0
    stundensatz: float = 0.0

    def gehalt(self):
        return super().gehalt() + self.überstunden * self.stundensatz


# %%
@dataclass
class Manager(Mitarbeiter):
    bonus: float

    def gehalt(self):
        return super().gehalt() + self.bonus


# %% [markdown]
#
# Erzeugen Sie einen Arbeiter mit Namen Hans, Personalnummer 123, einem
# Grundgehalt von  36000.0 Euro, der 3.5 Überstunden zu je 40.0 Euro gearbeit
# hat. Drucken Sie das Gehalt aus.

# %%
a = Arbeiter("Hans", "123", 36_000, 3.5, 40.0)
print(a.gehalt())
a

# %% [markdown]
#
# Erzeugen Sie einen Manager mit Namen Sepp, Personalnummer 666, der ein
# Grundgehalt von 60000.0 Euro und einen Bonus von 30000.0 Euro hat. Drucken Sie
# das Gehalt aus.

# %%
m = Manager("Sepp", "666", 60_000.0, 30_000.0)
print(m.gehalt())
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

# %%
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

# %%
BankAccount(100.0)

# %%
try:
    BankAccount(-100)
except ValueError as err:
    print("ERROR:", err)

# %%
b = BankAccount(100.0)
b

# %%
b.deposit(200.0)
b

# %%
try:
    b.deposit(-100.0)
except ValueError as err:
    print("ERROR:", err)

# %%
b.withdraw(50.0)
b

# %%
try:
    b.withdraw(-200.0)
except ValueError as err:
    print("ERROR:", err)

# %%
try:
    b.withdraw(1000.0)
except ValueError as err:
    print("ERROR:", err)

# %%
