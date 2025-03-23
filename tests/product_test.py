import time
import unittest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from pages.register_user_page import RegisterUserPage
from pages.register_success_page import RegisterSuccessPage
from pages.logout_page import LogoutPage
from pages.product_page import ProductPage
from utils.config import Config
from utils.driver_factory import get_driver
from utils.helper_tools import HelperTools


class RegisterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = Config.get_browser() # Get browser type from configuration
        cls.driver = get_driver(browser) # Initialize WebDriver
        cls.driver.get(Config.get_base_url()) # Open the base url from config

        # Initialize page objects
        cls.home_page = HomePage(cls.driver)
        cls.register_page = RegisterUserPage(cls.driver)
        cls.login_page = LoginPage(cls.driver)
        cls.register_success_page = RegisterSuccessPage(cls.driver)
        cls.logout_page = LogoutPage(cls.driver)
        cls.my_account_page = MyAccountPage(cls.driver)
        cls.product_page = ProductPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit() # close the browser session

    # tc 3
    def test_add_product_to_shopping_cart(self):

        # Navigate to the fragrance page
        self.home_page.choose_category_from_subnav("FRAGRANCE")
        # Click on the product name to open the product details page
        self.product_page.open_product_details("Acqua Di Gio Pour Homme")
        # Select a quantity (if applicable).
        self.product_page.change_quantity("3")
        # Click on "Add to Cart"
        self.product_page.add_to_cart_from_product_details()
        # Verify that shopping cart is open

        # Verify that the correct product name, price, and quantity are displayed