import unittest

from pages.home_page import HomePage
from utils.config import Config
from utils.driver_factory import get_driver


class RegisterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = Config.get_browser()
        cls.driver = get_driver(browser)
        cls.driver.get(Config.get_base_url())
        cls.home_page = HomePage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

