import pytest
from selenium import webdriver
from pages.broken_page import BrokenPage
import chromedriver_autoinstaller

# Automatically install and configure Chrome WebDriver
chromedriver_autoinstaller.install()

def setup_module(module):
    global driver
    driver = webdriver.Chrome()

def teardown_module(module):
    driver.quit()

@pytest.fixture
def broken_page():
    page = BrokenPage(driver)
    page.open("https://demoqa.com/broken")
    return page

def test_broken_image(broken_page):
    assert broken_page.is_broken_image_displayed(), "Broken image is not displayed on the page."
