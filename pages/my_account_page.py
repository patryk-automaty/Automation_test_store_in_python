from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MyAccountPage(BasePage):

    _my_account_header = (By.XPATH, "//span[contains(text(), 'My Account')]")
    _logout_from_my_account_box = (By.XPATH, "//div[@class='myaccountbox']//a[contains(text(),'Logoff')]")
    _wishlist_from_my_account_box = (By.XPATH, "//div[@class='myaccountbox']//a[contains(text(),'My wish list')]")
    _notification_tab_header = (By.XPATH, "//span[contains(.,'Notifications and Newsletter')]")
    _newsletter_checkbox = (By.ID, "imFrm_settingsnewsletteremail")
    _continue_button = (By.XPATH, "//button[@title='Continue']")
    _success_notification_message = (By.XPATH, "//div[@class='alert alert-success']")

    def get_my_account_header_text(self):
        return self.get_text(*self._my_account_header)

    def logout_from_my_account_box(self):
        self.click(self._logout_from_my_account_box)

    def wishlist_from_my_account_box(self):
        self.click(self._wishlist_from_my_account_box)

    def get_notification_tab_header(self):
        return self.find_element(*self._notification_tab_header)

    def is_newsletter_checkbox_selected(self):
        return self.find_element(*self._newsletter_checkbox).is_selected()

    def click_continue(self):
        self.click(self._continue_button)

    def get_success_notification_message(self):
        return self.find_element(*self._success_notification_message)