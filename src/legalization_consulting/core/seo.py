"""SEO metadata built only from a trusted configured public origin."""

from dataclasses import dataclass

from pydantic import AnyHttpUrl

from legalization_consulting.core.i18n import DEFAULT_LANGUAGE, LANGUAGES


@dataclass(frozen=True, slots=True)
class AlternateUrl:
    language: str
    url: str


@dataclass(frozen=True, slots=True)
class SeoMetadata:
    canonical_url: str | None
    alternate_urls: tuple[AlternateUrl, ...]
    locale: str
    alternate_locales: tuple[str, ...]
    image_url: str | None


def public_origin(public_base_url: AnyHttpUrl | None) -> str | None:
    """Return the configured public origin without a trailing slash."""
    if public_base_url is None:
        return None
    return str(public_base_url).rstrip("/")


def localized_path(path: str, language: str) -> str:
    """Return the public URL path used by one language version."""
    if language == DEFAULT_LANGUAGE:
        return path
    return f"{path}?lang={language}"


def build_seo_metadata(
    public_base_url: AnyHttpUrl | None,
    path: str,
    language: str,
) -> SeoMetadata:
    """Build canonical, alternate-language, and social metadata."""
    locale_by_language = {item["code"]: item["locale"] for item in LANGUAGES}
    locale = locale_by_language[language]
    origin = public_origin(public_base_url)
    if origin is None:
        return SeoMetadata(
            canonical_url=None,
            alternate_urls=(),
            locale=locale,
            alternate_locales=tuple(
                value for code, value in locale_by_language.items() if code != language
            ),
            image_url=None,
        )

    alternate_urls = tuple(
        AlternateUrl(
            language=item["code"],
            url=f"{origin}{localized_path(path, item['code'])}",
        )
        for item in LANGUAGES
    )
    return SeoMetadata(
        canonical_url=f"{origin}{localized_path(path, language)}",
        alternate_urls=alternate_urls,
        locale=locale,
        alternate_locales=tuple(
            value for code, value in locale_by_language.items() if code != language
        ),
        image_url=f"{origin}/static/images/og-cover.png",
    )
