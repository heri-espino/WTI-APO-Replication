"""Public Asian-option replication infrastructure.

The current release-candidate source includes only a synthetic educational
baseline; it does not reproduce results from the private empirical study.
"""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("wti-apo-replication")
except PackageNotFoundError:  # working source tree before editable installation
    __version__ = "0.1.0.dev0"

__all__ = ["__version__"]
