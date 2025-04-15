import unittest

import allure

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.config import Config
from utils.driver_factory import get_driver



class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = Config.get_browser()  # Get browser type from configuration
        cls.driver = get_driver(browser)  # Initialize WebDriver
        cls.driver.get(Config.get_base_url())  # Open the base url from config

        # Initialize page objects
        cls.home_page = HomePage(cls.driver)
        cls.login_page = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # close the browser session

    @allure.title("Verify Login with Invalid Credentials")
    @allure.description("Ensure an error message appears when logging in with incorrect credentials.")
    def test_login_with_invalid_credentials(self):
        wrong_login = "invalid_email1111@example.com"
        wrong_password = "WrongPassword123"
        second_wrong_password = "WrongPassword321"

        # Navigate to the Login page
        self.home_page.go_to_login_page()

        # Enter invalid login, password and click login
        self.login_page.login_to_account(wrong_login, wrong_password)


        # Verify that an error message appears stating "Invalid login credentials"
        expected_invalid_login_message = "Error: Incorrect login or password provided."
        actual_invalid_login_message = self.login_page.get_invalid_login_message()
        self.assertIn(expected_invalid_login_message, actual_invalid_login_message)

        # Try logging in again using another incorrect password
        self.login_page.login_to_account(wrong_login, second_wrong_password)

        # Verify that the login attempt still fails
        self.assertIn(expected_invalid_login_message, actual_invalid_login_message)


