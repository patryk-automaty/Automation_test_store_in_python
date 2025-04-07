from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class WishlistPage(BasePage):

    _product_name = (By.XPATH, "//td[@class='align_left']/a")
    _remove_button = (By.XPATH, "//a[@class='btn btn-sm btn-default btn-remove']")

    def get_product_name(self):
        return self.find_element(*self._product_name)

    def remove_product(self):
        self.click(self._remove_button)

