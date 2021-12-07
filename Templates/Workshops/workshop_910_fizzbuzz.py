# ---
# jupyter:
#   jupytext:
#     formats: py:percent
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

# j2 import 'macros.j2' as doc
# %% [markdown]
# ## Extra Credits: FizzBuzz
#
# Schreiben Sie eine Funktion `fizz_buzz(n)`, die die Zahlen von 1 bis `n`
# ausgibt aber dabei
#
# - jede Zahl, die durch 3 teilbar ist, durch `Fizz` ersetzt
# - jede Zahl, die durch 5 teilbar ist, durch `Buzz` ersetzt
# - jede Zahl, die durch 3 und 5 teilbar ist, durch `FizzBuzz` ersetzt
#
# Zum Beispiel soll `fizz_buzz(31)` die folgende Ausgabe erzeugen:
#
# ```
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# 19
# Buzz
# Fizz
# 22
# 23
# Fizz
# Buzz
# 26
# Fizz
# 28
# 29
# FizzBuzz
# 31
# ```

# %% {{ doc.solution() }}
def fizz_buzz(n):
    for n in range(1, n+1):
        if n % 15 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)


# %% {{ doc.solution() }}
fizz_buzz(31)
