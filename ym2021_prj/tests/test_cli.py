from .. import cli


def test_cli():
    response = cli.main()
    assert isinstance(response, str)
    assert response.find("ym2021_prj") >= 0
