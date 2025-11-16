from importlib.metadata import PackageNotFoundError, version as _version
import logging

"""Top-level package for mlproject."""


__all__ = ["__version__", "get_version", "logger"]

# Attempt to read installed package version, fallback to default during development.
try:
    __version__ = _version("mlproject")
except PackageNotFoundError:
    __version__ = "0.0.0"

def get_version() -> str:
    """Return package version."""
    return __version__

# Package-level logger
logger = logging.getLogger("mlproject")
logger.addHandler(logging.NullHandler())