# Documentation Migration Guide

This guide explains the migration from doc-builder to Sphinx with PyData theme.

## What Changed

### Documentation System
- **Before**: HuggingFace doc-builder with custom MDX processing
- **After**: Sphinx with PyData Sphinx Theme (same as pandas/numpy)

### File Formats
- **Primary format**: reStructuredText (.rst)
- **Also supported**: Markdown (.md, .mdx) via MyST parser
- The main index and API reference use .rst for better Sphinx integration
- Tutorial and guide content can remain as .md/.mdx files

### API Documentation Structure
The API documentation now follows pandas/numpy conventions:

```
docs/source/api/
├── index.rst          # API overview
├── dataset.rst        # Dataset class with autosummary
├── dataset_dict.rst   # DatasetDict class
├── iterable_dataset.rst
├── features.rst
├── builders.rst
├── loading.rst
└── utilities.rst
```

Each API file uses `autosummary` to automatically generate detailed documentation pages for each method/function.

### Theme and Styling
- **Theme**: PyData Sphinx Theme (used by pandas, numpy, scipy)
- **Custom CSS**: Added pandas/numpy-inspired styling in `_static/css/custom.css`
- **Navigation**: Improved sidebar navigation with collapsible sections
- **Search**: Enhanced search functionality
- **Dark mode**: Built-in dark/light theme switcher

## Building the Documentation

### Old Way (doc-builder)
```bash
doc-builder build datasets docs/source/ --build_dir ~/tmp/test-build
doc-builder preview datasets docs/source/
```

### New Way (Sphinx)
```bash
# Install dependencies
pip install -e ".[docs]"

# Build HTML documentation
cd docs
make html

# Live preview with auto-rebuild
make livehtml
```

## Key Differences

### Table of Contents
- **Before**: `_toctree.yml` YAML file
- **After**: `.. toctree::` directives in .rst files (more standard Sphinx approach)

### Links
- **Before**: MDX-style links like `[text](file)`
- **After**: 
  - RST: `:doc:\`file\`` or `:ref:\`label\``
  - Markdown: Still works with MyST parser

### Code Documentation
- **Before**: Custom `[[autodoc]]` syntax
- **After**: Standard Sphinx directives:
  ```rst
  .. autosummary::
     :toctree: generated/
     
     ClassName
     ClassName.method
  ```

### Admonitions
Both Markdown and RST admonitions work:

**Markdown (MyST)**:
```markdown
:::{note}
This is a note
:::
```

**RST**:
```rst
.. note::
   This is a note
```

## API Reference Organization

The new API structure groups methods by functionality (following pandas conventions):

- **Constructor methods**: `from_dict`, `from_pandas`, etc.
- **Attributes**: `shape`, `num_rows`, etc.
- **Data processing**: `map`, `filter`, `sort`, etc.
- **I/O operations**: `save_to_disk`, `to_csv`, etc.
- **Indexing**: `add_faiss_index`, `search`, etc.

## Migration Checklist for Contributors

When adding new documentation:

- [ ] API documentation goes in `docs/source/api/`
- [ ] Use `.. autosummary::` for listing class methods
- [ ] Add new pages to the appropriate `.. toctree::` directive
- [ ] Test locally with `make html` or `make livehtml`
- [ ] Check both light and dark themes
- [ ] Verify all internal links work

## Benefits of the New System

1. **Standard tooling**: Sphinx is the Python documentation standard
2. **Better IDE support**: RST has excellent editor support
3. **Consistent with ecosystem**: Same look as pandas, numpy, scipy
4. **Better API docs**: Autosummary generates comprehensive API reference
5. **Improved navigation**: Better sidebar and cross-referencing
6. **Version support**: Built-in versioning support
7. **Better PDF generation**: Sphinx has excellent LaTeX/PDF support
8. **Extensibility**: Vast ecosystem of Sphinx extensions

## Configuration Files

### Main Configuration
- `docs/source/conf.py` - Sphinx configuration (replaces `_config.py`)
- `docs/Makefile` - Build automation
- `docs/make.bat` - Windows build support

### Requirements
- `docs/requirements.txt` - All documentation dependencies
- `setup.py` - Updated `[docs]` extra with Sphinx packages

### Styling
- `docs/source/_static/css/custom.css` - Custom pandas/numpy-inspired styles
- `docs/source/_static/` - Static assets (logos, images)

## Troubleshooting

### Build Errors
```bash
# Clean build directory
cd docs
make clean
make html
```

### Import Errors
Make sure datasets is installed in development mode:
```bash
pip install -e .
```

### Missing Dependencies
```bash
pip install -r docs/requirements.txt
```

### Live Preview Issues
```bash
# Kill any existing sphinx-autobuild processes
pkill -f sphinx-autobuild

# Restart
cd docs
make livehtml
```

## Resources

- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/)
- [MyST Parser (Markdown support)](https://myst-parser.readthedocs.io/)
- [Sphinx Design (UI components)](https://sphinx-design.readthedocs.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/) - Reference example
- [NumPy Documentation](https://numpy.org/doc/stable/) - Reference example
