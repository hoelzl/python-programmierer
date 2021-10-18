# %%
from os import replace
from pathlib import Path
from pprint import pprint
from nbex.interactive import session
import re

# %%
notebooks = list(Path().glob("*.ipynb"))

# %%
if session.is_interactive:
    pprint(notebooks)

# %%
special_char_regex = re.compile(r"([ \-()])")

# %%
def create_new_path(old_path):
    old_name = old_path.name
    new_name = "lecture_" + re.sub(special_char_regex, "_", old_name)
    return old_path.with_name(new_name)


# %%
new_notebooks = [
    create_new_path(path) for path in notebooks if re.match(r"^\d{3}", path.name)
]

# %%
if session.is_interactive:
    pprint(new_notebooks)

# %%
renamings = list(zip(notebooks, new_notebooks))

# %%
if session.is_interactive:
    pprint(renamings)

# %%
if session.is_interactive:
    for old_path, new_path in renamings:
        assert old_path.exists(), f"Path {old_path} does not exist"
        assert not new_path.exists(), f"Path {new_path} already exists" 
        print(f"Renaming {old_path} to {new_path}")
        old_path.rename(new_path)

# %%
