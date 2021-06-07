#!/usr/bin/env python
# coding: utf-8

# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <h1 style="text-align:center;">Python: Module und Packages<br/><br/>
#     Mit Exkursionen zu Argparse, Pytest, Setuptools<h1>
# <h2 style="text-align:center;">Coding Akademie München GmbH</h2>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <div style="text-align:center;">Allaithy Raed</div>

# - Der Python Interpreter bietet nur einen kleinen Teil der für die meisten
#   Programme benötigten Funktionalität
#   - Kein Interaktion mit dem Betriebssystem
#   - Kein Netzwerkfunktionalität
#   - Keine GUI
#   - ...
# - Durch *Module* und *Packages* kann diese Funktionalität bei Bedarf geladen
#   werden.

# In[1]:


# Importieren eines Moduls/Packages
import os


# In[2]:


# Verwenden der Funktionalität
os.getcwd()


# Python bietet viele Standardmodule an, die mit dem Interpreter installiert
# werden:
# 
# - abc: Abstract base classes
# - argparse: Kommandozeilenargumente
# - asyncio: Asynchrone Programmierung
# - collections: Container-Datentypen
# - ...
# 
# [Hier](https://docs.python.org/3/py-modindex.html) ist eine vollständigere Liste.

# In[3]:


import os
{'num-cpus': os.cpu_count(), 'pid': os.getpid()}


# In[4]:


import ast
ast.dump(ast.parse('print(123)'), False)


# ## Benutzerdefinierte Module
# 
# Ein benutzerdefiniertes Modul ist eine Datei mit Python-Code.
# 
# Wie wir schon gesehen haben:
# - Wenn sich ein Python-Modul im Suchpfad befindet, kann es mit `import` geladen werden.
# - Jupyter Notebooks lassen sich nicht (ohne zusätzliche Pakete) als Module laden. 

# In[5]:


# Welche Python-Dateien gibt es im aktuellen Verzeichnis?
for filename in os.listdir(os.getcwd()):
    if filename[-3:] == '.py':
        print(filename)


# In[6]:


# Anzeigen des Quellcodes von `my_test_module.py`
# %pycat my_test_module.py


# In[7]:


# Andere Möglichkeit, den Inhalt von `my_test_module.py` anzuzeigen.
with open('my_test_module.py', 'r') as file:
    text = file.read()
    
print(text)


# In[19]:


# Top-level code wird ausgeführt
import my_test_module


# In[13]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# In[17]:


# Top-level code wird NICHT mehr ausgeführt
import my_test_module


# In[20]:


my_test_module.add1(2)


# In[22]:


# add1


# In[27]:


import my_test_module as mm
import numpy as np


# In[25]:


mm.add1(1)


# In[26]:


mm.perform_complex_computation(17)


# In[28]:


from my_test_module import multiply_by_2


# In[30]:


multiply_by_2(2)


# In[32]:


from my_test_module import multiply_by_2 as mult2


# In[33]:


mult2(4)


# In[34]:


# Im Regelfall besser vermeiden:
from my_test_module import *


# In[35]:


multiply_by_2(3)


# In[36]:


add1(3)


# In[37]:


# Anzeigen aller definierten Namen:
dir(my_test_module)


# In[38]:


[name for name in dir(my_test_module) if name[0] != '_']


# ## Beispiel: `HttpServer`
# 
# Der Python Interpreter hat keinen eingebauten HTTP Server. Mittels der Standardbibliothek ist es aber nicht schwer einen zu schreiben.

# ### Beispiel: `ModuleTest`
# 
# Das `ModuleTest` Beispiel zeigt, wie ein Programm aus mehreren Modulen bestehen kann.

# In[ ]:


__name__


# ## Packages
# 
# - Methode um Module mit zu strukturieren: `a.b.c`, `a.b.x`
# - Ein Package ist eine Zusammenfassung von mehreren Modulen
# - `b` ist Sub-Package von `a`, `c` und `x` sind Submodule von `b`

# In[41]:


from html.parser import HTMLParser
import html.entities


# In[43]:


HTMLParser()


# In[40]:


html.entities.entitydefs['Psi']


# ### Struktur von Packages
# 
# - Hierarchie durch Verzeichnisse und Python Dateien
#   - Z.B. Verzeichnis `html` mit Unterverzeichnissen `parser`, `entities`
# - Benötigt eine `__init__.py` Datei in jedem Verzeichnis, aus dem Code importiert werden soll
# - Die `__init__.py` Datei kann leer sein (und ist oft leer)

