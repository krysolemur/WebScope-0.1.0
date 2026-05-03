# Noctua 🦉

A Python desktop application for web inspection, penetration testing and ethical hacking.

> ⚠️ **Disclaimer:** This tool is intended for legal, authorized security testing only. The author is not responsible for any misuse.

---

## Features

- 🔍 HTML/CSS/JS source inspection
- 📡 HTTP header and request analysis
- 💥 Fuzzing and brute-force attacks
- 🛡️ SQL injection / XSS testing
- 🔎 Vulnerability scanning (CVE)
- 📊 Traffic monitoring and logging

---

## Requirements

- Python 3.10+
- PySide6

---

## Installation

```bash
git clone https://github.com/krysolemur/Noctua.git
cd Noctua
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e .
```

## Run

```bash
python -m noctua
```

Or via Makefile:

```bash
make install      # Install project
make run          # Run application
make test         # Run tests
make lint         # Check code
make format       # Format code
make clean        # Clean code
```

---

## Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run linter
ruff check .

# Install pre-commit hooks
pre-commit install
```

---

## Project Structure

```
noctua/
├── app.py              # Main application class
├── __main__.py         # Entry point
├── config_manager/     # Configuration handling
├── core/               # Shared context and utilities
├── logger/             # Logging setup
├── main_window/        # Main window UI
├── settings_dialog/    # Settings UI (general, logging, source pages)
├── style_manager/      # Stylesheet management
├── theme_manager/      # Theme management
├── ui_gen/             # Auto-generated UI files
└── error_dialog/       # Error dialog UI
```

---

## Version

`0.1.0` — initial release

---

## License

MIT © [krysolemur](https://github.com/krysolemur)
