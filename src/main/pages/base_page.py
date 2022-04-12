from selenium.webdriver.common.alert import Alert


class BasePage(object):
    mainPageUrl = 'https://sha-test-app.herokuapp.com/'
    callbackTestPageUrl = 'https://mdn.github.io/web-components-examples/life-cycle-callbacks/'
    testEnvPageUrl = 'https://elenastepuro.github.io/test_env/index.html'

    def __init__(self, driver):
        self.driver = driver

    def confirm_alert(self):
        Alert(self.driver).accept()

