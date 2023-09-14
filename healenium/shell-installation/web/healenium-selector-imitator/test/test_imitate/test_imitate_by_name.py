import pytest

from src.node import Node
from src.selector import Selector, SelectorType
from src.selector_imitator import SelectorImitator, ImitationError


def test_imitate_by_name():
    user_selector = Selector(
        selector_type=SelectorType.BY_NAME, other_attributes={"name": "element1"}
    )
    target_node = Node(tag="h1", other_attributes={"name": "element_1"})
    expected_result = Selector(
        selector_type=SelectorType.BY_NAME, other_attributes={"name": "element_1"}
    )
    imitated_selectors = SelectorImitator(user_selector, target_node).imitate()
    assert len(imitated_selectors) == 1
    assert imitated_selectors[0] == expected_result


def test_imitate_by_name_invalid_target():
    user_selector = Selector(
        selector_type=SelectorType.BY_NAME, other_attributes={"name": "element1"}
    )
    target_node = Node(tag="h1")
    with pytest.raises(ImitationError):
        SelectorImitator(user_selector, target_node).imitate()


def test_imitate_by_name_invalid_user_selector():
    user_selector = Selector(selector_type=SelectorType.BY_NAME)
    target_node = Node(tag="h1", other_attributes={"name": "element_1"})
    with pytest.raises(ImitationError):
        SelectorImitator(user_selector, target_node).imitate()
