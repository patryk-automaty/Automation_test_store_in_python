import pytest
import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from utils.config import Config
from utils.driver_factory import get_driver
from utils.helper_tools import HelperTools


@pytest.fixture(scope="class")
def setup_class_fixture(request):
    browser = Config.get_browser()
    driver = get_driver(browser)
    driver.get(Config.get_base_url())

    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    my_account_page = MyAccountPage(driver)
    helper_tool = HelperTools()

    request.cls.driver = driver
    request.cls.home_page = home_page
    request.cls.login_page = login_page
    request.cls.my_account_page = my_account_page
    request.cls.helper_tool = helper_tool

    yield
    driver.quit()


@allure.suite("Newsletter Suite")
@pytest.mark.usefixtures("setup_class_fixture")
class TestNewsletter:

    driver: WebDriver
    home_page: HomePage
    login_page: LoginPage
    my_account_page: MyAccountPage
    helper_tool: HelperTools

    @allure.title("Verify Newsletter Subscription")
    @allure.description("Ensure that users can subscribe to the newsletter.")
    def test_newsletter_sub(self):
        test_name = "test_newsletter_sub"
        user_data = self.helper_tool.get_last_saved_data()
        login = user_data["login_name"]
        password = user_data["password"]
        email = user_data["email"]

        expected_header = "NOTIFICATIONS AND NEWSLETTER"
        expected_success = "Success: Your notification settings has been successfully updated!"

        with allure.step("Log in with registered credentials"):
            self.home_page.go_to_login_page()
            self.login_page.login_to_account(login, password)
            self.helper_tool.take_screenshot(self.driver, test_name)

        with allure.step("Enter email and subscribe to newsletter"):
            self.home_page.subscribe_newsletter(email)
            self.helper_tool.take_screenshot(self.driver, test_name)

        with allure.step("Verify that the Notifications and Newsletter page is displayed"):
            actual_header = self.my_account_page.get_notification_tab_header().text
            assert expected_header in actual_header

        with allure.step("Verify that the newsletter checkbox is selected"):
            assert self.my_account_page.is_newsletter_checkbox_selected()

        with allure.step("Click Continue and verify success message"):
            self.my_account_page.click_continue()
            actual_success = self.my_account_page.get_success_notification_message().text
            assert expected_success in actual_success
