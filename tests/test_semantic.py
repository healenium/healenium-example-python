from src.main.constants.locator_type import LocatorType
from src.main.pages.markup_page import MarkupPage
from src.main.pages.testenv_page import TestEnvPage


class TestSemantic:

    def test_semantic_class_name(self):
        main_page = MarkupPage()

        main_page.open_browser()
        main_page.click_test_button()
        main_page.confirm_alert()

        main_page.generate_markup()
        main_page.click_test_button()  # should be healed
        main_page.confirm_alert()

        main_page.close()

    def test_semantic_id(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.find_test_element(LocatorType.id, "change_id")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.id, "change_id")  # should be healed

        test_page.close()

    def test_semantic_link_text(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.find_test_element(LocatorType.link_text, "Change: LinkText, PartialLinkText")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.link_text, "Change: LinkText, PartialLinkText")  # should be healed

        test_page.close()

    def test_semantic_partial_link_text(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.find_test_element(LocatorType.partial_link_text, "PartialLinkText")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.partial_link_text, "PartialLinkText")  # should be healed

        test_page.close()

    def test_semantic_name(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.find_test_element(LocatorType.name, "change_name")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.name, "change_name")  # should be healed

        test_page.close()

    def test_semantic_element(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.find_test_element(LocatorType.tag, "test_tag")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.tag, "test_tag")  # should be healed

        test_page.close()
