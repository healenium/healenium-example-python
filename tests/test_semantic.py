from src.main.constants.locator_type import LocatorType
from src.main.pages.markup_page import MarkupPage
from src.main.pages.testenv_page import TestEnvPage
from tests.test_base import TestBase


class TestSemantic(TestBase):

    def test_semantic_class_name(self, setup_method):
        main_page = MarkupPage(self.driver)

        main_page.open_browser()
        main_page.click_test_button()
        main_page.confirm_alert()

        main_page.generate_markup()
        main_page.click_test_button()  # should be healed
        main_page.confirm_alert()

    def test_semantic_id(self, setup_method):
        self.driver = setup_method
        test_page = TestEnvPage(self.driver)

        test_page.open_browser()
        test_page.find_test_element(LocatorType.id, "change_id")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.id, "change_id")  # should be healed

    def test_semantic_link_text(self, setup_method):
        self.driver = setup_method
        test_page = TestEnvPage(self.driver)

        test_page.open_browser()
        test_page.find_test_element(LocatorType.link_text, "Change: LinkText, PartialLinkText")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.link_text, "Change: LinkText, PartialLinkText")  # should be healed

    def test_semantic_partial_link_text(self, setup_method):
        self.driver = setup_method
        test_page = TestEnvPage(self.driver)

        test_page.open_browser()
        test_page.find_test_element(LocatorType.partial_link_text, "PartialLinkText")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.partial_link_text, "PartialLinkText")  # should be healed

    def test_semantic_name(self, setup_method):
        self.driver = setup_method
        test_page = TestEnvPage(self.driver)

        test_page.open_browser()
        test_page.find_test_element(LocatorType.name, "change_name")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.name, "change_name")  # should be healed

    def test_semantic_element(self, setup_method):
        self.driver = setup_method
        test_page = TestEnvPage(self.driver)

        test_page.open_browser()
        test_page.find_test_element(LocatorType.tag, "test_tag")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.tag, "test_tag")  # should be healed
