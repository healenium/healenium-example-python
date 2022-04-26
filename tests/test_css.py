from src.main.constants.locator_type import LocatorType
from src.main.pages.callback_page import CallbackPage
from src.main.pages.testenv_page import TestEnvPage


class TestCss:

    def test_css_attribute(self):
        callback_page = CallbackPage()

        callback_page.open_browser()
        callback_page.click_add_square_button()
        result = callback_page.verify_square_element()
        assert result == True

        callback_page.click_update_square_button()
        result = callback_page.verify_square_element()  # should be healed
        assert result == True

        callback_page.close()

    def test_css_id(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.find_test_element(LocatorType.css, "#change_id")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.css, "#change_id")

        test_page.close()

    def test_css_id_special_character(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.find_test_element(LocatorType.css, "input#change\\:name")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.css, "input#change\\:name")

        test_page.close()

    def test_css_element(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.find_test_element(LocatorType.css, "test_tag")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.css, "test_tag")

        test_page.close()

    def test_css_disabled(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.find_test_element(LocatorType.css, "input:disabled")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.css, "input:disabled")

        test_page.close()

    def test_css_enabled(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.find_test_element(LocatorType.css, "textarea:enabled")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.css, "textarea:enabled")

        test_page.close()

    def test_css_checked(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.find_test_element(LocatorType.css, "input:checked")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.css, "input:checked")

        test_page.close()

    def test_css_class_name(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.find_test_element(LocatorType.css, ".test_class")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.css, ".test_class")

        test_page.close()
