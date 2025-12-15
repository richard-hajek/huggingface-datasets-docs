# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import os
import sys
import re
from datetime import datetime

sys.path.insert(0, os.path.abspath("../../src"))

import datasets


# Process docstrings to convert Markdown code fences to RST code blocks
def process_docstring(app, what, name, obj, options, lines):
    """Convert Markdown code fences in docstrings to RST code blocks."""
    result = []
    in_code_block = False
    code_lang = None

    i = 0
    while i < len(lines):
        line = lines[i]

        # Check for code fence start
        match = re.match(r"^```(\w+)?", line.strip())
        if match:
            if not in_code_block:
                # Start of code block
                in_code_block = True
                code_lang = match.group(1) or "python"
                result.append("")
                result.append(f".. code-block:: {code_lang}")
                result.append("")
            else:
                # End of code block
                in_code_block = False
                code_lang = None
                result.append("")
            i += 1
            continue

        # If in code block, indent the line
        if in_code_block:
            result.append("    " + line)
        else:
            result.append(line)

        i += 1

    lines[:] = result


def setup(app):
    app.connect("autodoc-process-docstring", process_docstring)


# -- Project information -----------------------------------------------------

project = "Datasets"
copyright = f"{datetime.now().year}, HuggingFace Inc."
author = "HuggingFace Inc."

# The version info for the project you're documenting
version = datasets.__version__
release = datasets.__version__

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.githubpages",
    "sphinx_copybutton",
    "myst_parser",
    "nbsphinx",
    "sphinx_design",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The suffix(es) of source filenames.
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
    ".mdx": "markdown",
}

# The master toctree document.
master_doc = "index"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = "pydata_sphinx_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.
html_theme_options = {
    "github_url": "https://github.com/huggingface/datasets",
    "icon_links": [
        {
            "name": "Hugging Face",
            "url": "https://huggingface.co/datasets",
            "icon": "fa-solid fa-house",
        },
    ],
    "logo": {
        "text": "🤗 Datasets",
    },
    "use_edit_page_button": True,
    "header_links_before_dropdown": 4,
}

html_context = {
    "github_user": "huggingface",
    "github_repo": "datasets",
    "github_version": "main",
    "doc_path": "docs/source",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = [
    "css/custom.css",
]

html_js_files = []

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = "_static/datasets_logo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = "_static/datasets_logo.png"

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True

# Sidebar configuration removed - using default pydata theme sidebars

# -- Options for autodoc -----------------------------------------------------

autodoc_default_options = {
    "members": True,
    "show-inheritance": True,
}

autodoc_member_order = "bysource"

# Enable MyST parsing in docstrings
autodoc_docstring_signature = True

# -- Options for autosummary -------------------------------------------------

autosummary_generate = True
autosummary_imported_members = False

# -- Options for Napoleon ----------------------------------------------------

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True

# -- Options for intersphinx -------------------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "torch": ("https://pytorch.org/docs/stable/", None),
    "pyarrow": ("https://arrow.apache.org/docs/", None),
}

# -- Options for MyST --------------------------------------------------------

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]

# Enable parsing of docstrings as MyST
myst_update_mathjax = False

# -- Options for nbsphinx ----------------------------------------------------

nbsphinx_execute = "never"

# -- Options for copybutton --------------------------------------------------

copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_prompt_is_regexp = True
