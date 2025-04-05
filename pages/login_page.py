from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    _continue_button = (By.XPATH, "//button[@title='Continue']")
    _login_name_input = (By.ID, "loginFrm_loginname")
    _password_input = (By.ID, "loginFrm_password")
    _login_button = (By.XPATH, "//button[@title='Login']")
    _invalid_login_message = (By.XPATH, "//div[@class='alert alert-error alert-danger']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_continue(self):
        self.click(self._continue_button)

    def login_to_account(self, login_name, password):
        self.send_keys(*self._login_name_input, login_name)
        self.send_keys(*self._password_input, password)
        self.click(self._login_button)

    def get_invalid_login_message(self):
        return self.get_text(*self._invalid_login_message)
