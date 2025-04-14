import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    """Fixture que fornece uma instância do WebDriver"""
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    """Fixture que fornece uma instância da página de login"""
    from tests.pages.login_page import LoginPage
    return LoginPage(driver) 