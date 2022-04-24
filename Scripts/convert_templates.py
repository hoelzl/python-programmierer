# %%
from logging import warning, info
from pathlib import Path
import jupytext
import nbformat
from copy import deepcopy
from nbformat.notebooknode import NotebookNode

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
    cell.metadata["tags"] = tags


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
        if tag not in ["code-along", "solution"]:
            print(f"Found code tag: {tag!r}.")
    if add_keep_tag:
        info("Adding keep tag to cell.")
        tags.append("keep")


# %%
def process_markdown_cell_metadata(cell):
    assert cell.cell_type == "markdown"
    tags = get_tags(cell)
    if cell.metadata.get("lang") is None:
        print(f"Markdown cell {cell.source[:40]!r} has no language tag.")
    for tag in tags:
        if tag not in []:
            print(f"Found markdown tag: {tag!r}.")


# %%
def process_cell_metadata(cell):
    if cell.cell_type == "code":
        process_code_cell_metadata(cell)
    elif cell.cell_type == "markdown":
        process_markdown_cell_metadata(cell)
    else:
        warning(f"Not processing cell with type {cell.cell_type}.")


# %%
def print_cell_info(cell):
    print(
        f"Copy: type = {cell.cell_type}, "
        f"tags = {cell.metadata.get('tags', [])}, "
        f"lang = {cell.metadata.get('lang')}"
    )
    if cell.cell_type == "code":
        print(f"      source = {cell.source[:40]!r}")


# %%
def process_cell(cell):
    cell_type = cell.cell_type
    tags = cell.metadata.get("tags", [])
    lang = cell.metadata.get("lang")
    # Check that we don't receive a subtype
    result = deepcopy(cell)
    assert type(result) == type(cell)
    process_cell_metadata(result)
    # print_cell_info(cell)
    # print_cell_info(result)
    return result


# %%
def process_notebook(nb):
    for cell in nb.get("cells", []):
        process_cell(cell)


# %%
def load_and_process_notebook(path: Path):
    nb = jupytext.read(path)
    process_notebook(nb)


# %%
_playground = jupytext.read(OLD_SOURCE_PATH / "Slides/topic_000_playground.py")
_quickstart = jupytext.read(OLD_SOURCE_PATH / "Slides/topic_010_quickstart.py")

# %%
process_notebook(_playground)

# %%
process_notebook(_quickstart)

# %%
