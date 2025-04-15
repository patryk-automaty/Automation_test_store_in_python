import time
import unittest

import allure

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from pages.register_user_page import RegisterUserPage
from pages.register_success_page import RegisterSuccessPage
from pages.logout_page import LogoutPage
from pages.product_page import ProductPage
from utils.config import Config
from utils.driver_factory import get_driver
from pages.checkout_confirmation_page import CheckoutPage
from pages.success_order_page import SuccessOrderPage
from pages.search_page import SearchPage
from pages.product_details_page import ProductDetailsPage

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
        cls.product_page = ProductPage(cls.driver)
        cls.checkout_page = CheckoutPage(cls.driver)
        cls.success_order_page = SuccessOrderPage(cls.driver)
        cls.search_page = SearchPage(cls.driver)
        cls.product_details_page = ProductDetailsPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit() # close the browser session

    # tc 3
    @allure.title("Add a Product to the Shopping Cart and Verify")
    @allure.description("Ensure that a selected product is successfully added to the shopping cart.")
    def test_add_product_to_shopping_cart(self):

        # define data
        category = "FRAGRANCE"
        product_name = "Acqua Di Gio Pour Homme"
        product_quantity = "3"
        unit_product_price = "45.00"
        unit_product_price_for_assertion = "$45.00"
        int_total_product_price = int(product_quantity) * float(unit_product_price)
        total_product_price = f"${int_total_product_price:.2f}"

        # Navigate to the fragrance page
        self.home_page.choose_category_from_subnav(category)

        # Click on the product name to open the product details page
        self.product_page.open_product_details(product_name)

        # Select a quantity (if applicable).
        self.product_page.change_quantity(product_quantity)

        # Click on "Add to Cart"
        self.product_page.add_to_cart_from_product_details()

        # Verify that shopping cart is open
        expected_shopping_cart_header_text = "SHOPPING CART"
        actual_shopping_cart_header_text = self.product_page.get_shopping_cart_header()
        self.assertIn(expected_shopping_cart_header_text, actual_shopping_cart_header_text)

        # Verify that the correct product name, price, and quantity are displayed
        product_name_from_details = self.product_page.get_product_names_from_details()
        product_price_from_details = self.product_page.get_product_prices()
        product_quantity_from_details = self.product_page.get_quantities_from_details()

        self.assertEqual(product_name_from_details[0], product_name, "Product name does not match!")
        self.assertEqual(product_quantity_from_details[0], product_quantity, "Product quantity does not match!")
        self.assertEqual(product_price_from_details[0][0], unit_product_price_for_assertion, "Unit price does not match!")
        self.assertEqual(product_price_from_details[0][1], total_product_price, "Total price does not match!")

    # tc 4
    @allure.title("Remove a Product from the Shopping Cart")
    @allure.description("Ensure a user can remove an item from the shopping cart.")
    def test_remove_product_from_shop_cart(self):

        actual_empty_shop_cart_message = 'Your shopping cart is empty!'

        # Add any product to the cart.
        self.home_page.add_random_product()
        # Go to the Shopping Cart page.
        self.home_page.go_to_shopping_cart()
        # Click on the "Remove" (X) button next to the product.
        self.product_page.remove_product()
        # Verify that the item is successfully removed.
        expected_empty_shop_cart_message = self.product_page.empty_cart_message()
        self.assertIn(actual_empty_shop_cart_message, expected_empty_shop_cart_message)

    # tc 5
    @allure.title("Verify Checkout Process with a Registered User")
    @allure.description("Ensure that a registered user can complete the checkout process.")
    def test_verify_checkout_with_registered_account(self):

        login = "daniel898"
        password = "7PgKmgZz"

        # Login to an existing registered account.
        self.home_page.go_to_login_page()
        self.login_page.login_to_account(login, password)
        # Add any product to the cart.
        self.home_page.go_to_home_page()
        self.home_page.add_random_product()
        # Click on "Checkout".
        self.product_page.click_checkout()
        # Verify that the billing address and shipping address are pre-filled.
        self.assertTrue(self.checkout_page.shipping_address().is_displayed())
        self.assertTrue(self.checkout_page.payment_address().is_displayed())
        # Click on "Confirm Order".
        self.checkout_page.click_confirm()
        # Verify that an order confirmation message appears.
        self.assertIn("Your Order Has Been Processed!", self.success_order_page.get_success_order_message())

    # tc 6
    @allure.title("Verify Product Search Functionality")
    @allure.description("Ensure that users can search for products using the search bar.")
    def test_verify_product_search_func(self):

        # Locate the search bar and Enter a product name (e.g., "Shampoo").
        search_text = "Shampoo"
        self.home_page.search_product(search_text)
        # Verify that the search results display relevant products.
        displayed_products = [products for products in self.search_page.searched_product_names() if products.is_displayed()]
        self.assertTrue(len(displayed_products) > 0)
        # Click on a product to open the product details page.
        products = [prod for prod in self.search_page.searched_product_names()]
        products[0].click()
        # Verify that the product name matches the search query.
        product_name = self.product_details_page.get_product_name()
        self.assertIn(search_text.lower(), product_name.lower())

    # tc 7
    @allure.title("Verify Sorting Products by Price")
    @allure.description("Ensure that users can sort products by price from low to high.")
    def test_sorting_product_by_price(self):

        # Navigate to a category page (e.g., Skincare).
        self.home_page.choose_category_from_subnav("SKINCARE")
        # Locate the Sort By dropdown menu and select "Price: Low to High".
        self.product_page.sort_by_price_asc()
        # Verify that products are sorted in ascending order.
        self.assertTrue(self.product_page.are_products_sorted_asc_by_price())
        # Change sorting to "Price: High to Low".
        self.product_page.sort_by_price_desc()
        # Verify that products are now sorted in descending order.
        self.assertTrue(self.product_page.are_products_sorted_desc_by_price())

