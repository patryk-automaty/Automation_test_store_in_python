from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def get_driver(browser="chrome"):
    if browser == "chrome":
        # Automatically installs the appropriate ChromeDriver
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "firefox":
        # Automatically installs the appropriate GeckoDriver (Firefox)
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    return driver