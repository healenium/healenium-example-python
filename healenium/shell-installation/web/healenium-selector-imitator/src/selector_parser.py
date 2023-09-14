import re

from typing import List, Dict, Optional


class ParsingError(Exception):
    pass


class ParsingUtils:
    @staticmethod
    def remove_quoted_text(text: str) -> str:
        result = text
        single_quote_expression = re.compile("'.*'")
        double_quote_expression = re.compile('".*"')
        for expression in [single_quote_expression, double_quote_expression]:
            while True:
                search_result = expression.search(result)
                if search_result is not None:
                    idx_from, idx_to = search_result.span()
                    result = result[:idx_from] + result[idx_to:]
                else:
                    break
        return result


class CSSSelectorParser:
    def __init__(self, selector: str):
        self.selector = selector
        self.validate()

    def validate(self) -> None:
        expression = re.compile(r"^([\w-]*)(\.[\w-]+|#[\w-]+|\[.+])*$")
        if expression.match(self.selector) is None:
            raise ParsingError("Cannot parse CSS selector.")

    def get_tag(self) -> str:
        expression = re.compile(r"^[\w-]+")
        search_result = expression.search(self.selector)
        if search_result is None:
            return ""
        else:
            return search_result.group()

    def get_id(self) -> str:
        expression = re.compile(r"#([\w-]+)")
        search_result = expression.search(
            ParsingUtils.remove_quoted_text(self.selector)
        )
        if search_result is None:
            return ""
        else:
            return search_result.group(1)

    def get_classes(self) -> List[str]:
        expression = re.compile(r"\.([\w-]+)")
        return expression.findall(ParsingUtils.remove_quoted_text(self.selector))

    def get_attributes(self) -> Dict[str, str]:
        attributes = {}
        raw_attributes = re.compile(r"\[[^\[\]]+]").findall(self.selector)
        for attribute in raw_attributes:
            attribute_expression = re.compile(r"""\[([\w-]+)=('.*'|".*")]""")
            attribute_match = attribute_expression.match(attribute)
            if attribute_match is not None:
                attributes[attribute_match.group(1)] = (
                    attribute_match.group(2).strip("'").strip('"')
                )
        return attributes


class XPathParser:
    def __init__(self, selector: str):
        self.selector = selector
        self.validate()

    def validate(self) -> None:
        expression = re.compile(r"^//([\w-]*|\*)(\[.+])*$")
        if expression.match(self.selector) is None:
            raise ParsingError("Cannot parse XPath selector.")

    def get_tag(self) -> str:
        expression = re.compile(r"^//([\w-]+)")
        search_result = expression.search(self.selector)
        if search_result is None:
            return ""
        else:
            return search_result.group(1)

    def get_id(self) -> str:
        expression = re.compile(r"""@id=('[\w-]+'|"[\w-]+")""")
        search_result = expression.search(self.selector)
        if search_result is None:
            return ""
        else:
            return search_result.group(1).strip('"').strip("'")

    def get_classes(self) -> List[str]:
        expression_all_classes = r"""@class=('[ \w-]+'|"[ \w-]+")"""
        expression_contains = r"""contains\(@class,('[ \w-]+'|"[ \w-]+")\)"""
        for expression in [expression_all_classes, expression_contains]:
            search_result = re.compile(expression).search(self.selector)
            if search_result is not None:
                return search_result.group(1).strip('"').strip("'").split(" ")
        return []

    def get_attributes(self) -> Dict[str, str]:
        attributes = {}
        attribute_expression = re.compile(r"""@([\w-]+)=('[^']*'|"[^"]*")""")
        raw_attributes = attribute_expression.findall(self.selector)
        for attr_name, attr_value in raw_attributes:
            if attr_name not in ["class", "id"]:
                attributes[attr_name] = attr_value.strip("'").strip('"')
        return attributes

    def get_index(self) -> Optional[int]:
        expression = re.compile(r"""\[(\d)+]""")
        search_result = expression.search(
            ParsingUtils.remove_quoted_text(self.selector)
        )
        if search_result is None:
            return None
        else:
            return int(search_result.group(1))

    def get_inner_text(self) -> str:
        expression = re.compile(r"""text\(\)=('[^']*'|"[^"]*")""")
        search_result = expression.search(self.selector)
        if search_result is None:
            return ""
        else:
            return search_result.group(1)[1:-1]
