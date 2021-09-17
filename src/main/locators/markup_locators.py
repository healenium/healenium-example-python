
class Locators(object):
    # by id
    generate_markup_btn_id = 'markup-generation-button'
    test_generated_button = 'random-id'
    # by class name
    test_button = 'default-btn'

    # by xpath
    checkbox_account = '//*[@class="checkbox checkbox_size_m checkbox_theme_alfa-on-white"]'
    text_first_select = '(//*[text()="Select Account"])[1]'
    text_second_select = '(//*[text()="Select Account"])[2]'

from selenium.webdriver.common.by import By
class Locators_By(object):
    generate_markup_btn_id=(By.ID, 'markup-generation-button')
    test_button=(By.XPATH, '//button[contains(@class,"default-btn")]')

    button_invisible=(By.ID,'for-invisible-test')
    field_parent=(By.ID,'field-parent')

class Locators_Request(object):
    generate_markup_btn_id = {'by': By.ID, 'value': 'markup-generation-button'}
    test_generated_button = {'by': By.ID, 'value': 'random-id'}
    test_button = {'by': By.CLASS_NAME, 'value': 'default-btn'}