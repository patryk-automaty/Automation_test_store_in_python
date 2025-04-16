
import unittest

import allure

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from pages.register_user_page import RegisterUserPage
from pages.register_success_page import RegisterSuccessPage
from pages.logout_page import LogoutPage
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
        cls.helper_tool = HelperTools()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit() # close the browser session

    # tc 1
    @allure.title("Verify User Registration with Valid Data")
    @allure.description("Ensure a user can successfully register with valid details.")
    def test_register_user_with_valid_data(self):

        # Define test name to screenshots name
        test_name = "test_register_user_with_valid_data"

        # Generate and save test data
        generated_data = self.helper_tool.register_user_data_generator()
        self.helper_tool.save_test_data_to_json(generated_data)
        user_data = self.helper_tool.get_last_saved_data()

        # Set address details for the test"
        address1 = "Krucza 1/2"
        address2 = "apartament 5"
        city = "Warsaw"
        region = "Mazowieckie"
        zipcode = "01-100"
        country = "Poland"

        with allure.step("Navigate to login page and start registration"):
            self.home_page.go_to_login_page()
            self.login_page.click_continue()
            self.helper_tool.take_screenshot(self.driver, test_name)

        with allure.step("Input personal details"):
            self.register_page.input_personal_details(
                user_data["first_name"],
                user_data["last_name"],
                user_data["email"],
                user_data["telephone"],
                user_data["fax"]
            )
            self.helper_tool.take_screenshot(self.driver, test_name)

        with allure.step("Input address details"):
            self.register_page.input_address(
                company="company",
                address1=address1,
                address2=address2,
                city=city,
                country=country,
                region=region,
                zipcode=zipcode
            )
            self.helper_tool.take_screenshot(self.driver, test_name)

        with allure.step("Input login credentials"):
            self.register_page.login_details(
                login_name=user_data["login_name"],
                password=user_data["password"],
                confirm_password=user_data["password"]
            )
            self.helper_tool.take_screenshot(self.driver, test_name)

        with allure.step("Select newsletter subscription and agree to privacy policy"):
            self.register_page.newsletter_and_privacy_policy(
                subscribe=True,
                privacy_policy=True
            )
            self.helper_tool.take_screenshot(self.driver, test_name)

        with allure.step("Submit registration form"):
            self.register_page.click_continue()
            self.helper_tool.take_screenshot(self.driver, test_name)

        with allure.step("Verify success registration message"):
            expected_success_register_text = "YOUR ACCOUNT HAS BEEN CREATED!"
            actual_success_register_text = self.register_success_page.get_register_success_header_text()
            self.assertIn(expected_success_register_text, actual_success_register_text)

        with allure.step("Proceed to My Account page"):
            self.register_success_page.click_continue_button()
            self.helper_tool.take_screenshot(self.driver, test_name)

        with allure.step("Log out from account"):
            self.my_account_page.logout_from_my_account_box()
            self.helper_tool.take_screenshot(self.driver, test_name)

        with allure.step("Verify logout success message"):
            expected_logout_header_text = 'ACCOUNT LOGOUT'
            actual_logout_header_text = self.logout_page.get_account_logout_header_text()
            self.assertIn(expected_logout_header_text, actual_logout_header_text)

        with allure.step("Click continue after logout"):
            self.logout_page.click_continue()

        with allure.step("Login with the newly registered user"):
            self.home_page.go_to_login_page()
            self.login_page.login_to_account(user_data["login_name"], user_data["password"])
            self.helper_tool.take_screenshot(self.driver, test_name)

        with allure.step("Verify successful login to My Account page"):
            expected_my_account_header_text = 'MY ACCOUNT'
            actual_my_account_header_text = self.my_account_page.get_my_account_header_text()
            self.assertIn(expected_my_account_header_text, actual_my_account_header_text)
