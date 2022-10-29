from sphinx.application import Sphinx
from sphinx.ext.autodoc import ClassDocumenter, ALL

from pathlib import Path

try:
    from ._version import version as _default_version
except ImportError:
    _default_version = "0.0.1"


def _get_version():
    """Return the version string used for __version__."""
    # Only shell out to a git subprocess if really needed, and not on a
    # shallow clone, such as those used by CI, as the latter would trigger
    # a warning from setuptools_scm.
    root = Path(__file__).resolve().parents[1]
    if (root / ".git").exists() and not (root / ".git/shallow").exists():
        import setuptools_scm

        try:
            return setuptools_scm.get_version(
                root=str(root),
                version_scheme="post-release",
                fallback_version=_default_version,
            )
        except Exception:
            return _default_version
    else:  # Get the version from the _version.py setuptools_scm file.
        return _default_version


__version__ = _get_version()



class AutoCollapsibleClassDocumenter(ClassDocumenter):
    objtype = 'class'
    directivetype = ClassDocumenter.objtype
    priority = 10 + ClassDocumenter.priority
    option_spec = dict(ClassDocumenter.option_spec)

    def document_members(self, all_members: bool = False) -> None:
        # find out all the members that are documented
        want_all = all_members or self.options.inherited_members or self.options.members is ALL
        _, members = self.get_object_members(want_all)
        if members:
            sourcename = self.get_sourcename()
            self.add_line('', sourcename)
            self.add_line('.. rubric:: Member Details:', sourcename)
            self.add_line('', sourcename)
            self.add_line('.. collapse:: Click here to Expand', sourcename)
            self.indent += ' ' * 3
        super().document_members(all_members)


def setup(app: Sphinx) -> None:
    app.setup_extension('sphinx.ext.autodoc')  # Require autodoc extension
    app.setup_extension('sphinx_toolbox.collapse')  # Require sphinx_toolbox.collapse extension
    app.add_autodocumenter(AutoCollapsibleClassDocumenter)
