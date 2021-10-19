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
# # Einleitung
#
# Wie können Sie den String `Hello, world!` in Python darstellen?

# %%
'Hello, world!'

# %% [markdown]
# Wie können Sie Ihren Namen als Text (String) in Python darstellen?

# %%
'Matthias'

# %% [markdown]
# Wie können Sie den String `Hello, World!` auf dem Bildschirm ausgeben?

# %%
print('Hello, World!')

# %% [markdown]
# Wie können Sie Ihren Namen auf dem Bildschirm ausgeben?

# %%
print('Matthias')

# %% [markdown]
# Wie können Sie
#
# ```
# 130 g   Mehl
# 250 ml  Milch
# 1 EL    Vanillezucker
# 1 Prise Salz
# ```
#
# auf dem Bildschirm ausgeben?

# %%
print('130 g   Mehl')
print('250 ml  Milch')
print('1 EL    Vanillezucker')
print('1 Prise Salz')

# %%
# Alternativ:
print("""130 g   Mehl
250 ml  Milch
1 EL    Vanillezucker
1 Prise Salz""")

# %%
# Alternativ:
print("130 g   Mehl\n"
      "250 ml  Milch\n"
      "1 EL    Vanillezucker\n"
      "1 Prise Salz")

# %% [markdown]
# # Zahlen und Mathematik
#
# Wie können Sie die Zahl `32` in Python darstellen?

# %%
32

# %% [markdown]
# Was ist der Datentyp von `14` in Python?

# %%
type(14)

# %% [markdown]
# Was ist der Datentyp von `14.0` in Python?

# %%
type(14.0)

# %% [markdown]
# Was ist der Datentyp von `'14'` in Python?

# %%
type('14')

# %% [markdown]
# Was ist der Wert von `1 + 2 * 3`?

# %%
1 + 2 * 3

# %% [markdown]
# Was ist der Datentyp von `1 + 2 * 3` in Python?

# %%
type(1 + 2 * 3)

# %% [markdown]
# Was ist der Wert von `4 / 2` in Python?

# %%
4 / 2

# %% [markdown]
# Was ist der Datentyp von `4 / 2` in Python?

# %%
type(4 / 2)

# %% [markdown]
# Was sind Wert und Datentyp von `1 + 1.0` in Python? Können Sie den Datentyp ohne Verwendung von `type` feststellen?

# %%
1 + 1.0 # Typ ist float, da Ausgabe Nachkommastellen hat

# %% [markdown]
# # Piraten
#
# Der Legende nach wurde die Beute bei Piratenbanden gerecht durch alle Piraten geteilt. Falls sich die Beute sich nicht gerecht aufteilen ließ erhielt der Kapitän den überschüssigen Anteil.
#
# Wie viele Golddublonen erhält jeder Pirat einer 8-köpfigen Bande (7 Piraten + 1 Kapitän), wenn ein Schatz mit 1000 Golddublonen erbeutet wurde? 
#
# (Verwenden Sie Variablen um die Berechnung klarer zu machen.)

# %%
anzahl_piraten = 8
beute_gesamt = 1000
beute_pro_pirat = beute_gesamt // anzahl_piraten
beute_pro_pirat

# %% [markdown]
# Wie viele Golddublonen erhält der Kapitän extra?

# %%
beute_kapitän = beute_gesamt % anzahl_piraten
beute_kapitän

# %% [markdown]
# Die Piratenbande nimmt 3 neue Piraten-Lehrlinge auf.
#
# Wie verändert sich die Aufteilung der Beute?
#
# (Verwenden Sie Zuweisungen an die existierenden Variablen um das Problem zu lösen.)

# %%
# anzahl_piraten += 3 # anzahl_piraten = anzahl_piraten + 3
anzahl_piraten = 11 # besser, falls die Zelle potentiell mehrmals ausgewertet wird
beute_pro_pirat = beute_gesamt // anzahl_piraten
beute_pro_pirat

# %% [markdown]
# Wie viele Golddublonen erhält der Kapitän in diesem Fall zusätzlich?

