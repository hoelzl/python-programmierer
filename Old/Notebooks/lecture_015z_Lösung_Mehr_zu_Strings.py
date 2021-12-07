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
# # Shout
#
# Schreiben Sie eine Funktion `shout(text)`, die `text` in Großbuchstaben, gefolgt von drei Außrufezeichen auf dem Bildschirm ausgibt.

# %%
def shout(text):
    print(f"{text.upper()}!!!")


# %% [markdown]
# Testen Sie die Funktion mit Argument `"Hallo"`

# %%
shout("Hallo")

# %% [markdown] pycharm={"name": "#%% md\n"}
# # Vergleichen von Strings

# %% [markdown]
# Ist `Abc` kleiner als `aBC`?

# %% pycharm={"name": "#%%\n"}
'Abc' < 'aBC'

# %% [markdown]
# Ist gleichzeitig `abc` kleiner als `abcd` und `abcd` kleiner als `abd`?

# %% pycharm={"name": "#%%\n"}
'abc' < 'abcd' < 'abd'


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
def drucke_begrüßung(name):
    print('Hallo, ' + name + '!\n' +
          'Schön Sie heute wieder bei uns begrüßen zu dürfen.\n' +
          'Wir wünschen Ihnen viel Spaß, ' + name + '.')

drucke_begrüßung('Hans')


# %% [markdown]
# # Begrüßung 2
#
# Schreiben Sie eine Funktion `drucke_begrüßung(name)`, die die Funktionalität von
# `drucke_begrüßung(name)` mittels F-Strings implementiert.

# %% pycharm={"name": "#%%\n"}
def drucke_begrüßung_2(name):
    print(f'Hallo, {name}!\n'
          f'Schön Sie heute wieder bei uns begrüßen zu dürfen.'
          f'Wir wünschen Ihnen viel Spaß, {name}.')

drucke_begrüßung_2("Sepp")


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
def drucke_aufteilung_der_beute(dublonen, piraten):
    dublonen_pro_pirat, dublonen_kapitän = teile_beute_auf(dublonen, piraten)
    if dublonen_kapitän == 1:
        print(f'Jeder der {piraten} Piraten erhält {dublonen_pro_pirat} '
              f'der {dublonen} Golddublonen. '
              f'Der Kapitän erhält extra 1 Golddublone.')
    else:
        print(f'Jeder der {piraten} Piraten erhält {dublonen_pro_pirat} '
              f'der {dublonen} Golddublonen. '
              f'Der Kapitän erhält extra {dublonen_kapitän} Golddublonen.')



# %% pycharm={"name": "#%%\n"}
drucke_aufteilung_der_beute(1000, 11)
drucke_aufteilung_der_beute(17, 8)


# %% pycharm={"name": "#%%\n"}
def drucke_aufteilung_der_beute_v2(dublonen, piraten):
    dublonen_pro_pirat, dublonen_kapitän = teile_beute_auf(dublonen, piraten)
    print(f'Jeder der {piraten} Piraten erhält {dublonen_pro_pirat} '
          f'der {dublonen} Golddublonen. '
          f'Der Kapitän erhält extra {dublonen_kapitän} Golddublone'
          f'{"" if dublonen_kapitän == 1 else "n"}.')


# %% pycharm={"name": "#%%\n"}
drucke_aufteilung_der_beute_v2(1000, 11)
drucke_aufteilung_der_beute_v2(17, 8)


# %% pycharm={"name": "#%%\n"}
