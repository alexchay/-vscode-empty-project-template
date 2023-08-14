import os
from typing import Any
from unittest.mock import patch

from python_project.main import main


def test_main(capsys: Any) -> None:  # noqa: ANN401
    """
    Test the main functionality of the program.
    This function tests the behavior of the program when the ENVIRONMENT environment variable is set to 'test'.
    Args:
        capsys: The capsys fixture provided by pytest for capturing stdout and stderr.
    Returns:
        None
    """
    with patch.dict(os.environ, {"ENVIRONMENT": "test"}):
        main()
        captured = capsys.readouterr()
        assert "test" in captured.out

    with patch.dict(os.environ, {"ENVIRONMENT": "prod"}):
        main()
        captured = capsys.readouterr()
        assert "prod" in captured.out
