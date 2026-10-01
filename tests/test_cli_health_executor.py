from norn.cli import main


def test_health_cli_lists_dry_run(capsys):
    main(["health"])
    assert "dry-run" in capsys.readouterr().out
