import os
from datetime import datetime

class ScreenshotManager:
    @staticmethod
    def take_screenshot(driver, name, success=True):
        """Tira uma screenshot e salva com nome e status apropriados"""
        os.makedirs("screenshots", exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        status = "aprovado" if success else "erro"
        filename = f"screenshots/{name}_{status}_{timestamp}.png"
        
        driver.save_screenshot(filename)
        return filename 