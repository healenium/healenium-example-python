from src.selector import Selector, SelectorType


def test_from_class_name():
    assert Selector.from_class_name("cls") == Selector(
        selector_type=SelectorType.BY_CLASS_NAME, classes=["cls"]
    )


def test_from_css_simple():
    css_selector = "div"
    assert Selector.from_css(css_selector) == Selector(
        selector_type=SelectorType.BY_CSS_SELECTOR, tag="div"
    )


def test_from_css_complex():
    css_selector = "div#hello.class_name.cls2[href='hello world']"
    assert Selector.from_css(css_selector) == Selector(
        selector_type=SelectorType.BY_CSS_SELECTOR,
        tag="div",
        id="hello",
        classes=["class_name", "cls2"],
        other_attributes={"href": "hello world"},
    )


def test_from_id():
    assert Selector.from_id("hello") == Selector(
        selector_type=SelectorType.BY_ID, id="hello"
    )


def test_from_link_text():
    assert Selector.from_link_text("hello_world") == Selector(
        selector_type=SelectorType.BY_LINK_TEXT, inner_text="hello_world"
    )


def test_from_name():
    assert Selector.from_name("some_name") == Selector(
        selector_type=SelectorType.BY_NAME, other_attributes={"name": "some_name"}
    )


def test_from_partial_link_text():
    assert Selector.from_partial_link_text("hello_world") == Selector(
        selector_type=SelectorType.BY_PARTIAL_LINK_TEXT, inner_text="hello_world"
    )


def test_from_tag_name():
    assert Selector.from_tag_name("h3") == Selector(
        selector_type=SelectorType.BY_TAG_NAME, tag="h3"
    )


def test_from_xpath_simple():
    xpath_selector = "//div"
    assert Selector.from_xpath(xpath_selector) == Selector(
        selector_type=SelectorType.BY_XPATH, tag="div"
    )


def test_from_xpath_complex():
    xpath_selector = (
        "//div[@name='my_selector'][@class='classname cls2' and text()='hello world']"
    )
    assert Selector.from_xpath(xpath_selector) == Selector(
        selector_type=SelectorType.BY_XPATH,
        tag="div",
        classes=["classname", "cls2"],
        other_attributes={"name": "my_selector"},
        inner_text="hello world",
    )


def test_from_type_and_value():
    assert Selector.from_type_and_value(
        SelectorType.BY_ID, value="some-id"
    ) == Selector(selector_type=SelectorType.BY_ID, id="some-id")
