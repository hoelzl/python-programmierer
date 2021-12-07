# %%
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import jupytext
from traitlets.config import Config
from nbconvert import NotebookExporter
from nbconvert.preprocessors import TagRemovePreprocessor

# %%
ROOT_PATH = Path(
    r"C:\Users\tc\Programming\Python\Courses\Own\python-programmierer")
MACRO_PATH = ROOT_PATH / "Templates/Macros"


# %%
def process_cell(cell, tags_to_remove):
    if "tags" in cell.metadata.keys():
        for tag in tags_to_remove:
            if tag in cell.metadata["tags"]:
                cell.source = ""
                if cell.cell_type == "code":
                    cell.outputs = []
                break


# %%
def convert_template(jinja_env: Environment, template_name: str,
                     output_path: Path, tags_to_remove=None):
    template = jinja_env.get_template(template_name)
    result = template.render()
    output_file = output_path / template_name

    notebook = jupytext.reads(result)
    notebook.metadata.jupytext.formats = "ipynb"
    if tags_to_remove is not None:
        for cell in notebook.cells:
            process_cell(cell, tags_to_remove)
    jupytext.write(notebook, output_file.with_suffix(".ipynb"), fmt="ipynb")


# %%
def convert_all_python_templates(jinja_env: Environment, template_dir: Path,
                                 output_dir: Path, glob_pattern="*.py",
                                 tags_to_remove=None):
    output_dir.mkdir(exist_ok=True, parents=True)
    for file in template_dir.glob(glob_pattern):
        convert_template(jinja_env, file.name, output_dir, tags_to_remove)


# %%
def convert_slide_templates():
    template_path = ROOT_PATH / "Templates/Slides"
    output_path = ROOT_PATH / "Slides/Completed"

    jinja_env = Environment(line_statement_prefix="# j2",
                            loader=FileSystemLoader(
                                [MACRO_PATH, template_path]))
    convert_all_python_templates(jinja_env, template_path, output_path,
                                 glob_pattern="topic*.py")


# %%
def convert_slide_templates_to_codealongs():
    template_path = ROOT_PATH / "Templates/Slides"
    output_path = ROOT_PATH / "Slides/Code_Along"

    jinja_env = Environment(line_statement_prefix="# j2",
                            loader=FileSystemLoader(
                                [MACRO_PATH, template_path]))
    convert_all_python_templates(jinja_env, template_path, output_path,
                                 glob_pattern="topic*.py",
                                 tags_to_remove=("code-along",))


# %%
def convert_workshop_templates_to_solutions():
    template_path = ROOT_PATH / "Templates/Workshops"
    output_path = ROOT_PATH / "Workshops/Solutions"

    jinja_env = Environment(line_statement_prefix="# j2",
                            loader=FileSystemLoader(
                                [MACRO_PATH, template_path]))
    convert_all_python_templates(jinja_env, template_path, output_path,
                                 glob_pattern="workshop*.py")


# %%
def convert_workshop_templates_to_exercises():
    template_path = ROOT_PATH / "Templates/Workshops"
    output_path = ROOT_PATH / "Workshops/Exercises"

    jinja_env = Environment(line_statement_prefix="# j2",
                            loader=FileSystemLoader(
                                [MACRO_PATH, template_path]))
    convert_all_python_templates(jinja_env, template_path, output_path,
                                 glob_pattern="workshop*.py",
                                 tags_to_remove=("solution",))


# %%
if __name__ == "__main__":
    convert_slide_templates()
    convert_slide_templates_to_codealongs()
    convert_workshop_templates_to_solutions()
    convert_workshop_templates_to_exercises()
