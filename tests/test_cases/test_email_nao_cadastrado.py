import os
import time
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.screenshot_manager import ScreenshotManager

# === GARANTE QUE AS PASTAS EXISTAM ===
os.makedirs("logs", exist_ok=True)
os.makedirs("screenshots", exist_ok=True)

# === CONFIGURAÇÃO DO LOGGING COM UTF-8 ===
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/log_teste_email_nao_cadastrado.log", mode='w', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def test_email_nao_cadastrado():
    """Teste para verificar mensagem de erro com e-mail não cadastrado"""

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    
    # Inicializa o gerenciador de screenshots
    screenshot_manager = ScreenshotManager()

    try:
        logging.info("=" * 60)
        logging.info("🚀 INICIANDO TESTE: EMAIL NÃO CADASTRADO")
        logging.info("=" * 60)

        driver.get("https://curtaon.com.br")
        logging.info("🌐 Site carregado")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "header_MenuCurtaoOn_btnLoginModalEntrar"))
        ).click()
        logging.info("✅ Botão 'Entrar' clicado")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn-login-email"))
        ).click()
        logging.info("✅ Botão 'E-mail' clicado")

        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "txtUsuarioHeader"))
        )
        email_field.clear()
        email_field.send_keys("2213123@hotmail.com")
        logging.info("📩 E-mail preenchido")

        driver.find_element(By.ID, "txtPassHeader").send_keys("qualquer123")
        driver.find_element(By.ID, "btnLoginModalHeader").click()
        logging.info("🔒 Senha preenchida e botão de login clicado")

        # Validação do erro
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.swal2-popup.swal2-modal.swal2-show"))
            )
            mensagem_elemento = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div#swal2-content"))
            )
            mensagem = mensagem_elemento.text.strip()
            logging.info(f"📢 Mensagem exibida: '{mensagem}'")

            assert any(
                phrase in mensagem.lower()
                for phrase in [
                    "e-mail ou senha incorretos",
                    "email ou senha incorretos",
                    "e-mail ou senha incorrectos",
                    "email ou senha incorrectos"
                ]
            ), f"Mensagem não corresponde ao esperado. Recebido: '{mensagem}'"

            # Salva screenshot de sucesso
            screenshot_path = screenshot_manager.save_screenshot(driver, "teste_email_nao_cadastrado", "aprovado")
            logging.info(f"📂 Screenshot salvo em: {screenshot_path}")
            logging.info("✅ TESTE APROVADO: Mensagem de erro exibida corretamente")
            time.sleep(3)

        except Exception as e:
            logging.error("❌ TESTE REPROVADO: Falha ao validar a mensagem de erro")
            logging.error(str(e))
            
            # Salva screenshot de erro do modal
            screenshot_path = screenshot_manager.save_screenshot(driver, "teste_email_nao_cadastrado", "erro_modal")
            logging.info(f"📂 Screenshot salvo em: C:\Projects\curtaON!automacoes\tests\test_cases\test_screenshots\teste_email_nao_cadastrado_erro_modal_20240315_143022.png")
            pytest.fail(f"Falha ao validar mensagem de erro: {str(e)}")

    except Exception as e:
        logging.critical("💥 ERRO CRÍTICO: Falha geral na execução do teste")
        logging.critical(str(e))
        
        # Salva screenshot de erro geral
        screenshot_path = screenshot_manager.save_screenshot(driver, "teste_email_nao_cadastrado", "erro_execucao")
        logging.info(f"📂 Screenshot salvo em: C:\Projects\curtaON!automacoes\tests\test_cases\test_screenshots\teste_email_nao_cadastrado_erro_execucao_20240315_143022.png")
        pytest.fail(f"Falha na execução do teste: {str(e)}")

    finally:
        # Mostra o caminho da última screenshot
        ultima_screenshot = screenshot_manager.get_ultima_screenshot()
        if ultima_screenshot:
            logging.info(f"📸 Última screenshot salva em: {ultima_screenshot}")
            
        driver.quit()
        logging.info("🛑 Navegador fechado. Processo finalizado\n")

if __name__ == "__main__":
    test_email_nao_cadastrado()
