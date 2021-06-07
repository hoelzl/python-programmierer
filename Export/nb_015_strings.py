#!/usr/bin/env python
# coding: utf-8

# # Vergleich von Strings

# In[ ]:


"a" == 'a'


# In[ ]:


"A" == "a"


# In[ ]:


"A" < "B"


# In[ ]:


"A" < "a"


# In[ ]:


"a" < "A"


# Strings sind wie im Wörterbuch (lexikographisch) geordnet

# In[ ]:


"ab" < "abc"


# In[ ]:


"ab" < "ac"


# In[ ]:


"ab" != "ac"


# # Nochmal String Literale
# 
# - String-Literale werden in einfache oder doppelte Anführungszeichen eingeschlossen
#     - `"Hello, world!"`
#     - `'Hallo Welt!'`
#     - Welche Form man wählt spielt keine Rolle, außer man will Anführungszeichen im String haben
#     - `"Er sagt 'Huh?'"`
#     - `'Sie antwortet: "Genau."'`

# - String-Literale, können Unicode Zeichen enthalten:
#     - `"おはようございます"`
#     - `"😠🙃🙄"`

# In[ ]:


print("Er sagt 'Huh?'")
print('Sie antwortet: "Genau."')
print("おはようございます")
print("😠🙃🙄")


# - Sonderzeichen können mit *Escape-Notation* angegeben werden:
#     - `\n`, `\t`, `\\`, `\"`, `\'`, ...
#     - `\u`, `\U` für Unicode code points (16 bzw. 32 bit)
#     - `\N{...}` für Unicode

# In[ ]:


print("a\tbc\td\n123\t4\t5")


# In[ ]:


print("\"Let\'s go crazy\", she said")


# In[ ]:


print("C:\\Users\\John")


# In[ ]:


print("\u0394 \u03b1 \t\U000003b2 \U000003b3")
print("\U0001F62E \U0001f61a \U0001f630")


# In[ ]:


print("\N{GREEK CAPITAL LETTER DELTA} \N{GREEK SMALL LETTER ALPHA}")
print("\N{smiling face with open mouth and smiling eyes} \N{winking face}")


# - String Literale können auch in 3-fache Anführungszeichen eingeschlossen werden
# - Diese Art von Literalen kann über mehrere Zeilen gehen

# In[ ]:


"""Das ist
ein String-Literal,
das über mehrere
Zeilen geht."""


# In[ ]:


print('''Mit Backslash am Ende der Zeile kann der Zeilenvorschub unterdrückt werden.''')


# ## Konkatenation von Strings
# 
# Mit `+` können Strings aneinandergehängt (konkateniert) werden:

# In[ ]:


"Ein" + " " + "String"


# ## Mini-Workshop
# 
# - Notebook `015x-Workshop Mehr zu Strings`
# - Abschnitt "Begrüßung 1"

# # String Interpolation: F-Strings
# 
# Python bietet die Möglichkeit, Werte von Variablen in Strings einzusetzen:

# In[ ]:


name = "Hans"
zahl = 12
f"Hallo, {name}, die Zahl ist {zahl + 1}"


# In[ ]:


spieler_name = "Hans"
anzahl_spiele = 10
anzahl_gewinne = 2

ausgabe = f"Hallo {spieler_name}!\nSie haben {anzahl_spiele}-mal gespielt und dabei {anzahl_gewinne}-mal gewonnen."
print(ausgabe)


# In[ ]:


ausgabe = f"""Hallo {spieler_name}!
Sie haben {anzahl_spiele}-mal gespielt \
und dabei {anzahl_gewinne}-mal gewonnen.\
"""
print(ausgabe)


# ## Mini-Workshop
# 
# - Notebook `015x-Workshop Mehr zu Strings`
# - Abschnitt "Begrüßung 2"

# ## Mini-Workshop
# 
# - Notebook `015x-Workshop Mehr zu Strings`
# - Abschnitt "Piraten 4"
