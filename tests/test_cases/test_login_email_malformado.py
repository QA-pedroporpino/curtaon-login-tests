import time
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot_manager import ScreenshotManager

# === CONFIGURAÇÃO DO LOGGING COM UTF-8 ===
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/log_teste_email_malformado.log", mode='w', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def test_login_email_malformado():
    """Teste para verificar que e-mails com caracteres inválidos são rejeitados"""

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    
    # Inicializa o gerenciador de screenshots
    screenshot_manager = ScreenshotManager()

    try:
        logging.info("=" * 60)
        logging.info("🚨 INICIANDO TESTE: E-MAIL MALFORMADO COM CARACTERES INVÁLIDOS")
        logging.info("=" * 60)

        # 1. Acessa o site
        driver.get("https://curtaon.com.br")
        logging.info("🌐 Site carregado")

        # 2. Clica no botão 'Entrar'
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "header_MenuCurtaoOn_btnLoginModalEntrar"))
        ).click()
        logging.info("✅ Botão 'Entrar' clicado")

        # 3. Clica no botão 'E-mail'
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "btn-login-email"))
        ).click()
        logging.info("✅ Botão 'E-mail' clicado")

        # 4. Preenche e-mail malformado
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "txtUsuarioHeader"))
        ).send_keys("pedro@#@gmail.com")
        logging.info("📩 E-mail malformado com caracteres inválidos preenchido")

        # 5. Preenche senha correta
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "txtPassHeader"))
        ).send_keys("123456")
        logging.info("🔒 Senha preenchida")

        # 6. Clica no botão de login
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "btnLoginModalHeader"))
        ).click()
        logging.info("📤 Tentativa de login submetida")

        # 7. Valida modal de erro com mensagem de e-mail inválido
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "swal2-title"))
        )
        mensagem = driver.find_element(By.ID, "swal2-title").text.strip()
        logging.info(f"📢 Mensagem exibida: '{mensagem}'")

        assert "email inválido" in mensagem.lower(), f"Mensagem inesperada: {mensagem}"
        
        # Salva screenshot de sucesso
        screenshot_path = screenshot_manager.save_screenshot(driver, "teste_email_malformado", "aprovado")
        logging.info(f"📂 Screenshot salvo em: {screenshot_path}")
        logging.info("✅ TESTE APROVADO: E-mail malformado corretamente rejeitado")

        time.sleep(3)

    except Exception as e:
        logging.error("❌ TESTE REPROVADO")
        logging.error(str(e))
        
        # Salva screenshot de erro
        screenshot_path = screenshot_manager.save_screenshot(driver, "teste_email_malformado", "erro")
        logging.info(f"📂 Screenshot salvo em: {screenshot_path}")
        pytest.fail(f"Erro: {str(e)}")

    finally:
        # Mostra o caminho da última screenshot
        ultima_screenshot = screenshot_manager.get_ultima_screenshot()
        if ultima_screenshot:
            logging.info(f"📸 Última screenshot salva em: {ultima_screenshot}")
            
        driver.quit()
        logging.info("🛑 Navegador fechado. Fim do teste\n")

if __name__ == "__main__":
    test_login_email_malformado()
