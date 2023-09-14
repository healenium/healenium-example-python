from .node import Node
from .selector import Selector, SelectorType
from typing import List


class ImitationError(Exception):
    pass


class SelectorImitator:
    def __init__(self, user_selector: Selector, target_node: Node):
        self.user_selector = user_selector
        self.target_node = target_node

    def _imitate_class_name(self) -> List[Selector]:
        if self.target_node.classes:
            return [
                Selector(
                    selector_type=SelectorType.BY_CLASS_NAME,
                    classes=[target_class],
                )
                for target_class in self.target_node.classes
            ]
        else:
            raise ImitationError("Target node does not belong to any class.")

    def _imitate_css_or_xpath(self) -> Selector:
        target_selector = Selector(selector_type=self.user_selector.selector_type)
        if self.user_selector.tag is not None:
            if self.target_node.tag:
                target_selector.tag = self.target_node.tag
            else:
                raise ImitationError("Target node does not have any tag.")
        if self.user_selector.id is not None:
            if self.target_node.id:
                target_selector.id = self.target_node.id
            else:
                raise ImitationError("Target node does not have any id.")
        if self.user_selector.classes is not None:
            if self.target_node.classes:
                target_selector.classes = []
                some_class_changed = False
                for cls in self.user_selector.classes:
                    if cls in self.target_node.classes:
                        target_selector.classes.append(cls)
                    else:
                        some_class_changed = True
                        break
                if some_class_changed:
                    target_selector.classes = self.target_node.classes
            else:
                raise ImitationError("Target node does not belong to any classes.")
        target_selector.split_classes = (
            target_selector.classes != self.target_node.classes
        )
        if self.user_selector.index is not None:
            if self.target_node.index:
                target_selector.index = self.target_node.index
            else:
                raise ImitationError("Target node does not have any index.")
        if self.user_selector.inner_text is not None:
            if self.target_node.inner_text:
                target_selector.inner_text = self.target_node.inner_text
            else:
                raise ImitationError("Target node does not have any inner text.")
        if self.user_selector.other_attributes is not None:
            target_selector.other_attributes = {}
            for attribute in self.user_selector.other_attributes:
                if attribute in self.target_node.other_attributes:
                    target_selector.other_attributes[
                        attribute
                    ] = self.target_node.other_attributes[attribute]
                else:
                    raise ImitationError(
                        f"Target node does not have an attribute {attribute}."
                    )
        return target_selector

    def _imitate_id(self) -> Selector:
        if self.target_node.id:
            return Selector(selector_type=SelectorType.BY_ID, id=self.target_node.id)
        else:
            raise ImitationError("Target node does not have an id.")

    def _imitate_link_text(self) -> Selector:
        if self.target_node.tag != "a":
            raise ImitationError(
                "Target node is not an anchor tag, "
                "so selector by link text is not applicable."
            )
        if self.target_node.inner_text:
            return Selector(
                selector_type=self.user_selector.selector_type,
                inner_text=self.target_node.inner_text,
            )
        else:
            raise ImitationError("Target node does not have a link text.")

    def _imitate_name(self) -> Selector:
        if "name" in self.target_node.other_attributes:
            if (
                self.user_selector.other_attributes is not None
                and "name" in self.user_selector.other_attributes
            ):
                return Selector(
                    selector_type=SelectorType.BY_NAME,
                    other_attributes={
                        "name": self.target_node.other_attributes["name"]
                    },
                )
            else:
                raise ImitationError(
                    "Invalid user selector: does not contain name attribute, "
                    "while type is BY_NAME."
                )
        else:
            raise ImitationError("Target node does not have a name attribute.")

    def _by_tag_name(self) -> Selector:
        if self.target_node.tag:
            return Selector(
                selector_type=SelectorType.BY_TAG_NAME, tag=self.target_node.tag
            )
        else:
            raise ImitationError("Target node does not have a tag name.")

    def imitate(self) -> List[Selector]:
        """Return a list of possible selectors for a target node that imitates a user selector.
        Raise ImitationError if the target node cannot be imitated.
        """
        if self.user_selector.selector_type is SelectorType.BY_CLASS_NAME:
            return self._imitate_class_name()
        elif self.user_selector.selector_type in [
            SelectorType.BY_CSS_SELECTOR,
            SelectorType.BY_XPATH,
        ]:
            return [self._imitate_css_or_xpath()]
        elif self.user_selector.selector_type is SelectorType.BY_ID:
            return [self._imitate_id()]
        elif self.user_selector.selector_type in [
            SelectorType.BY_LINK_TEXT,
            SelectorType.BY_PARTIAL_LINK_TEXT,
        ]:
            return [self._imitate_link_text()]
        elif self.user_selector.selector_type is SelectorType.BY_NAME:
            return [self._imitate_name()]
        elif self.user_selector.selector_type is SelectorType.BY_TAG_NAME:
            return [self._by_tag_name()]
        else:
            raise ImitationError("Imitation for user selector type is not implemented.")
