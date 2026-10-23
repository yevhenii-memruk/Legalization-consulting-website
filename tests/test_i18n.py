from typing import Any

from legalization_consulting.core.i18n import DEFAULT_LANGUAGE, PAGE_CONTENT
from legalization_consulting.core.privacy_content import PRIVACY_CONTENT


def content_shape(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: content_shape(item) for key, item in value.items()}
    if isinstance(value, list):
        return [content_shape(value[0])] if value else []
    return str


def test_all_translations_have_the_same_structure() -> None:
    expected_shape = content_shape(PAGE_CONTENT[DEFAULT_LANGUAGE])

    for content in PAGE_CONTENT.values():
        assert content_shape(content) == expected_shape


def test_all_languages_have_complete_repeatable_sections() -> None:
    for content in PAGE_CONTENT.values():
        assert len(content["services"]["items"]) == 5
        assert len(content["process"]["items"]) == 4
        assert len(content["faq"]["items"]) == 4


def test_all_privacy_translations_have_the_same_structure() -> None:
    expected_shape = content_shape(PRIVACY_CONTENT[DEFAULT_LANGUAGE])

    assert set(PRIVACY_CONTENT) == set(PAGE_CONTENT)
    for content in PRIVACY_CONTENT.values():
        assert content_shape(content) == expected_shape
