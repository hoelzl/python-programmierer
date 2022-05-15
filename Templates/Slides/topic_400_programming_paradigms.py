# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Programmierparadigmen</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Programming paradigms</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# # Programmierparadigmen
# - Prozedural
# - Funktional (?)
# - Objektorientiert

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# # Programming paradigms
# - Procedural
# - Functional (?)
# - Object oriented

# %% {"slideshow": {"slide_type": "slide"}, "tags": ["code-along"]}
def add(x, y):
    return x + y


# %% {"tags": ["code-along"]}
add(2, 3)

# %% {"tags": ["code-along"]}
accu = 0


# %% {"slideshow": {"slide_type": "slide"}, "tags": ["code-along"]}
def inc(x):
    global accu
    accu += x


# %% {"tags": ["code-along"]}
def disp():
    print(f"Accumulator is {accu}.")


# %% {"tags": ["code-along"]}
disp()
inc(2)
inc(3)
disp()


# %% {"slideshow": {"slide_type": "slide"}, "tags": ["code-along"]}
def ntimes(n, f, x):
    if n <= 0:
        return x
    else:
        return ntimes(n - 1, f, f(x))


# %% {"tags": ["code-along"]}
ntimes(10, lambda x: x * 2, 1)

# %% {"slideshow": {"slide_type": "slide"}, "tags": ["code-along"]}
from pathlib import Path

path = Path("./some_file.txt")

# %% {"tags": ["code-along"]}
path.with_suffix(".md").absolute()
