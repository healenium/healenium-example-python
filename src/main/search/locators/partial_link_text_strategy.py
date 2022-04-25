from selenium import webdriver
from selenium.webdriver.common.by import By

from src.main.search.strategy import Strategy


class PartialLinkTextStrategy(Strategy):
    driver: webdriver

    def __init__(self, driver1):
        self.driver = driver1

    def do_action(self, selector) -> str:
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, selector)
        return element.is_displayed()
