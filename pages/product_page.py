from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):


    _product_list = (By.XPATH, "//div[@class='fixed']/a[@class='prdocutname']")
    _product_details_quantity = (By.ID, "product_quantity")
    _product_details_add_to_cart_button = (By.XPATH, "//ul[@class='productpagecart']")

    def open_product_details(self, product_name):
        products = self.find_elements(*self._product_list)
        for product in products:
            if product.text.strip() == str(product_name).upper():
                product.click()
                break

    def change_quantity(self, quantity):
        self.clear_input(self._product_details_quantity)
        self.send_keys(*self._product_details_quantity, quantity)

    def add_to_cart_from_product_details(self):
        self.click(self._product_details_add_to_cart_button)


