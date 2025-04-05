from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):

    _shipping_address = (By.XPATH, "//table[@class='table confirm_shippment_options']//td/address")
    _payment_address = (By.XPATH, "//table[@class='table confirm_payment_options']//td/address")
    _confirm_order_button = (By.ID, "checkout_btn")

    def shipping_address(self):
        return self.find_element(*self._shipping_address)

    def payment_address(self):
        return self.find_element(*self._payment_address)

    def click_confirm(self):
        self.click(self._confirm_order_button)