# <img src="img/package-structure.png" alt="Package structure"
#      style="display:block;margin:auto;width:40%"></img>

# ### Finden von Packages
# 
# - Python sucht in `sys.path` nach dem Package-Verzeichnis.
# - Dieser kann durch die Environment-Variable `PYTHONPATH` oder direkt von Python aus beeinflusst werden.
# - In den meisten Fällen ist es besser, keine komplizierten Operationen an `sys.path` vorzunehmen.

# ### Das `import` statement
# 
# `import a.b.c`:
# 
# - `a` und `b` müssen Packages (Verzeichnisse) sein
# - `c` kann ein Modul oder ein Package sein

# `from a.b.c import d`
# - `a` und `b` müssen Packages sein
# - `c` kann ein Modul oder ein Package sein
# - `d` kann ein Modul, ein Package oder ein Name (d.h. eine Variable, eine Funktion, eine Klasse, usw.) sein

# ### Referenzen innerhalb eines Packages
# 
# - `from . import a` importiert `a` aus dem aktuellen Package
# - `from .. import a` importiert `a` aus dem übergeordneten Package
# - `from .foo import a` importiert `a` aus dem "Geschwistermodul" `foo`

# ## Beispiel: `MessageQueue`
# 
# Das `MessageQueue` Beispiel zeigt, wie ein Programm aus mehreren Packages bestehen kann.

# ## Argparse: Verarbeiten von Command Line Arguments
# 
# - Für viele Anwendungsfälle ist eine Kommandozeilenanwendung ausreichend
# - Die manuelle Verarbeitung von Argumenten ist relativ aufwändig
# - Python bietet mit `argparse` eine sehr gute Bibliothek, die viele häufige Anwendungsfälle deutlich vereinfacht

# ### Bestandteile von Argparse:
# 
# - Klasse `argparse.ArgumentParser` zum Erzeugen eines Kommandozeilen-Parsers
# - Methode `add_argument()` zum Definieren von Argumenten
#   - Name, Varianten (z.B. `-l`, `--list`)
#   - Argumente (z.B. `gcc -o myprog`)
#   - Aktion, die ausgeführt werden soll
#   - Hilfetext für die Dokumentation
#   - usw.
# - Methode `parse_args()` zum Auswerten der Kommandozeile
# - Viele weiter Möglichkeiten:
#   - Subkommandos (`git status`, `git push`, ...)
#   - Sich gegenseitig ausschließende Argumente (`--case-fold`, `--no-case-fold`)

# # Pytest: Testen in Python
# 
# - Python bietet mehrere eingebaute Pakete zum Schreiben von Unit-Tests und Dokumentationstests an (`unittest` und `doctest`).
# - Viele Projekte verwenden trotzdem das `pytest` Paket, da es viel "Boilerplate" beim Schreiben von Tests vermeidet.
# - `pytest` kann `unittest` und `doctest`-Tests ausführen.

# ## Installation von Pytest
# 
# Pytest ist in der Anaconda-Installation vorinstalliert
# 
# Beim Verwenden der Standard Python Distribution kann es mit
# ```shell
# pip install pytest
# ```
# installiert werden 

# ## Schreiben von Tests
# 
# - Pytest kann sehr flexibel konfiguriert werden
# - Wir verwenden nur die einfachsten Features und verlassen uns auf die automatische Konfiguration
# - Tests für ein Paket werden in einem Unter-Package `test` geschrieben
# - Tests für die Datei `foo.py` sind in der Datei `test/foo_test.py`
# - Jeder Test ist eine Funktion, deren Name mit `test` beginnt
# - Assertions werden mit der `assert` Anweisung geschrieben

# ## Beispiel Testen von `MessageQueueDist`
# 
# Siehe `Examples/MessageQueueDist`

# # Setuptools: Distribution von Python Packeten
# 
# - Setuptools sind das Standard-Tool um installierbare Python-Pakete zu erzeugen.
# - Das Wort "Packages" ist in der Python Welt überladen:
#     - Sammlung von Python Dateien wie in diesem Kapitel beschrieben
#     - Distribution einer installierbaren Version einer Bibliothek ("wheel"), die dann importiert werden kann.

# ### Beispiel: Erstellen einer Anwendung mit Bibliothek
# 
# - Hinzufügen einer `setup.py`-Datei mit Information über die zu installierenden Packages und Skripte
# - Hinzufügen einiger Hilfsdateien (`README.md`, `LICENSE`)
# - Erstellen der Distribution mit `python setup.py bdist_wheel`
# - Installation mit `pip` und dem generierten Wheel
# - Installation während der Entwicklung: `pip install -e .`
