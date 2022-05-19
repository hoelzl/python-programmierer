import json
import typer
from pathlib import Path

app = typer.Typer(add_completion=False)


def load_questions(path: Path = Path("questions.json")):
    with open(path, "r", encoding="utf-8") as file:
        questions = json.load(file)
        return questions


@app.command()
def say_hi():
    print("Hi!")


if __name__ == "__main__":
    # app()
    print(load_questions())
