# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] lang="de"
# ## Worthäufigkeiten
#
# Schreiben Sie eine Funktion `zähle_worte(text: str) -> dict`, die ein
# Dictionary zurückgibt, das die Anzahl der Vorkommen aller Worte in `text`
# enthält. Zum Beispiel soll
#
# ```
# zähle_worte("It was the best of times it was the worst of times")
# ```
#
# folgendes Dictionary zurückgeben:
#
# ```
# { 'it': 2,
#   'was': 2,
#   'the': 2,
#   'best': 1,
#   'of': 2,
#   'times': 2,
#   'worst': 1
# }
# ```
# Beachten Sie, dass alle Wörter in Kleinbuchstaben umgewandelt wurden.
#
# ###  Hinweise
# - Sie können einen String mit der Methode `string.split()` in eine
#   Liste von Wörtern umwandeln
# - Sie können einen String mit der Methode `string.lower()` in einen String
#   umwandeln, der nur aus Kleinbuchstaben besteht.

# %% [markdown] lang="en"
# ## Word frequencies
#
# Write a function `count_words(text: str) -> dict` that returns a dictionary containing the number of occurrences of all words in `text`. For example,
#
# ```
# count_words("It was the best of times it was the worst of times")
# ```
#
# should return the following dictionary:
#
# ```
# { 'it': 2,
#   'what': 2,
#   'the': 2,
#   'best': 1,
#   'of': 2,
#   'times': 2,
#   'worst': 1
# }
# ```
# Note that all words have been converted to lowercase.
#
# ###  Hints
# - You can convert a string into a list of words using the `string.split()` method
# - You can convert a string into a string containing only lower-case letters using the `string.lower()` method.

# %% tags=["solution"]
def zähle_worte(text: str) -> dict:
    words = text.lower().split()
    result = {}
    for word in words:
        count = result.get(word, 0)
        result[word] = count + 1
    return result


# %% [markdown] lang="de"
# Testen Sie Ihre Implementierung mit dem folgenden String:

# %% [markdown] lang="en"
# Test your implementation with the following string:

# %%
dickens = "It was the best of times it was the worst of times"

# %% tags=["solution"]
zähle_worte(dickens)

# %% tags=["solution"]
from pprint import pprint

pprint(zähle_worte(dickens), width=30)

# %% tags=["solution"]
help(pprint)

# %%
