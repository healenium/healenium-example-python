
from src.main.pages.callback_page import CallbackPage

from test_base import TestBase


class TestCallback(TestBase):

    def test_css_locators(self, setup_method):
        self.driver = setup_method
        callback_page = CallbackPage(self.driver)

        callback_page.open_browser()
        callback_page.click_add_square_button()
        result = callback_page.verify_square_element()
        assert result == True

        callback_page.click_update_square_button()
        result = callback_page.verify_square_element()  # should be healed
        assert result == True
