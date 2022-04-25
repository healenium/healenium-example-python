from src.main.pages.testenv_page import TestEnvPage
from tests.test_base import TestBase


class TestGeneral(TestBase):

    def test_select_checkboxes(self, setup_method):
        self.driver = setup_method
        test_page = TestEnvPage(self.driver)

        test_page.open_browser()
        test_page.select_checkboxes()
        test_page.click_form_submit_btn()
        test_page.select_checkboxes()  # should be healed
