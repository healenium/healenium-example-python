from src.main.pages.base_page import BasePage
from src.main.locators.markup_locators import *


class TestEnvPage(BasePage):
    def open_browser(self):
        self.driver.get(BasePage.testEnvPageUrl)
        return self

    def select_checkboxes(self):
        checkboxes = self.driver.find_elements(By.XPATH, "//*[contains(@class,'test-form')]//*[@class='input1']")
        for ch in checkboxes:
            ch.click()
        return self

    def click_form_submit_btn(self):
        self.driver.find_element_by_id('Submit_checkbox').click()
        return self

    def click_btn_id(self):
        self.driver.find_element_by_id('change_id').click()
        return self

    def click_submit_btn(self):
        self.driver.find_element_by_id('Submit').click()
        return self
