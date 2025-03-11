from selenium.webdriver.common.by import By
from utils.driver_factory import get_driver


class BasePage:
    def __init__(self):
        self.driver = get_driver("chrome")


    def find_element(self, by, value):
        return self.driver.find_element(by, value)