import unittest
from utils.driver_factory import get_driver
from utils.config import Config
from pages.home_page import HomePage

class HomePageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = Config.get_browser()
        cls.driver = get_driver(browser)
        cls.driver.get(Config.get_base_url())
        cls.home_page = HomePage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_go_to_login_page(self):
        self.home_page.go_to_login_page()

if __name__ == "__main__":
    unittest.main()