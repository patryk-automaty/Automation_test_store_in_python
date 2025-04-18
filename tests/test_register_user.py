
import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from pages.register_user_page import RegisterUserPage
from pages.register_success_page import RegisterSuccessPage
from pages.logout_page import LogoutPage
from utils.config import Config
from utils.driver_factory import get_driver
from utils.helper_tools import HelperTools

@pytest.fixture(scope="function")
def setup_class_fixture(request):
    browser = Config.get_browser()
    driver = get_driver(browser)
    driver.get(Config.get_base_url())

    # Page objects and helper tools
    home_page = HomePage(driver)
    register_page = RegisterUserPage(driver)
    login_page = LoginPage(driver)
    register_success_page = RegisterSuccessPage(driver)
    logout_page = LogoutPage(driver)
    my_account_page = MyAccountPage(driver)
    helper_tool = HelperTools()

    request.cls.driver = driver
    request.cls.home_page = home_page
    request.cls.register_page = register_page
    request.cls.login_page = login_page
    request.cls.register_success_page = register_success_page
    request.cls.logout_page = logout_page
    request.cls.my_account_page = my_account_page
    request.cls.helper_tool = helper_tool

    yield

    driver.quit()

@allure.suite("Register Suite")
@pytest.mark.usefixtures("setup_class_fixture")
class RegisterTest:
    helper_tool: HelperTools
    home_page: HomePage
    login_page: LoginPage
    driver: WebDriver
    register_page: RegisterUserPage
    register_success_page: RegisterSuccessPage
    my_account_page: MyAccountPage
    logout_page: LogoutPage

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

        # Set address details for the test
        address1 = "Krucza 1/2"
        address2 = "apartament 5"
        city = "Warsaw"
        region = "Mazowieckie"
        zipcode = "01-100"
        country = "Poland"

        # test data
        expected_success_register_text = "YOUR ACCOUNT HAS BEEN CREATED!"
        expected_logout_header_text = 'ACCOUNT LOGOUT'
        expected_my_account_header_text = 'MY ACCOUNT'

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
            actual_success_register_text = self.register_success_page.get_register_success_header_text()
            assert expected_success_register_text in actual_success_register_text
            self.helper_tool.take_screenshot(self.driver, test_name)

        with allure.step("Proceed to My Account page"):
            self.register_success_page.click_continue_button()
            self.helper_tool.take_screenshot(self.driver, test_name)

        with allure.step("Log out from account"):
            self.my_account_page.logout_from_my_account_box()
            self.helper_tool.take_screenshot(self.driver, test_name)

        with allure.step("Verify logout success message"):
            actual_logout_header_text = self.logout_page.get_account_logout_header_text()
            assert expected_logout_header_text in actual_logout_header_text
            self.helper_tool.take_screenshot(self.driver, test_name)

        with allure.step("Click continue after logout"):
            self.logout_page.click_continue()
            self.helper_tool.take_screenshot(self.driver, test_name)

        with allure.step("Login with the newly registered user"):
            self.home_page.go_to_login_page()
            self.login_page.login_to_account(user_data["login_name"], user_data["password"])
            self.helper_tool.take_screenshot(self.driver, test_name)

        with allure.step("Verify successful login to My Account page"):
            actual_my_account_header_text = self.my_account_page.get_my_account_header_text()
            assert expected_my_account_header_text in actual_my_account_header_text
            self.helper_tool.take_screenshot(self.driver, test_name)
