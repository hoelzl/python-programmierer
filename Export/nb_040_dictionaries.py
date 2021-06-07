#!/usr/bin/env python
# coding: utf-8

# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <h1 style="text-align:center;">Python: Dictionaries</h1>
# <h2 style="text-align:center;">Coding Akademie München GmbH</h2>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <div style="text-align:center;">Allaithy Raed</div>

# ## Dictionaries
# 
# Indizes in Listen
# 
# - können nur Integer-Werte sein
# - müssen ein Intervall von 0 bis `len(liste) - 1` umfassen
# 
# Elemente in einer Liste sind sortiert.

# In[1]:


non_sparse = [0] * 10
non_sparse[0] = 1
non_sparse[9] = 1
non_sparse


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

# In[3]:


sparse = {0: 1, 9: 1}


# In[4]:


sparse


# In[5]:


sparse[0]


# In[7]:


# Fehler
# sparse[1]


# In[9]:


sparse[12] = 3
print(sparse[12])
sparse


# In[10]:


translations = {'snake': 'Schlange', 'bat': 'Fledermaus', 'horse': 'Hose', 'bird': 'Vogel'}


# In[12]:


print(translations['snake'])
print(translations.get('bat', '<unbekannt>'))
print(translations.get('monkey', 'Affe'))
print(translations.get('tree'))


# In[14]:


# Fehler:
# translations['monkey']
translations


# In[15]:


translations['horse'] = 'Pferd'
translations['horse']


# In[16]:


del translations['bird']
print(translations.get('bird', '<unbekannt>'))
print(translations.setdefault('bird', 'Vogel'))
print(translations.setdefault('bird', '<auch unbekannt>'))
print(translations.get('bird', '<unbekannt>'))


# In[17]:


for key in translations:
    print(key, end=" ")


# In[18]:


for key in translations.keys():
    print(key, end=" ")


# In[19]:


for val in translations.values():
    print(val, end=" ")


# In[20]:


for item in translations.items():
    print(item, end=" ")


# In[21]:


for key, val in translations.items():
    print("Key:", key, "\tValue:", val)


# ## Mini-Workshop
# 
# - Notebook `040x-Workshop Dictionaries`
# - Abschnitt "Worthäufigkeiten"

# ## Mini-Workshop
# 
# - Notebook `042x-Workshop Todo-Liste V0`
# - Abschnitt "TODO-Liste Version 0"
