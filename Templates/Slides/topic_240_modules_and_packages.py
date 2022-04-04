# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
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

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Module und Packages</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Modules and Packages</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
#
#  - Der Python Interpreter bietet nur einen kleinen Teil der für die meisten
#    Programme benötigten Funktionalität
#    - Kein Interaktion mit dem Betriebssystem
#    - Kein Netzwerkfunktionalität
#    - Keine GUI
#    - ...
#  - Durch *Module* und *Packages* kann diese Funktionalität bei Bedarf geladen
#    werden.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# - The Python interpreter provides only a small part of the functionality needed for most
#   programs:
#   - No interaction with the operating system
#   - No network functionality
#   - No GUI
#   - ...
# - Additional functionality can be loaded using *modules* and *packages*.

# %% {"tags": ["code-along"], "slideshow": {"slide_type": "subslide"}}
# Importieren eines Moduls/Packages
import os


# %% {"tags": ["code-along"]}
# Verwenden der Funktionalität
os.getcwd()


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
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

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# Python provides many standard modules that are installed with the interpreter:
#
#  - abc: Abstract base classes
#  - argparse: command line arguments
#  - asyncio: Asynchronous programming
#  - collections: container data types
#  - ...
#
#  [Here](https://docs.python.org/3/py-modindex.html) is a more complete list.

# %% {"tags": ["code-along"]}
import os

{"num-cpus": os.cpu_count(), "pid": os.getpid()}


# %% {"tags": ["code-along"]}
import ast

ast.dump(ast.parse("print(123)"), False)


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
#
#  ## Benutzerdefinierte Module
#
#  Ein benutzerdefiniertes Modul ist eine Datei mit Python-Code.
#
#  Wie wir schon gesehen haben:
#  - Wenn sich ein Python-Modul im Suchpfad befindet, kann es mit `import` geladen werden.
#  - Jupyter Notebooks lassen sich nicht (ohne zusätzliche Pakete) als Module laden.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## User-defined modules
#
# A user-defined module is simply a file containing Python code.
#
# As we have already seen:
# - If a Python module is in the search path, it can be loaded with `import`.
# - Jupyter notebooks cannot be loaded (without additional packages) as modules.

# %% {"tags": ["code-along"], "slideshow": {"slide_type": "subslide"}}
# Welche Python-Dateien gibt es im aktuellen Verzeichnis?
for filename in os.listdir(os.getcwd()):
    if filename[-3:] == ".py":
        print(filename)


# %%
# Anzeigen des Quellcodes von `my_test_module.py`
# # %pycat my_test_module.py


# %% {"tags": ["code-along"]}
# Andere Möglichkeit, den Inhalt von `my_test_module.py` anzuzeigen.
with open("my_test_module.py", "r") as file:
    text = file.read()

print(text)


# %%
# Top-level code wird ausgeführt


# %%
# get_ipython().run_line_magic('load_ext', 'autoreload')
# get_ipython().run_line_magic('autoreload', '2')


# %% {"tags": ["code-along"]}
# Top-level code wird NICHT mehr ausgeführt
import my_test_module


# %% {"tags": ["code-along"]}
my_test_module.add1(2)


# %% {"tags": ["code-along"]}
# add1


# %% {"tags": ["code-along"]}
import my_test_module as mm

# %% {"tags": ["code-along"]}
mm.add1(1)


# %% {"tags": ["code-along"]}
mm.perform_complex_computation(17)


# %% {"tags": ["code-along"]}
from my_test_module import multiply_by_2


# %% {"tags": ["code-along"]}
multiply_by_2(2)


# %% {"tags": ["code-along"]}
from my_test_module import multiply_by_2 as mult2


# %% {"tags": ["code-along"]}
mult2(4)


# %% {"tags": ["code-along"]}
# Im Regelfall besser vermeiden:
from my_test_module import *


# %% {"tags": ["code-along"]}
multiply_by_2(3)


# %% {"tags": ["code-along"]}
add1(3)


# %% {"tags": ["code-along"]}
# Anzeigen aller definierten Namen:
dir(my_test_module)


# %% {"tags": ["code-along"]}
[name for name in dir(my_test_module) if name[0] != "_"]


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
#
#  ## Beispiel: `HttpServer`
#
# Der Python Interpreter hat keinen eingebauten HTTP Server. Mittels der
# Standardbibliothek ist es aber nicht schwer einen zu schreiben.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Example: `HttpServer`
#
# The Python interpreter does not have a built-in HTTP server. Using the
# standard library, it is not difficult to write one.

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  ### Beispiel: `ModuleTest`
#
# Das `ModuleTest` Beispiel zeigt, wie ein Programm aus mehreren Modulen
# bestehen kann.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ### Example: `ModuleTest`
#
# The `ModuleTest` example shows how a program can be composed of several modules.

# %%
__name__


# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
#
#  ## Packages
#
#  - Methode um Module mit zu strukturieren: `a.b.c`, `a.b.x`
#  - Ein Package ist eine Zusammenfassung von mehreren Modulen
#  - `b` ist Sub-Package von `a`, `c` und `x` sind Submodule von `b`

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Packages
#
# - Packages are a method to structure modules in a hierarchy: `a.b.c`, `a.b.x`
# - A package is a combination of several modules
# - `b` is subpackage of `a`, `c` and `x` are submodules of `b`

