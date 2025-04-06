from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):


    _product_list = (By.XPATH, "//div[@class='fixed']/a[@class='prdocutname']")
    _product_details_quantity = (By.ID, "product_quantity")
    _product_details_add_to_cart_button = (By.XPATH, "//ul[@class='productpagecart']")
    _shopping_cart_header = (By.XPATH, "//span[contains(text(), 'Shopping Cart')]")
    _sort_by_select = (By.ID, "sort")
    _product_prices = (By.CLASS_NAME, "price")
    _new_product_price = (By.XPATH, "//div[@class='pricetag jumbotron']//div[@class='pricenew']")
    _one_product_price = (By.XPATH, "//div[@class='pricetag jumbotron']//div[@class='oneprice']")



    _product_name_from_details = (By.XPATH, "//tr/td[@class='align_left']/a")
    _quantity_from_details = (By.XPATH, "//td/div[@class='input-group input-group-sm']/input")
    _price_from_details = (By.XPATH, "//td[@class='align_right']")
    _remove_button = (By.XPATH, "//i[@class='fa fa-trash-o fa-fw']")
    _empty_cart_message = (By.XPATH, "//div[contains(text(), 'Your shopping cart is empty')]")
    _checkout_button_1 = (By.ID, "cart_checkout1")


    def open_product_details(self, product_name):
        products = self.find_elements(*self._product_list)
        for product in products:
            if product.text.strip() == str(product_name).upper():
                product.click()
                break

    def change_quantity(self, quantity):
        self.clear_input(self._product_details_quantity)
        self.send_keys(*self._product_details_quantity, quantity)

    def add_to_cart_from_product_details(self):
        self.click(self._product_details_add_to_cart_button)

    def get_shopping_cart_header(self):
        return self.get_text(*self._shopping_cart_header)

    def get_product_names_from_details(self):
        product_names = self.find_elements(*self._product_name_from_details)

        product_names_list = []
        for names in product_names:
            product_names_list.append(names.text)

        return product_names_list

    def get_quantities_from_details(self):

        quantities = self.find_elements(*self._quantity_from_details)
        quantities_list = []
        for quantity in quantities:
            quantities_list.append(quantity.get_attribute("value"))

        return quantities_list


    def get_product_prices(self):
        prices = self.find_elements(*self._price_from_details)

        product_prices = []
        for i in range(0, len(prices), 2):
            unit_price = prices[i].text.strip()
            total_price = prices[i + 1].text.strip() if i + 1 < len(prices) else None
            product_prices.append([unit_price, total_price])

        return product_prices

    def remove_product(self):
        self.click(self._remove_button)

    def empty_cart_message(self):
        return self.find_element(*self._empty_cart_message).text

    def click_checkout(self):
        self.click(self._checkout_button_1)

    def sort_by_price_asc(self):
        self.select(*self._sort_by_select, value="p.price-ASC", selection_type="value")

    def sort_by_price_desc(self):
        self.select(*self._sort_by_select, value="p.price-DESC", selection_type="value")

    def are_products_sorted_asc_by_price(self):
        product_containers = self.find_elements(*self._product_prices)

        prices = []

        for container in product_containers:
            try:
                price_element = container.find_element(*self._new_product_price)

            except:
                price_element = container.find_element(*self._one_product_price)

            price_text = price_element.text.strip().replace("$", "")
            prices.append(float(price_text))

        return prices == sorted(prices)

    def are_products_sorted_desc_by_price(self):
        product_containers = self.find_elements(*self._product_prices)

        prices = []

        for container in product_containers:
            try:
                price_element = container.find_element(*self._new_product_price)

            except:
                price_element = container.find_element(*self._one_product_price)

            price_text = price_element.text.strip().replace("$", "")
            prices.append(float(price_text))

        return prices == sorted(prices, reverse=True)
