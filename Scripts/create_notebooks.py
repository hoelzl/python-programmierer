from pathlib import Path
from jinja2 import Environment, FileSystemLoader

ROOT_PATH = Path(
    r"C:\Users\tc\Programming\Python\Courses\Own\python-programmierer")


def convert_template(jinja_env: Environment, template_name: str,
                     output_path: Path):
    template = jinja_env.get_template(template_name)
    result = template.render()
    output_file = output_path / template_name
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(result)


def convert_all_python_templates(jinja_env: Environment, template_dir: Path,
                                 output_dir: Path, glob_pattern="*.py"):
    output_dir.mkdir(exist_ok=True, parents=True)
    for file in template_dir.glob(glob_pattern):
        convert_template(jinja_env, file.name, output_dir)


def convert_slide_templates():
    template_path = ROOT_PATH / "Templates/"
    output_path = ROOT_PATH / "Slides"

    jinja_env = Environment(line_statement_prefix="# j2",
                            loader=FileSystemLoader(template_path))
    convert_all_python_templates(jinja_env, template_path, output_path,
                                 glob_pattern="topic*.py")


def convert_workshop_templates_to_solutions():
    template_path = ROOT_PATH / "Templates/"
    output_path = ROOT_PATH / "Workshops/Solutions"

    jinja_env = Environment(line_statement_prefix="# j2",
                            loader=FileSystemLoader(template_path))
    convert_all_python_templates(jinja_env, template_path, output_path,
                                 glob_pattern="workshop*.py")


def convert_workshop_templates_to_exercises():
    template_path = ROOT_PATH / "Templates/"
    output_path = ROOT_PATH / "Workshops/Exercises"

    jinja_env = Environment(line_statement_prefix="# j2",
                            loader=FileSystemLoader(template_path))
    convert_all_python_templates(jinja_env, template_path, output_path,
                                 glob_pattern="workshop*.py")


if __name__ == "__main__":
    convert_slide_templates()
