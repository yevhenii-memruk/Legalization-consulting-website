# Non-stop Documents

FastAPI website for **Non-stop Documents**, a legalization and document consulting
company in Poland.

## Current features

- Responsive Polish landing page
- Accessible navigation and mobile menu
- Consultation form UI with an optional comment field
- Services, company information, process, reviews placeholder, and FAQ sections
- FastAPI health endpoint and automated route/static-asset tests

The consultation form is currently a frontend demonstration. Server-side validation
and Google Sheets delivery will be implemented in a later milestone.

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
├── main.py          # Application entry point & factory
├── core/            # Settings, paths, and Jinja2 setup
├── routers/         # HTML page and API routes
├── static/          # Static assets (CSS, JS, images)
└── templates/       # Jinja2 HTML templates
tests/               # Automated test suites
```

Copy `.env.example` to `.env` when local settings need to override the defaults.
