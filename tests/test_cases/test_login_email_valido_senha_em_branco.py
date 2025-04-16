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
        logging.FileHandler("logs/log_teste_senha_em_branco.log", mode='w', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def test_login_email_valido_senha_em_branco():
    """Teste para verificar alerta ao tentar login com e-mail preenchido mas senha em branco"""

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    
    # Inicializa o gerenciador de screenshots
    screenshot_manager = ScreenshotManager()

    try:
        logging.info("=" * 60)
        logging.info("🚨 INICIANDO TESTE: E-MAIL VÁLIDO + SENHA EM BRANCO")
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

        # 5. Deixa o campo senha em branco
        logging.info("🔓 Campo de senha deixado em branco")

        # 6. Clica no botão de login
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "btnLoginModalHeader"))
        ).click()
        logging.info("📤 Login submetido")

        # 7. Validação da mensagem de erro (SweetAlert2)
        try:
            # Espera o modal e o conteúdo da mensagem
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".swal2-popup.swal2-modal.swal2-show"))
            )
            mensagem = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.ID, "swal2-content"))
            ).text.strip()

            logging.info(f"📢 Mensagem exibida: '{mensagem}'")

            assert "campos email e senha são obrigatórios" in mensagem.lower(), \
                f"Mensagem inesperada: '{mensagem}'"

            # Salva screenshot de sucesso
            screenshot_path = screenshot_manager.save_screenshot(driver, "teste_senha_em_branco", "aprovado")
            logging.info(f"📂 Screenshot salvo em: {screenshot_path}")
            logging.info("✅ TESTE APROVADO: Sistema alertou corretamente campos obrigatórios")

        except Exception as erro_validacao:
            logging.error("❌ TESTE REPROVADO: Modal de erro não apareceu ou mensagem incorreta")
            logging.error(str(erro_validacao))
            
            # Salva screenshot de erro de validação
            screenshot_path = screenshot_manager.save_screenshot(driver, "teste_senha_em_branco", "erro_validacao")
            logging.info(f"📂 Screenshot salvo em: {screenshot_path}")
            pytest.fail("Modal de erro não apareceu ou mensagem não era a esperada")

        time.sleep(4)

    except Exception as e:
        logging.critical("❌ ERRO CRÍTICO DURANTE O FLUXO")
        logging.critical(str(e))
        
        # Salva screenshot de erro crítico
        screenshot_path = screenshot_manager.save_screenshot(driver, "teste_senha_em_branco", "erro_critico")
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
    test_login_email_valido_senha_em_branco()
