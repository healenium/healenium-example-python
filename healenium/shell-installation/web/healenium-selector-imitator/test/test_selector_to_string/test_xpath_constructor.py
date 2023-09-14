from src.selector_to_string import XPathConstructor


def test_xpath_constructor_only_tag():
    assert XPathConstructor(tag="h2").get_string_representation() == "//h2"


def test_xpath_constructor_only_id():
    assert (
        XPathConstructor(element_id="hello").get_string_representation()
        == "//*[@id='hello']"
    )


def test_xpath_constructor_id_with_tag():
    assert (
        XPathConstructor(tag="h2", element_id="hello").get_string_representation()
        == "//h2[@id='hello']"
    )


def test_xpath_constructor_id_with_tag_and_classes():
    assert (
        XPathConstructor(
            tag="h2", element_id="hello", classes=["class1", "cls2"]
        ).get_string_representation()
        == "//h2[@id='hello'][@class='class1 cls2']"
    )


def test_xpath_constructor_id_with_tag_and_classes_split():
    assert (
        XPathConstructor(
            tag="h2", element_id="hello", classes=["class1", "cls2"]
        ).get_string_representation(split_classes=True)
        == "//h2[@id='hello'][contains(@class, 'class1')][contains(@class, 'cls2')]"
    )


def test_xpath_constructor_all_elements():
    assert (
        XPathConstructor(
            tag="h2",
            element_id="hello",
            classes=["cls1"],
            other_attributes={"value": "42"},
            index=11,
            inner_text="Hello, World!",
        ).get_string_representation()
        == "//h2[@id='hello'][@class='cls1']"
        "[@value='42'][text()='Hello, World!'][11]"
    )
