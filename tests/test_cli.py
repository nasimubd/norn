from norn.cli import main


def test_route_cli_json(capsys):
    assert main(["route", "list files", "--json"]) == 0
    assert '"kind": "direct"' in capsys.readouterr().out
