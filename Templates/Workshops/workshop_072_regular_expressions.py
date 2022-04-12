# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py:percent
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

# %% [markdown] lang="de"
# # Reguläre Ausdrücke
#
# Schreiben Sie einen Regulären Ausdruck, der Gleitkommazahlen matcht (ein oder
# mehrere Ziffern, gefolgt von einem Punkt, gefolgt von ein oder mehreren
# Ziffern).
#
# Testen Sie den Regulären Ausdruck mit folgenden Werten: `1.0`, `842.234`,
# `23-38`, `12.`, `.1`.
#
# *Hinweis:* `\d` matcht eine einzelne Ziffer.

# %% [markdown] lang="en"
# # Regular Expressions
#
# Write a regular expression that matches floating point literals (one or more
# digits, followed by a decimal point, followed by one or more digits).
#
# Test you regular expressions with the following values: `1.0`, `842.234`,
# `23-38`, `12.`, `.1`.
#
# *Hint:* `\d` matches a single digit.

# %% tags=["solution"]
import re

fp_rx = re.compile(r"\d+\.\d+")

# %% tags=["solution"]
fp_rx.fullmatch("1.0")

# %% tags=["solution"]
fp_rx.fullmatch("842.234")

# %% tags=["solution"]
fp_rx.fullmatch("23-38")

# %% tags=["solution"]
fp_rx.fullmatch("12.")

# %% tags=["solution"]
fp_rx.fullmatch(".1")

# %% [markdown] lang="de"
#
# Schreiben Sie einen Regulären Ausdruck, der URLs matcht, die `http` oder
# `https` Protokoll haben und nach dem Domain-Namen höchstens einen einzelnen
# `/` als Pfad.
#
# Zum Beispiel soll `https://www.example.com/` gematcht werden, nicht aber
# `email://example.com`, `http://example.com/foo` oder
# `http://www..example.com/`.

# %% [markdown] lang="en"
#
# Write a regular expression that matches URLs that use the `http` or `https`
# protocol and whose domain name is followed either no path or a single slash.
#
# For example, the regular expression should match `http://example.com/` and
# `https://www.example.com/`, but not `email://example.com`,
# `http://example.com/foo`, or `http://www..example.com/`.

# %% tags=["solution"]
url_rx = re.compile(r"https?://(\w+\.)+\w+/?")

# %% tags=["solution"]
url_rx.fullmatch(r"http://example.com/")

# %% tags=["solution"]
url_rx.fullmatch(r"https://www.example.com/")

# %% tags=["solution"]
url_rx.fullmatch(r"email://example.com/") is None

# %% tags=["solution"]
url_rx.fullmatch(r"http://example.com/foo") is None

# %% tags=["solution"]
url_rx.fullmatch(r"https://www..example.com/") is None

# %% [markdown] lang="de"
#
# Ersetzen Sie alle URLs im folgenden Text durch die Zeichenkette `<URL>`.

# %% [markdown] lang="en"
#
# Replace all URLs in the following text with the string `<URL>`

# %%
text = "Use http://www.example.com or https://www.example.com/ as example domains."


# %% tags=["solution"]
url_rx.sub("<URL>", text)

# %%
