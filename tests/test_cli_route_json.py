import json

from norn.cli import main


def test_route_json_is_parseable(capsys):
    main(["route", "check git status", "--json"])
    assert json.loads(capsys.readouterr().out)["kind"] == "direct"
