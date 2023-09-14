import pytest

from src.selector_parser import CSSSelectorParser, ParsingError


def test_validation_success_simple():
    CSSSelectorParser("p")


def test_validation_success_complex():
    CSSSelectorParser("div#hello.class_name[href='hello world']")


def test_validation_error():
    with pytest.raises(ParsingError):
        CSSSelectorParser("div#hello_world span.some_class")


def test_parse_tag():
    selector = "div#hello.class_name[href='hello world']"
    assert CSSSelectorParser(selector).get_tag() == "div"


def test_parse_no_tag():
    selector = "#hello.class_name[href='hello world']"
    assert CSSSelectorParser(selector).get_tag() == ""


def test_parse_tag_simple():
    selector = "div"
    assert CSSSelectorParser(selector).get_tag() == "div"


def test_parse_id():
    selector = "div#hello-world.class_name[href='hello world']"
    assert CSSSelectorParser(selector).get_id() == "hello-world"


def test_parse_id_empty():
    selector = "div.class_name[href='hello #world']"
    assert CSSSelectorParser(selector).get_id() == ""


def test_parse_classes():
    selector = "div#hello.class_name.class_2[href='hello world']"
    assert set(CSSSelectorParser(selector).get_classes()) == {"class_name", "class_2"}


def test_parse_classes_empty():
    selector = "div#hello[href='hello.world']"
    assert set(CSSSelectorParser(selector).get_classes()) == set()


def test_parse_attributes_single_quotes():
    selector = "div#hello[href='hello.world']"
    assert CSSSelectorParser(selector).get_attributes() == {"href": "hello.world"}


def test_parse_attributes_double_quotes():
    selector = 'div.class_hello[name="hello"]'
    assert CSSSelectorParser(selector).get_attributes() == {"name": "hello"}


def test_parse_attributes_empty():
    selector = "div.class_hello"
    assert CSSSelectorParser(selector).get_attributes() == {}
