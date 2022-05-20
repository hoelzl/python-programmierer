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
# # Erzeugen von NumPy Arrays

# %% [markdown] lang="en"
# # Creating NumPy arrays

# %% tags=["solution"]
import numpy as np

# %% [markdown] lang="de"
# Erzeugen Sie folgende NumPy Arrays:

# %% [markdown] lang="en"
# Create the following NumPy arrays:

# %% [markdown] lang="de"
# ```python
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# ```

# %% [markdown] lang="en"
# ```pythons
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# ```

# %% tags=["solution"]
np.arange(10)

# %% [markdown] lang="de"
# ```python
# array([0.  , 1.25, 2.5 , 3.75, 5.  ])
# ```

# %% [markdown] lang="en"
# ```pythons
# array([0. , 1.25, 2.5 , 3.75, 5. ])
# ```

# %% tags=["solution"]
np.linspace(0, 5, 5)

# %% [markdown] lang="de"
# ```python
# array([ 1,  3, 12, 92])
# ```

# %% [markdown] lang="en"
# ```pythons
# array([ 1, 3, 12, 92])
# ```

# %% tags=["solution"]
np.array([1, 3, 12, 92])

# %% [markdown] lang="de"
# ```python
# array([[1, 2, 3, 4],
#        [5, 6, 7, 8]])
# ```

# %% [markdown] lang="en"
# ```pythons
# array([[1, 2, 3, 4],
#        [5, 6, 7, 8]])
# ```

# %% tags=["solution"]
np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# %% [markdown] lang="de"
# ```python
# array([[[0, 2, 4, 6],
#         [1, 3, 5, 7]],
#
#        [[1, 2, 3, 4],
#         [5, 6, 7, 8]],
#
#        [[9, 8, 7, 6],
#         [5, 4, 3, 2]]])
# ```

# %% [markdown] lang="en"
# ```pythons
# array([[[0, 2, 4, 6],
#         [1, 3, 5, 7]],
#
#        [[1, 2, 3, 4],
#         [5, 6, 7, 8]],
#
#        [[9, 8, 7, 6],
#         [5, 4, 3, 2]]])
# ```

# %% tags=["solution"]
np.array(
    [
        [[0, 2, 4, 6], [1, 3, 5, 7]],
        [[1, 2, 3, 4], [5, 6, 7, 8]],
        [[9, 8, 7, 6], [5, 4, 3, 2]],
    ]
)

# %% tags=["solution"]
np.array(
    [
        [range(0, 7, 2), range(1, 8, 2)],
        [range(1, 5), range(5, 9)],
        [range(9, 5, -1), range(5, 1, -1)],
    ]
)

# %% [markdown] lang="de"
# Ein $2\times 8$ Array, das gleichverteilte Zufallszahlen in $[0, 1)$ enthält.

# %% [markdown] lang="en"
# A $2\times 8$ array containing uniformly distributed random numbers in $[0, 1)$.

# %% tags=["solution"]
np.random.rand(2, 8)

# %% [markdown] lang="de"
# ```python
# array([[1., 0., 0.],
#        [0., 1., 0.],
#        [0., 0., 1.]])
# ```

# %% [markdown] lang="en"
# ```pythons
# array([[1st, 0th, 0th],
#        [0th, 1st, 0th],
#        [0th, 0th, 1st]])
# ```

# %% tags=["solution"]
np.eye(3)

# %% [markdown] lang="de"
# Einen Vektor der Länge 5, der normalverteilte Zahlen enthält.

# %% [markdown] lang="en"
# A vector of length 5 containing normally distributed numbers.

# %% tags=["solution"]
np.random.standard_normal(5)

# %% [markdown] lang="de"
# Ein $3 \times 4$ Array, das normalverteilte Zahlen mit Mittelwert $5$ und Standardabweichung $0.5$ enthält.

# %% [markdown] lang="en"
# A $3 \times 4$ array containing normally distributed numbers with mean $5$ and standard deviation $0.5$.

# %% tags=["solution"]
np.random.normal(5, 0.5, (3, 4))

# %% [markdown] lang="de"
# ## Gleichungssysteme
#
# Lösen Sie folgendes Gleichungssystem:
#
# $x_1 - x_2 + 2x_3 = 6$
#
# $2x_1 + 3x_2 + 2x_3 = 8$
#
# $3x_1 + 2x_2 + x_3 = 8$

# %% [markdown] lang="en"
# ## Systems of equations
#
# Solve the following system of equations:
#
# $x_1 - x_2 + 2x_3 = 6$
#
# $2x_1 + 3x_2 + 2x_3 = 8$
#
# $3x_1 + 2x_2 + x_3 = 8$

