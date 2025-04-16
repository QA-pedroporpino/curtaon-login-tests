import time
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.screenshot_manager import ScreenshotManager
from base_test import BaseTest

# === CONFIGURAÇÃO DO LOGGING ===
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/log_teste_login_positivo.log", mode='w', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def wait_for_element(driver, by, value, timeout=20, retry_count=3):
    """Função auxiliar para esperar por elementos com retry"""
    for attempt in range(retry_count):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            if attempt < retry_count - 1:
                logging.warning(f"Tentativa {attempt + 1} falhou. Tentando novamente...")
                time.sleep(2)  # Espera antes de tentar novamente
            else:
                raise

class TestValidLogin(BaseTest):
    """Teste de login com e-mail e senha corretos"""

    def __init__(self):
        super().__init__("teste_login_positivo")

    def test_valid_login(self):
        """Executa o teste de login"""
        try:
            logging.info("=" * 60)
            logging.info("🚀 INICIANDO TESTE POSITIVO DE LOGIN")
            logging.info("=" * 60)

            # 1. Acessa o site
            self.driver.get("https://curtaon.com.br")
            logging.info("🌐 Site carregado")

            # 2. Clica no botão 'Entrar'
            self.click_element(
                By.ID, 
                "header_MenuCurtaoOn_btnLoginModalEntrar",
                "Botão 'Entrar'"
            )

            # 3. Clica em 'E-mail'
            self.click_element(
                By.ID, 
                "btn-login-email",
                "Botão 'E-mail'"
            )

            # 4. Preenche e-mail
            self.fill_field(
                By.ID, 
                "txtUsuarioHeader", 
                "nataliatheodorico@tamandua.org.br",
                "Campo de e-mail"
            )

            # 5. Preenche senha
            self.fill_field(
                By.ID, 
                "txtPassHeader", 
                "123456",
                "Campo de senha"
            )

            # 6. Clica no botão de login
            self.click_element(
                By.ID, 
                "btnLoginModalHeader",
                "Botão de login"
            )

            # 7. Valida login com múltiplas estratégias de espera
            try:
                # Primeira tentativa: procura pelo elemento com ID e classe
                self.wait_for_element(
                    By.CSS_SELECTOR, 
                    "div#header_imgUserAvatarCtlBar.image-frame",
                    timeout=30
                )
                logging.info("🎯 Elemento de avatar pós-login identificado com sucesso!")
            except TimeoutException:
                # Segunda tentativa: procura apenas pelo ID
                self.wait_for_element(
                    By.ID,
                    "header_imgUserAvatarCtlBar",
                    timeout=30
                )
                logging.info("🎯 Elemento de avatar pós-login identificado com sucesso!")

            # Salva screenshot de sucesso
            self.save_screenshot("aprovado")
            logging.info("✅ TESTE APROVADO: Login realizado com sucesso!")

        except Exception as e:
            logging.error("❌ TESTE REPROVADO: Erro no fluxo de login")
            logging.error(str(e))
            
            # Salva screenshot de erro
            self.save_screenshot("erro")
            pytest.fail(f"Falha no teste de login: {str(e)}")

        finally:
            self.cleanup()

def test_valid_login():
    """Função de teste para compatibilidade com pytest"""
    test = TestValidLogin()
    test.setup_driver()
    test.test_valid_login()

if __name__ == "__main__":
    test_valid_login()
