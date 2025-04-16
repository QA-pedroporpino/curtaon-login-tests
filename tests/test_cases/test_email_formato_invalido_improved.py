import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import os
import datetime
from utils.screenshot_manager import ScreenshotManager

# Configurações básicas
class Config:
    URL = "https://curtaon.com.br"
    TIMEOUT = 10
    
    # Seletores dos elementos na página
    BOTAO_ENTRAR = "header_MenuCurtaoOn_btnLoginModalEntrar"
    BOTAO_EMAIL = "btn-login-email"
    CAMPO_USUARIO = "txtUsuarioHeader"
    CAMPO_SENHA = "txtPassHeader"
    BOTAO_LOGIN = "btnLoginModalHeader"
    MENSAGEM_ERRO = "//*[contains(text(), 'Email inválido!')]"
    
    # Mensagens esperadas
    EMAIL_INVALIDO = "Email inválido!"

# Dados de teste
class Dados:
    EMAIL_INVALIDO = "123"
    SENHA = "qualquer123"

# Gerenciador de logs com emojis
class Logger:
    @staticmethod
    def criar(nome_teste):
        logger = logging.getLogger(nome_teste)
        logger.setLevel(logging.INFO)
        
        # Limpa handlers existentes
        if logger.handlers:
            logger.handlers.clear()
        
        # Cria pasta de logs
        os.makedirs("logs", exist_ok=True)
        
        # Log para arquivo
        arquivo = logging.FileHandler(f"logs/log_{nome_teste}.log", mode='w', encoding='utf-8')
        arquivo.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        logger.addHandler(arquivo)
        
        # Log para terminal com emojis
        terminal = logging.StreamHandler()
        terminal.setFormatter(EmojiFormatter())
        logger.addHandler(terminal)
        
        return logger

