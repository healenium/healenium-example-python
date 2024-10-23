from src.main.pages.testenv_page import TestEnvPage


class TestWait:

    def test_conditional_wait(self):
        test_page = TestEnvPage()

        test_page.open_browser()
        test_page.click_wait_btn()
        test_page.execute_script("disable_healing_true")
        test_page.click_test_button_wait()
        test_page.execute_script("disable_healing_false")

        test_page.close()
