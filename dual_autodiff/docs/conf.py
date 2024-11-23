import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Dual Number Automatic Differentiation'
copyright = '2024, Xueqing Xu'
author = 'Xueqing Xu'

# Add any Sphinx extension module names here
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
]



# The theme to use for HTML and HTML Help pages
html_theme = 'sphinx_rtd_theme'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

