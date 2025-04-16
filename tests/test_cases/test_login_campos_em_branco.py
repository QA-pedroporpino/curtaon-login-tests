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
        logging.FileHandler("logs/log_teste_campos_em_branco.log", mode='w', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def test_login_campos_em_branco():
    """Teste para verificar mensagem de erro ao tentar login sem preencher nenhum campo"""

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    
    # Inicializa o gerenciador de screenshots
    screenshot_manager = ScreenshotManager()

    try:
        logging.info("=" * 60)
        logging.info("🚨 INICIANDO TESTE: CAMPOS EM BRANCO")
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

        # 4. Não preenche nada e clica direto no botão de login
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "btnLoginModalHeader"))
        ).click()
        logging.info("📤 Tentativa de login com campos em branco")

        # 5. Validação da mensagem de erro SweetAlert2
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.swal2-popup.swal2-modal.swal2-show"))
            )
            mensagem = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.ID, "swal2-content"))
            ).text.strip()

            logging.info(f"📢 Mensagem exibida: '{mensagem}'")
            assert "campos email e senha são obrigatórios" in mensagem.lower()

            # Salva screenshot de sucesso
            screenshot_path = screenshot_manager.save_screenshot(driver, "teste_campos_em_branco", "aprovado")
            logging.info(f"📂 Screenshot salvo em: {screenshot_path}")
            logging.info("✅ TESTE APROVADO: Erro exibido corretamente para campos em branco")

        except Exception as erro_modal:
            logging.error("❌ TESTE REPROVADO: Modal de erro não apareceu como esperado")
            logging.error(str(erro_modal))
            
            # Salva screenshot de erro do modal
            screenshot_path = screenshot_manager.save_screenshot(driver, "teste_campos_em_branco", "erro_modal")
            logging.info(f"📂 Screenshot salvo em: {screenshot_path}")
            pytest.fail("Modal de erro não apareceu para campos em branco")

        time.sleep(4)

    except Exception as e:
        logging.critical("❌ ERRO CRÍTICO DURANTE O FLUXO")
        logging.critical(str(e))
        
        # Salva screenshot de erro geral
        screenshot_path = screenshot_manager.save_screenshot(driver, "teste_campos_em_branco", "erro_critico")
        logging.info(f"📂 Screenshot salvo em: {screenshot_path}")
        pytest.fail(f"Falha na execução do teste: {str(e)}")

    finally:
        # Mostra o caminho da última screenshot
        ultima_screenshot = screenshot_manager.get_ultima_screenshot()
        if ultima_screenshot:
            logging.info(f"📸 Última screenshot salva em: {ultima_screenshot}")
            
        driver.quit()
        logging.info("🛑 Navegador fechado. Fim do teste\n")

# Execução direta
if __name__ == "__main__":
    test_login_campos_em_branco()
