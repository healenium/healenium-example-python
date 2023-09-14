from dataclasses import dataclass
from enum import Enum
from .selector_parser import CSSSelectorParser, XPathParser
from .selector_to_string import CSSSelectorConstructor, XPathConstructor
from typing import Optional, List, Dict


class SelectorType(str, Enum):
    BY_CLASS_NAME = "By.className"
    BY_CSS_SELECTOR = "By.cssSelector"
    BY_ID = "By.id"
    BY_LINK_TEXT = "By.linkText"
    BY_NAME = "By.name"
    BY_PARTIAL_LINK_TEXT = "By.partialLinkText"
    BY_TAG_NAME = "By.tagName"
    BY_XPATH = "By.xpath"


@dataclass
class Selector:
    selector_type: SelectorType
    tag: Optional[str] = None
    id: Optional[str] = None
    classes: Optional[List[str]] = None
    index: Optional[int] = None
    other_attributes: Optional[Dict[str, str]] = None
    inner_text: Optional[str] = None
    split_classes: bool = False

    @classmethod
    def from_type_and_value(cls, selector_type: SelectorType, value: str) -> "Selector":
        if selector_type is SelectorType.BY_CLASS_NAME:
            return cls.from_class_name(value)
        elif selector_type is SelectorType.BY_CSS_SELECTOR:
            return cls.from_css(value)
        elif selector_type is SelectorType.BY_ID:
            return cls.from_id(value)
        elif selector_type is SelectorType.BY_LINK_TEXT:
            return cls.from_link_text(value)
        elif selector_type is SelectorType.BY_NAME:
            return cls.from_name(value)
        elif selector_type is SelectorType.BY_PARTIAL_LINK_TEXT:
            return cls.from_partial_link_text(value)
        elif selector_type is SelectorType.BY_TAG_NAME:
            return cls.from_tag_name(value)
        elif selector_type is SelectorType.BY_XPATH:
            return cls.from_xpath(value)
        else:
            raise ValueError(f"Invalid selector type: {selector_type}")

    @classmethod
    def from_class_name(cls, class_name: str) -> "Selector":
        return cls(selector_type=SelectorType.BY_CLASS_NAME, classes=[class_name])

    @classmethod
    def from_css(cls, css_selector: str) -> "Selector":
        parser = CSSSelectorParser(css_selector)
        return cls(
            selector_type=SelectorType.BY_CSS_SELECTOR,
            tag=parser.get_tag() or None,
            id=parser.get_id() or None,
            classes=parser.get_classes() or None,
            other_attributes=parser.get_attributes() or None,
        )

    @classmethod
    def from_id(cls, element_id: str) -> "Selector":
        return cls(selector_type=SelectorType.BY_ID, id=element_id)

    @classmethod
    def from_link_text(cls, link_text: str) -> "Selector":
        return cls(selector_type=SelectorType.BY_LINK_TEXT, inner_text=link_text)

    @classmethod
    def from_name(cls, name: str) -> "Selector":
        return cls(selector_type=SelectorType.BY_NAME, other_attributes={"name": name})

    @classmethod
    def from_partial_link_text(cls, partial_link_text: str) -> "Selector":
        return cls(
            selector_type=SelectorType.BY_PARTIAL_LINK_TEXT,
            inner_text=partial_link_text,
        )

    @classmethod
    def from_tag_name(cls, tag_name: str) -> "Selector":
        return cls(selector_type=SelectorType.BY_TAG_NAME, tag=tag_name)

    @classmethod
    def from_xpath(cls, xpath_selector: str) -> "Selector":
        parser = XPathParser(xpath_selector)
        return cls(
            selector_type=SelectorType.BY_XPATH,
            tag=parser.get_tag() or None,
            id=parser.get_id() or None,
            classes=parser.get_classes() or None,
            index=parser.get_index(),
            other_attributes=parser.get_attributes() or None,
            inner_text=parser.get_inner_text() or None,
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Selector):
            return False
        return (
            self.selector_type == other.selector_type
            and self.tag == other.tag
            and self.id == other.id
            and set(self.classes or []) == set(other.classes or [])
            and self.index == other.index
            and self.other_attributes == other.other_attributes
            and self.inner_text == other.inner_text
        )

    def __str__(self) -> str:
        if self.selector_type is SelectorType.BY_CLASS_NAME:
            if self.classes is None or len(self.classes) == 0:
                raise ValueError(
                    "BY_CLASS_NAME selector must contain one class name, none provided."
                )
            if len(self.classes) == 1:
                return self.classes[0]
            else:
                raise ValueError(
                    "Ambiguous BY_CLASS_NAME selector. "
                    "Only one class allowed for this selector type."
                )
        elif self.selector_type is SelectorType.BY_CSS_SELECTOR:
            return CSSSelectorConstructor(
                tag=self.tag,
                element_id=self.id,
                classes=self.classes,
                other_attributes=self.other_attributes,
            ).get_string_representation()
        elif self.selector_type is SelectorType.BY_ID:
            return self.id if self.id is not None else ""
        elif self.selector_type is SelectorType.BY_LINK_TEXT:
            return self.inner_text if self.inner_text is not None else ""
        elif self.selector_type is SelectorType.BY_NAME:
            if self.other_attributes is not None and "name" in self.other_attributes:
                return self.other_attributes["name"]
            else:
                raise ValueError("BY_NAME selector must contain name attribute.")
        elif self.selector_type is SelectorType.BY_PARTIAL_LINK_TEXT:
            return self.inner_text if self.inner_text is not None else ""
        elif self.selector_type is SelectorType.BY_TAG_NAME:
            return self.tag if self.tag is not None else ""
        elif self.selector_type is SelectorType.BY_XPATH:
            return XPathConstructor(
                tag=self.tag,
                element_id=self.id,
                classes=self.classes,
                other_attributes=self.other_attributes,
                index=self.index,
                inner_text=self.inner_text,
            ).get_string_representation(split_classes=self.split_classes)
        else:
            return ""
