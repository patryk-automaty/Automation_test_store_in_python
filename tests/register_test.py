import unittest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_user_page import RegisterUserPage
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

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_user_with_valid_data(self):

        helper_tool = HelperTools()


        generated_data = helper_tool.register_user_data_generator()
        helper_tool.save_test_data_to_json(generated_data)


        user_data = helper_tool.get_last_saved_data()

        self.home_page.go_to_login_page()
        self.login_page.click_continue()
        self.register_page.input_personal_details(
            user_data["first_name"],
            user_data["last_name"],
            user_data["email"],
            user_data["telephone"],
            user_data["fax"]
        )
