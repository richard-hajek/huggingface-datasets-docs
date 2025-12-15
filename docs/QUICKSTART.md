# Documentation Quick Start Guide

## TL;DR

```bash
# Install dependencies
pip install -e ".[docs]"

# Build documentation
cd docs
make html

# Open in browser
open build/html/index.html  # macOS
xdg-open build/html/index.html  # Linux
start build/html/index.html  # Windows
```

## Live Preview (with auto-reload)

```bash
cd docs
make livehtml
# Opens at http://localhost:8000
```

## Common Tasks

### Clean and rebuild
```bash
cd docs
make clean
make html
```

### Check for broken links
```bash
cd docs
make linkcheck
```

### Build different formats
```bash
make html      # HTML output (default)
make latex     # LaTeX output
make latexpdf  # PDF output (requires LaTeX)
make epub      # ePub output
```

## Troubleshooting

### "datasets module not found"
```bash
# Make sure datasets is installed in editable mode
pip install -e .
```

### "Command not found: sphinx-build"
```bash
# Install documentation dependencies
pip install -r docs/requirements.txt
```

### Build errors
```bash
# Clean and rebuild
cd docs
make clean
make html
```

### Port already in use (livehtml)
```bash
# Kill existing process
pkill -f sphinx-autobuild

# Or specify different port
sphinx-autobuild source build/html --port 8001
```

## Project Structure

```
docs/
├── source/           # Documentation source files
│   ├── api/          # API reference (RST files)
│   ├── _static/      # Static files (CSS, images)
│   ├── _templates/   # Custom templates
│   ├── conf.py       # Sphinx configuration
│   └── index.rst     # Main page
├── build/            # Generated documentation (not committed)
├── Makefile          # Build automation
└── requirements.txt  # Dependencies
```

## Adding New Content

### Add a new page
1. Create `docs/source/my_page.rst` or `.md`
2. Add to toctree in `index.rst`:
   ```rst
   .. toctree::
      
      my_page
   ```

### Add to API reference
1. Edit appropriate file in `docs/source/api/`
2. Add method to autosummary list:
   ```rst
   .. autosummary::
      :toctree: generated/
      
      MyClass.my_method
   ```

## Style Guide

- Use **RST** for API reference and structured content
- Use **Markdown** for tutorials and guides
- Follow pandas/numpy documentation style
- Group API methods by functionality
- Include examples in docstrings

## More Information

- `README.md` - Detailed build instructions
- `MIGRATION_GUIDE.md` - Migration from doc-builder
- `SPHINX_MIGRATION_SUMMARY.md` - Complete overview of changes
