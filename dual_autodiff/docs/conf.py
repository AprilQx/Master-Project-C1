import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'dual_autodiff'
copyright = '2024, Xueqing Xu'
author = 'Xueqing Xu'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'nbsphinx',
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']