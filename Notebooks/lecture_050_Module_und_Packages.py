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
# <h1 style="text-align:center;">Python: Module und Packages<br/><br/>
#     Mit Exkursionen zu Argparse, Pytest, Setuptools<h1>
# <h2 style="text-align:center;">Coding Akademie München GmbH</h2>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <div style="text-align:center;">Allaithy Raed</div>

# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "slide"}
# - Der Python Interpreter bietet nur einen kleinen Teil der für die meisten
#   Programme benötigten Funktionalität
#   - Kein Interaktion mit dem Betriebssystem
#   - Kein Netzwerkfunktionalität
#   - Keine GUI
#   - ...
# - Durch *Module* und *Packages* kann diese Funktionalität bei Bedarf geladen
#   werden.

# %% slideshow={"slide_type": "subslide"}
# Importieren eines Moduls/Packages
import os

# %% pycharm={"name": "#%%\n"}
# Verwenden der Funktionalität
os.getcwd()

# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "subslide"}
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

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
import os
{'num-cpus': os.cpu_count(), 'pid': os.getpid()}

# %% pycharm={"name": "#%%\n"}
import ast
ast.dump(ast.parse('print(123)'), False)

# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "slide"}
# ## Benutzerdefinierte Module
#
# Ein benutzerdefiniertes Modul ist eine Datei mit Python-Code.
#
# Wie wir schon gesehen haben:
# - Wenn sich ein Python-Modul im Suchpfad befindet, kann es mit `import` geladen werden.
# - Jupyter Notebooks lassen sich nicht (ohne zusätzliche Pakete) als Module laden. 

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
# Welche Python-Dateien gibt es im aktuellen Verzeichnis?
for filename in os.listdir(os.getcwd()):
    if filename[-3:] == '.py':
        print(filename)

# %% slideshow={"slide_type": "subslide"}
# Anzeigen des Quellcodes von `my_test_module.py`
# # %pycat my_test_module.py

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
# Andere Möglichkeit, den Inhalt von `my_test_module.py` anzuzeigen.
with open('my_test_module.py', 'r') as file:
    text = file.read()
    
print(text)

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "slide"}
# Top-level code wird ausgeführt
import my_test_module

# %%
# %load_ext autoreload
# %autoreload 2

# %%
# Top-level code wird NICHT mehr ausgeführt
import my_test_module

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
my_test_module.add1(2)

# %% pycharm={"name": "#%%\n"}
# add1

# %% slideshow={"slide_type": "subslide"}
import my_test_module as mm
import numpy as np

# %%
mm.add1(1)

# %%
mm.perform_complex_computation(17)

# %% slideshow={"slide_type": "subslide"}
from my_test_module import multiply_by_2

# %%
multiply_by_2(2)

# %%
from my_test_module import multiply_by_2 as mult2

# %%
mult2(4)

# %% slideshow={"slide_type": "subslide"}
# Im Regelfall besser vermeiden:
from my_test_module import *

# %%
multiply_by_2(3)

# %%
add1(3)

# %% slideshow={"slide_type": "slide"}
# Anzeigen aller definierten Namen:
dir(my_test_module)

# %% slideshow={"slide_type": "subslide"}
[name for name in dir(my_test_module) if name[0] != '_']

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Beispiel: `HttpServer`
#
# Der Python Interpreter hat keinen eingebauten HTTP Server. Mittels der Standardbibliothek ist es aber nicht schwer einen zu schreiben.

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Beispiel: `ModuleTest`
#
# Das `ModuleTest` Beispiel zeigt, wie ein Programm aus mehreren Modulen bestehen kann.

# %%
__name__

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Packages
#
# - Methode um Module mit zu strukturieren: `a.b.c`, `a.b.x`
# - Ein Package ist eine Zusammenfassung von mehreren Modulen
# - `b` ist Sub-Package von `a`, `c` und `x` sind Submodule von `b`

# %% slideshow={"slide_type": "subslide"}
from html.parser import HTMLParser
import html.entities

# %%
HTMLParser()

# %%
html.entities.entitydefs['Psi']

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Struktur von Packages
#
# - Hierarchie durch Verzeichnisse und Python Dateien
#   - Z.B. Verzeichnis `html` mit Unterverzeichnissen `parser`, `entities`
# - Benötigt eine `__init__.py` Datei in jedem Verzeichnis, aus dem Code importiert werden soll
# - Die `__init__.py` Datei kann leer sein (und ist oft leer)

