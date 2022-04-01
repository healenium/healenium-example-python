from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from src.main.locators.markup_locators import *
from src.main.pages.base_page import BasePage


class MarkupPage(BasePage):

    def open_browser(self):
        self.driver.get(BasePage.mainPageUrl)
        return self

    def generate_markup(self):
        generate_markup = self.driver.find_element_by_id(Locators.generate_markup_btn_id)
        generate_markup.click()
        return self

    def click_test_button(self):
        self.driver.find_element_by_class_name(Locators.test_button).click()

    def click_test_generated_button(self):
        self.driver.find_element_by_id(Locators.test_generated_button).click()

    def test_button_id_enabled(self):
        try:
            return self.driver.find_element_by_id(Locators.test_generated_button).is_enabled()
        except NoSuchElementException:
            return False

    def displayed_text(self):
        try:
            return self.driver.find_element_by_xpath(Locators.text_first_select).is_enabled()
        except NoSuchElementException:
            return False

    def select_first_checkbox(self):
        self.driver.find_element_by_xpath(Locators.checkbox_account).click()

    def verify_first_checkbox(self):
        return self.driver.find_element_by_xpath(Locators.checkbox_account).is_enabled()


class MarkupPageBy(BasePage):

    def open_browser(self):
        self.driver.get(BasePage.mainPageUrl)
        return self

    def generate_markup(self):
        generate_markup = self.driver.find_element(*Locators_By.generate_markup_btn_id)
        generate_markup.click()
        return self

    def click_test_button(self):
        test_button = self.driver.find_element(*Locators_By.test_button)
        test_button.click()
        return self

    def click_button_for_invisible(self):
        button_invisible = self.driver.find_element(*Locators_By.button_invisible)
        button_invisible.click()
        return self

    def check_that_button_invisible(self):
        try:
            WebDriverWait(self.driver, 5).until(
                expected_conditions.invisibility_of_element(*Locators_By.button_invisible))
            return True
        except Exception:
            return False


class MarkupPageRequest(BasePage):

    def open_browser(self):
        self.driver.get(BasePage.mainPageUrl)
        return self

    def generate_markup(self):
        generate_markup = self.driver.find_element(**Locators_Request.generate_markup_btn_id)
        generate_markup.click()
        return self

    def generate_markup(self):
        generate_markup = self.driver.find_element(**Locators_Request.generate_markup_btn_id)
        generate_markup.click()
        return self

    def click_test_button(self):
        self.driver.find_element(**Locators_Request.test_button).click()

    def click_test_generated_button(self):
        self.driver.find_element(**Locators_Request.test_generated_button).click()