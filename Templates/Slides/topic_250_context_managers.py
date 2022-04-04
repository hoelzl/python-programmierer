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

# %%

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Context Manager</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Context managers</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>


# %% [markdown] {"lang": "de"}
#
#  # Context Managers
#
#  Context Manager sind Objekte, die häufig verwendete `try-except-finally`
#  Patterns für `with`-Blöcke kapseln.

# %% [markdown] {"lang": "en"}
# # Context Managers
#
# Context managers are objects that are commonly used to encapsulate `try-except-finally`
# patterns in `with` blocks.

# %% {"tags": ["code-along"]}
from contextlib import AbstractContextManager
import sys


class ProgressNotifier(AbstractContextManager):
    def __init__(self, entry_message, width=72):
        self.entry_message = entry_message
        self.width = width
        self.num_completed_items = 0

    def __enter__(self):
        print(f"{self.entry_message}")
        sys.stdout.flush()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print("failed!")
        else:
            print("done.")

    def item_completed(self):
        self.num_completed_items += 1
        print(".", end="\n" if self.num_completed_items % self.width == 0 else "")
        sys.stdout.flush()

    def item_skipped(self):
        self.num_completed_items += 1
        print("-", end="\n" if self.num_completed_items % self.width == 0 else "")
        sys.stdout.flush()


def progress(entry_message):
    return ProgressNotifier(entry_message)


# %% {"tags": ["code-along"]}
import random


def download_items(n):
    with progress("Downloading articles") as p:
        for i in range(n):
            r = random.random()
            if r < 0.001:
                raise IOError("Download failed")
            elif r < 0.1:
                p.item_skipped()
            else:
                p.item_completed()


# %% {"tags": ["code-along"]}
try:
    download_items(500)
    print("Finished successfully")
except IOError:
    print("Caught IOError")
