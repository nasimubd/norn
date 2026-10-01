from norn.cli import build_parser


def test_cli_has_health_command():
    assert "health" in build_parser().format_help()
