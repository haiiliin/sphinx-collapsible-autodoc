===========
Basic Usage
===========

Installation
------------

To install the package, run the following command::

    pip install sphinx-collapsible-autodoc

This will install the package and its dependencies.

Usage
-----

To use the package, add the following to your Sphinx configuration file::

    extensions = [
        'sphinx.ext.autodoc',
        'sphinx_collapsible_autodoc',
    ]

Then, in your documentation, use the `autodoc` directive, below if an example incorporating with the 
`autoclasstoc <https://github.com/kalekundert/autoclasstoc>`_ extension:

.. autoclass:: example.Example
    :members:
    :private-members:
    :special-members:

    .. autoclasstoc::
