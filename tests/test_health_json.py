import json

from norn.cli import main


def test_health_output_is_json(capsys):
    main(["health"])
    assert json.loads(capsys.readouterr().out)["ready"] is True
