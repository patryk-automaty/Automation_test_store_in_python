from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SuccessOrderPage(BasePage):

    _success_order_page_header = (By.XPATH, "//span[@class='maintext']")


    def get_success_order_message(self):
        return self.find_element(*self._success_order_page_header).text