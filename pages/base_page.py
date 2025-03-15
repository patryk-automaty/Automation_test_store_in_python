from selenium.webdriver.support.select import Select

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

    def select(self, by, value, selection_type="text"):

        element = self.find_element(by, value)
        select_element = Select(element)

        if selection_type == "text":
            select_element.select_by_visible_text(value)  # Select by option text
        elif selection_type == "value":
            select_element.select_by_value(value)  # Select by option value attribute
        elif selection_type == "index":
            select_element.select_by_index(int(value))  # Select by option index
        else:
            raise ValueError("Invalid selection_type. Use 'text', 'value', or 'index'.")
