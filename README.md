# Non-stop Documents

FastAPI website for **Non-stop Documents**, a legalization and document consulting
company in Poland.

## Current features

- Responsive Polish landing page
- Accessible navigation and mobile menu
- Consultation form with server-side validation and an optional comment field
- Services, company information, process, reviews placeholder, and FAQ sections
- FastAPI health endpoint and automated route/static-asset tests

Lead collection is disabled by default. When enabled, validated consultation requests
are appended to a private Google Sheet through Application Default Credentials.
While it is disabled, the public endpoint returns a controlled `503` response and does
not retain submitted personal data.

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

## Lead collection

Create a Google Sheet with these columns in the `Leads` tab:

```text
Lead ID | Created at UTC | Full name | Phone | Comment | Language | Source
```

Copy `.env.example` to `.env`, set the spreadsheet ID, configure Google Application
Default Credentials, and enable lead collection only after publishing the required
privacy information. Credential files and private keys must never be committed.
