from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):

    _searched_product_names = (By.XPATH, "//div[@class='thumbnails grid row list-inline']//a[@class='prdocutname']")


    def searched_product_names(self):
        return self.find_elements(*self._searched_product_names)

