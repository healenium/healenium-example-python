from typing import List, Dict, Optional


class CSSSelectorConstructor:
    def __init__(
        self,
        tag: Optional[str] = None,
        element_id: Optional[str] = None,
        classes: Optional[List[str]] = None,
        other_attributes: Optional[Dict[str, str]] = None,
    ):
        self.tag = tag
        self.element_id = element_id
        if classes is not None:
            self.classes = classes
        else:
            self.classes = []
        if other_attributes is not None:
            self.other_attributes = other_attributes
        else:
            self.other_attributes = {}

    def get_string_representation(self) -> str:
        result = ""
        if self.tag is not None:
            result += self.tag
        if self.element_id is not None:
            result += f"#{self.element_id}"
        for class_name in self.classes:
            result += f".{class_name}"
        for attr_name, attr_value in self.other_attributes.items():
            result += f"[{attr_name}='{attr_value}']"
        return result


class XPathConstructor:
    def __init__(
        self,
        tag: Optional[str] = None,
        element_id: Optional[str] = None,
        classes: Optional[List[str]] = None,
        other_attributes: Optional[Dict[str, str]] = None,
        index: Optional[int] = None,
        inner_text: Optional[str] = None,
    ):
        self.tag = tag
        self.element_id = element_id
        if classes is not None:
            self.classes = classes
        else:
            self.classes = []
        if other_attributes is not None:
            self.other_attributes = other_attributes
        else:
            self.other_attributes = {}
        self.index = index
        self.inner_text = inner_text

    def get_string_representation(self, split_classes: bool = False) -> str:
        result = "//"
        if self.tag is None:
            result += "*"
        else:
            result += self.tag
        if self.element_id is not None:
            result += f"[@id='{self.element_id}']"
        if split_classes:
            for classname in self.classes:
                result += f"[contains(@class, '{classname}')]"
        elif self.classes:
            merged_classes = " ".join(self.classes)
            result += f"[@class='{merged_classes}']"
        for attr_name, attr_value in self.other_attributes.items():
            result += f"[@{attr_name}='{attr_value}']"
        if self.inner_text is not None:
            result += f"[text()='{self.inner_text}']"
        if self.index is not None:
            result += f"[{self.index}]"
        return result
