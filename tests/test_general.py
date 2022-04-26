from src.main.pages.testenv_page import TestEnvPage


class TestGeneral:

    def test_select_checkboxes(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.select_checkboxes()
        test_page.click_form_submit_btn()
        test_page.select_checkboxes()  # should be healed

        test_page.close()
