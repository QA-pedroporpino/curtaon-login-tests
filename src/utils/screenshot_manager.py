import os
import time
from datetime import datetime
from typing import Optional

class ScreenshotManager:
    def __init__(self, base_dir: str = "screenshots"):
        """
        Inicializa o gerenciador de screenshots
        :param base_dir: Diretório base para salvar os screenshots
        """
        self.base_dir = os.path.abspath(base_dir)
        self._create_base_directory()
        self.ultima_screenshot: Optional[str] = None
        print(f"📁 Pasta de screenshots: {self.base_dir}")
        
    def _create_base_directory(self) -> None:
        """Cria o diretório base se não existir"""
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)
            print(f"📁 Criada pasta de screenshots: {self.base_dir}")
            
    def _get_timestamp(self) -> str:
        """Retorna timestamp formatado para nome do arquivo"""
        return datetime.now().strftime("%Y%m%d_%H%M%S")
        
    def take_screenshot(self, driver, test_name: str, status: str = "aprovado") -> Optional[str]:
        """
        Salva um screenshot com nome padronizado
        :param driver: Instância do WebDriver
        :param test_name: Nome do teste (ex: 'teste_login')
        :param status: Status do teste ('aprovado' ou 'erro')
        :return: Caminho do arquivo salvo ou None em caso de erro
        """
        timestamp = self._get_timestamp()
        filename = f"{test_name}_{status}_{timestamp}.png"
        filepath = os.path.join(self.base_dir, filename)
        
        try:
            driver.save_screenshot(filepath)
            self.ultima_screenshot = filepath
            print(f"📸 Screenshot salvo com sucesso!")
            print(f"📂 Caminho: {filepath}")
            return filepath
        except Exception as e:
            print(f"❌ Erro ao salvar screenshot: {str(e)}")
            return None
            
    def save_screenshot(self, driver, test_name: str, status: str = "aprovado") -> Optional[str]:
        """
        Alias para take_screenshot para manter compatibilidade com testes existentes
        :param driver: Instância do WebDriver
        :param test_name: Nome do teste (ex: 'teste_login')
        :param status: Status do teste ('aprovado' ou 'erro')
        :return: Caminho do arquivo salvo ou None em caso de erro
        """
        return self.take_screenshot(driver, test_name, status)
            
    def get_screenshot_dir(self) -> str:
        """Retorna o diretório base dos screenshots"""
        return self.base_dir
        
    def get_ultima_screenshot(self) -> Optional[str]:
        """Retorna o caminho da última screenshot salva"""
        if self.ultima_screenshot:
            print(f"📸 Última screenshot salva em: {self.ultima_screenshot}")
            return self.ultima_screenshot
        print("❌ Nenhuma screenshot foi salva ainda")
        return None 