# %% [markdown] slideshow={"slide_type": "subslide"}
# <img src="img/package-structure.png" alt="Package structure"
#      style="display:block;margin:auto;width:40%"></img>

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Finden von Packages
#
# - Python sucht in `sys.path` nach dem Package-Verzeichnis.
# - Dieser kann durch die Environment-Variable `PYTHONPATH` oder direkt von Python aus beeinflusst werden.
# - In den meisten Fällen ist es besser, keine komplizierten Operationen an `sys.path` vorzunehmen.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Das `import` statement
#
# `import a.b.c`:
#
# - `a` und `b` müssen Packages (Verzeichnisse) sein
# - `c` kann ein Modul oder ein Package sein

# %% [markdown] slideshow={"slide_type": "subslide"}
# `from a.b.c import d`
# - `a` und `b` müssen Packages sein
# - `c` kann ein Modul oder ein Package sein
# - `d` kann ein Modul, ein Package oder ein Name (d.h. eine Variable, eine Funktion, eine Klasse, usw.) sein

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Referenzen innerhalb eines Packages
#
# - `from . import a` importiert `a` aus dem aktuellen Package
# - `from .. import a` importiert `a` aus dem übergeordneten Package
# - `from .foo import a` importiert `a` aus dem "Geschwistermodul" `foo`

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Beispiel: `MessageQueue`
#
# Das `MessageQueue` Beispiel zeigt, wie ein Programm aus mehreren Packages bestehen kann.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Argparse: Verarbeiten von Command Line Arguments
#
# - Für viele Anwendungsfälle ist eine Kommandozeilenanwendung ausreichend
# - Die manuelle Verarbeitung von Argumenten ist relativ aufwändig
# - Python bietet mit `argparse` eine sehr gute Bibliothek, die viele häufige Anwendungsfälle deutlich vereinfacht

# %% [markdown] slideshow={"slide_type": "subslide"}
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

# %% [markdown] slideshow={"slide_type": "slide"}
# # Pytest: Testen in Python
#
# - Python bietet mehrere eingebaute Pakete zum Schreiben von Unit-Tests und Dokumentationstests an (`unittest` und `doctest`).
# - Viele Projekte verwenden trotzdem das `pytest` Paket, da es viel "Boilerplate" beim Schreiben von Tests vermeidet.
# - `pytest` kann `unittest` und `doctest`-Tests ausführen.

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Installation von Pytest
#
# Pytest ist in der Anaconda-Installation vorinstalliert
#
# Beim Verwenden der Standard Python Distribution kann es mit
# ```shell
# pip install pytest
# ```
# installiert werden 

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Schreiben von Tests
#
# - Pytest kann sehr flexibel konfiguriert werden
# - Wir verwenden nur die einfachsten Features und verlassen uns auf die automatische Konfiguration
# - Tests für ein Paket werden in einem Unter-Package `test` geschrieben
# - Tests für die Datei `foo.py` sind in der Datei `test/foo_test.py`
# - Jeder Test ist eine Funktion, deren Name mit `test` beginnt
# - Assertions werden mit der `assert` Anweisung geschrieben

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Beispiel Testen von `MessageQueueDist`
#
# Siehe `Examples/MessageQueueDist`

# %% [markdown] slideshow={"slide_type": "slide"}
# # Setuptools: Distribution von Python Packeten
#
# - Setuptools sind das Standard-Tool um installierbare Python-Pakete zu erzeugen.
# - Das Wort "Packages" ist in der Python Welt überladen:
#     - Sammlung von Python Dateien wie in diesem Kapitel beschrieben
#     - Distribution einer installierbaren Version einer Bibliothek ("wheel"), die dann importiert werden kann.

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Beispiel: Erstellen einer Anwendung mit Bibliothek
#
# - Hinzufügen einer `setup.py`-Datei mit Information über die zu installierenden Packages und Skripte
# - Hinzufügen einiger Hilfsdateien (`README.md`, `LICENSE`)
# - Erstellen der Distribution mit `python setup.py bdist_wheel`
# - Installation mit `pip` und dem generierten Wheel
# - Installation während der Entwicklung: `pip install -e .`

# %% [markdown]
# ## Alternative: Projekt-Generatoren
#
# - Beispiele: [PyScaffold](https://pypi.org/project/PyScaffold/), [Cookiecutter PyPackage](https://github.com/audreyr/cookiecutter-pypackage)

# %%
