import time
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.screenshot_manager import ScreenshotManager

# === CONFIGURAÇÃO DO LOGGING COM UTF-8 ===
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/log_teste_senha_incorreta.log", mode='w', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def test_login_email_valido_senha_incorreta():
    """Teste para verificar comportamento ao usar e-mail válido com senha incorreta"""

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    
    # Inicializa o gerenciador de screenshots
    screenshot_manager = ScreenshotManager()

    try:
        logging.info("=" * 60)
        logging.info("🚨 INICIANDO TESTE: E-MAIL VÁLIDO + SENHA INCORRETA")
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

        # 4. Preenche e-mail válido
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "txtUsuarioHeader"))
        ).send_keys("nataliatheodorico@tamandua.org.br")
        logging.info("📩 E-mail preenchido")

        # 5. Preenche senha incorreta
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "txtPassHeader"))
        ).send_keys("senha_incorreta")
        logging.info("🔒 Senha incorreta preenchida")

        # 6. Clica no botão de login
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "btnLoginModalHeader"))
        ).click()
        logging.info("📤 Login submetido")

        # 7. Validação da mensagem de erro (SweetAlert2)
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".swal2-popup.swal2-modal.swal2-show"))
            )
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".swal2-icon.swal2-error"))
            )
            logging.info("🚫 Modal de erro exibido corretamente para senha incorreta")
            
            # Salva screenshot de sucesso
            screenshot_path = screenshot_manager.save_screenshot(driver, "teste_senha_incorreta", "aprovado")
            logging.info(f"📂 Screenshot salvo em: {screenshot_path}")
            logging.info("✅ TESTE APROVADO: Erro tratado como esperado")

        except Exception as erro_validacao:
            logging.error("❌ TESTE REPROVADO: Modal de erro não apareceu como esperado")
            logging.error(str(erro_validacao))
            
            # Salva screenshot de erro de validação
            screenshot_path = screenshot_manager.save_screenshot(driver, "teste_senha_incorreta", "erro_validacao")
            logging.info(f"📂 Screenshot salvo em: {screenshot_path}")
            pytest.fail("Modal de erro não apareceu para senha incorreta")

        time.sleep(4)

    except Exception as e:
        logging.critical("❌ ERRO CRÍTICO DURANTE O FLUXO")
        logging.critical(str(e))
        
        # Salva screenshot de erro crítico
        screenshot_path = screenshot_manager.save_screenshot(driver, "teste_senha_incorreta", "erro_critico")
        logging.info(f"📂 Screenshot salvo em: {screenshot_path}")
        pytest.fail(f"Falha na execução do teste: {str(e)}")

    finally:
        # Mostra o caminho da última screenshot
        ultima_screenshot = screenshot_manager.get_ultima_screenshot()
        if ultima_screenshot:
            logging.info(f"📸 Última screenshot salva em: {ultima_screenshot}")
            
        driver.quit()
        logging.info("🛑 Navegador fechado. Fim do teste\n")

# Execução direta (opcional)
if __name__ == "__main__":
    test_login_email_valido_senha_incorreta()
