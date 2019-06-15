"""
    sphinxcontrib.sqldomain
    ~~~~~~~~~~~~~~~~~~~~~~~

    Sphinx Domain for documenting SQL databases

    :copyright: Copyright 2017 by Jan Brohl <janbrohl@t-online.de>
    :license: BSD, see LICENSE for details.
"""

import pbr.version

if False:
    # For type annotations
    from typing import Any, Dict  # noqa
    from sphinx.application import Sphinx  # noqa

__version__ = pbr.version.VersionInfo('sqldomain').version_string()


def setup(app):
    # type: (Sphinx) -> Dict[unicode, Any]
    return {'version': __version__, 'parallel_read_safe': True}
