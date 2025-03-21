from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    # Locators to the home page
    _login_register_navbar = (By.ID, "customer_menu_top")
    _specials_navbar = (By.XPATH, "//div[@id='topnav']//li[@data-id='menu_specials']")
    _account_navbar = (By.XPATH, "//div[@id='topnav']//li[@data-id='menu_account']")
    _cart_navbar = (By.XPATH, "//div[@id='topnav']//li[@data-id='menu_account']")
    _checkout_navbar = (By.XPATH, "//div[@id='topnav']//li[@data-id='menu_checkout']")
    _logout_navbar = (By.XPATH, "//ul[@id='main_menu']//span[(@class='menu_text') and (text()='Logout')]")

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_login_page(self):
        self.click(self._login_register_navbar)

    def logout_from_navbar(self):
        self.click(self._logout_navbar)

    def hover_account_tab(self):
        self.hover(*self._account_navbar)


