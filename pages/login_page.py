from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    _continue_button = (By.XPATH, "//button[@title='Continue']")


    def __init__(self, driver):
        super().__init__(driver)

    def click_continue(self):
        self.click(self._continue_button)

