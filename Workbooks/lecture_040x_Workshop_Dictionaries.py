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

# %% [markdown] pycharm={"name": "#%% md\n"}
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

# %% pycharm={"is_executing": false, "name": "#%%\n"}

# %% [markdown] pycharm={"name": "#%% md\n"}
# Testen Sie Ihre Implementierung mit dem folgenden String:

# %% pycharm={"is_executing": false, "name": "#%%\n"}
dickens = "It was the best of times it was the worst of times"

# %% pycharm={"name": "#%%\n"}


