from src.selector_to_string import CSSSelectorConstructor


def test_css_constructor_only_tag():
    assert CSSSelectorConstructor(tag="h2").get_string_representation() == "h2"


def test_css_constructor_only_id():
    assert (
        CSSSelectorConstructor(element_id="hello").get_string_representation()
        == "#hello"
    )


def test_css_constructor_id_with_tag():
    assert (
        CSSSelectorConstructor(tag="h2", element_id="hello").get_string_representation()
        == "h2#hello"
    )


def test_css_constructor_id_with_tag_and_classes():
    assert (
        CSSSelectorConstructor(
            tag="h2", element_id="hello", classes=["class1", "cls2"]
        ).get_string_representation()
        == "h2#hello.class1.cls2"
    )


def test_css_constructor_all_elements():
    assert (
        CSSSelectorConstructor(
            tag="h2",
            element_id="hello",
            classes=["class1", "cls2"],
            other_attributes={"href": "hello world"},
        ).get_string_representation()
        == "h2#hello.class1.cls2[href='hello world']"
    )
