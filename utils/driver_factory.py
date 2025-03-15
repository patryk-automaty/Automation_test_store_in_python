from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def get_driver(browser="chrome"):

    if browser.lower() == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")  # Maximize window
        service = ChromeService(ChromeDriverManager().install())  # Use ChromeService
        driver = webdriver.Chrome(service=service, options=chrome_options)

    elif browser.lower() == "firefox":
        firefox_options = FirefoxOptions()
        service = FirefoxService(GeckoDriverManager().install())  # Use FirefoxService
        driver = webdriver.Firefox(service=service, options=firefox_options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    return driver