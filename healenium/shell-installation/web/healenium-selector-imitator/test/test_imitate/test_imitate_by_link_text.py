import pytest

from src.node import Node
from src.selector import Selector, SelectorType
from src.selector_imitator import SelectorImitator, ImitationError


def test_imitate_by_link_text():
    user_selector = Selector(selector_type=SelectorType.BY_LINK_TEXT, inner_text="link")
    target_node = Node(tag="a", inner_text="link to external page")
    expected_result = Selector(
        selector_type=SelectorType.BY_LINK_TEXT, inner_text="link to external page"
    )
    imitated_selectors = SelectorImitator(user_selector, target_node).imitate()
    assert len(imitated_selectors) == 1
    assert imitated_selectors[0] == expected_result


def test_imitate_by_link_text_not_anchor():
    user_selector = Selector(selector_type=SelectorType.BY_LINK_TEXT, inner_text="link")
    target_node = Node(tag="p", inner_text="link to external page")
    with pytest.raises(ImitationError):
        SelectorImitator(user_selector, target_node).imitate()


def test_imitate_by_link_text_invalid_target():
    user_selector = Selector(selector_type=SelectorType.BY_LINK_TEXT, inner_text="link")
    target_node = Node(tag="a", inner_text="")
    with pytest.raises(ImitationError):
        SelectorImitator(user_selector, target_node).imitate()
