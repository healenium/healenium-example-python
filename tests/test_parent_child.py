from src.main.constants.locator_type import LocatorType
from src.main.pages.testenv_page import TestEnvPage
from tests.test_base import TestBase


class TestParentChild(TestBase):

    def test_select_checkboxes_under_parent(self, setup_method):
        test_page = TestEnvPage(self.driver)

        test_page.open_browser()
        test_page.select_checkboxes_under_parent()
        test_page.click_form_submit_btn()
        test_page.select_checkboxes_under_parent()

    def test_parent_xpath(self, setup_method):
        # "parent::"
        self.driver = setup_method
        testenv_page = TestEnvPage(self.driver)

        testenv_page.open_browser()
        testenv_page.find_test_element(LocatorType.xpath, "")
        testenv_page.click_submit_btn()
        testenv_page.find_test_element(LocatorType.xpath, "")

    def test_css_first_child(self, setup_method):
        self.driver = setup_method
        testenv_page = TestEnvPage(self.driver)

        testenv_page.open_browser()
        testenv_page.find_test_element(LocatorType.css, "test_tag:first-child")
        testenv_page.click_submit_btn()
        testenv_page.find_test_element(LocatorType.css, "test_tag:first-child")

    def test_css_last_child(self, setup_method):
        self.driver = setup_method
        testenv_page = TestEnvPage(self.driver)

        testenv_page.open_browser()
        testenv_page.find_test_element(LocatorType.css, "child_tag:last-child")
        testenv_page.click_submit_btn()
        testenv_page.find_test_element(LocatorType.css, "child_tag:last-child")
