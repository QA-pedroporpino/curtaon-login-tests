import time
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.screenshot_manager import ScreenshotManager

# === CONFIGURAÇÃO DO LOGGING ===
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/log_teste_login_positivo.log", mode='w', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def test_valid_login():
    """Teste de login com e-mail e senha corretos"""

    options = webdriver.ChromeOptions()
    # Otimizações para melhorar performance
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.page_load_strategy = 'eager'  # Não espera carregar recursos não essenciais
    
    driver = webdriver.Chrome(options=options)
    
    # Inicializa o gerenciador de screenshots
    screenshot_manager = ScreenshotManager()

    try:
        logging.info("=" * 60)
        logging.info("🚀 INICIANDO TESTE POSITIVO DE LOGIN")
        logging.info("=" * 60)

        # 1. Acessa o site
        driver.get("https://curtaon.com.br")
        logging.info("🌐 Site carregado")

        # 2. Clica no botão 'Entrar'
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "header_MenuCurtaoOn_btnLoginModalEntrar"))
        ).click()
        logging.info("✅ Botão 'Entrar' clicado")

        # 3. Clica em 'E-mail'
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn-login-email"))
        ).click()
        logging.info("✅ Botão 'E-mail' clicado")

        # 4. Preenche e-mail
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "txtUsuarioHeader"))
        )
        email_field.send_keys("nataliatheodorico@tamandua.org.br")
        logging.info("📩 E-mail inserido")

        # 5. Preenche senha
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "txtPassHeader"))
        )
        password_field.send_keys("123456")
        logging.info("🔒 Senha inserida")

        # 6. Clica no botão de login do modal
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btnLoginModalHeader"))
        )
        login_button.click()
        logging.info("📤 Login submetido")

        # 7. Valida se o elemento pós-login foi encontrado (com timeout otimizado)
        try:
            # Primeira tentativa: procura pelo elemento com ID e classe
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div#header_imgUserAvatarCtlBar.image-frame"))
            )
        except:
            # Segunda tentativa: procura apenas pelo ID
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "header_imgUserAvatarCtlBar"))
            )
        
        logging.info("🎯 Elemento de avatar pós-login identificado com sucesso!")
        
        # Salva screenshot de sucesso
        screenshot_path = screenshot_manager.save_screenshot(driver, "teste_login_positivo", "aprovado")
        logging.info(f"📂 Screenshot salvo em: {screenshot_path}")
        logging.info("✅ TESTE APROVADO: Login realizado com sucesso!")

    except Exception as e:
        logging.error("❌ TESTE REPROVADO: Erro no fluxo de login")
        logging.error(str(e))
        
        # Salva screenshot de erro
        screenshot_path = screenshot_manager.save_screenshot(driver, "teste_login_positivo", "erro")
        logging.info(f"📂 Screenshot salvo em: {screenshot_path}")
        pytest.fail(f"Falha no teste de login: {str(e)}")

    finally:
        # Mostra o caminho da última screenshot
        ultima_screenshot = screenshot_manager.get_ultima_screenshot()
        if ultima_screenshot:
            logging.info(f"📸 Última screenshot salva em: {ultima_screenshot}")
            
        driver.quit()
        logging.info("🛑 Navegador fechado. Fim do teste\n")

if __name__ == "__main__":
    test_valid_login()
