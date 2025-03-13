from selenium.webdriver.common.by import By
from utils.driver_factory import get_driver


class BasePage:
    def __init__(self):
        self.driver = get_driver("chrome")


    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def click(self, by, value):
        element = self.driver.find_element(by, value)
        element.click()

    def send_keys(self, by, value, text):
        element = self.driver.find_element(by, value)
        element.send_keys(text)

    def get_text(self, by, value):
        element = self.driver.find_element(by, value)
        return element.text
