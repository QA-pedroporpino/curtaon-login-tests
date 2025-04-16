import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.screenshot_manager import ScreenshotManager

class BaseTest:
    """Classe base para todos os testes com funcionalidades comuns"""
    
    def __init__(self, test_name):
        self.test_name = test_name
        self.setup_logging()
        self.screenshot_manager = ScreenshotManager()
        self.driver = None

    def setup_logging(self):
        """Configura o logging para o teste"""
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler(f"logs/log_{self.test_name}.log", mode='w', encoding='utf-8'),
                logging.StreamHandler()
            ]
        )

    def setup_driver(self):
        """Configura o driver do Chrome com opções otimizadas"""
        options = webdriver.ChromeOptions()
        # Otimizações para melhorar performance e evitar detecção
        options.add_argument("--start-maximized")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-web-security")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.page_load_strategy = 'eager'
        
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_page_load_timeout(30)

    def wait_for_element(self, by, value, timeout=20, retry_count=3):
        """Função auxiliar para esperar por elementos com retry"""
        for attempt in range(retry_count):
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((by, value))
                )
                return element
            except TimeoutException:
                if attempt < retry_count - 1:
                    logging.warning(f"Tentativa {attempt + 1} falhou. Tentando novamente...")
                    time.sleep(2)
                else:
                    raise

    def click_element(self, by, value, element_name=""):
        """Clica em um elemento com tratamento de exceção"""
        try:
            element = self.wait_for_element(by, value)
            element.click()
            logging.info(f"✅ {element_name or 'Elemento'} clicado")
        except TimeoutException:
            logging.error(f"❌ {element_name or 'Elemento'} não encontrado após múltiplas tentativas")
            raise

    def fill_field(self, by, value, text, field_name=""):
        """Preenche um campo com tratamento de exceção"""
        try:
            field = self.wait_for_element(by, value)
            field.clear()
            field.send_keys(text)
            logging.info(f"📝 {field_name or 'Campo'} preenchido")
        except TimeoutException:
            logging.error(f"❌ {field_name or 'Campo'} não encontrado após múltiplas tentativas")
            raise

    def save_screenshot(self, status):
        """Salva screenshot com status específico"""
        screenshot_path = self.screenshot_manager.save_screenshot(
            self.driver, 
            self.test_name, 
            status
        )
        logging.info(f"📂 Screenshot salvo em: {screenshot_path}")
        return screenshot_path

    def cleanup(self):
        """Limpeza após o teste"""
        if self.driver:
            ultima_screenshot = self.screenshot_manager.get_ultima_screenshot()
            if ultima_screenshot:
                logging.info(f"📸 Última screenshot salva em: {ultima_screenshot}")
            self.driver.quit()
            logging.info("🛑 Navegador fechado. Fim do teste\n") 