from typer.testing import CliRunner

from rick_portal_gun.main import app

runner = CliRunner()


def test_main_shoot():
    result = runner.invoke(app, ["shoot"])
    assert "Abre el portal Morty!!!" in result.stdout
    assert result.exit_code == 0


def test_main_reload():
    result = runner.invoke(app, ["reload"])
    assert result.exit_code == 0
    assert "Recarga la pistola Morty!!!" in result.stdout