# %% tags=["solution"]
a = np.array([[1.0, -1.0, 2.0], [2.0, 3.0, 2.0], [3.0, 2.0, 1.0]])
b = np.array([6.0, 8.0, 8.0])

# %% tags=["solution"]
import scipy.linalg as linalg

lu = linalg.lu_factor(a)

# %% tags=["solution"]
x = linalg.lu_solve(lu, b)

# %% tags=["solution"]
x

# %% tags=["solution"]
a.dot(x)

# %% [markdown] lang="de"
# # Erzeugen von NumPy Arrays 2
#
# Erzeugen Sie das folgende NumPy Array:
#
# ```python
# array([[ 0,  2,  4,  6],
#        [ 8, 10, 12, 14],
#        [16, 18, 20, 22],
#        [24, 26, 28, 30],
#        [32, 34, 36, 38]])
# ```

# %% [markdown] lang="en"
# # Create NumPy arrays 2
#
# Create the following NumPy array:
#
# ```pythons
# array([[ 0, 2, 4, 6],
#        [8, 10, 12, 14],
#        [16, 18, 20, 22],
#        [24, 26, 28, 30],
#        [32, 34, 36, 38]])
# ```

# %% tags=["solution"]
np.arange(0, 40, 2).reshape(5, 4)

# %% [markdown] lang="de"
# Erzeugen Sie das folgende NumPy Array:
#
# ```python
# array([[10, 19, 28, 37, 46, 55],
#        [13, 22, 31, 40, 49, 58],
#        [16, 25, 34, 43, 52, 61]])
# ```

# %% [markdown] lang="en"
# Create the following NumPy array:
#
# ```pythons
# array([[10, 19, 28, 37, 46, 55],
#        [13, 22, 31, 40, 49, 58],
#        [16, 25, 34, 43, 52, 61]])
# ```

# %% tags=["solution"]
np.arange(10, 64, 3).reshape(3, 6, order="F")

# %% [markdown] lang="de"
# # Extrema
#
# Erzeugen Sie einen Vektor der Länge 100 mit Zufallswerten, die im Intervall
# $[10, 20)$ gleichverteilt sind.
#
# Berechnen Sie Minimum und Maximum der im Vektor
# enthaltenen Werte sowie die Positionen von Minimum und Maximum.

# %% [markdown] lang="en"
# # Extreme values
#
# Generate a vector of length 100 containing random values equally
# distributed in the interval $[10, 20)$.
#
# Calculate minimum and maximum of the values
# contained in the vector as well as the indices of minimum and maximum.

# %% tags=["solution"]
vec = np.random.random(100) * 10 + 10
vec[:10]

# %% tags=["solution"]
vec.min()

# %% tags=["solution"]
vec.argmin()

# %% tags=["solution"]
vec.max()

# %% tags=["solution"]
vec.argmax()

# %% [markdown] lang="de"
# # Mittelwert
#
# Erzeugen Sie ein $6 \times 8$ Array, das standardverteilten Zahlen mit
# Mittelwert $2$ und Standardabweichung $1$ enthält.
#
#

# %% [markdown] lang="en"
#
# # Average
#
# Create a $6 \times 8$ array with numbers normally distributed with
# mean $2$ and standard deviation $1$.

# %% tags=["solution"]
my_array = np.random.normal(2.0, 1.0, (6, 8))

# %% [markdown] lang="de"
# Berechnen Sie den Mittelwert aller darin vorkommenden Werte.
#

# %% [markdown] lang="en"
# Calculate the mean of all values in the array.

# %% tags=["solution"]
my_array.mean()

# %% [markdown] lang="de"
# Berechnen Sie die zeilen- und spaltenweisen Mittelwerte.

# %% [markdown] lang="en"
# Calculate the row and column means.

# %% tags=["solution"]
my_array.mean(axis=0)

# %% tags=["solution"]
my_array.mean(axis=1)

# %% [markdown] lang="de"
# Berechnen Sie den Mittelwert aller vorkommenden Werte ohne Verwendung der
# Methode `mean()`.

# %% [markdown] lang="en"
# Calculate the mean of all  values in the array without using the
# `mean()` method.

# %% tags=["solution"]
mean = my_array.sum() / my_array.size
mean

# %% [markdown] lang="de"
# Berechnen Sie die zeilen- und spaltenweisen Mittelwerte ohne Verwendung der
# Methode `mean()`.

# %% [markdown] lang="en"
# Calculate the row and column means without using the
# `mean()` method.

