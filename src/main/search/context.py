from src.main.constants.locator_type import LocatorType
from src.main.search.locators.class_name_strategy import ClassNameStrategy
from src.main.search.locators.css_strategy import CssStrategy
from src.main.search.locators.id_strategy import IdStrategy
from src.main.search.locators.link_text_strategy import LinkTextStrategy
from src.main.search.locators.name_strategy import NameStrategy
from src.main.search.locators.partial_link_text_strategy import PartialLinkTextStrategy
from src.main.search.locators.tag_strategy import TagStrategy
from src.main.search.locators.xpath_strategy import XpathStrategy
from src.main.search.strategy import Strategy


class Context:
    strategy: Strategy

    def set_strategy(self, driver, locator_type):
        if locator_type == LocatorType.class_name:
            self.strategy = ClassNameStrategy(driver)
        if locator_type == LocatorType.xpath:
            self.strategy = XpathStrategy(driver)
        if locator_type == LocatorType.css:
            self.strategy = CssStrategy(driver)
        if locator_type == LocatorType.name:
            self.strategy = NameStrategy(driver)
        if locator_type == LocatorType.tag:
            self.strategy = TagStrategy(driver)
        if locator_type == LocatorType.partial_link_text:
            self.strategy = PartialLinkTextStrategy(driver)
        if locator_type == LocatorType.link_text:
            self.strategy = LinkTextStrategy(driver)
        if locator_type == LocatorType.id:
            self.strategy = IdStrategy(driver)

        return self

    def execute_strategy(self, selector):
        return self.strategy.do_action(selector)
