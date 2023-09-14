import pytest

from src.selector import Selector, SelectorType


def test_class_name_selector_to_string():
    assert (
        str(Selector(selector_type=SelectorType.BY_CLASS_NAME, classes=["clsname"]))
        == "clsname"
    )


def test_class_name_selector_to_string_many_classes():
    with pytest.raises(ValueError):
        str(
            Selector(selector_type=SelectorType.BY_CLASS_NAME, classes=["cls1", "cls2"])
        )


def test_class_name_selector_to_string_no_class():
    with pytest.raises(ValueError):
        str(Selector(selector_type=SelectorType.BY_CLASS_NAME))


def test_css_selector_to_string():
    assert (
        str(Selector(selector_type=SelectorType.BY_CSS_SELECTOR, tag="h2", id="hello"))
        == "h2#hello"
    )


def test_id_selector_to_string():
    assert str(Selector(selector_type=SelectorType.BY_ID, id="hello")) == "hello"


def test_link_text_selector_to_string():
    assert (
        str(Selector(selector_type=SelectorType.BY_LINK_TEXT, inner_text="hello world"))
        == "hello world"
    )


def test_name_selector_to_string():
    assert (
        str(
            Selector(
                selector_type=SelectorType.BY_NAME, other_attributes={"name": "hello"}
            )
        )
        == "hello"
    )


def test_name_selector_to_string_no_name():
    with pytest.raises(ValueError):
        str(
            Selector(
                selector_type=SelectorType.BY_NAME, other_attributes={"value": "hello"}
            )
        )


def test_partial_link_text_selector_to_string():
    assert (
        str(
            Selector(
                selector_type=SelectorType.BY_PARTIAL_LINK_TEXT,
                inner_text="hello world",
            )
        )
        == "hello world"
    )


def test_tag_selector_to_string():
    assert str(Selector(selector_type=SelectorType.BY_TAG_NAME, tag="div")) == "div"


def test_xpath_selector_to_string():
    assert (
        str(Selector(selector_type=SelectorType.BY_XPATH, tag="h2", id="hello"))
        == "//h2[@id='hello']"
    )
