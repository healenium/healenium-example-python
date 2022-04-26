from selenium import webdriver
from selenium.webdriver.common.by import By
from src.main.pages.base_page import BasePage


class CallbackPage(BasePage):

    add_square_button = '//button[contains(@class, "add")]'
    update_square_button = '//button[contains(@class, "update")]'
    remove_square_button = '//button[contains(@class, "remove")]'

    test_button = '//custom-square[contains(@c, "red")]'
    test_button_css = '[c="red"]'

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
        self.driver.get(BasePage.callbackTestPageUrl)
        return self

    def click_add_square_button(self):
        add_square_button = self.driver.find_element(By.XPATH, self.add_square_button)
        add_square_button.click()

    def verify_square_element(self):
        square = self.driver.find_element(By.CSS_SELECTOR, self.test_button_css)
        return square.is_enabled()

    def click_update_square_button(self):
        self.driver.find_element(By.XPATH, self.update_square_button).click()

    def click_remove_square_button(self):
        self.driver.find_element(By.XPATH, self.remove_square_button).click()

    def close(self):
        self.driver.quit()
