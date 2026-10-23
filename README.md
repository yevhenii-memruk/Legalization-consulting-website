# Non-Stop Documents

FastAPI website for **Non-Stop Documents**, a legalization and document consulting
company in Poland.

## Current features

- Responsive landing page in Polish, Ukrainian, Russian, and English
- Accessible navigation and mobile menu
- Consultation form with server-side validation and an optional comment field
- Localized privacy policy and public contact details
- Canonical, multilingual, and social-sharing metadata after a public URL is configured
- Dynamic `robots.txt` and XML sitemap with safe pre-production defaults
- Services, company information, process, reviews placeholder, and FAQ sections
- FastAPI health endpoint, automated tests, and GitHub Actions quality checks

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

Polish is the default language. Other versions are available with the `lang` query
parameter, for example <http://127.0.0.1:8000/?lang=uk>.

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

## Production configuration

Set `APP_PUBLIC_BASE_URL` to the final HTTPS origin, without a path, after choosing a
domain. Until it is set, pages use `noindex,nofollow`, `robots.txt` disallows crawling,
and `/sitemap.xml` is unavailable. This prevents preview environments from being
indexed accidentally.

The application includes a production container that runs as a non-root user:

```powershell
docker build -t non-stop-documents .
docker run --rm -p 8080:8080 --env-file .env non-stop-documents
```

Open <http://127.0.0.1:8080/health> to verify the container. Never bake `.env` or Google
credentials into the image; inject them through the hosting platform's secret settings.

## Lead collection

Create a Google Sheet with these columns in the `Leads` tab:

```text
Lead ID | Created at Europe/Warsaw | Full name | Phone | Comment | Language | Source
```

Copy `.env.example` to `.env`, set the spreadsheet ID, configure Google Application
Default Credentials, and enable lead collection only after publishing the required
privacy information. Credential files and private keys must never be committed.
