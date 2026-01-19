import json

import allure
import pytest
from allure_commons.types import AttachmentType

from utils.driver_factory import DriverFactory

CONFIG_PATH = "config.json"
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ["chrome", "firefox", "edge"]
DEFAULT_URL = "https://demoqa.com/broken"

@pytest.fixture(scope="function")
def config():
    with open(CONFIG_PATH) as config_file:
        return json.load(config_file)

@pytest.fixture(scope="function")
def browser_setup(config):
    if "browser" not in config:
        raise KeyError('The config file does not contain "browser"')
    elif config["browser"] not in SUPPORTED_BROWSERS:
        raise ValueError(f'"{config["browser"]}" is not a supported browser')
    return config["browser"]

@pytest.fixture(scope='function')
def wait_time_setup(config):
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME

@pytest.fixture(scope='function')
def url_setup(config):
    return config["base_url"] if "base_url" in config else DEFAULT_URL

@pytest.fixture()
def setup(request, config):
    driver = DriverFactory.get_driver(config)
    driver.implicitly_wait(config["timeout"])
    pytest.driver = driver  # Assign driver to pytest for global access
    print("Debug: Driver initialized in setup fixture.")
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    if config["browser"] == "firefox":
        driver.maximize_window()
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(),
                      name="Test failed", attachment_type=AttachmentType.PNG)
    driver.quit()
    pytest.driver = None  # Clean up after test
