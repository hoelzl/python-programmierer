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

# %% [markdown]
# # Operatoren, Vergleiche
#
# Ist $2^{16}$ größer als $32\,000\,\,/\,\,2$?

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Ist $72$ ohne Rest durch $3$ teilbar?

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Ist $72$ eine gerade Zahl (d.h. ohne Rest durch 2 teilbar)?

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Schreiben Sie eine Funktion `ist_teilbar_durch(m, n)` die (genau dann) `True` zurückgibt, wenn `m` ohne Rest durch `n` teilbar ist

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Schreiben Sie eine Funktion `ist_teilbar_durch_2_und_3(n)`, die genau dann `True` zurückgibt, wenn `n` ohne Rest durch $2$ und durch $3$ teilbar ist.

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Testen Sie, ob $72$ ohne Rest durch $2$ und durch $3$ teilbar ist.

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# # Volljährig
#
# Schreiben Sie eine Funktion `drucke_volljährig(alter)`, die `Volljährig` auf dem Bildschirm ausgibt, wenn `alter >= 18` ist und `Minderjährig` sonst.

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Testen Sie `drucke_volljährig(alter)` mit den Werten 17 und 18.

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# # Einkaufsliste
#
# Definieren Sie Variablen
# - `meine_einkaufsliste`, die die Strings `Tee` und `Kaffee` enthält,
# - `eine_andere_einkaufsliste`, die ebenfalls die Strings `Tee` und `Kaffee` enthält.

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
#
# Definieren Sie eine Funktion `drucke_einkaufsliste(einkaufsliste)`, die die als Argument übergebene
# Einkaufsliste ausdruckt:
#
# ```
# Einkaufsliste:
#   Tee
#   Kaffee
# ```

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Testen Sie die Funktion `drucke_einkaufsliste(einkaufsliste)` mit beiden Einkaufslisten.

# %% pycharm={"name": "#%%\n"}

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Definieren Sie eine Funktion `kaufe(produkt, einkaufsliste)`, das `produkt` zu  `einkaufsliste` hinzufügt.

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Fügen Sie `Butter` und `Brot` zur Einkaufsliste `meine_einkaufsliste` hinzu.

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Drucken Sie beide Einkauslisten nochmal aus.

# %% pycharm={"name": "#%%\n"}

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Was passiert, wenn Sie `Butter` und `Brot` nochmals zur Einkaufsliste `meine_einkaufsliste` hinzufügen?

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# # Ausgabe von Quadratzahlen
#
# Schreiben Sie eine Funktion `drucke_quadrate(m, n)`, die die Quadrate der Zahlen zwischen `m` und `n` (einschließlich) in der folgenden Form ausgibt:
#
# ```
# Das Quadrat von 5 ist 25
# Das Quadrat von 6 ist 36
# Das Quadrat von 7 ist 49
# ```

# %%

# %% [markdown]
# Testen Sie die Funktion mit Argumenten 5, 7

# %%

# %% [markdown]
# # Verbesserte Einkaufsliste
#
# In dieser Aufgabe wollen wir eine verbesserte Version der Einkaufsliste definieren,
# in der sowohl die Einkaufsliste als auch die Einträge durch benutzerdefinierte
# Datentypen repräsentiert werden. Jeder Eintrag soll das Produkt und die davon
# benötigte Menge enthalten.
#
# Definieren Sie eine Klasse `Item`, die Attribute für Produkt und Menge hat.
# `Item` soll eine `__repr__`-Methode haben, die das Item in einer angemessenen Form darstellt.

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Erzeugen sie ein Item, das 500g Kaffee repräsentiert:

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Definieren Sie eine Klasse `ShoppingList`, die eine Liste von `Item`-Instanzen
# beinhaltet:
#
# - Der Konstruktor `__init__(self, items=[])` erzeugt eine Einkaufsliste, die
#   die Einträge `items` enthält (jedes Element von `items` soll eine `Item`-Instanz
#   sein).
# - Die Methode `shopping_list.add_item(item: Item)` fügt ein `Item` zur Einkaufsliste
#   `shopping_list` hinzu.
# - Die Methode `print()` druckt die Einkaufsliste aus.
#
# `ShoppingList` soll eine `__repr__`-Methode haben, die die Einkaufsliste in
# einer geeigneten Form darstellt.

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Definieren Sie Variable `meine_einkaufsliste`, die eine Einkaufsliste mit folgenden Items repräsentiert:
# - 2 Pakete Tee,
# - 1 Paket Kaffee

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Drucken Sie `meine_einkaufsliste` aus.

# %% pycharm={"name": "#%%\n"}

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Fügen Sie  250 g Butter und  1 Laib Brot zur Einkaufsliste `meine_einkaufsliste` hinzu.

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Drucken Sie die Einkausliste nochmal aus.

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Was passiert, wenn Sie `Butter` und `Brot` nochmals zur Einkaufsliste `meine_einkaufsliste` hinzufügen?

# %% pycharm={"name": "#%%\n"}



