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
from pages.checkout_confirmation_page import CheckoutPage
from pages.success_order_page import SuccessOrderPage
from pages.search_page import SearchPage
from pages.product_details_page import ProductDetailsPage
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
        cls.checkout_page = CheckoutPage(cls.driver)
        cls.success_order_page = SuccessOrderPage(cls.driver)
        cls.search_page = SearchPage(cls.driver)
        cls.product_details_page = ProductDetailsPage(cls.driver)
        cls.helper_tool = HelperTools()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit() # close the browser session


    def test_wishlist_func(self):
        # Retrieve the last saved data
        user_data = self.helper_tool.get_last_saved_data()

        login = user_data["login_name"]
        password = user_data["password"]
        category = "SKINCARE"
        product_name = "Total Moisture Facial Cream"

        # Login to a registered account.
        self.home_page.go_to_login_page()
        self.login_page.login_to_account(login, password)
        # Navigate to a product category
        self.home_page.choose_category_from_subnav(category)
        self.product_page.open_product_details(product_name)
        # Click on the "Add to Wishlist" button for a product
        self.product_page.add_product_to_wishlist()
        # Navigate to the Wishlist page
        self.home_page.go_to_account_page()
        self.my_account_page.wishlist_from_my_account_box()
        # Verify that the product appears in the wishlist
        # Click on the Remove button to delete the product from the wishlist
        # Verify that the wishlist is now empty
