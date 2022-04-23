import typer

app = typer.Typer()


@app.callback(no_args_is_help=True)
def callback():
    """
    Morty! Morty! Esta es la ayuda, Morty.
    """


@app.command()
def shoot():
    """
    Dispara la pistola de portales, Morty!!!
    """
    typer.echo("Abre el portal Morty!!!")


@app.command()
def reload():
    """
    Recarga la pistola de portales, Morty!!!
    """
    typer.echo("Recarga la pistola Morty!!!")
