from click.testing import CliRunner
from json_to_files.cli import cli
import json
import pathlib
import pytest


@pytest.mark.parametrize(
    "input,error",
    (
        ("not JSON", "Expecting value: line 1 column 1 (char 0)"),
        ("[]", "JSON must be an object"),
        ('{"a": 1}', "JSON values must be strings"),
        (
            '{"/path/to/thing.txt": "1"}',
            "Invalid filename: /path/to/thing.txt - only relative paths are supported",
        ),
        (
            '{"../../thing.txt": "1"}',
            "Invalid filename: ../../thing.txt - only relative paths are supported",
        ),
    ),
)
def test_errors(input, error):
    runner = CliRunner()
    result = runner.invoke(cli, input=input)
    assert result.exit_code == 1
    assert result.output == "Error: {}\n".format(error)


@pytest.mark.parametrize("directory", (None, "output"))
def test_success(directory):
    runner = CliRunner()
    with runner.isolated_filesystem():
        args = []
        if directory:
            args = ["--directory", directory]
        result = runner.invoke(
            cli,
            input=json.dumps({"a.txt": "1", "b.txt": "22", "c/d.txt": "333"}),
            args=args,
        )
        assert result.exit_code == 0
        assert result.output == (
            "a.txt: 1 byte\n" "b.txt: 2 bytes\n" "c/d.txt: 3 bytes\n"
        )
        directory = pathlib.Path(directory or ".")
        assert (directory / "a.txt").read_text() == "1"
        assert (directory / "b.txt").read_text() == "22"
        assert (directory / "c" / "d.txt").read_text() == "333"
