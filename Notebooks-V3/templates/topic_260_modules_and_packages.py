# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.2
# ---

# j2 import 'macros.j2' as doc
# %% [markdown] {{ doc.slide() }}
# {{ doc.header (Module und Packages) }}


# %% [markdown]
#
#  - Der Python Interpreter bietet nur einen kleinen Teil der für die meisten
#    Programme benötigten Funktionalität
#    - Kein Interaktion mit dem Betriebssystem
#    - Kein Netzwerkfunktionalität
#    - Keine GUI
#    - ...
#  - Durch *Module* und *Packages* kann diese Funktionalität bei Bedarf geladen
#    werden.

# %%
# Importieren eines Moduls/Packages
import os


# %%
# Verwenden der Funktionalität
os.getcwd()


# %% [markdown]
#
#  Python bietet viele Standardmodule an, die mit dem Interpreter installiert
#  werden:
#
#  - abc: Abstract base classes
#  - argparse: Kommandozeilenargumente
#  - asyncio: Asynchrone Programmierung
#  - collections: Container-Datentypen
#  - ...
#
#  [Hier](https://docs.python.org/3/py-modindex.html) ist eine vollständigere Liste.

# %%
import os
{'num-cpus': os.cpu_count(), 'pid': os.getpid()}


# %%
import ast
ast.dump(ast.parse('print(123)'), False)


# %% [markdown]
#
#  ## Benutzerdefinierte Module
#
#  Ein benutzerdefiniertes Modul ist eine Datei mit Python-Code.
#
#  Wie wir schon gesehen haben:
#  - Wenn sich ein Python-Modul im Suchpfad befindet, kann es mit `import` geladen werden.
#  - Jupyter Notebooks lassen sich nicht (ohne zusätzliche Pakete) als Module laden.

# %%
# Welche Python-Dateien gibt es im aktuellen Verzeichnis?
for filename in os.listdir(os.getcwd()):
    if filename[-3:] == '.py':
        print(filename)


# %%
# Anzeigen des Quellcodes von `my_test_module.py`
# # %pycat my_test_module.py


# %%
# Andere Möglichkeit, den Inhalt von `my_test_module.py` anzuzeigen.
with open('my_test_module.py', 'r') as file:
    text = file.read()
    
print(text)


# %%
# Top-level code wird ausgeführt
import my_test_module


# %%
# get_ipython().run_line_magic('load_ext', 'autoreload')
# get_ipython().run_line_magic('autoreload', '2')


# %%
# Top-level code wird NICHT mehr ausgeführt
import my_test_module


# %%
my_test_module.add1(2)


# %%
# add1


# %%
import my_test_module as mm
import numpy as np


# %%
mm.add1(1)


# %%
mm.perform_complex_computation(17)


# %%
from my_test_module import multiply_by_2


# %%
multiply_by_2(2)


# %%
from my_test_module import multiply_by_2 as mult2


# %%
mult2(4)


# %%
# Im Regelfall besser vermeiden:
from my_test_module import *


# %%
multiply_by_2(3)


# %%
add1(3)


# %%
# Anzeigen aller definierten Namen:
dir(my_test_module)


# %%
[name for name in dir(my_test_module) if name[0] != '_']


# %% [markdown]
#
#  ## Beispiel: `HttpServer`
#
#  Der Python Interpreter hat keinen eingebauten HTTP Server. Mittels der Standardbibliothek ist es aber nicht schwer einen zu schreiben.

# %% [markdown]
#
#  ### Beispiel: `ModuleTest`
#
#  Das `ModuleTest` Beispiel zeigt, wie ein Programm aus mehreren Modulen bestehen kann.

# %%
__name__


# %% [markdown]
#
#  ## Packages
#
#  - Methode um Module mit zu strukturieren: `a.b.c`, `a.b.x`
#  - Ein Package ist eine Zusammenfassung von mehreren Modulen
#  - `b` ist Sub-Package von `a`, `c` und `x` sind Submodule von `b`

# %%
from html.parser import HTMLParser
import html.entities


# %%
HTMLParser()


# %%
html.entities.entitydefs['Psi']


# %% [markdown]
#
#  ### Struktur von Packages
#
#  - Hierarchie durch Verzeichnisse und Python Dateien
#    - Z.B. Verzeichnis `html` mit Unterverzeichnissen `parser`, `entities`
#  - Benötigt eine `__init__.py` Datei in jedem Verzeichnis, aus dem Code importiert werden soll
#  - Die `__init__.py` Datei kann leer sein (und ist oft leer)

# %% [markdown]
#
#  <img src="img/package-structure.png" alt="Package structure"
#       style="display:block;margin:auto;width:40%"></img>

