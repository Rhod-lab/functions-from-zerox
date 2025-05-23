from mylib.calc import add, sub, mul, div, power
from CalCLI import cli
from click.testing import CliRunner
import pytest


@pytest.fixture
def runner():
    """Create a test runner."""
    return CliRunner()


# write a test for the each function in the calc.py file
def test_add_cmd(runner):
    result = runner.invoke(cli, ["add", "1", "2"])
    assert result.exit_code == 0
    assert "3" in result.output


def test_sub_cmd(runner):
    result = runner.invoke(cli, ["sub", "1", "2"])
    assert result.exit_code == 0
    assert "-1" in result.output


def test_mul_cmd(runner):
    result = runner.invoke(cli, ["mul", "1", "2"])
    assert result.exit_code == 0
    assert "2" in result.output


def test_div_cmd(runner):
    result = runner.invoke(cli, ["div", "1", "2"])
    assert result.exit_code == 0
    assert "0.5" in result.output


def test_power_cmd(runner):
    result = runner.invoke(cli, ["power", "2", "3"])
    assert result.exit_code == 0
    assert "8" in result.output


# write a test for the help command
def test_help_cmd(runner):
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "A calculator program" in result.output
