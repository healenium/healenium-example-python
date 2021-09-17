from src.main.pages.markup_page import *
from test_base import Test_Base


class Test_Markup(Test_Base):

# Markup_Page: different locator types with string property
    def test_button_click_specific_find_element(self, setup_method):
        main_page = Markup_Page(self.driver)

        main_page.open_browser()
        main_page.click_test_button()
        main_page.confirm_alert()

        main_page.generate_markup()
        main_page.click_test_button() #should be healed
        main_page.confirm_alert()

    def test_select_checkboxes(self, setup_method):
        main_page = Markup_Page(self.driver)
        main_page.open_browser().generate_markup()

        while main_page.displayed_text() != True:
            main_page.generate_markup()

        for i in [0,1,2,3,4,5]:
            main_page.select_first_checkbox() #should be healed

        result = main_page.verify_first_checkbox() #should be healed
        assert result == True

    def test_ButtonClickWithId(self, setup_method):
        main_page = Markup_Page(self.driver)

        main_page.open_browser().click_test_button()
        main_page.confirm_alert()

        while main_page.test_button_id_enabled()!=True:
            main_page.generate_markup()

        for i in [0,1,2]:
            main_page.click_test_generated_button() #should be healed
            main_page.confirm_alert()
            main_page.generate_markup()

# Markup_Page_By: different locator types with By in property
    def test_button_click_find_by(self, setup_method):
        markup_page_by=Markup_Page_By(self.driver)

        markup_page_by.open_browser()
        markup_page_by.click_button_for_invisible()
        invisible = markup_page_by.check_that_button_invisible()

        markup_page_by.open_browser()
        markup_page_by.click_test_button()
        markup_page_by.confirm_alert()

        markup_page_by.generate_markup()
        markup_page_by.click_test_button() #should be healed
        markup_page_by.confirm_alert()

# Markup_Page_Request: different locator types with By in request
    def test_button_click_find_request(self, setup_method):
        markup_page_request=Markup_Page_Request(self.driver)

        markup_page_request.open_browser()
        markup_page_request.click_test_button()
        markup_page_request.confirm_alert()

        markup_page_request.generate_markup()
        markup_page_request.click_test_button() #should be healed
        markup_page_request.confirm_alert()