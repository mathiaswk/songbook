"""
    songbook.core
    ~~~~~~~~~~~~~

    A one line summary of the module or program, terminated by a period.

    :copyright: Copyright 2007-2021 by the Sphinx team, see AUTHORS.
    :license: MIT, see LICENSE for details.
"""

class Songbook(object):
    def build(self, progress_update=None, progress_total=None):
        if progress_total is not None:
            progress_total(100000)

        for i in range(100000):
            progress_update(i+1)
