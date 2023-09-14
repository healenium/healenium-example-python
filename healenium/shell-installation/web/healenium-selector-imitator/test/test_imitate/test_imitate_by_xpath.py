import pytest

from src.node import Node
from src.selector import Selector, SelectorType
from src.selector_imitator import SelectorImitator, ImitationError


def test_imitate_by_xpath():
    user_selector = Selector(
        selector_type=SelectorType.BY_XPATH,
        tag="img",
        other_attributes={"name": "some_name"},
    )
    target_node = Node(tag="img", other_attributes={"name": "name2"})
    expected_result = Selector(
        selector_type=SelectorType.BY_XPATH,
        tag="img",
        other_attributes={"name": "name2"},
    )
    imitated_selectors = SelectorImitator(user_selector, target_node).imitate()
    assert len(imitated_selectors) == 1
    assert imitated_selectors[0] == expected_result


def test_imitate_by_xpath_invalid_attributes():
    user_selector = Selector(
        selector_type=SelectorType.BY_XPATH,
        classes=["class1"],
        other_attributes={"name": "some_name"},
    )
    target_node = Node(
        classes=["class2", "class3"], other_attributes={"src": "img.png"}
    )
    with pytest.raises(ImitationError):
        SelectorImitator(user_selector, target_node).imitate()


def test_imitate_by_xpath_invalid_target():
    user_selector = Selector(
        selector_type=SelectorType.BY_XPATH,
        tag="img",
        other_attributes={"name": "some_name"},
    )
    target_node = Node(other_attributes={"name": "some_name"})
    with pytest.raises(ImitationError):
        SelectorImitator(user_selector, target_node).imitate()
