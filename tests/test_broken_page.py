import pytest
from pages.main_menu.main_menu_page import MainMenuPage
from pages.broken_image.broken_page import BrokenPage
from pages.side_menu import SideMenuPage
from tests.config_test import setup, config  # Explicitly import the setup and config fixtures


@pytest.mark.usefixtures("setup")
class TestBrokenPage:
    def test_broken_image(self, config):
        assert hasattr(pytest, "driver"), "Driver is not initialized in pytest. Ensure the setup fixture is executed."
        page = MainMenuPage(pytest.driver)
        page.open(config["base_url"])
        page.click_to_elements()
        page = SideMenuPage(pytest.driver)
        page.click_to_elements()
        page.navigate_to_broken_images()
        page = BrokenPage(pytest.driver)
        assert page.is_broken_image_displayed(), "Broken image is not displayed on the page."
