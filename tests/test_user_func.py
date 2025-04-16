import unittest

import allure

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
    @allure.title("Verify Newsletter Subscription")
    @allure.description("Ensure that users can subscribe to the newsletter.")
    def test_newsletter_sub(self):
        test_name = "test_newsletter_sub"
        user_data = self.helper_tool.get_last_saved_data()
        login = user_data["login_name"]
        password = user_data["password"]
        email = user_data["email"]

        expected_notification_page_header = "NOTIFICATIONS AND NEWSLETTER"
        expected_success_message = "Success: Your notification settings has been successfully updated!"

        with allure.step("Log in with registered credentials"):
            self.home_page.go_to_login_page()
            self.login_page.login_to_account(login, password)
            self.helper_tool.take_screenshot(self.driver, test_name)

        with allure.step("Enter email and subscribe to newsletter"):
            self.home_page.subscribe_newsletter(email)
            self.helper_tool.take_screenshot(self.driver, test_name)

        with allure.step("Verify Notifications and Newsletter page is displayed"):
            actual_notification_page_header = self.my_account_page.get_notification_tab_header().text
            self.assertIn(expected_notification_page_header, actual_notification_page_header)

        with allure.step("Verify that the newsletter checkbox is selected"):
            self.assertTrue(self.my_account_page.is_newsletter_checkbox_selected())

        with allure.step("Click Continue and check success message"):
            self.my_account_page.click_continue()
            actual_success_message = self.my_account_page.get_success_notification_message().text
            self.assertIn(expected_success_message, actual_success_message)
