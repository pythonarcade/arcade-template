from importlib.metadata import version as _ilversion

from .__main__ import main

__version__ = _ilversion("{{ cookiecutter.project_slug }}")

__all__ = ["__version__", "main"]

