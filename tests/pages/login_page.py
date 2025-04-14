from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.config.test_config import TestConfig

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TestConfig.TIMEOUT_PADRAO)
    
    def acessar_site(self):
        """Acessa o site do CurtaON"""
        self.driver.get(TestConfig.URL_BASE)
        return self
    
    def clicar_botao_entrar(self):
        """Clica no botão de entrar"""
        self.wait.until(
            EC.element_to_be_clickable((By.ID, TestConfig.Seletores.BOTAO_ENTRAR))
        ).click()
        return self
    
    def clicar_botao_email(self):
        """Clica no botão de email"""
        self.wait.until(
            EC.element_to_be_clickable((By.ID, TestConfig.Seletores.BOTAO_EMAIL))
        ).click()
        return self
    
    def preencher_email(self, email):
        """Preenche o campo de email"""
        campo = self.wait.until(
            EC.presence_of_element_located((By.ID, TestConfig.Seletores.CAMPO_USUARIO))
        )
        campo.clear()
        campo.send_keys(email)
        return self
    
    def preencher_senha(self, senha):
        """Preenche o campo de senha"""
        self.driver.find_element(By.ID, TestConfig.Seletores.CAMPO_SENHA).send_keys(senha)
        return self
    
    def clicar_botao_login(self):
        """Clica no botão de login"""
        self.driver.find_element(By.ID, TestConfig.Seletores.BOTAO_LOGIN).click()
        return self
    
    def fazer_login(self, email, senha):
        """Realiza o processo completo de login"""
        return (self
                .preencher_email(email)
                .preencher_senha(senha)
                .clicar_botao_login())
    
    def obter_mensagem_erro(self):
        """Obtém a mensagem de erro exibida"""
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, TestConfig.Seletores.MENSAGEM_ERRO))
        ).text.strip() 