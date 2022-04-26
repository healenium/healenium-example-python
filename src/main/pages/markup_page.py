from selenium import webdriver

from src.main.pages.base_page import BasePage


class MarkupPage(BasePage):

    # by id
    generate_markup_btn_id = 'markup-generation-button'
    # by class name
    test_button = 'default-btn'

    driver: webdriver

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Remote(
            command_executor="http://localhost:8085",
            desired_capabilities=webdriver.DesiredCapabilities.CHROME,
            options=options)

    def open_browser(self):
        self.driver.get(BasePage.mainPageUrl)
        return self

    def generate_markup(self):
        generate_markup = self.driver.find_element_by_id(self.generate_markup_btn_id)
        generate_markup.click()
        return self

    def click_test_button(self):
        self.driver.find_element_by_class_name(self.test_button).click()

    def close(self):
        self.driver.quit()
