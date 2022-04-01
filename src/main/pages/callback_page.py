from selenium.webdriver.common.by import By

from src.main.locators.callback_locators import Locators
from src.main.pages.base_page import BasePage


class CallbackPage(BasePage):

    def open_browser(self):
        self.driver.get(BasePage.callbackTestPageUrl)
        return self

    def click_add_square_button(self):
        add_square_button = self.driver.find_element(By.XPATH, Locators.add_square_button)
        add_square_button.click()

    def verify_square_element(self):
        square = self.driver.find_element(By.CSS_SELECTOR, Locators.test_button_css)
        return square.is_enabled()

    def click_update_square_button(self):
        self.driver.find_element(By.XPATH, Locators.update_square_button).click()

    def click_remove_square_button(self):
        self.driver.find_element(By.XPATH, Locators.remove_square_button).click()
