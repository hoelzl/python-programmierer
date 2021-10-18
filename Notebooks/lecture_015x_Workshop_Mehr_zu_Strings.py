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
# # Vergleiche auf Strings

# %% [markdown]
# Ist `Abc` kleiner als `aBC`?

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# Ist gleichzeitig `abc` kleiner als `abcd` und `abcd` kleiner als `abd`?

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# # Begrüßung 1
#
# Schreiben Sie eine Funktion `drucke_begrüßung(name)`, die eine personalisierte Begrüßung ausgibt, z.B.
# ```
# Hallo, Hans!
# Schön Sie heute wieder bei uns begrüßen zu dürfen.
# Wir wünschen Ihnen viel Spaß, Hans.
# ```
# Verwenden Sie dazu die `print()`-Funktion mit einem Argument und String-Konkatenation.

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# # Begrüßung 2
#
# Schreiben Sie eine Funktion `drucke_begrüßung(name)`, die die Funktionalität von
# `drucke_begrüßung(name)` mittels F-Strings implementiert.

# %% pycharm={"name": "#%%\n"}

# %% [markdown]
# # Piraten, Teil 4
#
# Das Ausdrucken der Beute-Aufteilund mittels `drucke_aufteilung_der_beute(dublonen, piraten)` verbraucht zu viel Papier.
#
# Implementieren Sie eine neue Version der Funktion, die den folgenden Text ausgibt:
#
# ```
# Jeder der 8 Piraten erhält 2 der 17 Golddublonen. Der Kapitän erhält extra 1 Golddublone.
# ```
# bzw.
# ```
# Jeder der 8 Piraten erhält 2 der 17 Golddublonen. Der Kapitän erhält extra 2 Golddublonen.
# ```
#
# Verwenden Sie F-Strings um die Ausgabetexte zu erzeugen.
# Sie können die folgende Funktion verwenden, um die Aufteilung der Beute zu berechnen:

# %% pycharm={"name": "#%%\n"}
def teile_beute_auf(dublonen, piraten):
    dublonen_pro_pirat = dublonen // piraten
    dublonen_kapitän = dublonen % piraten
    return dublonen_pro_pirat, dublonen_kapitän

# %% pycharm={"name": "#%%\n"}


