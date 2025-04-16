import unittest
import allure
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.config import Config
from utils.driver_factory import get_driver
from utils.helper_tools import HelperTools

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = Config.get_browser()  # Get browser type from configuration
        cls.driver = get_driver(browser)  # Initialize WebDriver
        cls.driver.get(Config.get_base_url())  # Open the base url from config

        # Initialize page objects
        cls.home_page = HomePage(cls.driver)
        cls.login_page = LoginPage(cls.driver)
        cls.helper_tools = HelperTools()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # close the browser session

    @allure.title("Verify Login with Invalid Credentials")
    @allure.description("Ensure an error message appears when logging in with incorrect credentials.")
    def test_login_with_invalid_credentials(self):
        test_name = "test_login_with_invalid_credentials"
        wrong_login = "invalid_email1111@example.com"
        wrong_password = "WrongPassword123"
        second_wrong_password = "WrongPassword321"

        with allure.step("Navigate to the login page"):
            self.home_page.go_to_login_page()
            self.helper_tools.take_screenshot(self.driver, test_name)

        with allure.step("Enter invalid credentials and attempt login"):
            self.login_page.login_to_account(wrong_login, wrong_password)
            self.helper_tools.take_screenshot(self.driver, test_name)

        with allure.step("Verify that an error message appears stating 'Invalid login credentials'"):
            expected_invalid_login_message = "Error: Incorrect login or password provided."
            actual_invalid_login_message = self.login_page.get_invalid_login_message()
            self.assertIn(expected_invalid_login_message, actual_invalid_login_message)
            self.helper_tools.take_screenshot(self.driver, test_name)

        with allure.step("Try logging in again using another incorrect password'"):
            self.login_page.login_to_account(wrong_login, second_wrong_password)
            self.helper_tools.take_screenshot(self.driver, test_name)

        with allure.step("Verify that the login attempt still fails"):
            self.assertIn(expected_invalid_login_message, actual_invalid_login_message)
            self.helper_tools.take_screenshot(self.driver, test_name)



