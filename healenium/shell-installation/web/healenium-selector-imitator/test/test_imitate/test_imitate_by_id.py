import pytest

from src.node import Node
from src.selector import Selector, SelectorType
from src.selector_imitator import SelectorImitator, ImitationError


def test_imitate_by_id():
    user_selector = Selector(selector_type=SelectorType.BY_ID, id="element1")
    target_node = Node(tag="h1", id="element2")
    expected_result = Selector(selector_type=SelectorType.BY_ID, id="element2")
    imitated_selectors = SelectorImitator(user_selector, target_node).imitate()
    assert len(imitated_selectors) == 1
    assert imitated_selectors[0] == expected_result


def test_imitate_by_id_invalid_target():
    user_selector = Selector(selector_type=SelectorType.BY_ID, id="element1")
    target_node = Node(tag="p", other_attributes={"name": "element1"})
    with pytest.raises(ImitationError):
        SelectorImitator(user_selector, target_node).imitate()
