import pytest
import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.config import Config
from utils.driver_factory import get_driver
from utils.helper_tools import HelperTools


@pytest.fixture(scope="function")
def setup_class_fixture(request):
    browser = Config.get_browser()
    driver = get_driver(browser)
    driver.get(Config.get_base_url())

    # Page objects
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    helper_tools = HelperTools()


    request.cls.driver = driver
    request.cls.home_page = home_page
    request.cls.login_page = login_page
    request.cls.helper_tools = helper_tools

    yield

    driver.quit()


@allure.suite("Login Suite")
@pytest.mark.usefixtures("setup_class_fixture")
class TestLogin:

    driver: WebDriver
    home_page: HomePage
    login_page: LoginPage
    helper_tools: HelperTools

    @allure.title("Verify Login with Invalid Credentials")
    @allure.description("Ensure an error message appears when logging in with incorrect credentials.")
    def test_login_with_invalid_credentials(self):
        test_name = "test_login_with_invalid_credentials"
        wrong_login = "invalid_email1111@example.com"
        wrong_password = "WrongPassword123"
        second_wrong_password = "WrongPassword321"
        expected_invalid_login_message = "Error: Incorrect login or password provided."

        with allure.step("Navigate to the login page"):
            self.home_page.go_to_login_page()
            self.helper_tools.take_screenshot(self.driver, test_name)

        with allure.step("Enter invalid credentials and attempt login"):
            self.login_page.login_to_account(wrong_login, wrong_password)
            self.helper_tools.take_screenshot(self.driver, test_name)

        with allure.step("Verify error message appears"):
            actual_invalid_login_message = self.login_page.get_invalid_login_message()
            assert expected_invalid_login_message in actual_invalid_login_message
            self.helper_tools.take_screenshot(self.driver, test_name)

        with allure.step("Try again with different invalid password"):
            self.login_page.login_to_account(wrong_login, second_wrong_password)
            self.helper_tools.take_screenshot(self.driver, test_name)

        with allure.step("Verify login still fails"):
            actual_invalid_login_message = self.login_page.get_invalid_login_message()
            assert expected_invalid_login_message in actual_invalid_login_message
            self.helper_tools.take_screenshot(self.driver, test_name)
