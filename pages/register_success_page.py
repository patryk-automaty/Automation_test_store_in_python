from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterSuccessPage(BasePage):

    _register_success_header = (By.XPATH, "//h1/span[contains(text(), 'Your Account Has Been Created')]")
    _contact_us_link = (By.XPATH, "//a[text()='contact us']")
    _continue_button = (By.XPATH, "//a[@title='Continue']")


    def get_register_success_header_text(self):
        return self.get_text(*self._register_success_header)

    def click_contact_us_link(self):
        self.click(self._contact_us_link)

    def click_continue_button(self):
        self.click(self._continue_button)

