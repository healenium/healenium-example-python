import pytest

from src.selector_parser import XPathParser, ParsingError


def test_validation_success_simple():
    XPathParser("//p")


def test_validation_success_complex():
    XPathParser("//label[@id='message23']")


def test_validation_success_no_tag():
    XPathParser("//*[@class='cls1'][1]")


def test_validation_error():
    with pytest.raises(ParsingError):
        XPathParser("//*[@type='text']//following::input")


def test_parse_tag():
    assert XPathParser("//label[@id='message23']").get_tag() == "label"


def test_parse_tag_simple():
    assert XPathParser("//h2").get_tag() == "h2"


def test_parse_no_tag():
    assert XPathParser("//*[@class='cls1'][1]").get_tag() == ""


def test_parse_id():
    assert XPathParser("//*[@id='rt-feature']").get_id() == "rt-feature"


def test_parse_no_id():
    assert XPathParser("//*[@class='cls1'][1]").get_id() == ""


def test_parse_classes_single_class():
    assert XPathParser("//*[@class='cls1'][1]").get_classes() == ["cls1"]


def test_parse_classes_multiple_classes():
    assert XPathParser("//*[@class='cls1 cls2'][1]").get_classes() == ["cls1", "cls2"]


def test_parse_classes_single_class_with_contains():
    assert XPathParser("//*[contains(@class,'btn')]").get_classes() == ["btn"]


def test_parse_classes_multiple_classes_with_contains():
    assert XPathParser("//*[contains(@class,'btn cls1')]").get_classes() == [
        "btn",
        "cls1",
    ]


def test_parse_classes_no_class():
    assert XPathParser("//label[@id='message23']").get_classes() == []


def test_parse_attributes_single_quotes():
    selector = "//div[@id='hello'][@href='hello.world']"
    assert XPathParser(selector).get_attributes() == {"href": "hello.world"}


def test_parse_attributes_double_quotes():
    selector = '//*[@class="class-hello" and @name="hello"]'
    assert XPathParser(selector).get_attributes() == {"name": "hello"}


def test_parse_attributes_empty():
    selector = "//*[@class='class-hello']"
    assert XPathParser(selector).get_attributes() == {}


def test_parse_index():
    selector = "//*[@class='cls1 cls2'][2]"
    assert XPathParser(selector).get_index() == 2


def test_parse_index_no_index():
    selector = "//div[@id='hello'][@href='hello.world']"
    assert XPathParser(selector).get_index() is None


def test_parse_inner_text():
    selector = "//p[@class='cls1 cls2' and text()='Hello, World!'][2]"
    assert XPathParser(selector).get_inner_text() == "Hello, World!"


def test_parse_inner_text_empty():
    selector = "//p[@class='cls1 cls2'][2]"
    assert XPathParser(selector).get_inner_text() == ""