# Formatador de logs com emojis
class EmojiFormatter(logging.Formatter):
    # Emojis para níveis de log
    NIVEIS = {
        logging.DEBUG: "🔍",
        logging.INFO: "ℹ️",
        logging.WARNING: "⚠️",
        logging.ERROR: "❌",
        logging.CRITICAL: "🔥"
    }
    
    # Emojis para palavras-chave
    PALAVRAS = {
        "iniciando": "🚀",
        "aprovado": "✅",
        "reprovado": "❌",
        "erro": "❌",
        "sucesso": "✅",
        "site": "🌐",
        "clicado": "🖱️",
        "preenchido": "✏️",
        "mensagem": "📢",
        "screenshot": "📸",
        "navegador": "🌐",
        "fechado": "🛑",
        "fim": "🏁",
        "teste": "🧪",
        "login": "🔑",
        "email": "📧",
        "senha": "🔒",
        "botão": "🔘",
        "formulário": "📝",
        "submetido": "📤",
        "validação": "🔍",
        "exibida": "👀",
        "salvo": "💾",
        "algo deu errado": "💥",
        "durante": "⏱️",
        "execução": "⚙️",
        "fluxo": "🔄",
        "obtém": "🔍",
        "valida": "✅",
        "registra": "📝",
        "falha": "❌",
        "raise": "💥",
        "separador": "🔷",
        "configuração": "⚙️",
        "dados": "📊",
        "logger": "📝",
        "formatador": "🎨",
        "screenshot": "📸",
        "página": "📄",
        "driver": "🚗",
        "espera": "⏳",
        "elemento": "🔍",
        "visível": "👁️",
        "clicável": "🖱️",
        "encontrado": "🔍",
        "não encontrado": "❓",
        "texto": "📝",
        "assert": "✅",
        "exceção": "💥",
        "finalmente": "🏁",
        "fixture": "🔧",
        "execução": "▶️",
        "principal": "🎯",
        "configuração": "⚙️",
        "terminal": "🖥️",
        "arquivo": "📁",
        "pasta": "📂",
        "criado": "✨",
        "limpo": "🧹",
        "handler": "🔌",
        "formatter": "🎨",
        "mensagem": "💬",
        "hora": "⏰",
        "colorido": "🎨",
        "ciano": "🔵",
        "final": "🏁",
        "início": "🚀",
        "meio": "🔄",
        "processo": "⚙️",
        "passo": "👣",
        "etapa": "📋",
        "concluído": "✅",
        "falhou": "❌",
        "erro": "💥",
        "aviso": "⚠️",
        "crítico": "🔥",
        "debug": "🔍",
        "info": "ℹ️",
        "warning": "⚠️",
        "error": "❌",
        "critical": "🔥",
        "nivel": "📊",
        "palavra": "📝",
        "chave": "🔑",
        "valor": "💎",
        "mapeamento": "🗺️",
        "adiciona": "➕",
        "remove": "➖",
        "verifica": "🔍",
        "contém": "🔍",
        "não contém": "❌",
        "formata": "🎨",
        "retorna": "↩️",
        "captura": "📸",
        "salva": "💾",
        "define": "⚙️",
        "cria": "✨",
        "acessa": "🔗",
        "clica": "🖱️",
        "preenche": "✏️",
        "obtém": "🔍",
        "espera": "⏳",
        "até": "⏱️",
        "ser": "🔍",
        "visível": "👁️",
        "clicável": "🖱️",
        "localizado": "🔍",
        "encontrado": "🔍",
        "texto": "📝",
        "strip": "🧹",
        "assert": "✅",
        "em": "🔍",
        "mensagem": "💬",
        "esperada": "✅",
        "não": "❌",
        "foi": "❌",
        "exibida": "👀",
        "recebido": "📥",
        "registra": "📝",
        "sucesso": "✅",
        "falha": "❌",
        "captura": "📸",
        "screenshot": "📸",
        "erro": "❌",
        "raise": "💥",
        "finally": "🏁",
        "fim": "🏁",
        "teste": "🧪",
        "driver": "🚗",
        "options": "⚙️",
        "chrome": "🌐",
        "maximized": "🔲",
        "yield": "↩️",
        "quit": "🛑",
        "login_page": "🔑",
        "execução": "▶️",
        "direta": "🎯",
        "configuração": "⚙️",
        "exibir": "👀",
        "logs": "📝",
        "terminal": "🖥️",
        "basicConfig": "⚙️",
        "level": "📊",
        "INFO": "ℹ️",
        "executa": "▶️",
        "main": "🎯",
        "file": "📄",
        "v": "✅",
        "capture": "📸",
        "no": "❌"
    }
    
    def format(self, record):
        # Emoji baseado no nível de log
        nivel_emoji = self.NIVEIS.get(record.levelno, "")
        
        # Adiciona emojis baseados em palavras-chave
        mensagem = record.msg
        for palavra, emoji in self.PALAVRAS.items():
            if palavra.lower() in mensagem.lower():
                # Adiciona o emoji apenas se ainda não estiver na mensagem
                if emoji not in mensagem:
                    mensagem = f"{emoji} {mensagem}"
        
        # Adiciona hora colorida
        hora = datetime.datetime.now().strftime("%H:%M:%S")
        hora_colorida = f"\033[36m{hora}\033[0m"  # Ciano
        
        # Formata a mensagem final
        return f"{hora_colorida} {nivel_emoji} {mensagem}"

# Gerenciador de screenshots
class Screenshot:
    @staticmethod
    def capturar(driver, nome, sucesso=True):
        # Cria pasta de screenshots
        os.makedirs("screenshots", exist_ok=True)
        
        # Define nome do arquivo
        prefixo = "teste" if sucesso else "erro"
        arquivo = f"screenshots/{prefixo}_{nome}.png"
        
        # Captura o screenshot
        driver.save_screenshot(arquivo)
        return arquivo

