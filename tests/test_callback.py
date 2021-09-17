from src.main.pages.callback_page import Callback_Page
from test_base import Test_Base


class Test_Callback(Test_Base):

    def test_element_from_shadow_root(self, setup_method):
        callback_page=Callback_Page(self.driver)

        callback_page.open_browser()
        callback_page.click_add_square_button()
        result = callback_page.verify_shadow_element()
        assert result == True

        callback_page.click_update_square_button()
        result = callback_page.verify_shadow_element() #should be healed
        assert result == True

    def test_css_locators(self, setup_method):
        callback_page=Callback_Page(self.driver)

        callback_page.open_browser()
        callback_page.click_add_square_button()
        result = callback_page.verify_square_element()
        assert result==True

        callback_page.click_update_square_button()
        result = callback_page.verify_square_element() #should be healed
        assert result == True