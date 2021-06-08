# %% [markdown]
#
# ## Identität von Objekten

# %%
a = [1, 2, 3]
b = [1, 2, 3]
c = b

# %%
print(f"a = {a}, b = {b}, c = {c}")

# %%
a[0] = 10

# %%
print(f"a = {a}, b = {b}, c = {c}")

# %%
b[0] = 20

# %%
c[1] = 30

# %%
print(f"a = {a}, b = {b}, c = {c}")

# %% [markdown]
#
# <img src="img/identity.svg" style="display:block;width:70%;margin:auto;"/>


# %% [markdown]
#
# ## Test der Identität von Objekten

# %%
a = [1, 2, 3]
b = a
c = [1, 2, 3]
d = c[:]

# %% [markdown]
#
# `==` testet Gleichheit der Werte, nicht (notwendigerweise) Objektidentität.

# %%
a == b

# %%
b == c

# %%
c == d

# %% [markdown]
#
# Mit `is` kann man Objektidentität testen:

# %%
a = [1, 2, 3]
b = a
c = [1, 2, 3]
d = c[:]

# %%
a is b

# %%
b is c

# %%
c is d

# %% [markdown]
#
# Die Funktion `id()` gibt die Adresse eines Objekts zurück:

# %%
id([1, 2, 3])

# %% [markdown]
#
# Meistens stellt man Adressen in hexadezimaler Form dar:

# %%
hex(id([1, 2, 3]))

# %% [markdown]
# 
# Gilt für Zahlen mit `x == y` immer `x is y`?

# %%
x = 1
y = 1
z = 1.0
print(x == y)
print(x is y)
print(x == z)
print(x is z)

# %%
x = 256
y = 256
print(x == y)
print(x is y)

# %%
import ctypes
x_refcount = ctypes.c_long.from_address(id(x)).value
x_int_value = ctypes.c_long.from_address(id(x) + 24).value

# %%
print(hex(id(x)))
print(x_refcount)
print(x_int_value)

# %%
