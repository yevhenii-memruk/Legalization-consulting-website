# Non-stop Documents

FastAPI website for **Non-stop Documents**, a legalization and document consulting
company in Poland.

## Requirements

- Python 3.14
- [uv](https://docs.astral.sh/uv/)

## Local development

Install the locked dependencies:

```powershell
uv sync
```

Start the development server:

```powershell
uv run uvicorn legalization_consulting.main:app --reload
```

Then open <http://127.0.0.1:8000>. The health endpoint is available at
<http://127.0.0.1:8000/health>.

## Quality checks

```powershell
uv run pytest
uv run ruff check .
```

## Project structure

```text
src/legalization_consulting/
├── main.py          # Application assembly
├── core/            # Settings, paths, and Jinja2 setup
├── routers/         # HTML page and API routes
├── static/          # CSS and future browser assets
└── templates/       # Jinja2 HTML templates
tests/               # Automated tests grouped by application area
```

Copy `.env.example` to `.env` when local settings need to override the defaults.
