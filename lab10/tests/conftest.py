import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    """Initialize WebDriver and quit after test."""
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
