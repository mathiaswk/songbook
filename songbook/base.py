"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""
import typing as t

if t.TYPE_CHECKING:
    from .plugins import Plugin


class Songbook:

    def __init__(
        self,
        title: str = "Sangbog",
        songs: t.Mapping[str, t.Optional[int]] = {},
        plugins: t.Sequence[t.Union[str, t.Type["Plugin"]]] = (),
        ordering: t.Sequence[str] = (),

    ):
        self.plugins = plugins

    def build(self, progress_update=None, progress_total=None):
        if progress_total is not None:
            progress_total(100000)

        for i in range(100000):
            progress_update(i+1)
