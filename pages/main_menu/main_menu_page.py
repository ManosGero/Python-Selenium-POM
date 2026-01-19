from pages.main_menu.main_menu_page_locators import MainMenuPageLocators
import logging
from pages.base_page import BasePage
class MainMenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click_to_elements(self):
        try:
            self.click(MainMenuPageLocators.ELEMENT_LINK)
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return False

    def click_to_forms(self):
        try:
            self.click(MainMenuPageLocators.FORMS_LINK)
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return False

    def click_to_alerts(self):
        try:
            self.click(MainMenuPageLocators.ALERTS_LINK)
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return False

    def click_to_widgets(self):
        try:
            self.click(MainMenuPageLocators.WIDGETS_LINK)
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return False

    def click_to_interactions(self):
        try:
            self.click(MainMenuPageLocators.INTERACTIONS_LINK)
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return False

    def click_to_book_store_application(self):
        try:
            self.click(MainMenuPageLocators.BOOK_STORE_APPLICATION_LINK)
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return False