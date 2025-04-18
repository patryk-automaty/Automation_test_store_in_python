from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os


def get_driver(browser="chrome"):

    if browser.lower() == "chrome":
        chrome_options = ChromeOptions()

        if os.getenv("CI"):
            chrome_options.add_argument("--headless=new")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
        else:
            chrome_options.add_argument("--start-maximized")

        service = ChromeService(ChromeDriverManager().install())  # Use ChromeService
        driver = webdriver.Chrome(service=service, options=chrome_options)

    elif browser.lower() == "firefox":
        firefox_options = FirefoxOptions()

        if os.getenv("CI"):
            firefox_options.add_argument("--headless")
            firefox_options.add_argument("--no-sandbox")
            firefox_options.add_argument("--disable-dev-shm-usage")
            firefox_options.add_argument("--window-size=1920,1080")
        else:
            firefox_options.add_argument("--start-maximized")

        service = FirefoxService(GeckoDriverManager().install())  # Use FirefoxService
        driver = webdriver.Firefox(service=service, options=firefox_options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    return driver