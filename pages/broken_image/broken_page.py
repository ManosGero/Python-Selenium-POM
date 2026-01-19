from pages.broken_image.broken_page_locators import BrokenPageLocators
import logging
from selenium.webdriver.support.ui import WebDriverWait

class BrokenPage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def is_broken_image_displayed(self):
        try:
            broken_image = self.wait.until(lambda driver: driver.find_element(*BrokenPageLocators.BROKEN_IMAGE))
            return broken_image.is_displayed()
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return False
