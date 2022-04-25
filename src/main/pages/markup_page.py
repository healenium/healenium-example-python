from src.main.pages.base_page import BasePage


class MarkupPage(BasePage):

    # by id
    generate_markup_btn_id = 'markup-generation-button'
    # by class name
    test_button = 'default-btn'

    def open_browser(self):
        self.driver.get(BasePage.mainPageUrl)
        return self

    def generate_markup(self):
        generate_markup = self.driver.find_element_by_id(self.generate_markup_btn_id)
        generate_markup.click()
        return self

    def click_test_button(self):
        self.driver.find_element_by_class_name(self.test_button).click()