# %% {"tags": ["code-along"]}
from html.parser import HTMLParser
import html.entities


# %% {"tags": ["code-along"]}
HTMLParser()


# %% {"tags": ["code-along"]}
html.entities.entitydefs["Psi"]


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  ### Struktur von Packages
#
#  - Hierarchie durch Verzeichnisse und Python Dateien
#    - Z.B. Verzeichnis `html` mit Unterverzeichnissen `parser`, `entities`
#  - Benötigt eine `__init__.py` Datei in jedem Verzeichnis, aus dem Code importiert werden soll
#  - Die `__init__.py` Datei kann leer sein (und ist oft leer)

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ### Structure of packages
#
# - Hierarchy comprised of directories and Python files
#   - E.g. directory `html` with subdirectories `parser`, `entities`
# - Requires a `__init__.py` file in each directory containing code that should be imported
#   - This is not quite true...
# - The `__init__.py` file can be (and often is) empty

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
#
#  <img src="img/package-structure.png" alt="Package structure"
#       style="display:block;margin:auto;width:40%"></img>

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
#
#  ### Finden von Packages
#
#  - Python sucht in `sys.path` nach dem Package-Verzeichnis.
#  - Dieser kann durch die Environment-Variable `PYTHONPATH` oder direkt von
#    Python aus beeinflusst werden.
#  - In den meisten Fällen ist es besser, keine komplizierten Operationen an
#    `sys.path` vorzunehmen.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ### Finding packages
#
#  - Python looks for the package directory in `sys.path`.
#  - This can be set using the environment variable `PYTHONPATH` or directly from
#    Python.
#  - In most cases it is better not to undertake complicated operations on
#    `sys.path`.

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
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

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ### The `import` statement
#
#  `import a.b.c`:
#
#  - `a` and `b` must be packages (directories).
#  - `c` can be a module or a package
#
#  `from a.b.c import d`
#  - `a` and `b` must be packages
#  - `c` can be a module or a package
#  - `d` can be a module, package, or name (i.e. variable, function, class, etc.).

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
#
#  ### Referenzen innerhalb eines Packages
#
#  - `from . import a` importiert `a` aus dem aktuellen Package
#  - `from .. import a` importiert `a` aus dem übergeordneten Package
#  - `from .foo import a` importiert `a` aus dem "Geschwistermodul" `foo`

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ### References within a package
#
#  - `from . import a` imports `a` from the current package
#  - `from .. import a` imports `a` from the parent package
#  - `from .foo import a` imports `a` from its "sibling module" `foo`

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
#
#  ## Beispiel: `MessageQueue`
#
#  Das `MessageQueue` Beispiel zeigt, wie ein Programm aus mehreren Packages bestehen kann.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Example: `MessageQueue`
#
#  The `MessageQueue` example shows how a program can consist of several packages.

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
#
#  # Pytest: Testen in Python
#
#  - Python bietet mehrere eingebaute Pakete zum Schreiben von Unit-Tests und Dokumentationstests an (`unittest` und `doctest`).
#  - Viele Projekte verwenden trotzdem das `pytest` Paket, da es viel "Boilerplate" beim Schreiben von Tests vermeidet.
#  - `pytest` kann `unittest` und `doctest`-Tests ausführen.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # Pytest: testing in Python
#
#  - Python provides several built-in packages for writing unit tests and documentation tests (`unittest` and `doctest`).
#  - Many projects use the `pytest` package anyway, as it avoids a lot of "boilerplate" when writing tests.
#  - `pytest` can run `unittest` and `doctest` tests.

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
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

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Installing pytest
#
#  Pytest is pre-installed in the Anaconda installation
#
#  When using the standard Python distribution, it can be installed with
#  ```shell
#  pip install pytest
#  ```

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  ## Schreiben von Tests
#
#  - Pytest kann sehr flexibel konfiguriert werden
#  - Wir verwenden nur die einfachsten Features und verlassen uns auf die automatische Konfiguration
#  - Tests für ein Paket werden in einem Unter-Package `test` geschrieben
#  - Tests für die Datei `foo.py` sind in der Datei `test/foo_test.py`
#  - Jeder Test ist eine Funktion, deren Name mit `test` beginnt
#  - Assertions werden mit der `assert` Anweisung geschrieben

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Writing tests
#
#  - Pytest can be configured very flexibly
#  - We only use the most basic features and rely on automatic configuration
#  - Tests for a package are written in a sub-package `test`
#  - Tests for the `foo.py` file are in the `test/foo_test.py` file
#  - Each test is a function whose name starts with `test`
#  - Assertions are written with the `assert` statement

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  ## Beispiel Testen von `MessageQueueDist`
#
#  Siehe `Examples/MessageQueueDist`

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Example testing `MessageQueueDist`
#
#  See `Examples/MessageQueueDist`

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Workshop
#
# - `Workshop_136_todo_list_v3`
# - Bis Abschnitt "Laden und Speichern"

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Workshop
#
# - `Workshop_136_todo_list_v3`
# - Up to "Load and Save" section

# %%
