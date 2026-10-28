# Non-Stop Documents

FastAPI-based multilingual website for Non-Stop Documents, a Polish legalization and document consulting company.

This project provides a modern, accessible landing page with localized content, a consultation form, SEO optimization, and a safe lead-capture flow designed for production and preview environments.

## Overview

Non-Stop Documents helps clients with legalization and document-related consulting services in Poland. The website is built to be:

- multilingual and customer-friendly
- responsive on mobile and desktop
- optimized for search engines and social sharing
- secure by default in pre-production and staging
- easy to deploy with Docker
- testable and ready for CI quality checks

## Features

- Responsive landing page in Polish, Ukrainian, Russian, and English
- Multilingual content switching via language query parameter
- Accessible navigation with a mobile-friendly menu
- Consultation form with server-side validation
- Optional comment field for client inquiries
- Privacy policy and contact details localized by language
- SEO metadata support for canonical URLs, social cards, and localization
- Dynamic robots.txt and sitemap generation
- Safe pre-production defaults with noindex/nofollow when public base URL is not configured
- Services, company info, process, reviews, and FAQ sections
- FastAPI health check endpoint
- Automated tests for pages, localization, SEO, and lead processing
- Dockerized production setup
- Optional Google Sheets integration for lead collection (disabled by default)

## Tech Stack

- Python 3.14
- FastAPI
- Jinja2 templates
- Pydantic settings
- phonenumberslite
- Google API client
- pytest + ruff
- Docker

## Project Structure

```text
src/legalization_consulting/
├── main.py                 # FastAPI app factory and entry point
├── core/                  # Settings, path handling, and Jinja setup
├── integrations/          # Third-party integrations
├── routers/               # Page and API route handlers
├── schemas/               # Request/response schemas
├── services/              # Business logic
├── static/                # CSS, JS, images, and static assets
├── templates/             # HTML templates
└── __init__.py

tests/
├── conftest.py
├── test_api.py
├── test_i18n.py
├── test_leads.py
├── test_pages.py
└── test_seo.py
```

## Requirements

- Python 3.14
- [uv](https://docs.astral.sh/uv/)

## Local Development

1. Install dependencies:

```bash
uv sync
```

2. Start the development server:

```bash
uv run uvicorn legalization_consulting.main:app --reload
```

3. Open the app in your browser: <http://127.0.0.1:8000>
The health endpoint is available at: <http://127.0.0.1:8000/health>

Polish is the default language. You can switch language using the `lang` query parameter, for example:

```text
http://127.0.0.1:8000/?lang=uk
```

## Environment Configuration

Copy the example environment file:

```bash
cp .env.example .env
```

Key configuration values include:

- `APP_NAME`
- `APP_DESCRIPTION`
- `APP_CONTACT_EMAIL`
- `APP_PUBLIC_BASE_URL`
- `APP_LEADS_ENABLED`
- `APP_GOOGLE_SHEETS_SPREADSHEET_ID`

Important:

- Lead collection is disabled by default.
- Public SEO settings are only enabled once a production URL is configured.
- Until `APP_PUBLIC_BASE_URL` is set, pages use `noindex, nofollow` and sitemap/robots behavior stays restricted.

## Production Deployment

The project includes a Docker setup for production deployment.

Build the image:

```bash
docker build -t non-stop-documents .
```

Run the container:

```bash
docker run --rm -p 8080:8080 --env-file .env non-stop-documents
```

Then verify:

```text
http://127.0.0.1:8080/health
```

## Lead Collection

Lead collection is supported through Google Sheets, but remains disabled by default until the service is properly configured.

To enable it:

1. Create a Google Sheet with the required columns
2. Set `APP_GOOGLE_SHEETS_SPREADSHEET_ID`
3. Configure Google Application Default Credentials
4. Enable `APP_LEADS_ENABLED` only after privacy requirements are in place

Important: credentials and private keys must never be committed to the repository.

## Quality Checks

Run tests:

```bash
uv run pytest
```

Run lint checks:

```bash
uv run ruff check .
```

## License

This project is intended for the Non-Stop Documents business website and is configured for project-specific deployment. If you plan to publish it publicly, add the appropriate license file and legal notice.