# %%
beute_kapitän = beute_gesamt % anzahl_piraten
beute_kapitän


# %% [markdown]
# # Spenden
#
# Bei einer Spendenaktion hat der Fernsehsender ZRD zugesagt, jede eingehende Spende zu verdoppeln. Der Regionalsender YB3 erhöht jede eingehende Spende um 10 Euro. (ZRD verdoppelt bevor die 10 Euro von YB3 hinzugefügt werden.)
#
# Schreiben Sie eine Python Funktion `effektive_spende(n)`, die berechnet, welcher Betrag effektiv gespendet wird, wenn ein Zuschauer $N$ Euro spendet.

# %%
def effektive_spende(spende):
    return 2 * spende + 10


# %% [markdown]
# Wie hoch ist die effektive Spende, wenn ein Zuschauer 20 Euro spendet?

# %%
effektive_spende(20)

# %% [markdown]
# Geben Sie die effektiven Spenden für 25, 50, 100 und 500 Euro auf dem Bildschirm aus.
#
# *Hinweis:* Sie können Eingaben mit der `Tab`-Taste vervollständigen. Es genügt also, wenn Sie 
#
# `pri`-*Tab* `eff`-*Tab*
#
# eingeben bevor Sie die Argumente eintippen.

# %%
print(effektive_spende(10))
print(effektive_spende(25))
print(effektive_spende(50))
print(effektive_spende(100))
print(effektive_spende(500))
print(effektive_spende(1000))

# %%
effektive_spende(10)
effektive_spende(25)
effektive_spende(50)


# %% [markdown]
# # Piraten, Teil 2
#
# Ihre Piraten-Crew droht zu meutern, weil die Berechnung der Beuteaufteilung zu lange dauert.
#
# Schreiben Sie eine Funktion `drucke_aufteilung_der_beute(dublonen, piraten)`,
# die die Aufteilung berechnet und in folgendem Format ausgibt:
#
# ```
# Piraten: 8
# Golddublonen: 17
# Jeder Pirat erhält: 2 Golddublone(n)
# Kapitän erhält extra: 1 Golddublone(n)
# ```

# %%
def drucke_aufteilung_der_beute(dublonen, piraten):
    dublonen_pro_pirat = dublonen // piraten
    dublonen_kapitän = dublonen % piraten
    print('Piraten:', piraten)
    print('Golddublonen:', dublonen)
    print('Jeder Pirat erhält:', dublonen_pro_pirat, 'Golddublone(n)')
    print('Kapitän erhält extra:', dublonen_kapitän, 'Golddublone(n)')

drucke_aufteilung_der_beute(17, 8)


# %% [markdown]
# # Piraten, Teil 3
#
# Nachdem die Gefahr der Meuterei gebannt ist haben Sie Zeit sich um die Verbesserung Ihrer Software zu kümmern.
#
# Schreiben Sie eine Funktion `teile_beute_auf(dublonen, piraten)` die den Beuteanteil jedes Piraten und die Extra-Beute des Kapitäns als zwei Werte zurückgibt.

# %%
def teile_beute_auf(dublonen, piraten):
#     dublonen_pro_pirat = dublonen // piraten
#     dublonen_kapitän = dublonen % piraten
#     return dublonen_pro_pirat, dublonen_kapitän
    return divmod(dublonen, piraten)


# %% [markdown]
# Schreiben Sie eine verbesserte Version der Funktion `drucke_aufteilung_der_beute()`, die `teile_beute_auf()` als Hilfsfunktion verwendet.

# %%
def drucke_aufteilung_der_beute(dublonen, piraten):
    dublonen_pro_pirat, dublonen_kapitän = teile_beute_auf(dublonen, piraten)
    print('Piraten:', piraten)
    print('Golddublonen:', dublonen)
    print('Jeder Pirat erhält:', dublonen_pro_pirat, 'Golddublone(n)')
    print('Kapitän erhält extra:', dublonen_kapitän, 'Golddublone(n)')

drucke_aufteilung_der_beute(1000, 11)
