import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Importação da página de login
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def driver():
    """
    Fixture que fornece uma instância do WebDriver para cada teste
    """
    # Configuração do Chrome
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # Inicializa o driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Define um timeout implícito
    driver.implicitly_wait(10)
    
    # Remove o webdriver flag
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    yield driver
    
    # Fecha o navegador após o teste
    driver.quit()

@pytest.fixture(scope="function")
def login_page(driver):
    """
    Fixture que fornece uma instância da página de login
    """
    return LoginPage(driver) 