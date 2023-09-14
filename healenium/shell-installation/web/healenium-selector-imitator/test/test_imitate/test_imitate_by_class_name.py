import pytest

from src.node import Node
from src.selector import Selector, SelectorType
from src.selector_imitator import SelectorImitator, ImitationError


def test_imitate_by_class_name():
    user_selector = Selector(
        selector_type=SelectorType.BY_CLASS_NAME, classes=["class1"]
    )
    target_node = Node(classes=["class2"])
    expected_result = Selector(
        selector_type=SelectorType.BY_CLASS_NAME, classes=["class2"]
    )
    imitated_selectors = SelectorImitator(user_selector, target_node).imitate()
    assert len(imitated_selectors) == 1
    assert imitated_selectors[0] == expected_result


def test_imitate_by_class_name_two_classes():
    user_selector = Selector(
        selector_type=SelectorType.BY_CLASS_NAME, classes=["class1"]
    )
    target_node = Node(classes=["class2", "class3"])
    expected_result = [
        Selector(selector_type=SelectorType.BY_CLASS_NAME, classes=["class2"]),
        Selector(selector_type=SelectorType.BY_CLASS_NAME, classes=["class3"]),
    ]
    imitated_selectors = SelectorImitator(user_selector, target_node).imitate()
    assert expected_result == imitated_selectors


def test_imitate_by_class_name_invalid_target():
    user_selector = Selector(
        selector_type=SelectorType.BY_CLASS_NAME, classes=["class1"]
    )
    target_node = Node(tag="p", id="some_id")
    with pytest.raises(ImitationError):
        SelectorImitator(user_selector, target_node).imitate()
