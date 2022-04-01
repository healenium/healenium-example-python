from selenium import webdriver

from src.main.pages.markup_page import *
from src.main.pages.testenv_page import TestEnvPage
from test_base import TestBase


class TestMarkup(TestBase):

    # Markup_Page: different locator types with string property
    def test_button_click_specific_find_element(self, setup_method):
        main_page = MarkupPage(self.driver)

        main_page.open_browser()
        main_page.click_test_button()
        main_page.confirm_alert()

        main_page.generate_markup()
        main_page.click_test_button()  # should be healed
        main_page.confirm_alert()

    def test_select_checkboxes(self, setup_method):
        test_page = TestEnvPage(self.driver)

        test_page.open_browser()
        test_page.select_checkboxes()
        test_page.click_form_submit_btn()
        test_page.select_checkboxes()  # should be healed

    def test_button_click_with_id(self, setup_method):
        test_page = TestEnvPage(self.driver)

        test_page.open_browser()
        test_page.click_btn_id()
        test_page.click_submit_btn()
        test_page.click_btn_id()  # should be healed

    # Markup_Page_By: different locator types with By in property
    def test_button_click_find_by(self, setup_method):
        markup_page_by = MarkupPageBy(self.driver)

        markup_page_by.open_browser()
        markup_page_by.click_button_for_invisible()
        markup_page_by.check_that_button_invisible()

        markup_page_by.open_browser()
        markup_page_by.click_test_button()
        markup_page_by.confirm_alert()

        markup_page_by.generate_markup()
        markup_page_by.click_test_button()  # should be healed
        markup_page_by.confirm_alert()

    # Markup_Page_Request: different locator types with By in request
    def test_button_click_find_request(self, setup_method):
        markup_page_request = MarkupPageRequest(self.driver)

        markup_page_request.open_browser()
        markup_page_request.click_test_button()
        markup_page_request.confirm_alert()

        markup_page_request.generate_markup()
        markup_page_request.click_test_button()  # should be healed
        markup_page_request.confirm_alert()
