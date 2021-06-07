# %% [markdown]
#
# ## Test der Identität von Objekten

# %%
a = [1, 2, 3]
b = a
c = [1, 2, 3]
d = c[:]

# %%
a == b

# %%
b == c

# %%
c == d

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

# %%
hex(id([1, 2, 3]))

# %%
def modify_list(lst):
    print("modify_list: before", lst)
    lst.append("abc")
    print("modify_list: after", lst)


# %%
my_list = [1, 2, 3]
modify_list(my_list)

# %%
my_list

# %%
