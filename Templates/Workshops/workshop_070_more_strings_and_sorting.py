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
# # Shout
#
# Schreiben Sie eine Funktion `shout(text)`, die `text` in Großbuchstaben,
# gefolgt von drei Außrufezeichen auf dem Bildschirm ausgibt.

# %% [markdown] lang="en"
# # Shout
#
# Write a function `shout(text)` that will print `text` in upper case letters,
# followed by three exclamation marks on the screen.

# %% tags=["solution"]
def shout(text):
    print(f"{text.upper()}!!!")


# %% [markdown] lang="de"
# Testen Sie die Funktion mit Argument `"Hallo"`

# %% [markdown] lang="en"
# Test the function with argument `"Hello"`

# %% tags=["solution"]
shout("Hallo")

# %% [markdown] lang="de"
# # Vergleichen von Strings

# %% [markdown] lang="en"
# # Comparing strings

# %% [markdown] lang="de"
# Ist `Abc` kleiner als `aBC`?

# %% [markdown] lang="en"
# Is `Abc` less than `aBC`?

# %% tags=["solution"]
"Abc" < "aBC"

# %% [markdown] lang="de"
# Ist gleichzeitig `abc` kleiner als `abcd` und `abcd` kleiner als `abd`?

# %% [markdown] lang="en"
# Is `abc` less than `abcd` and simultaneously `abcd` less than `abd`?

# %% tags=["solution"]
"abc" < "abcd" < "abd"


# %% [markdown] lang="de"
# # Begrüßung 1
#
# Schreiben Sie eine Funktion `drucke_begrüßung(name)`, die eine personalisierte
# Begrüßung ausgibt, z.B.
# ```
# Hallo, Hans!
# Schön Sie heute wieder bei uns begrüßen zu dürfen.
# Wir wünschen Ihnen viel Spaß, Hans.
# ```
# Verwenden Sie dazu die `print()`-Funktion mit einem Argument und
# String-Konkatenation.

# %% [markdown] lang="en"
# # Greeting 1
#
# Write a function `print_greeting(name)` that does a personalized
# outputs a greeting, e.g.
# ```
# Hello Hans!
# Nice to welcome you again today.
# We wish you a lot of fun, Hans.
# ```
# To do this, use the `print()` function with one argument and string concatenation.

# %% tags=["solution"]
def drucke_begrüßung(name):
    print(
        "Hallo, "
        + name
        + "!\n"
        + "Schön Sie heute wieder bei uns begrüßen zu dürfen.\n"
        + "Wir wünschen Ihnen viel Spaß, "
        + name
        + "."
    )


drucke_begrüßung("Hans")


# %% [markdown] lang="de"
# # Begrüßung 2
#
# Schreiben Sie eine Funktion `drucke_begrüßung_2(name)`, die die
# Funktionalität von `drucke_begrüßung(name)` mittels F-Strings implementiert.

# %% [markdown] lang="en"
# # Greeting 2
#
# Write a function `print_greeting_2(name)` that implements the functionality of `print_greeting(name)` using F-strings.

# %% tags=["solution"]
def drucke_begrüßung_2(name):
    print(
        f"Hallo, {name}!\n"
        f"Schön Sie heute wieder bei uns begrüßen zu dürfen."
        f"Wir wünschen Ihnen viel Spaß, {name}."
    )


drucke_begrüßung_2("Sepp")


# %% [markdown] lang="de"
# # Piraten, Teil 4
#
# Das Ausdrucken der Beute-Aufteilund mittels
# `drucke_aufteilung_der_beute(dublonen, piraten)` verbraucht zu viel Papier.
#
# Implementieren Sie eine neue Version der Funktion, die den folgenden Text
# ausgibt:
#
# ```
# Jeder der 8 Piraten erhält 2 der 17 Golddublonen. Der Kapitän erhält extra 1 Golddublone.
# ```
# bzw.
# ```
# Jeder der 8 Piraten erhält 2 der 17 Golddublonen. Der Kapitän erhält extra 2 Golddublonen.
# ```
#
# Verwenden Sie F-Strings um die Ausgabetexte zu erzeugen. Sie können die
# folgende Funktion verwenden, um die Aufteilung der Beute zu berechnen:

# %% [markdown] lang="en"
# # Pirates, part 4
#
# The printout of the loot allocation and means
# `print_division_of_loot(doubloons, pirates)` uses too much paper.
#
# Implement a new version of the function containing the following text
# outputs:
#
# ```
# Each of the 8 pirates gets 2 of the 17 gold doubloons. The captain receives an extra 1 gold doubloon.
# ```
# or.
# ```
# Each of the 8 pirates gets 2 of the 17 gold doubloons. The captain receives an extra 2 gold doubloons.
# ```
#
# Use F-strings to generate the output texts. You can the
# use the following function to calculate the division of spoils:

# %%
def teile_beute_auf(dublonen, piraten):
    dublonen_pro_pirat = dublonen // piraten
    dublonen_kapitän = dublonen % piraten
    return dublonen_pro_pirat, dublonen_kapitän


# %% tags=["solution"]
def drucke_aufteilung_der_beute(dublonen, piraten):
    dublonen_pro_pirat, dublonen_kapitän = teile_beute_auf(dublonen, piraten)
    if dublonen_kapitän == 1:
        print(
            f"Jeder der {piraten} Piraten erhält {dublonen_pro_pirat} "
            f"der {dublonen} Golddublonen. "
            f"Der Kapitän erhält extra 1 Golddublone."
        )
    else:
        print(
            f"Jeder der {piraten} Piraten erhält {dublonen_pro_pirat} "
            f"der {dublonen} Golddublonen. "
            f"Der Kapitän erhält extra {dublonen_kapitän} Golddublonen."
        )


# %% tags=["solution"]
drucke_aufteilung_der_beute(1000, 11)
drucke_aufteilung_der_beute(17, 8)


# %% tags=["solution"]
def drucke_aufteilung_der_beute_v2(dublonen, piraten):
    dublonen_pro_pirat, dublonen_kapitän = teile_beute_auf(dublonen, piraten)
    print(
        f"Jeder der {piraten} Piraten erhält {dublonen_pro_pirat} "
        f"der {dublonen} Golddublonen. "
        f"Der Kapitän erhält extra {dublonen_kapitän} Golddublone"
        f'{"" if dublonen_kapitän == 1 else "n"}.'
    )


# %% tags=["solution"]
drucke_aufteilung_der_beute_v2(1000, 11)
drucke_aufteilung_der_beute_v2(17, 8)
