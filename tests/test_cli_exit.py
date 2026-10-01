from norn.cli import main


def test_cli_returns_success_for_route():
    assert main(["route", "list files"]) == 0
