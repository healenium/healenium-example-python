from src.main.constants.locator_type import LocatorType
from src.main.pages.testenv_page import TestEnvPage


class TestXpath:

    def test_xpath_special_character(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.find_test_element(LocatorType.xpath, "//*[@id='change:name']")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.xpath, "//*[@id='change:name']")

        test_page.close()

    def test_xpath_following(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.find_test_element(LocatorType.xpath, "//*[@id='change_className']/following::test_tag")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.xpath, "//*[@id='change_className']/following::test_tag")

        test_page.close()

    def test_xpath_contains(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.find_test_element(LocatorType.xpath, "//input[contains(@class, 'test')]")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.xpath, "//input[contains(@class, 'test')]")

        test_page.close()

    def test_xpath_not_contains(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.find_test_element(LocatorType.xpath, "//input[not(contains(@class, 'input1'))]")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.xpath, "//input[not(contains(@class, 'input1'))]")

        test_page.close()

    def test_xpath_following_sibling(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.find_test_element(LocatorType.xpath, "//*[starts-with(@class, 'test')]/following-sibling::*")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.xpath, "//*[starts-with(@class, 'test')]/following-sibling::*")

        test_page.close()

    def test_xpath_ancestor(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.find_test_element(LocatorType.xpath, "(//*[starts-with(@class, 'test')]/ancestor::div[@class='healenium-form validate-form']//input)[1]")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.xpath, "(//*[starts-with(@class, 'test')]/ancestor::div[@class='healenium-form validate-form']//input)[1]")

        test_page.close()

    def test_xpath_or(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.find_test_element(LocatorType.xpath, "//*[@id='change_id' or @id='omg']")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.xpath, "//*[@id='change_id' or @id='omg']")

        test_page.close()

    def test_xpath_and(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.find_test_element(LocatorType.xpath, "//*[@id='change_id' and @type='text']")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.xpath, "//*[@id='change_id' and @type='text']")

        test_page.close()

    def test_xpath_starts_with(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.find_test_element(LocatorType.xpath, "//*[starts-with(@class, 'test')]")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.xpath, "//*[starts-with(@class, 'test')]")

        test_page.close()

    def test_xpath_precending(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.find_test_element(LocatorType.xpath, "//*[@id='change_className']/preceding::*[@id='change_id']")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.xpath, "//*[@id='change_className']/preceding::*[@id='change_id']")

        test_page.close()

    def test_xpath_descendant(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.find_test_element(LocatorType.xpath, "//*[@id='descendant_change']/descendant::input")
        test_page.click_submit_btn()
        test_page.find_test_element(LocatorType.xpath, "//*[@id='descendant_change']/descendant::input")

        test_page.close()
