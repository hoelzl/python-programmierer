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

# %% [markdown] slideshow={"slide_type": "slide"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <h1 style="text-align:center;">Python: Dictionaries</h1>
# <h2 style="text-align:center;">Coding Akademie München GmbH</h2>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <div style="text-align:center;">Allaithy Raed</div>

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Dictionaries
#
# Indizes in Listen
#
# - können nur Integer-Werte sein
# - müssen ein Intervall von 0 bis `len(liste) - 1` umfassen
#
# Elemente in einer Liste sind sortiert.

# %% pycharm={"is_executing": false}
non_sparse = [0] * 10
non_sparse[0] = 1
non_sparse[9] = 1
non_sparse

# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "subslide"}
# Dictionaries sind eine Datenstruktur, in der Indizes
#
# - viele verschiedene Typen haben können:
#   - Integer-Werte
#   - Strings
#   - Tupel
#   - ...
#
# Im Gegensatz zu Listen sind die Elemente in einem Dictionary nicht in einer
# bestimmten Reihenfolge angeordnet.

# %% pycharm={"is_executing": false} slideshow={"slide_type": "subslide"}
sparse = {0: 1, 9: 1}

# %% pycharm={"is_executing": false}
sparse

# %% pycharm={"is_executing": false, "name": "#%%\n"}
sparse[0]

# %% pycharm={"is_executing": false, "name": "#%%\n"}
# Fehler
# sparse[1]

# %% pycharm={"is_executing": false, "name": "#%%\n"}
sparse[12] = 3
print(sparse[12])
sparse

# %% pycharm={"is_executing": false} slideshow={"slide_type": "subslide"}
translations = {'snake': 'Schlange', 'bat': 'Fledermaus', 'horse': 'Hose', 'bird': 'Vogel'}

# %% pycharm={"is_executing": false}
print(translations['snake'])
print(translations.get('bat', '<unbekannt>'))
print(translations.get('monkey', 'Affe'))
print(translations.get('tree'))

# %% pycharm={"is_executing": false}
# Fehler:
# translations['monkey']
translations

# %% pycharm={"is_executing": false} slideshow={"slide_type": "subslide"}
translations['horse'] = 'Pferd'
translations['horse']

# %% pycharm={"is_executing": false, "name": "#%%\n"}
del translations['bird']
print(translations.get('bird', '<unbekannt>'))
print(translations.setdefault('bird', 'Vogel'))
print(translations.setdefault('bird', '<auch unbekannt>'))
print(translations.get('bird', '<unbekannt>'))

# %% pycharm={"is_executing": false} slideshow={"slide_type": "subslide"}
for key in translations:
    print(key, end=" ")

# %%
for key in translations.keys():
    print(key, end=" ")

# %% pycharm={"is_executing": false}
for val in translations.values():
    print(val, end=" ")

# %% pycharm={"is_executing": false} slideshow={"slide_type": "subslide"}
for item in translations.items():
    print(item, end=" ")

# %% pycharm={"is_executing": false}
for key, val in translations.items():
    print("Key:", key, "\tValue:", val)


# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `lecture_040x_Workshop_Dictionaries`
# - Abschnitt "Worthäufigkeiten"

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Workshop
#
# - Notebook `lecture_042x_Workshop_Todo-Liste V0`
# - Abschnitt "TODO-Liste Version 0"
