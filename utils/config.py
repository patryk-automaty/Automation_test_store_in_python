import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')

class Config:
    @staticmethod
    def get_browser():
        return config.get("DEFAULT", "browser")

    @staticmethod
    def get_base_url():
        return config.get("DEFAULT", "base_url")