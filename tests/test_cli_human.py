from norn.cli import main


def test_human_cli_prints_route(capsys):
    assert main(["route", "run the test suite"]) == 0
    assert "direct" in capsys.readouterr().out
