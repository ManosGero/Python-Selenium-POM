import logging

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SideMenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def side_menu_locators(self):
        return {
            "ELEMENT_LINK": (By.XPATH, "//span[contains(.,'Elements')]"),
            "FORMS_LINK": (By.XPATH, "//span[contains(.,'Forms')]"),
            "ALERTS_LINK": (By.XPATH, "//span[contains(.,'Alerts, Frame & Windows')]"),
            "WIDGETS_LINK": (By.XPATH, "//span[contains(.,'Widgets')]"),
            "INTERACTIONS_LINK": (By.XPATH, "//span[contains(.,'Interactions')]"),
            "BOOK_STORE_APPLICATION_LINK": (By.XPATH, "//span[contains(.,'Book Store Application')]"),
            "BROKEN_LINKS_IMAGES_LINK": (By.XPATH, "//span[contains(.,'Broken Links - Images')]")
        }

    def click_to_elements(self):
        try:
            self.click(self.side_menu_locators()["ELEMENT_LINK"])
        except Exception as e:
            logging.error(f"Error occurred: {e}")

    def click_to_forms(self):
        try:
            self.click(self.side_menu_locators()["FORMS_LINK"])
        except Exception as e:
            logging.error(f"Error occurred: {e}")

    def click_to_alerts(self):
        try:
            self.click(self.side_menu_locators()["ALERTS_LINK"])
        except Exception as e:
            logging.error(f"Error occurred: {e}")

    def click_to_widgets(self):
        try:
            self.click(self.side_menu_locators()["WIDGETS_LINK"])
        except Exception as e:
            logging.error(f"Error occurred: {e}")

    def click_to_interactions(self):
        try:
            self.click(self.side_menu_locators()["INTERACTIONS_LINK"])
        except Exception as e:
            logging.error(f"Error occurred: {e}")

    def click_to_book_store_application(self):
        try:
            self.click(self.side_menu_locators()["BOOK_STORE_APPLICATION_LINK"])
        except Exception as e:
            logging.error(f"Error occurred: {e}")

    def navigate_to_broken_images(self):
        self.click(self.side_menu_locators()["BROKEN_LINKS_IMAGES_LINK"])