# %% tags=["solution"]
my_array.sum(axis=0) / my_array.shape[0]

# %% tags=["solution"]
my_array.sum(axis=1) / my_array.shape[1]

# %% [markdown] lang="de"
# # Roulette
#
# Analysieren Sie die Gewinnerwartung eines Spielers in folgender
# vereinfachter Form eines Roulettespiels mittels Monte Carlo Simulation:
#
# - Der Kessel ist in 36 Zahlen unterteilt.
# - Der Spieler wählt eine der Zahlen 1 bis 36 und wettet 1 Euro.
# - Fällt die Kugel auf die gewählte Zahl, so erhält der Spieler seinen Einsatz
#   plus 35 Euro zurück.
# - Andernfalls verliert der Spieler seinen Einsatz.
#
# Schreiben Sie eine Version der Simulation mit `for`-Schleife in Python und
# testen Sie die Performance dieser Version vor und nach Kompilierung mit
# Numba. Schreiben Sie dann eine vektorisierte Version und testen Sie deren
# Performance in beiden Fällen.
#
# *Hinweise:*
# - Die NumPy Bibliothek enthält eine Funktion
#   `np.random.randint(low, high, size=None)`, mit der Sie ein Array mit Shape
#   `size` erzeugen können, das gleichverteilte Zufallszahlen zwischen `low`
#   (inklusive) und `high` (exklusive) enthält.
# - Wird `np.random.randint()` mit nur zwei Argumenten aufgerufen, so gibt es
#   eine einzige Zahl zurück.
# - Die NumPy Bibliothek enthält eine Funtion
#   `np.random.binomial(n, p, size=None)`, mit der Sie binomialverteilte
#   Zufallszahlen erzeugen können.

# %% [markdown] lang="en"
# # Roulette
#
# Use Monte Carlo simulation to analyze a player's winning expectation in the following simplified form of a roulette game:
#
# - The croupier spins a wheel divided into 36 equal segments, numbered from 1 to 36.
# - The player chooses one of the numbers 1 to 36 and bets 1 euro.
# - If the ball lands on the selected number, the player receives his bet
#   plus 35 euros back.
# - Otherwise, the player loses his bet.
#
# Write a version of the simulation with a `for` loop in Python and
# test the performance of this version before and after compilation with
# Numba. Then write a vectorized version and test the
# performance with and without compiling it with Numba.
#
# *Notes:*
# - The NumPy library contains a function
#   `np.random.randint(low, high, size=None)`, which you can use to
#   create an array with Shape `size` containing uniformly distributed
#   random numbers between `low` (inclusive) and `high` (exclusive).
# - If `np.random.randint()` is called with only two arguments it returns
#   a single number.
# - The NumPy library contains a function
#   `np.random.binomial(n, p, size=None)` with which you can generate
#   binomially distributed random numbers.

# %% tags=["solution"]
import numpy as np


# %% tags=["solution"]
def roulette1(n):
    # We can assume that the player always bets on the 1
    # Wir können davon ausgehen, dass der Spieler immer auf die 1 wettet
    money_spent = 0
    money_won = 0
    for i in range(n):
        money_spent += 1
        if np.random.randint(1, 37) == 1:
            money_won += 36
    return (money_won - money_spent) / n


# %% tags=["solution"]
def test_roulette(roulette):
    np.random.seed(123)
    for n in [1000, 100_000, 1_000_000]:
        # %time print(f"Gewinnerwartung ist {100 * roulette(n):.1f}% ({n} Versuche)")


# %% tags=["solution"]
test_roulette(roulette1)

# %% tags=["solution"]
import numba

roulette1_nb = numba.jit(roulette1)

# %% tags=["solution"]
test_roulette(roulette1_nb)


# %% tags=["solution"]
def roulette2(n):
    money_spent = np.ones(n)
    money_won = np.random.binomial(1, 1.0 / 36.0, n) * 36
    return (money_won - money_spent).sum() / n


# %% tags=["solution"]
test_roulette(roulette2)

# %% tags=["solution"]
roulette2_nb = numba.jit(roulette2)

# %% tags=["solution"]
test_roulette(roulette2_nb)


# %% tags=["solution"]
def roulette3(n):
    money_spent = n
    money_won = np.random.binomial(n, 1.0 / 36.0) * 36
    return (money_won - money_spent) / n


# %% tags=["solution"]
test_roulette(roulette3)

# %% tags=["solution"]
roulette3_nb = numba.jit(roulette3)

# %% tags=["solution"]
test_roulette(roulette3_nb)

# %%
