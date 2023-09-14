from src.node import Node
from src.selector import Selector
from src.selector_imitator import SelectorImitator


def test_integration_css_selector_name():
    user_selector = Selector.from_css("div[name='old_name']")
    target_node = Node(
        tag="div",
        id="my_div",
        classes=["cls1", "class2"],
        index=1,
        other_attributes={"name": "new_name", "href": "some_link"},
        inner_text="hello world",
    )
    assert (
        str(SelectorImitator(user_selector, target_node).imitate()[0])
        == "div[name='new_name']"
    )


def test_integration_css_selector_tag():
    user_selector = Selector.from_css("h1.cls1[name='some_name']")
    target_node = Node(
        tag="h2",
        id="my_div",
        classes=["cls1", "class2"],
        index=1,
        other_attributes={"name": "some_name", "href": "some_link"},
        inner_text="hello world",
    )
    assert (
        str(SelectorImitator(user_selector, target_node).imitate()[0])
        == "h2.cls1[name='some_name']"
    )


def test_integration_xpath_selector_value():
    user_selector = Selector.from_xpath("//*[@value='Log In']")
    target_node = Node(
        tag="input",
        classes=["fadeIn", "fourth"],
        other_attributes={
            "_ngcontent-wvw-c3": "",
            "type": "button",
            "value": "Log In New",
        },
    )
    assert (
        str(SelectorImitator(user_selector, target_node).imitate()[0])
        == "//*[@value='Log In New']"
    )


def test_integration_xpath_selector_class_split():
    user_selector = Selector.from_xpath("//*[@class='fadeIn'][@value='Log In']")
    target_node = Node(
        tag="input",
        classes=["fadeIn", "fourth"],
        other_attributes={
            "_ngcontent-wvw-c3": "",
            "type": "button",
            "value": "Log In New",
        },
    )
    assert (
        str(SelectorImitator(user_selector, target_node).imitate()[0])
        == "//*[contains(@class, 'fadeIn')][@value='Log In New']"
    )


def test_integration_xpath_selector_class_no_split():
    user_selector = Selector.from_xpath("//*[@class='fadeIn fourth'][@value='Log In']")
    target_node = Node(
        tag="input",
        classes=["fadeIn", "fourth"],
        other_attributes={
            "_ngcontent-wvw-c3": "",
            "type": "button",
            "value": "Log In New",
        },
    )
    assert (
        str(SelectorImitator(user_selector, target_node).imitate()[0])
        == "//*[@class='fadeIn fourth'][@value='Log In New']"
    )
