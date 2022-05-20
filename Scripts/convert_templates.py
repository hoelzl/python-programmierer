# %%
import logging
from logging import warning, info, debug
from pathlib import Path
from pprint import pprint

import jupytext
from copy import deepcopy

# %%
logging.getLogger().setLevel(logging.INFO)

# %%
OLD_SOURCE_PATH = Path(
    r"C:\Users\tc\Programming\Python\Courses\Own\python-programmierer\Templates"
)
NEW_SOURCE_PATH = Path(
    r"C:\Users\tc\Programming\Python\Courses\Own\python-courses\Blueprints"
)

# %%
assert OLD_SOURCE_PATH.exists()
assert OLD_SOURCE_PATH.is_dir()

# %%
NEW_SOURCE_PATH.mkdir(exist_ok=True, parents=True)

# %%
REMOVE_CELL = 0
KEEP_CELL = 1


# %%
def get_tags(cell):
    return cell.metadata.setdefault("tags", [])


# %%
def set_tags(cell, tags):
    if tags:
        cell.metadata["tags"] = tags
    elif cell.metadata.get("tags") is not None:
        del cell.metadata["tags"]


# %%
def get_cell_lang(cell):
    return cell.metadata.get("lang")


# %%
def convert_slide_metadata_to_tag(cell):
    slide_type = cell.metadata.get("slideshow", {}).get("slide_type")
    if slide_type is not None:
        if slide_type != "-":
            tags = get_tags(cell)
            tags.append(slide_type)
            set_tags(cell, tags)
        del cell.metadata["slideshow"]


# %%
_EXPECTED_CODE_TAGS = ["code-along", "solution", "slide", "subslide"]


# %%
def process_code_cell_metadata(cell):
    assert cell.cell_type == "code"
    tags = get_tags(cell)
    add_keep_tag = True
    if "code-along" in tags:
        tags.remove("code-along")
        add_keep_tag = False
    if "solution" in tags:
        tags.remove("solution")
        add_keep_tag = False
    for tag in tags:
        if tag not in _EXPECTED_CODE_TAGS:
            print(f"Found unexpected code tag: {tag!r}.")
    if add_keep_tag:
        debug("Adding keep tag to cell.")
        tags.append("keep")
    set_tags(cell, tags)


# %%
_EXPECTED_MARKDOWN_TAGS = ["slide", "subslide"]


# %%
def process_markdown_cell_metadata(cell):
    assert cell.cell_type == "markdown"
    tags = get_tags(cell)
    if get_cell_lang(cell) is None:
        warning(f"Markdown cell {cell.source[:40]!r} has no language tag.")
    for tag in tags:
        if tag not in _EXPECTED_MARKDOWN_TAGS:
            warning(f"Found markdown tag: {tag!r}.")
    set_tags(cell, tags)


# %%
def process_cell_metadata(cell):
    convert_slide_metadata_to_tag(cell)
    if cell.cell_type == "code":
        process_code_cell_metadata(cell)
    elif cell.cell_type == "markdown":
        process_markdown_cell_metadata(cell)
    else:
        warning(f"Not processing cell with type {cell.cell_type}.")


# %%
def print_cell_info(cell, prefix="Cell"):
    print(
        f"{prefix}: type = {cell.cell_type}, "
        f"tags = {get_tags(cell)}, "
        f"lang = {cell.metadata.get('lang')}"
    )
    if cell.cell_type == "code":
        print(f"{' ' * len(prefix)}  source = {cell.source[:40]!r}")


# %%
def process_cell(cell):
    process_cell_metadata(cell)


# %%
def process_notebook(nb):
    for cell in nb.get("cells", []):
        process_cell(cell)


# %%
_playground_path = OLD_SOURCE_PATH / "Slides/topic_000_playground.py"
_intro_path = OLD_SOURCE_PATH / "Slides/topic_010_getting_started.py"
_quickstart_path = OLD_SOURCE_PATH / "Slides/topic_040_quickstart.py"

# %%
_playground = jupytext.read(_playground_path)
_intro = jupytext.read(_intro_path)
_quickstart = jupytext.read(_quickstart_path)

# %%
process_notebook(_playground)

# %%
process_notebook(_intro)

# %%
process_notebook(_quickstart)


# %%
def load_and_process_notebook(path: Path):
    output_path = NEW_SOURCE_PATH / path.relative_to(OLD_SOURCE_PATH)
    nb = jupytext.read(path)
    process_notebook(nb)
    info(f"Writing processed notebook to '{output_path.relative_to(NEW_SOURCE_PATH)}'.")
    output_path.parent.mkdir(exist_ok=True, parents=True)
    jupytext.write(nb, output_path, fmt={
        "extension": "py", "format_name": "percent", "cell_metadata_json": False
    })


# %%
load_and_process_notebook(_playground_path)

# %%
load_and_process_notebook(_intro_path)

# %%
load_and_process_notebook(_quickstart_path)


# %%
def load_and_process_notebooks(dir_path: Path, pattern="*.py"):
    nb_paths = list(dir_path.glob(pattern))
    for nb_path in nb_paths:
        load_and_process_notebook(nb_path)


# %%
load_and_process_notebooks(OLD_SOURCE_PATH / "Slides")

# %%
load_and_process_notebooks(OLD_SOURCE_PATH / "Workshops")
