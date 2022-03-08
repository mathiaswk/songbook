"""Songbook is a library for creating

    Songbook
    ~~~~~~~~

    A one line summary of the module or program, terminated by a period.

    :copyright: Copyright 2007-2021 by the Sphinx team, see AUTHORS.
    :license: MIT, see LICENSE for details.
"""

from songbook.base import Songbook

__version__ = '1.0.0'
__all__ = ['Songbook']


# The Songs package is for producing songbooks containing lyrics and chords
# (but not sheet music).  Each songs document can produce a lyric-only songbook
# for singers, a chorded songbook for musicians, a set of overhead
# transparencies, or a set of digital projector slides, all from a single master
# document.  It can also automatically generate partial songbooks consisting of
# only some songs from the master document in a specified order.  Facilities for
# automatic transposition and creation of guitar tablature diagrams are also
# included.
