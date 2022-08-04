import logging

from selenium import webdriver
from selenium.webdriver.common.by import By

from src.main.pages.base_page import BasePage
from src.main.search.context import Context


class TestEnvPage(BasePage):
    submit_btn = 'Submit'
    submit_form_btn = 'Submit_checkbox'

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
        self.driver.get(BasePage.testEnvPageUrl)
        return self

    def select_checkboxes(self):
        checkboxes = self.driver.find_elements(By.XPATH, "//*[contains(@class,'test-form')]//*[@class='input1']")
        for ch in checkboxes:
            ch.click()
        return self

    def click_form_submit_btn(self):
        self.driver.find_element_by_id(self.submit_form_btn).click()
        return self

    def click_submit_btn(self):
        self.driver.find_element_by_id(self.submit_btn).click()
        return self

    def select_checkboxes_under_parent(self):
        checkboxes = self.driver.find_element(By.XPATH, "//*[contains(@class,'test-form')]").find_elements(By.XPATH,
                                                                                                           ".//*[@class='input1']")
        for ch in checkboxes:
            ch.click()
        return self

    def find_test_element(self, locator_type, selector):
        logging.info("Find element By ")
        result = Context().set_strategy(self.driver, locator_type).execute_strategy(selector)
        assert result == True

    def close(self):
        self.driver.quit()
