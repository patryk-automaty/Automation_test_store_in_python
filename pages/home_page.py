from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    # Locators to the home page
    _login_register_navbar = (By.ID, "customer_menu_top")
    _specials_navbar = (By.XPATH, "//div[@id='topnav']//li[@data-id='menu_specials']")
    _account_navbar = (By.XPATH, "//div[@id='topnav']//li[@data-id='menu_account']")
    _cart_navbar = (By.XPATH, "//div[@id='topnav']//li[@data-id='menu_account']")
    _checkout_navbar = (By.XPATH, "//div[@id='topnav']//li[@data-id='menu_checkout']")

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_login_page(self):
        self.click(self._login_register_navbar)


