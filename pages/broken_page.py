from selenium.webdriver.common.by import By

class BrokenPage:
    def __init__(self, driver):
        self.driver = driver
        self.broken_image_locator = (By.XPATH, "//img[contains(@src, 'broken')]")

    def open(self, url):
        self.driver.get(url)

    def is_broken_image_displayed(self):
        try:
            broken_image = self.driver.find_element(*self.broken_image_locator)
            return broken_image.is_displayed()
        except Exception:
            return False
