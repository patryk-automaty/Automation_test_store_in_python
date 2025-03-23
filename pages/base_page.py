from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from utils.driver_factory import get_driver

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    def find_element(self, by, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, locator)))

    def find_elements(self, by, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((by, locator)))

    def click(self, locator):
        self.find_element(*locator).click()

    def send_keys(self, by, value, text):
        self.find_element(by, value).send_keys(text)

    def get_text(self, by, value):
        return self.find_element(by, value).text

    def select(self, by, locator, value, selection_type="index"):

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, locator)))
        select_element = Select(element)

        if selection_type == "text":
            select_element.select_by_visible_text(value)  # Select by option text
        elif selection_type == "value":
            select_element.select_by_value(value)  # Select by option value attribute
        elif selection_type == "index":
            select_element.select_by_index(int(value))  # Select by option index
        else:
            raise ValueError("Invalid selection_type. Use 'text', 'value', or 'index'.")

    def hover_and_choose(self, locator, dropdown_option_locator):
        self.actions.move_to_element(locator).perform()
        dropdown_option = self.find_element(*dropdown_option_locator)
        dropdown_option.click()

    def clear_input(self, locator):
        self.find_element(*locator).clear()

