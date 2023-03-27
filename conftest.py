import pytest
from selenium import webdriver


# @pytest.fixture()
# def set_up():
#     print("START TEST")
#     yield
#     print("END TEST")
#
#
# @pytest.fixture(scope="module")
# def set_group():
#     print("ENTER SYSTEM")
#     yield
#     print("EXIT SYSTEM")

@pytest.fixture(scope="session")
def browser():
    chrome_driver_path = "/Users/mariasuhinina/venv/chromedriver_mac64/chromedriver"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    yield driver
    driver.quit()