import os
import pytest

from .. import cli


def test_cli():
    response = cli.main()
    assert isinstance(response, str)
    assert response.find("ym2021_prj") >= 0


@pytest.mark.parametrize(
    "var_name, exists, value",
    [
        ["TESTABLE", True, "testable"],
        ["NO_SUCH_ENV_VAR", False, None],
    ],
)
def test_env_var(var_name, exists, value):
    assert (var_name in os.environ) is exists
    env_var = os.environ.get(var_name)
    assert env_var == value
