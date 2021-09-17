class Base_Page(object):
    mainPageUrl = 'https://sha-test-app.herokuapp.com/'
    callbackTestPageUrl = 'https://mdn.github.io/web-components-examples/life-cycle-callbacks/'

    def __init__(self, driver):
        self.driver = driver

    def confirm_alert(self):
        allert = self.driver.switch_to_alert()
        allert.accept()
