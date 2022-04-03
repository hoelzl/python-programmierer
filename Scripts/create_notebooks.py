# %%
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import jupytext

# %%
ROOT_PATH = Path(
    r"C:\Users\tc\Programming\Python\Courses\Own\python-programmierer")
MACRO_PATH = ROOT_PATH / "Templates/Macros"

# %%
REMOVE_CELL = 0
KEEP_CELL = 1

# %%
def process_cell(cell, tags_to_remove=None, language=None):
    if tags_to_remove is not None and "tags" in cell.metadata.keys():
        for tag in tags_to_remove:
            if tag in cell.metadata["tags"]:
                cell.source = ""
                if cell.cell_type == "code":
                    cell.outputs = []
                break
    if language and cell.cell_type == "markdown" and "lang" in cell.metadata.keys():
        if cell.metadata["lang"] != language:
            return REMOVE_CELL
    return KEEP_CELL


# %%
def convert_template(jinja_env: Environment, template_name: str,
                     output_path: Path, tags_to_remove=None, language=None):
    template = jinja_env.get_template(template_name)
    result = template.render()
    output_file = output_path / template_name

    notebook = jupytext.reads(result)
    notebook.metadata.jupytext.formats = "ipynb"
    if tags_to_remove is not None or language is not None:
        indices_to_remove = []
        for index, cell in enumerate(notebook.cells):
            result = process_cell(cell, tags_to_remove, language)
            if result == REMOVE_CELL:
                indices_to_remove.append(index)
        for index in reversed(indices_to_remove):
            del notebook.cells[index]
            
    jupytext.write(notebook, output_file.with_suffix(".ipynb"), fmt="ipynb")


# %%
def convert_all_python_templates(jinja_env: Environment, template_dir: Path,
                                 output_dir: Path, glob_pattern="*.py",
                                 tags_to_remove=None, language=None):
    output_dir.mkdir(exist_ok=True, parents=True)
    for file in template_dir.glob(glob_pattern):
        convert_template(jinja_env, file.name, output_dir, tags_to_remove, language)


# %%
def convert_slide_templates(language=None):
    template_path = ROOT_PATH / "Templates/Slides"
    output_path = ROOT_PATH / "Slides/Completed"
    if language:
        output_path = output_path / language.title()

    jinja_env = Environment(line_statement_prefix="# j2",
                            loader=FileSystemLoader(
                                [MACRO_PATH, template_path]))
    convert_all_python_templates(jinja_env, template_path, output_path,
                                 glob_pattern="topic*.py", language=language)


# %%
def convert_slide_templates_to_codealongs(language=None):
    template_path = ROOT_PATH / "Templates/Slides"
    output_path = ROOT_PATH / "Slides/Code_Along"
    if language:
        output_path = output_path / language.title()

    jinja_env = Environment(line_statement_prefix="# j2",
                            loader=FileSystemLoader(
                                [MACRO_PATH, template_path]))
    convert_all_python_templates(jinja_env, template_path, output_path,
                                 glob_pattern="topic*.py",
                                 tags_to_remove=("code-along",),
                                 language=language)


# %%
def convert_workshop_templates_to_solutions(language=None):
    template_path = ROOT_PATH / "Templates/Workshops"
    output_path = ROOT_PATH / "Workshops/Solutions"
    if language:
        output_path = output_path / language.title()

    jinja_env = Environment(line_statement_prefix="# j2",
                            loader=FileSystemLoader(
                                [MACRO_PATH, template_path]))
    convert_all_python_templates(jinja_env, template_path, output_path,
                                 glob_pattern="workshop*.py", language=language)


# %%
def convert_workshop_templates_to_exercises(language=None):
    template_path = ROOT_PATH / "Templates/Workshops"
    output_path = ROOT_PATH / "Workshops/Exercises"
    if language:
        output_path = output_path / language.title()

    jinja_env = Environment(line_statement_prefix="# j2",
                            loader=FileSystemLoader(
                                [MACRO_PATH, template_path]))
    convert_all_python_templates(jinja_env, template_path, output_path,
                                 glob_pattern="workshop*.py",
                                 tags_to_remove=("solution",), language=language)


# %%
if __name__ == "__main__":
    # convert_slide_templates()
    # convert_slide_templates_to_codealongs()
    convert_slide_templates(language="en")
    convert_slide_templates_to_codealongs(language="en")
    convert_slide_templates(language="de")
    convert_slide_templates_to_codealongs(language="de")
    convert_workshop_templates_to_solutions(language="en")
    convert_workshop_templates_to_exercises(language="en")
    convert_workshop_templates_to_solutions(language="en")
    convert_workshop_templates_to_exercises(language="en")
