import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    print("Creating Chrome driver")
    new_driver = webdriver.Chrome()
    yield new_driver
    print("Tear down Chrome Driver")
    new_driver.quit()