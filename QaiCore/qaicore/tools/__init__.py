"""Compatibility re-exports for `qaicore.tools`.

Prefer importing from `tools` directly when possible:

    from tools import extract_content

This module keeps existing agent prompts/docs working:

    from qaicore.tools import extract_content
"""

from tools import *  # noqa: F403
from tools import __all__  # noqa: F401
