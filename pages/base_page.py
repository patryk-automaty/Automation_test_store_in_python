from utils.driver_factory import get_driver

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def click(self, locator):
        self.find_element(*locator).click()

    def send_keys(self, by, value, text):
        self.find_element(by, value).send_keys(text)

    def get_text(self, by, value):
        return self.find_element(by, value).text