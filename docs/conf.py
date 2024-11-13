# docs/conf.py
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'E-commerce Sales report'
author = 'Adedeji'
release = '0.1'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
html_static_path = ['_static']
