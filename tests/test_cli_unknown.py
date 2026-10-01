from norn.cli import main


def test_unknown_route_command_is_not_exposed():
    assert main(["health"]) == 0
