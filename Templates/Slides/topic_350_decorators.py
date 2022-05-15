# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
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
# <div style="text-align:center; font-size:200%;"><b>Decorators</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Decorators</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Decorators
#
# Siehe [PEP 318](https://peps.python.org/pep-0318/)

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# ## The XML Package
#
# See [PEP 318](https://peps.python.org/pep-0318/)

# %% {"tags": ["code-along"]}
def log_exec(fun):
	def logged_fun(*args, **kwargs):
		print(f"Calling {fun.__name__} on {args}, {kwargs}.")
		return fun(*args, **kwargs)
	return logged_fun

# %% {"tags": ["code-along"]}
@log_exec
def say_hi(name="world"):
	print(f"Hi {name}!")

# %% {"tags": ["code-along"]}
say_hi()

# %% {"tags": ["code-along"]}
say_hi("Joe")

# %% {"tags": ["code-along"]}
@log_exec
def my_dict(id, **kwargs):
	return dict(id=id, **kwargs)

# %% {"tags": ["code-along"]}
my_dict(123)

# %% {"tags": ["code-along"]}
my_dict(123, foo=234, bar=345)

# %% {"tags": ["code-along"]}
d = dict(foo=234, bar=345)

# %% {"tags": ["code-along"]}
my_dict(1, **d)

# %%
