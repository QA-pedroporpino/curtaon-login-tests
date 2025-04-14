import os
import time
from datetime import datetime

class ScreenshotManager:
    def __init__(self, base_dir="test_screenshots"):
        """
        Inicializa o gerenciador de screenshots
        :param base_dir: Diretório base para salvar os screenshots
        """
        self.base_dir = os.path.abspath(base_dir)  # Converte para caminho absoluto
        self._create_base_directory()
        self.ultima_screenshot = None  # Armazena o caminho da última screenshot
        print(f"📁 Pasta de screenshots: {self.base_dir}")
        
    def _create_base_directory(self):
        """Cria o diretório base se não existir"""
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)
            print(f"📁 Criada pasta de screenshots: {self.base_dir}")
            
    def _get_timestamp(self):
        """Retorna timestamp formatado para nome do arquivo"""
        return datetime.now().strftime("%Y%m%d_%H%M%S")
        
    def save_screenshot(self, driver, test_name, step_name):
        """
        Salva um screenshot com nome padronizado
        :param driver: Instância do WebDriver
        :param test_name: Nome do teste (ex: 'teste_login')
        :param step_name: Nome do passo (ex: 'login_sucesso')
        """
        timestamp = self._get_timestamp()
        filename = f"{test_name}_{step_name}_{timestamp}.png"
        filepath = os.path.join(self.base_dir, filename)
        
        try:
            driver.save_screenshot(filepath)
            self.ultima_screenshot = filepath  # Armazena o caminho da última screenshot
            print(f"📸 Screenshot salvo com sucesso!")
            print(f"📂 Caminho completo: {filepath}")
            return filepath
        except Exception as e:
            print(f"❌ Erro ao salvar screenshot: {str(e)}")
            return None
            
    def get_screenshot_dir(self):
        """Retorna o diretório base dos screenshots"""
        return self.base_dir
        
    def get_ultima_screenshot(self):
        """Retorna o caminho da última screenshot salva"""
        if self.ultima_screenshot:
            print(f"📸 Última screenshot salva em: {self.ultima_screenshot}")
            return self.ultima_screenshot
        else:
            print("❌ Nenhuma screenshot foi salva ainda")
            return None 