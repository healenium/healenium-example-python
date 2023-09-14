import pytest

from src.node import Node
from src.selector import Selector
from src.selector_imitator import SelectorImitator, ImitationError


def test_imitate_unimplemented():
    user_selector = Selector(
        selector_type=42,
        tag="img",
        other_attributes={"name": "some_name"},
    )
    target_node = Node(other_attributes={"name": "some_name"})
    with pytest.raises(ImitationError):
        SelectorImitator(user_selector, target_node).imitate()
