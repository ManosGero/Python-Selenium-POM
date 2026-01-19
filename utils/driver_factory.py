from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from helpers.webdriver_listener import WebDriverListener
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import EdgeOptions
from extensions.webdriver_extensions import WebDriverExtended
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

class DriverFactory:
    @staticmethod
    def get_driver(config) -> WebDriverExtended:
        if config["browser"] == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            if config["headless_mode"] is True:
                options.add_argument("--headless")
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            return WebDriverExtended(driver, WebDriverListener(), config)
        elif config["browser"] == "firefox":
            options = webdriver.FirefoxOptions()
            if config["headless_mode"] is True:
                options.headless = True
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)
            return WebDriverExtended(driver, WebDriverListener(), config)
        elif config["browser"] == "edge":
            options = EdgeOptions()
            options.use_chromium = True
            if config["headless_mode"] is True:
                options.headless = True
            service = EdgeService(EdgeChromiumDriverManager().install())
            driver = Edge(service=service, options=options)
            return WebDriverExtended(driver, WebDriverListener(), config)
        raise ValueError(f"Unsupported browser: {config.get('browser')}")