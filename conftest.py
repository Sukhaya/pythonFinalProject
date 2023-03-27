import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    chrome_driver_path = "/Users/mariasuhinina/venv/chromedriver_mac64/chromedriver"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    yield driver
    driver.quit()