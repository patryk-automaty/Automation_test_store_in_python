import pytest
import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.checkout_confirmation_page import CheckoutPage
from pages.success_order_page import SuccessOrderPage
from pages.search_page import SearchPage
from pages.product_details_page import ProductDetailsPage
from utils.config import Config
from utils.driver_factory import get_driver
from utils.helper_tools import HelperTools

@pytest.fixture(scope="function")
def setup_class_fixture(request):
    browser = Config.get_browser()
    driver = get_driver(browser)
    driver.get(Config.get_base_url())

    request.cls.driver = driver
    request.cls.home_page = HomePage(driver)
    request.cls.login_page = LoginPage(driver)
    request.cls.product_page = ProductPage(driver)
    request.cls.checkout_page = CheckoutPage(driver)
    request.cls.success_order_page = SuccessOrderPage(driver)
    request.cls.search_page = SearchPage(driver)
    request.cls.product_details_page = ProductDetailsPage(driver)
    request.cls.helper_tools = HelperTools()
    yield
    driver.quit()

@allure.suite("Register Suite")
@pytest.mark.usefixtures("setup_class_fixture")
class TestProduct:

    driver: WebDriver
    home_page: HomePage
    login_page: LoginPage
    product_page: ProductPage
    checkout_page: CheckoutPage
    success_order_page: SuccessOrderPage
    search_page: SearchPage
    product_details_page: ProductDetailsPage
    helper_tools: HelperTools

    # tc 3
    @allure.title("Add a Product to the Shopping Cart and Verify")
    @allure.description("Ensure that a selected product is successfully added to the shopping cart.")
    def test_add_product_to_shopping_cart(self):

        # Define data
        test_name = "test_add_product_to_shopping_cart"
        category = "FRAGRANCE"
        product_name = "Acqua Di Gio Pour Homme"
        product_quantity = "3"
        unit_product_price = "45.00"
        unit_product_price_for_assertion = "$45.00"
        int_total_product_price = int(product_quantity) * float(unit_product_price)
        total_product_price = f"${int_total_product_price:.2f}"

        with allure.step("Navigate to the fragrance page"):
            self.home_page.choose_category_from_subnav(category)
            self.helper_tools.take_screenshot(self.driver, test_name)

        with allure.step("Click on the product name to open the product details page"):
            self.product_page.open_product_details(product_name)
            self.helper_tools.take_screenshot(self.driver, test_name)

        with allure.step("Select a quantity (if applicable)"):
            self.product_page.change_quantity(product_quantity)
            self.helper_tools.take_screenshot(self.driver, test_name)


        with allure.step("Click on 'Add to Cart'"):
            self.product_page.add_to_cart_from_product_details()
            self.helper_tools.take_screenshot(self.driver, test_name)

        with allure.step("Verify that shopping cart is open"):
            expected_shopping_cart_header_text = "SHOPPING CART"
            actual_shopping_cart_header_text = self.product_page.get_shopping_cart_header()
            assert expected_shopping_cart_header_text in actual_shopping_cart_header_text
            self.helper_tools.take_screenshot(self.driver, test_name)

        with allure.step("Verify that the correct product name, price, and quantity are displayed"):

            product_name_from_details = self.product_page.get_product_names_from_details()
            product_price_from_details = self.product_page.get_product_prices()
            product_quantity_from_details = self.product_page.get_quantities_from_details()

            assert product_name_from_details[0] == product_name
            assert product_quantity_from_details[0] == product_quantity
            assert product_price_from_details[0][0] == unit_product_price_for_assertion
            assert product_price_from_details[0][1] == total_product_price
            self.helper_tools.take_screenshot(self.driver, test_name)


    # tc 4
    @allure.title("Remove a Product from the Shopping Cart")
    @allure.description("Ensure a user can remove an item from the shopping cart.")
    def test_remove_product_from_shop_cart(self):
        test_name = "test_remove_product_from_shop_cart"
        actual_empty_shop_cart_message = 'Your shopping cart is empty!'

        with allure.step("Add a random product to the cart"):
            self.home_page.add_random_product()
            self.helper_tools.take_screenshot(self.driver, test_name)

        with allure.step("Navigate to the shopping cart page"):
            self.home_page.go_to_shopping_cart()
            self.helper_tools.take_screenshot(self.driver, test_name)

        with allure.step("Click the remove button next to the product"):
            self.product_page.remove_product()
            self.helper_tools.take_screenshot(self.driver, test_name)

        with allure.step("Verify the shopping cart is empty"):
            expected_empty_shop_cart_message = self.product_page.empty_cart_message()
            assert actual_empty_shop_cart_message in expected_empty_shop_cart_message
            self.helper_tools.take_screenshot(self.driver, test_name)

    # tc 6
    @allure.title("Verify Product Search Functionality")
    @allure.description("Ensure that users can search for products using the search bar.")

    def test_verify_product_search_func(self):
        test_name = "test_product_search"
        search_text = "Shampoo"

        with allure.step(f"Search for '{search_text}' using the search bar"):
            self.home_page.search_product(search_text)
            self.helper_tools.take_screenshot(self.driver, test_name)

        with allure.step("Verify that search results are displayed"):
            displayed_products = [p for p in self.search_page.searched_product_names() if p.is_displayed()]
            assert len(displayed_products) > 0

        with allure.step("Click the first visible product"):
            products = self.search_page.searched_product_names()
            products[0].click()
            self.helper_tools.take_screenshot(self.driver, test_name)

        with allure.step("Verify product name contains search text"):
            product_name = self.product_details_page.get_product_name()
            assert search_text.lower() in product_name.lower()
            self.helper_tools.take_screenshot(self.driver, test_name)


    # tc 7
    @allure.title("Verify Sorting Products by Price")
    @allure.description("Ensure that users can sort products by price from low to high.")
    @allure.title("Verify Sorting Products by Price")
    @allure.description("Ensure that users can sort products by price from low to high.")

    def test_sorting_product_by_price(self):
        test_name = "test_sorting"

        with allure.step("Navigate to the 'SKINCARE' category"):
            self.home_page.choose_category_from_subnav("SKINCARE")
            self.helper_tools.take_screenshot(self.driver, test_name)

        with allure.step("Sort products by Price: Low to High"):
            self.product_page.sort_by_price_asc()
            self.helper_tools.take_screenshot(self.driver, test_name)

        with allure.step("Verify that products are sorted in ascending order"):
            assert self.product_page.are_products_sorted_asc_by_price()

        with allure.step("Sort products by Price: High to Low"):
            self.product_page.sort_by_price_desc()
            self.helper_tools.take_screenshot(self.driver, test_name)

        with allure.step("Verify that products are sorted in descending order"):
            assert self.product_page.are_products_sorted_desc_by_price()
            self.helper_tools.take_screenshot(self.driver, test_name)


