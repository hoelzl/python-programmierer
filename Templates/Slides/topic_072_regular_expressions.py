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
# <div style="text-align:center; font-size:200%;"><b>Reguläre Ausdrücke</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Regular Expressions</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
# # Finden und Ersetzen in Strings

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # Finding and replacing in strings

# %%
tounge_twister = (
    "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"
)

# %% {"tags": ["code-along"]}
first_index = tounge_twister.index("wood")
first_index

# %% {"tags": ["code-along"]}
tounge_twister[first_index : first_index + len("wood")]

# %% {"tags": ["code-along"]}
print(first_index)
print(first_index + len("wood"))

# %% {"tags": ["code-along"]}
# tounge_twister[9:13] = "coffee"

# %% {"tags": ["code-along"]}
tounge_twister[:9] + "coffee" + tounge_twister[13:]

# %% {"tags": ["code-along"]}
tounge_twister.index("wood", first_index + 1)

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
# # Finden mit Regulären Ausdrücken

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # Finding with regular expressions

# %% {"tags": ["code-along"]}
import re

# %% {"tags": ["code-along"]}
re.findall("wood", tounge_twister)

# %% {"tags": ["code-along"]}
result = re.search("wood", tounge_twister)
result

# %% {"tags": ["code-along"]}
start, end = result.span()
print("start:", start)
print("end:", end)

# %% {"tags": ["code-along"]}
result.start()

# %% {"tags": ["code-along"]}
result.end()

# %% {"tags": ["code-along"]}
result = re.search("wood", tounge_twister[end:])
result

# %% {"tags": ["code-along"]}
tounge_twister[end:][result.start() :]

# %% {"tags": ["code-along"]}
re.sub("wood", "coffee", tounge_twister)

# %% {"tags": ["code-along"]}
re.sub("wood ", "coffee ", tounge_twister)

# %% {"tags": ["code-along"]}
re.sub("wood\\W", "coffee", tounge_twister)

# %% {"tags": ["code-along"]}
re.sub("wood(\\W)", "coffee\\1", tounge_twister)

# %% {"tags": ["code-along"]}
re.sub(r"wood(\W)", r"coffee\1", tounge_twister)

# %% {"tags": ["code-along"]}
wood_rx = re.compile("wood")
type(wood_rx)

# %% {"tags": ["code-along"]}
wood_rx.findall(tounge_twister)

# %% {"tags": ["code-along"]}
wood_rx.search(tounge_twister)

# %% {"tags": ["code-along"]}
wood_rx.search(tounge_twister, 13)

# %% {"tags": ["code-along"]}
wood_rx2 = re.compile(r"\bwood\b")

# %% {"tags": ["code-along"]}
wood_rx2.sub(r"coffee", tounge_twister)

# %% {"tags": ["code-along"]}
def annotate(match):
    return f"{match.group()}[{match.start()}-{match.end()}]"

# %% {"tags": ["code-along"]}
wood_rx2.sub(annotate, tounge_twister)

# %% {"tags": ["code-along"]}
four_letter_word_rx = re.compile(r"\b\w{4}\b")

# %% {"tags": ["code-along"]}
four_letter_word_rx.sub("XXXX", tounge_twister)

# %% {"tags": ["code-along"]}
any_length_rx = re.compile(r"\w*")

# %% {"tags": ["code-along"]}
def x_out(match):
    return "X" * (match.end() - match.start())

# %% {"tags": ["code-along"]}
any_length_rx.sub(x_out, tounge_twister)

# %% {"tags": ["code-along"]}
short_word_rx = re.compile(r"\b\w{1,4}\b")

# %% {"tags": ["code-along"]}
short_word_rx.sub(lambda m: "X" * len(m.group()), tounge_twister)

# %% {"tags": ["code-along"]}
long_word_rx = re.compile(r"\b\w{5,}\b")

# %% {"tags": ["code-along"]}
long_word_rx.sub(lambda m: m.group().upper(), tounge_twister)

# %% {"tags": ["code-along"]}
long_word_rx.search(tounge_twister)

# %% {"tags": ["code-along"]}
long_word_rx.search("To be or not to be?")

# %% {"tags": ["code-along"]}
long_word_rx.search("To be or not to be?") is None

# %% {"tags": ["code-along"]}
double_vocal_rx = re.compile(r"\w*([aeiou]{2})\w*")

# %% {"tags": ["code-along"]}
match = double_vocal_rx.search(tounge_twister)
match

# %% {"tags": ["code-along"]}
match.group(0)

# %% {"tags": ["code-along"]}
match.group(1)

# %% {"tags": ["code-along"]}
match = double_vocal_rx.search(tounge_twister, 13)
match

# %% {"tags": ["code-along"]}
match.group(0)

# %% {"tags": ["code-along"]}
match.group(1)

# %% {"tags": ["code-along"]}
email_rx = re.compile(r"([\w._+-]+)@([\w._+-]+)", re.IGNORECASE)

# %% {"tags": ["code-along"]}
match = email_rx.match("joe.cool@people.example.com")

# %% {"tags": ["code-along"]}
match.group(0, 1, 2)

# %%
email_rx.match("Email: joe.cool@people.example.com") is None

# %% {"tags": ["code-along"]}
match = email_rx.match("joe-cool+123@my_domain.example.com or something")

# %% {"tags": ["code-along"]}
match.group(0, 1, 2)

# %% {"tags": ["code-along"]}
match = email_rx.fullmatch("joe-cool+123@my_domain.example.com")

# %% {"tags": ["code-along"]}
match.group(0, 1, 2)

# %% {"tags": ["code-along"]}
email_rx.fullmatch("joe-cool+123@my_domain.example.com or something")

# %%
