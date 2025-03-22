from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LogoutPage(BasePage):

    _account_logout_header = (By.XPATH, "//span[contains(text(), 'Account Logout')]")
    _continue_button = (By.XPATH, "//a[@title='Continue']")

    def get_account_logout_header_text(self):
        return self.get_text(*self._account_logout_header)

    def click_continue(self):
        self.click(self._continue_button)

