from selenium import webdriver

from src.main.pages.testenv_page import TestEnvPage
from tests.test_base import TestBase


class TestGeneral(TestBase):

    def test_select_checkboxes(self, setup_method):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Remote(
            command_executor="http://localhost:8085",
            desired_capabilities=webdriver.DesiredCapabilities.CHROME,
            options=options)
        test_page = TestEnvPage(self.driver)

        test_page.open_browser()
        test_page.select_checkboxes()
        test_page.click_form_submit_btn()
        test_page.select_checkboxes()  # should be healed
