from src.main.pages.markup_page import MarkupPage
from tests.test_base import TestBase


class TestWait(TestBase):

    def test_conditional_wait(self,setup_method):
        self.driver=setup_method
        markup_page=MarkupPage(self.driver)

        markup_page.open_browser()
        markup_page.click_test_button()
        markup_page.confirm_alert()

        markup_page.generate_markup()
        markup_page.click_test_button() #should be healed
        markup_page.confirm_alert()

        markup_page.generate_markup()
        markup_page.click_test_button_wait(5) #should be healed
        markup_page.confirm_alert()
