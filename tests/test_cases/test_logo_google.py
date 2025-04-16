import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import base64
import os
from src.utils.screenshot_manager import ScreenshotManager

class TestCurtaOnFavicon(unittest.TestCase):
    def setUp(self):
        # Configurar opções do Chrome para evitar detecção de automação
        chrome_options = Options()
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)
        
        # Remover flag do webdriver
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        # Inicializar gerenciador de screenshots
        self.screenshot_manager = ScreenshotManager()
        
        # Base64 do favicon antigo (tamanduá) para comparação - trecho mais específico
        self.old_favicon_signatures = [
            "/9j/4AAQSkZJRgABAQAAAQABAAD",  # Assinatura 1
            "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys"  # Assinatura 2
        ]

    def test_favicon_in_google_results(self):
        driver = self.driver
        
        try:
            # 1. Acessar o Google
            print("🌐 Iniciando teste do logo...")
            print("🔍 Acessando o Google...")
            driver.get("https://www.google.com")
            time.sleep(3)  # Aguardar carregamento inicial
            
            # 2. Realizar a pesquisa por "CurtaOn"
            print("⌨️ Digitando 'CurtaOn' na busca...")
            search_box = self.wait.until(EC.presence_of_element_located((By.NAME, "q")))
            search_box.clear()
            search_box.send_keys("CurtaOn")
            time.sleep(1)  # Pequena pausa antes de pressionar Enter
            print("🔎 Realizando a pesquisa...")
            search_box.send_keys(Keys.RETURN)
            
            # 3. Localizar o favicon do resultado principal
            print("🔍 Procurando o logo do CurtaON nos resultados...")
            self.wait.until(EC.presence_of_element_located((By.ID, "search")))
            time.sleep(2)  # Aguardar carregamento dos resultados
            
            # Tirar screenshot dos resultados
            print("📸 Salvando screenshot dos resultados...")
            self.screenshot_manager.save_screenshot(driver, "teste_logo", "resultados_busca")
            
            # Tentar diferentes seletores para encontrar o favicon
            favicon_selectors = [
                "img.XNo5Ab[src*='data:image']",
                "img[src*='data:image'][alt*='favicon']",
                "img.XNo5Ab"
            ]
            
            favicon = None
            print("🔎 Procurando o logo usando diferentes métodos...")
            for selector in favicon_selectors:
                try:
                    favicon = self.wait.until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    if favicon:
                        print(f"✅ Logo encontrado!")
                        break
                except:
                    continue
            
            if not favicon:
                print("❌ Logo não encontrado em nenhum lugar!")
                self.screenshot_manager.save_screenshot(driver, "teste_logo", "logo_nao_encontrado")
                raise Exception("Logo não encontrado em nenhum dos seletores testados")
            
            # 4. Verificar se o favicon é o antigo
            favicon_src = favicon.get_attribute("src")
            print("🔍 Analisando o logo encontrado...")
            print(f"📝 Código do logo encontrado: {favicon_src[:100]}...")
            
            for signature in self.old_favicon_signatures:
                if signature in favicon_src:
                    print("🚨 ATENÇÃO: Logo antigo do tamanduá detectado!")
                    self.screenshot_manager.save_screenshot(driver, "teste_logo", "logo_antigo_encontrado")
                    raise AssertionError(
                        f"❌ BUG ENCONTRADO: O logo antigo (com tamanduá) ainda está sendo exibido nos resultados do Google.\n"
                        f"🔍 Assinatura encontrada: {signature}"
                    )
            
            print("✨ SUCESSO: O logo novo está sendo exibido corretamente!")
            self.screenshot_manager.save_screenshot(driver, "teste_logo", "logo_novo_encontrado")
                
        except Exception as e:
            print("📸 Salvando screenshot do erro...")
            self.screenshot_manager.save_screenshot(driver, "teste_logo", "erro_teste")
            if "BUG ENCONTRADO" in str(e):
                print(f"❌ {str(e)}")
                raise
            print(f"⚠️ Erro durante o teste: {str(e)}")
            raise Exception(f"❌ Erro durante o teste: {str(e)}")

    def tearDown(self):
        if self.driver:
            print("👋 Finalizando o teste...")
            # Mostra o caminho da última screenshot salva
            self.screenshot_manager.get_ultima_screenshot()
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()