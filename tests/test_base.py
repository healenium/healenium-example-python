import pytest
from selenium import webdriver


class Test_Base():

    @pytest.fixture()
    def setup_method(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        self.driver = webdriver.Remote(
            command_executor="http://localhost:8085",
            desired_capabilities=webdriver.DesiredCapabilities.CHROME,
            options=options)

        # options = webdriver.FirefoxOptions()
        # browser = webdriver.Remote(
        #     command_executor="http://localhost:4444/wd/hub/",
        #     desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
        #     options=options)

    def teardown_method(self, method):
        self.driver.quit()
