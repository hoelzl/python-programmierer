import typer

app = typer.Typer(add_completion=False)


@app.command()
def say_hi():
	print("Hi!")

if __name__ == "__main__":
    app()
