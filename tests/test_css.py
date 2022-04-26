import pytest
from selenium import webdriver

from src.main.constants.locator_type import LocatorType
from src.main.pages.callback_page import CallbackPage
from src.main.pages.testenv_page import TestEnvPage
from tests.test_base import TestBase


class TestCss:

    @pytest.fixture()
    def setup_method(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Remote(
            command_executor="http://localhost:8085",
            desired_capabilities=webdriver.DesiredCapabilities.CHROME,
            options=options)
        return self.driver

    def test_css_attribute(self, setup_method):
        self.driver = setup_method
        callback_page = CallbackPage(self.driver)

        callback_page.open_browser()
        callback_page.click_add_square_button()
        result = callback_page.verify_square_element()
        assert result == True

        callback_page.click_update_square_button()
        result = callback_page.verify_square_element()  # should be healed
        assert result == True

    def test_css_id(self, setup_method):
        self.driver = setup_method
        test_page = TestEnvPage(self.driver)

        test_page.open_browser()
        test_page.find_test_element(LocatorType.css, "#change_id")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.css, "#change_id")

    def test_css_id_special_character(self, setup_method):
        self.driver = setup_method
        test_page = TestEnvPage(self.driver)

        test_page.open_browser()
        test_page.find_test_element(LocatorType.css, "input#change\\:name")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.css, "input#change\\:name")

    def test_css_element(self, setup_method):
        self.driver = setup_method
        test_page = TestEnvPage(self.driver)

        test_page.open_browser()
        test_page.find_test_element(LocatorType.css, "test_tag")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.css, "test_tag")

    def test_css_disabled(self, setup_method):
        self.driver = setup_method
        test_page = TestEnvPage(self.driver)

        test_page.open_browser()
        test_page.find_test_element(LocatorType.css, "input:disabled")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.css, "input:disabled")

    def test_css_enabled(self, setup_method):
        self.driver = setup_method
        test_page = TestEnvPage(self.driver)

        test_page.open_browser()
        test_page.find_test_element(LocatorType.css, "textarea:enabled")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.css, "textarea:enabled")

    def test_css_checked(self, setup_method):
        self.driver = setup_method
        test_page = TestEnvPage(self.driver)

        test_page.open_browser()
        test_page.find_test_element(LocatorType.css, "input:checked")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.css, "input:checked")

    def test_css_class_name(self, setup_method):
        self.driver = setup_method
        test_page = TestEnvPage(self.driver)

        test_page.open_browser()
        test_page.find_test_element(LocatorType.css, ".test_class")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.css, ".test_class")

    def teardown_method(self):
        self.driver.quit()