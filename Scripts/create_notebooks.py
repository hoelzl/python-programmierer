from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def convert_template(jinja_env: Environment, template_name: str,
                     output_path: Path):
    template = jinja_env.get_template(template_name)
    result = template.render()
    output_file = output_path / template_name
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(result)


def convert_all_python_templates(jinja_env: Environment, template_dir: Path,
                                 output_dir: Path):
    output_dir.mkdir(exist_ok=True)
    for file in template_dir.glob("*.py"):
        convert_template(jinja_env, file.name, output_dir)


if __name__ == "__main__":
    _root_path = Path(
        r"C:\Users\tc\Programming\Python\Courses\Own\python-programmierer")
    _template_path = _root_path / "Notebooks-V3/templates/"
    _output_path = _root_path / "Tmp"

    _jinja_env = Environment(line_statement_prefix="# j2",
                             loader=FileSystemLoader(_template_path))
    convert_all_python_templates(_jinja_env, _template_path, _output_path)
