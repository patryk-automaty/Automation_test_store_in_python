from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterUserPage(BasePage):

    # Locators for register user page
    _create_user_header = (By.XPATH, "//span[contains(text(),'Create Account')]")
    _login_page_link = (By.XPATH, "//a[contains(text(),'login page')]")
    # Your Personal Details
    _first_name_input = (By.ID, "AccountFrm_firstname")
    _last_name_input = (By.ID, "AccountFrm_lastname")
    _email_input = (By.ID, "AccountFrm_email")
    _telephone_input = (By.ID, "AccountFrm_telephone")
    _fax_input = (By.ID, "AccountFrm_fax")
    # Your Address
    _company_input = (By.ID, "AccountFrm_company")
    _address1_input = (By.ID, "AccountFrm_address_1")
    _address2_input = (By.ID, "AccountFrm_address_2")
    _city_input = (By.ID, "AccountFrm_city")
    _region_select = (By.ID, "AccountFrm_zone_id")
    _zipcode_input = (By.ID, "AccountFrm_postcode")
    _country_select = (By.ID, "AccountFrm_country_id")
    # Login Details
    _login_name_input = (By.ID, "AccountFrm_loginname")
    _password_input = (By.ID, "AccountFrm_password")
    _password_confirm_input = (By.ID, "AccountFrm_confirm")
    # Newsletter
    _subscribe_radiobutton_yes = (By.ID, "AccountFrm_newsletter1")
    _subscribe_radiobutton_no = (By.ID, "AccountFrm_newsletter0")
    # Privacy Policy
    _agree_privacy_policy_checkbox = (By.ID, "AccountFrm_agree")
    _agree_privacy_policy_link = (By.XPATH, "//b[contains(text(), 'Privacy Policy')]")
    _continue_button = (By.XPATH, "//button[@title='Continue']")

    def get_header_text(self):
        return self.get_text(*self._create_user_header)

    def click_on_login_link(self):
        self.click(self._login_page_link)

    def input_personal_details(self, first_name, last_name, email, telephone, fax):
        self.send_keys(*self._first_name_input, first_name)
        self.send_keys(*self._last_name_input, last_name)
        self.send_keys(*self._email_input, email)
        self.send_keys(*self._telephone_input, telephone)
        self.send_keys(*self._email_input, email)
        self.send_keys(*self._fax_input, fax)







