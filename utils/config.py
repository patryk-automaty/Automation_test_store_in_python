import configparser
import os

# Get the absolute path of the config file
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "config.ini")

config = configparser.ConfigParser()
config.read(CONFIG_PATH)

class Config:
    @staticmethod
    def get_browser():
        return config.get("DEFAULT", "browser")

    @staticmethod
    def get_base_url():
        return config.get("DEFAULT", "base_url")