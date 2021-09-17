from selenium.webdriver.common.by import By

from src.main.locators.callback_locators import Locators
from src.main.pages.base_page import Base_Page


class Callback_Page(Base_Page):

    def open_browser(self):
        self.driver.get(Base_Page.callbackTestPageUrl);
        return self

    def click_add_square_button(self):
        self.add_square_button = self.driver.find_element(By.XPATH, Locators.add_square_button)
        self.add_square_button.click()

    def verify_shadow_element(self):
        shadowRoot = self.driver.find_element(By.XPATH, Locators.test_button);
        button = self.driver.execute_script("return arguments[0].shadowRoot", shadowRoot)
        return button.is_enabled()

    def verify_square_element(self):
        square = self.driver.find_element(By.CSS_SELECTOR, Locators.test_button_css)
        return square.is_enabled()

    def click_update_square_button(self):
        self.driver.find_element(By.XPATH, Locators.update_square_button).click()

    def click_remove_square_button(self):
        self.driver.find_element(By.XPATH, Locators.remove_square_button).click()
