from src.main.constants.locator_type import LocatorType
from src.main.pages.testenv_page import TestEnvPage


class TestParentChild:

    def test_select_checkboxes_under_parent(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.select_checkboxes_under_parent()
        test_page.click_form_submit_btn()
        test_page.select_checkboxes_under_parent()

        test_page.close()

    def test_parent_xpath(self):
        testenv_page = TestEnvPage()

        testenv_page.open_browser()
        testenv_page.find_test_element(LocatorType.xpath, "(//*[@class='input1']//parent::*[contains(@class, 'input1')])[8]")
        testenv_page.click_submit_btn()
        testenv_page.find_test_element(LocatorType.xpath, "(//*[@class='input1']//parent::*[contains(@class, 'input1')])[8]")

        testenv_page.close()

    def test_css_first_child(self):
        testenv_page = TestEnvPage()

        testenv_page.open_browser()
        testenv_page.find_test_element(LocatorType.css, "test_tag:first-child")
        testenv_page.click_submit_btn()
        testenv_page.find_test_element(LocatorType.css, "test_tag:first-child")

        testenv_page.close()

    def test_css_last_child(self):
        testenv_page = TestEnvPage()

        testenv_page.open_browser()
        testenv_page.find_test_element(LocatorType.css, "child_tag:last-child")
        testenv_page.click_submit_btn()
        testenv_page.find_test_element(LocatorType.css, "child_tag:last-child")

        testenv_page.close()
