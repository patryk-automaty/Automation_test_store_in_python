import unittest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_user_page import RegisterUserPage
from pages.logout_page import LogoutPage
from pages.product_page import ProductPage
from pages.wishlist_page import WishlistPage
from pages.my_account_page import MyAccountPage
from utils.config import Config
from utils.driver_factory import get_driver
from utils.helper_tools import HelperTools


class RegisterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setup WebDriver
        browser = Config.get_browser()
        cls.driver = get_driver(browser)
        cls.driver.get(Config.get_base_url())

        # Initialize only needed page objects
        cls.home_page = HomePage(cls.driver)
        cls.register_page = RegisterUserPage(cls.driver)
        cls.login_page = LoginPage(cls.driver)
        cls.logout_page = LogoutPage(cls.driver)
        cls.my_account_page = MyAccountPage(cls.driver)
        cls.product_page = ProductPage(cls.driver)
        cls.wishlist_page = WishlistPage(cls.driver)
        cls.helper_tool = HelperTools()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # tc 8
    def test_wishlist_func(self):


        # Get test user data
        user_data = self.helper_tool.get_last_saved_data()
        login = user_data["login_name"]
        password = user_data["password"]

        # Test data
        category = "SKINCARE"
        product_name = "Total Moisture Facial Cream"

        # Log in
        self.home_page.go_to_login_page()
        self.login_page.login_to_account(login, password)

        # Go to product and add to wishlist
        self.home_page.choose_category_from_subnav(category)
        self.product_page.open_product_details(product_name)
        self.product_page.add_product_to_wishlist()

        # Go to wishlist
        self.home_page.go_to_account_page()
        self.my_account_page.wishlist_from_my_account_box()

        # Assert product is in wishlist

        self.assertTrue(
            self.wishlist_page.get_product_name().is_displayed(),
            "Expected product to be visible in the wishlist"
        )

        # Remove product and assert it's gone
        self.wishlist_page.remove_product()
        self.assertFalse(
            self.wishlist_page.get_product_name().is_displayed(),
            "Expected wishlist to be empty after removing the product"
        )

    # tc 9

    def test_newsletter_sub(self):

        # Get test user data
        user_data = self.helper_tool.get_last_saved_data()
        login = user_data["login_name"]
        password = user_data["password"]
        email = user_data["email"]

        # Expected results to assertion
        expected_notification_page_header = "NOTIFICATIONS AND NEWSLETTER"
        expected_success_message = "Success: Your notification settings has been successfully updated!"
        # Log in
        self.home_page.go_to_login_page()
        self.login_page.login_to_account(login, password)

        # Enter a valid email address and click on the Subscribe button.
        self.home_page.subscribe_newsletter(email)

        # Verify that the Notifications and Newsletter page is displayed
        actual_notification_page_header = self.my_account_page.get_notification_tab_header().text
        self.assertIn(expected_notification_page_header, actual_notification_page_header)

        # Verify that the Newsletters checkbox is checked.
        self.assertTrue(self.my_account_page.is_newsletter_checkbox_selected())
        # Click on the Continue button.
        self.my_account_page.click_continue()
        # Verify that a success message appears confirming the subscription.
        actual_success_message = self.my_account_page.get_success_notification_message().text
        self.assertIn(expected_success_message, actual_success_message)

