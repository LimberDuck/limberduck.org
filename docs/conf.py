import sphinx_fontawesome
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'LimberDuck'
copyright = '2018-2022, Damian Krawczyk'
author = 'Damian Krawczyk'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_fontawesome',
    'sphinx_design',
    'sphinx_copybutton',
    'myst_nb'
]

execution_timeout = -1

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_title = "LimberDuck"

html_show_sphinx = False

html_show_sphinx = True

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#FF6200",
        "color-brand-content": "#FF6200",
    },
    "navigation_with_keys": True,
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/limberduck",
            "html": "",
            "class": "fa fa-github fa-2x",
        },
        {
            "name": "Mail",
            "url": "mailto:damian.krawczyk@limberduck.org?subject=Question%20about%20LimberDuck",
            "html": "",
            "class": "fa fa-envelope fa-2x",
        },
    ],
}

html_logo = "_static/img/LimberDuck-logo.png"

html_favicon = "_static/img/favicon.ico"

html_css_files = [
    # "http://netdna.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
    "css/font-awesome.css",
    "css/custom.css",
]

rst_prolog =  sphinx_fontawesome.prolog + """
.. |GUI| replace:: :abbr:`GUI (Graphical User Interface)`
.. |CLI| replace:: :abbr:`CLI (command-line interfaces)`
.. |csv| replace:: :abbr:`csv (comma-separated value)`
.. |xlsx| replace:: :abbr:`xlsx (Microsoft Excel Open XML Spreadsheet)`
.. |VA| replace:: :abbr:`VA (Vulnerability Assessment)`
"""