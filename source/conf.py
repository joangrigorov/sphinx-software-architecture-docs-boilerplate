# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import datetime
# import sphinx_qas_plugin
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '{PROJECT_NAME} Software Architecture Documentation'
copyright = (
   f'{datetime.datetime.now().year}' + ', {PROJECT_NAME} {AUTHOR}'
)
author = '{AUTHOR}'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.bibtex',
    'sphinx_rtd_theme',
    'sphinx_qas_plugin',
]

templates_path = ['_templates']
exclude_patterns = ['**/*.inc.rst']


# -- Options for HTML output -------------------------------------------------

highlight_options = {
  'default': {'stripall': True},
  'php': {'startinline': True},
}

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

html_css_files = [
    'css/width.css',
    'css/sections_clear.css'
]

bibtex_bibfiles = ['references.bib']
bibtex_default_style = 'plain'
