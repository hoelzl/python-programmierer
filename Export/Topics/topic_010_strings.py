# %% [markdown]
#
# # Vergleich von Strings

# %%
"a" == "a"

# %%
"A" == "a"

# %%
"A" < "B"

# %%
"A" < "a"

# %%
"a" < "A"

# %% [markdown]
#
# Strings sind wie im Wörterbuch (lexikographisch) geordnet

# %%
"ab" < "abc"

# %%
"ab" < "ac"

# %%
"ab" != "ac"

# %% [markdown]
#
# # Nochmal String Literale
#
# - String-Literale werden in einfache oder doppelte Anführungszeichen eingeschlossen
#     - `"Hello, world!"`
#     - `'Hallo Welt!'`
#     - Welche Form man wählt spielt keine Rolle, außer man will Anführungszeichen im String haben
#     - `"Er sagt 'Huh?'"`
#     - `'Sie antwortet: "Genau."'`

# %% [markdown]
#
# - String-Literale, können Unicode Zeichen enthalten:
#     - `"おはようございます"`
#     - `"😠🙃🙄"`

# %%
print("Er sagt 'Huh?'")
print('Sie antwortet: "Genau."')
print("おはようございます")
print("😠🙃🙄")

# %% [markdown]
#
# - Sonderzeichen können mit *Escape-Notation* angegeben werden:
#     - `\n`, `\t`, `\\`, `\"`, `\'`, ...
#     - `\u`, `\U` für Unicode code points (16 bzw. 32 bit)
#     - `\N{...}` für Unicode

# %%
print("a\tbc\td\n123\t4\t5")

# %%
print('"Let\'s go crazy", she said')

# %%
print("C:\\Users\\John")

# %%
print("\u0394 \u03b1 \t\U000003b2 \U000003b3")
print("\U0001F62E \U0001f61a \U0001f630")

# %%
print("\N{GREEK CAPITAL LETTER DELTA} \N{GREEK SMALL LETTER ALPHA}")
print("\N{smiling face with open mouth and smiling eyes} \N{winking face}")

# %% [markdown]
#
# - String Literale können auch in 3-fache Anführungszeichen eingeschlossen werden
# - Diese Art von Literalen kann über mehrere Zeilen gehen

# %%
"""Das ist
ein String-Literal,
das über mehrere
Zeilen geht."""

# %%
print("""Mit Backslash am Ende der Zeile kann der Zeilenvorschub unterdrückt werden.""")

# %% [markdown]
#
# ## Konkatenation von Strings
#
# Mit `+` können Strings aneinandergehängt (konkateniert) werden:

# %%
"Ein" + " " + "String"

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `015x-Workshop Mehr zu Strings`
# - Abschnitt "Begrüßung 1"

# %% [markdown]
#
# # String Interpolation: F-Strings
#
# Python bietet die Möglichkeit, Werte von Variablen in Strings einzusetzen:

# %%
name = "Hans"
zahl = 12
f"Hallo, {name}, die Zahl ist {zahl + 1}"

# %%
spieler_name = "Hans"
anzahl_spiele = 10
anzahl_gewinne = 2

ausgabe = f"Hallo {spieler_name}!\nSie haben {anzahl_spiele}-mal gespielt und dabei {anzahl_gewinne}-mal gewonnen."
print(ausgabe)

# %%
ausgabe = f"""Hallo {spieler_name}!
Sie haben {anzahl_spiele}-mal gespielt \
und dabei {anzahl_gewinne}-mal gewonnen.\
"""
print(ausgabe)

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `015x-Workshop Mehr zu Strings`
# - Abschnitt "Begrüßung 2"

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `015x-Workshop Mehr zu Strings`
# - Abschnitt "Piraten 4"

# %%

# %% [markdown]
#
# # Umwandlung in Strings
#
# Python bietet zwei Funktionen an, mit denen beliebige Werte in Strings
# umgewandelt werden können:
#
# - `repr` für eine "programmnahe" Darstellung (wie könnte der Wert im Programm
#   erzeugt werden)
# - `str` für eine "benutzerfreundliche" Darstellung

# %%
print(str("Hallo!"))

# %%
print(repr("Hallo!"))

# %% [markdown]
#
# Für manche Datentypen liefern `str` und `repr` den gleichen String zurück:

# %%
print(str(["a", "b", "c"]))
print(repr(["a", "b", "c"]))

# %%