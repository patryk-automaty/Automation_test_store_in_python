from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductDetailsPage(BasePage):

    _product_name = (By.XPATH, "//span[@class='bgnone']")

    def get_product_name(self):
        return self.find_element(*self._product_name).text