
import unittest
import time
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
    first_name = "Pat"
    last_name = "Kat"
    email = "123@123.pl"
    telephone = "123123123"
    fax = "123123123"

    @classmethod
    def setUpClass(cls):
        browser = Config.get_browser()
        cls.driver = get_driver(browser)
        cls.driver.get(Config.get_base_url())
        cls.home_page = HomePage(cls.driver)
        cls.register_page = RegisterUserPage(cls.driver)
        cls.login_page = LoginPage(cls.driver)
        cls.register_success_page = RegisterSuccessPage(cls.driver)
        cls.logout_page = LogoutPage(cls.driver)
        cls.my_account_page = MyAccountPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # tc 1
    def test_register_user_with_valid_data(self):

        helper_tool = HelperTools()

        generated_data = helper_tool.register_user_data_generator()
        helper_tool.save_test_data_to_json(generated_data)

        user_data = helper_tool.get_last_saved_data()


        # define data for test
        address1 = "Krucza 1/2"
        address2 = "apartament 5"
        city = "Warsaw"
        region = "Mazowieckie"
        zipcode = "01-100"
        country = "Poland"

        # define expected results for assertion
        expected_success_register_text = "YOUR ACCOUNT HAS BEEN CREATED!"
        expected_logout_header_text = 'LOGOUT PAGE'

        self.home_page.go_to_login_page()
        self.login_page.click_continue()
        self.register_page.input_personal_details(
            user_data["first_name"],
            user_data["last_name"],
            user_data["email"],
            user_data["telephone"],
            user_data["fax"]
        )


        self.register_page.input_address(
            company="company",
            address1=address1,
            address2=address2,
            city=city,
            country=country,
            region=region,
            zipcode=zipcode
        )

        self.register_page.login_details(
            login_name=user_data["login_name"],
            password=user_data["password"],
            confirm_password=user_data["password"]
        )

        self.register_page.newsletter_and_privacy_policy(
            subscribe=True,
            privacy_policy=True
        )

        self.register_page.click_continue()

        actual_success_register_text = self.register_success_page.get_register_success_header_text()
        self.assertIn(expected_success_register_text, actual_success_register_text)

        self.register_success_page.click_continue_button()

        self.my_account_page.logout_from_my_account_box()
        self.logout_page.click_continue()
        self.home_page.go_to_login_page()

    #    actual_logout_header_text = self.logout_page.get_account_logout_header_text()
     #   self.assertIn(expected_logout_header_text, actual_logout_header_text)

        self.login_page.login_to_account(user_data["login_name"], user_data["password"])
