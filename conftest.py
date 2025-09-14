import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from urls import BASE_URL

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    options = Options()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    driver.get(BASE_URL)
    yield driver
    driver.quit()
