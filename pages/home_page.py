import random

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    # Locators to the home page
    _login_register_navbar = (By.ID, "customer_menu_top")
    _specials_navbar = (By.XPATH, "//div[@id='topnav']//li[@data-id='menu_specials']")
    _account_navbar = (By.XPATH, "//div[@id='topnav']//li[@data-id='menu_account']")
    _cart_navbar = (By.XPATH, "//div[@id='topnav']//li[@data-id='menu_cart']")
    _checkout_navbar = (By.XPATH, "//div[@id='topnav']//li[@data-id='menu_checkout']")
    _logout_navbar = (By.XPATH, "//ul[@id='main_menu']//span[(@class='menu_text') and (text()='Logout')]")
    _subnav_list = (By.XPATH, "//ul[@class='nav-pills categorymenu']/li/a")
    _add_product = (By.XPATH, "//i[@class='fa fa-cart-plus fa-fw']")
    _go_to_home_page = (By.XPATH, "//img[@title='Automation Test Store']")
    _search_bar = (By.ID, "filter_keyword")
    _search_perform = (By.XPATH, "//div[@title='Go']")
    _account_menu = (By.ID, "customer_menu_top")
    _dropdown_item_from_account_menu = (By.CSS_SELECTOR, "//li[@class='dropdown']/a")
    _subscribe_nl_input = (By.ID, "appendedInputButton")
    _subscribe_button = (By.XPATH, "//button[text()='Subscribe']")

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_login_page(self):
        self.click(self._login_register_navbar)

    def logout_from_navbar(self):
        self.click(self._logout_navbar)

    def choose_category_from_subnav(self, category_name):
        categories = self.find_elements(*self._subnav_list)

        for category in categories:
            if category.text.strip() == category_name:
                category.click()
                break

    def add_random_product(self):
        products = self.find_elements(*self._add_product)
        random_product = random.choice(products)
        random_product.click()

    def go_to_shopping_cart(self):
        self.click(self._cart_navbar)

    def go_to_home_page(self):
        self.click(self._go_to_home_page)

    def search_product(self, search_input):
        self.send_keys(*self._search_bar, search_input)
        self.click(self._search_perform)

    # to fix
    def choose_dropdown_option_from_account_menu(self, option_text):

        account_menu_element = self.find_element(*self._account_menu)
        dropdown_items = self._dropdown_item_from_account_menu

        ActionChains(self.driver).move_to_element(account_menu_element).perform()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".sub_menu.dropdown-menu li a"))
        )

        for item in dropdown_items:
            item_text = item.strip()
            if option_text.lower() in item_text.lower():
                item.click()
                return

    def go_to_account_page(self):
        self.click(self._account_navbar)

    def subscribe_newsletter(self, email):
        self.send_keys(*self._subscribe_nl_input, email)
        self.click(self._subscribe_button)