# %% [markdown]
#
#  ### Finden von Packages
#
#  - Python sucht in `sys.path` nach dem Package-Verzeichnis.
#  - Dieser kann durch die Environment-Variable `PYTHONPATH` oder direkt von
#    Python aus beeinflusst werden.
#  - In den meisten Fällen ist es besser, keine komplizierten Operationen an
#    `sys.path` vorzunehmen.

# %% [markdown]
#
#  ### Das `import` statement
#
#  `import a.b.c`:
#
#  - `a` und `b` müssen Packages (Verzeichnisse) sein
#  - `c` kann ein Modul oder ein Package sein
#
#  `from a.b.c import d`
#  - `a` und `b` müssen Packages sein
#  - `c` kann ein Modul oder ein Package sein
#  - `d` kann ein Modul, ein Package oder ein Name (d.h. eine Variable, eine Funktion, eine Klasse, usw.) sein

# %% [markdown]
#
#  ### Referenzen innerhalb eines Packages
#
#  - `from . import a` importiert `a` aus dem aktuellen Package
#  - `from .. import a` importiert `a` aus dem übergeordneten Package
#  - `from .foo import a` importiert `a` aus dem "Geschwistermodul" `foo`

# %% [markdown]
#
#  ## Beispiel: `MessageQueue`
#
#  Das `MessageQueue` Beispiel zeigt, wie ein Programm aus mehreren Packages bestehen kann.

# %% [markdown]
#
#  ## Argparse: Verarbeiten von Command Line Arguments
#
#  - Für viele Anwendungsfälle ist eine Kommandozeilenanwendung ausreichend
#  - Die manuelle Verarbeitung von Argumenten ist relativ aufwändig
#  - Python bietet mit `argparse` eine sehr gute Bibliothek, die viele häufige Anwendungsfälle deutlich vereinfacht

# %% [markdown]
#
#  ### Bestandteile von Argparse:
#
#  - Klasse `argparse.ArgumentParser` zum Erzeugen eines Kommandozeilen-Parsers
#  - Methode `add_argument()` zum Definieren von Argumenten
#    - Name, Varianten (z.B. `-l`, `--list`)
#    - Argumente (z.B. `gcc -o myprog`)
#    - Aktion, die ausgeführt werden soll
#    - Hilfetext für die Dokumentation
#    - usw.
#  - Methode `parse_args()` zum Auswerten der Kommandozeile
#  - Viele weiter Möglichkeiten:
#    - Subkommandos (`git status`, `git push`, ...)
#    - Sich gegenseitig ausschließende Argumente (`--case-fold`, `--no-case-fold`)

# %% [markdown]
#
#  # Pytest: Testen in Python
#
#  - Python bietet mehrere eingebaute Pakete zum Schreiben von Unit-Tests und Dokumentationstests an (`unittest` und `doctest`).
#  - Viele Projekte verwenden trotzdem das `pytest` Paket, da es viel "Boilerplate" beim Schreiben von Tests vermeidet.
#  - `pytest` kann `unittest` und `doctest`-Tests ausführen.

# %% [markdown]
#
#  ## Installation von Pytest
#
#  Pytest ist in der Anaconda-Installation vorinstalliert
#
#  Beim Verwenden der Standard Python Distribution kann es mit
#  ```shell
#  pip install pytest
#  ```
#  installiert werden

# %% [markdown]
#
#  ## Schreiben von Tests
#
#  - Pytest kann sehr flexibel konfiguriert werden
#  - Wir verwenden nur die einfachsten Features und verlassen uns auf die automatische Konfiguration
#  - Tests für ein Paket werden in einem Unter-Package `test` geschrieben
#  - Tests für die Datei `foo.py` sind in der Datei `test/foo_test.py`
#  - Jeder Test ist eine Funktion, deren Name mit `test` beginnt
#  - Assertions werden mit der `assert` Anweisung geschrieben

# %% [markdown]
#
#  ## Beispiel Testen von `MessageQueueDist`
#
#  Siehe `Examples/MessageQueueDist`

# %% [markdown]
#
#  # Setuptools: Distribution von Python Packeten
#
#  - Setuptools sind das Standard-Tool um installierbare Python-Pakete zu erzeugen.
#  - Das Wort "Packages" ist in der Python Welt überladen:
#      - Sammlung von Python Dateien wie in diesem Kapitel beschrieben
#      - Distribution einer installierbaren Version einer Bibliothek ("wheel"), die dann importiert werden kann.

# %% [markdown]
#
#  ### Beispiel: Erstellen einer Anwendung mit Bibliothek
#
#  - Hinzufügen einer `setup.py`-Datei mit Information über die zu installierenden Packages und Skripte
#  - Hinzufügen einiger Hilfsdateien (`README.md`, `LICENSE`)
#  - Erstellen der Distribution mit `python setup.py bdist_wheel`
#  - Installation mit `pip` und dem generierten Wheel
#  - Installation während der Entwicklung: `pip install -e .`
