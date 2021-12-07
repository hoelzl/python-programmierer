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
# {{ doc.header("Context Manager") }}


# %% [markdown]
#
#  # Context Managers
#
#  Context Manager sind Objekte, die häufig verwendete `try-except-finally`
#  Patterns für `with`-Blöcke kapseln.

# %% {{ doc.codealong() }}
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



# %% {{ doc.codealong() }}
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



# %% {{ doc.codealong() }}
try:
    download_items(500)
    print("Finished successfully")
except IOError:
    print("Caught IOError")

