from norn.cli import main


def test_health_cli_succeeds(capsys):
    assert main(["health"]) == 0
    assert '"ready": true' in capsys.readouterr().out
