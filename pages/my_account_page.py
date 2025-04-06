from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MyAccountPage(BasePage):

    _my_account_header = (By.XPATH, "//span[contains(text(), 'My Account')]")
    _logout_from_my_account_box = (By.XPATH, "//div[@class='myaccountbox']//a[contains(text(),'Logoff')]")
    _wishlist_from_my_account_box = (By.XPATH, "//div[@class='myaccountbox']//a[contains(text(),'My wish list')]")

    def get_my_account_header_text(self):
        return self.get_text(*self._my_account_header)

    def logout_from_my_account_box(self):
        self.click(self._logout_from_my_account_box)

    def wishlist_from_my_account_box(self):
        self.click(self._wishlist_from_my_account_box)

