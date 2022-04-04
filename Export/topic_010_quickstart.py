#!/usr/bin/env python
# coding: utf-8

# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Quickstart</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# # Python and Jupyter notebooks
#
# We'll start with a brief introduction:
# - How does Python work?
# - What are Jupyter notebooks?

# ## Compiler (C++)
#
# <img src="img/compiler.svg" style="width:60%;margin:auto"/>

# ## interpreter (Python)
#
# <img src="img/interpreter.svg" style="width:60%;margin:auto"/>

# ## Jupyter Notebooks
#
# <img src="img/jupyter-notebook.svg" style="width:60%;margin:auto"/>

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

page_load_time = np.random.normal(3.0, 1.0, 1000)
purchase_amount = np.random.normal(50.0, 1.5, 1000) - page_load_time

plt.figure(figsize=(12, 8))
plt.scatter(page_load_time, purchase_amount)


# ## Variables and data types
#
# Numbers and arithmetic:

# In[2]:


1 + 2 + 3


# In[3]:


1.5 + 7.4


# In[4]:


1 + 2 * 3


# ## Strings

# In[5]:


"This is a string"


# In[6]:


"This is also a string"


# In[8]:


str(1 + 2)


# In[10]:


"3" + "2"


# In[13]:


("literal strings" " can be " "concatenated")


# ### Variables

# In[19]:


answer = 12


# In[21]:


my_value = answer + 2


# In[22]:


my_value


# ## Jupyter notebooks: displaying values
#
# - Jupyter notebooks print the last value of each cell on the screen
# - That doesn't happen in "normal" Python programs!
#   - At least when they are executed as programs
#   - The interactive interpreter behaves similar to notebooks

# In[17]:


123


# To prevent the output of the last value of a cell in Jupyter
# you can end the line with a semicolon:

# In[18]:


123


# Jupyter also displays the value of variables:

# In[ ]:


# In[ ]:


# In[ ]:


# To display multiple values ​​you can use the `print()` function:
#
# `print(...)` prints the values between the trailing parens on the screen.

# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# Compare the output to the following cell:

# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# ## Types

# In[ ]:


# In[ ]:


# In[ ]:


# ### Predefined functions

# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


print(round(0.5), round(1.5), round(2.5), round(3.5))


# ## Functions

# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


print(my_round(0.5), my_round(1.5), my_round(2.5), my_round(3.5))


# ### Micro workshop
#
# Write a function `greeting(name)` that prints a greeting in the form
# "Hello *name*!" to the screen, e.g.
# ```python
# >>> greeting("Max")
# Hi Max!
# >>>
# ```

# In[ ]:


# In[ ]:


# ### Methods

# In[ ]:


# In[ ]:


# In[ ]:


# ### Multiple parameters, default arguments

# In[ ]:


# In[ ]:


# In[ ]:


# ### Nested function calls

# In[ ]:


# ### Type annotations

# In[ ]:


# In[ ]:


# In[ ]:


# ## Lists and tuples

# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# ## Boolean values ​​and `if` statements

# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


def print_size(n):
    if n < 10:
        print("Very small")
    elif n < 15:
        print("Pretty small")
    elif n < 30:
        print("Average")
    else:
        print("Large")


# In[ ]:


print_size(1)
print_size(10)
print_size(20)
print_size(100)


# ### Micro workshop
#
# Write a function `fits_in_line(text: str, line_length: int = 72)`,
# which returns `True` or `False` depending on whether `text` fits into a line of
# length `line_length`:
# ```python
# >>> fits_in_line("Hello")
# True
# >>> fits_in_line("Hello", 3)
# false
# >>>
# ```
#
# Write a function `print_line(text: str, line_length:int = 72)`,
# that
# * prints `text` to the screen if that is possible in a line of length
#   `line_length`
# * prints `...` if that is not possible.
#
# ```python
# >>> print_line("Hello")
# Hello
# >>> print_line("Hello", 3)
# ...
# >>>
# ```

# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# ## `for` loops

# In[ ]:


# In[ ]:


# ### Micro workshop
#
# Write a function `print_all(items: list)` that prints the elements of a
# list `items` to the screen, one item per line:
#
# ```python
# >>> print_all([1, 2, 3])
# 1
# 2
# 3
# >>>
# ```
# What happens if you call the function with a string as an argument,
# e.g. `print_all("abc")`

# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# ### Micro workshop
#
# Write a function `print_squares(n: int)` that prints the squares of the
# numbers from 1 to n, one element per line:
#
# ```python
# >>>print_square(3)
# 1**2 = 1
# 2**2 = 4
# 3**2 = 9
# >>>
# ```

# In[ ]:


# In[ ]:


# ## Dictionaries

# In[ ]:


translations = {"snake": "Schlange", "bat": "Fledermaus", "horse": "Hose"}


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:
