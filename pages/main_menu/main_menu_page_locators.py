from selenium.webdriver.common.by import By

class MainMenuPageLocators:
    ELEMENT_LINK = (By.XPATH, "//div[@class='category-cards']/div//h5[contains(.,'Elements')]")
    FORMS_LINK = (By.XPATH, "//div[@class='category-cards']/div//h5[contains(.,'Forms')]")
    ALERTS_LINK = (By.XPATH, "//div[@class='category-cards']/div//h5[contains(.,'Alerts, Frame & Windows')]")
    WIDGETS_LINK = (By.XPATH, "//div[@class='category-cards']/div//h5[contains(.,'Widgets')]")
    INTERACTIONS_LINK = (By.XPATH, "//div[@class='category-cards']/div//h5[contains(.,'Interactions')]")
    BOOK_STORE_APPLICATION_LINK = (By.XPATH, "//div[@class='category-cards']/div//h5[contains(.,'Book Store Application')]")