# Página de login
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.TIMEOUT)
        self.screenshot_manager = ScreenshotManager()
    
    def acessar_site(self):
        self.driver.get(Config.URL)
        return self
    
    def clicar_botao_entrar(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, Config.BOTAO_ENTRAR)
        )).click()
        return self
    
    def clicar_botao_email(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, Config.BOTAO_EMAIL)
        )).click()
        return self
    
    def fazer_login(self, email, senha):
        self.driver.find_element(By.ID, Config.CAMPO_USUARIO).send_keys(email)
        self.driver.find_element(By.ID, Config.CAMPO_SENHA).send_keys(senha)
        self.driver.find_element(By.ID, Config.BOTAO_LOGIN).click()
        return self
    
    def obter_mensagem_erro(self):
        erro = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, Config.MENSAGEM_ERRO))
        )
        return erro.text.strip()

# Teste de email inválido
class TestLoginEmailInvalido:
    """Teste para verificar mensagem de erro ao digitar email em formato inválido"""
    
    def setup_method(self):
        """Setup executado antes de cada método de teste"""
        self.logger = Logger.criar("email_formato_invalido")
        self.logger.info("=" * 60)
        self.logger.info("🚀 INICIANDO TESTE: FORMATO INVÁLIDO DE E-MAIL")
        self.logger.info("=" * 60)
    
    def test_email_formato_invalido(self, driver, login_page):
        """Teste para verificar mensagem de erro ao digitar email em formato inválido"""
        try:
            # Executa o fluxo de login
            self.logger.info("🔄 Iniciando fluxo de login com email inválido")
            
            self.logger.info("🌐 Acessando o site do CurtaON")
            login_page.acessar_site()
            
            self.logger.info("🔘 Clicando no botão 'Entrar'")
            login_page.clicar_botao_entrar()
            
            self.logger.info("🔘 Clicando no botão 'E-mail'")
            login_page.clicar_botao_email()
            
            self.logger.info(f"✏️ Preenchendo formulário com email inválido: '{Dados.EMAIL_INVALIDO}'")
            login_page.fazer_login(Dados.EMAIL_INVALIDO, Dados.SENHA)
            
            self.logger.info("✅ Fluxo de login executado com sucesso")
            
            # Obtém e valida a mensagem de erro
            self.logger.info("🔍 Obtendo mensagem de erro exibida")
            mensagem = login_page.obter_mensagem_erro()
            self.logger.info(f"📢 Mensagem exibida: '{mensagem}'")
            
            self.logger.info("🔍 Validando mensagem de erro")
            assert Config.EMAIL_INVALIDO in mensagem, \
                f"Mensagem esperada não foi exibida. Recebido: '{mensagem}'"
            
            # Registra sucesso
            self.logger.info("📸 Capturando screenshot de sucesso")
            screenshot_path = login_page.screenshot_manager.save_screenshot(driver, "teste_email_invalido", "sucesso")
            self.logger.info(f"📂 Screenshot salvo em: {screenshot_path}")
            self.logger.info("✅ TESTE APROVADO: Sistema identificou formato inválido corretamente")
            
        except Exception as e:
            # Registra falha
            self.logger.error(f"❌ TESTE REPROVADO: {str(e)}")
            self.logger.info("📸 Capturando screenshot de erro")
            screenshot_path = login_page.screenshot_manager.save_screenshot(driver, "teste_email_invalido", "erro")
            self.logger.info(f"📂 Screenshot salvo em: {screenshot_path}")
            raise
        finally:
            # Mostra o caminho da última screenshot
            ultima_screenshot = login_page.screenshot_manager.get_ultima_screenshot()
            if ultima_screenshot:
                self.logger.info(f"📸 Última screenshot salva em: {ultima_screenshot}")
            
            self.logger.info("=" * 60)
            self.logger.info("🏁 FIM DO TESTE")
            self.logger.info("=" * 60)

# Configurações do pytest
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

# Execução direta
if __name__ == "__main__":
    # Configuração para exibir logs no terminal
    logging.basicConfig(level=logging.INFO)
    
    # Executa o teste
    pytest.main([__file__, "-v", "--capture=no"]) 