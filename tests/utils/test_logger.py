import logging
import os

class TestLogger:
    @staticmethod
    def setup_logger(test_name):
        """Configura o logger para o teste específico"""
        os.makedirs("logs", exist_ok=True)
        log_file = f"logs/log_{test_name}.log"
        
        logger = logging.getLogger(test_name)
        logger.setLevel(logging.INFO)
        
        # Limpa handlers existentes
        logger.handlers = []
        
        # Handler para arquivo
        file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        )
        
        # Handler para console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        )
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        return logger 