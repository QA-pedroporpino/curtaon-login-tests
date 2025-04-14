import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import os
import datetime

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
    
    # Mensagens esperadas
    EMAIL_INVALIDO = "Email inválido!"
    EMAIL_NAO_CADASTRADO = "Email não cadastrado!"
    SENHA_INCORRETA = "Senha incorreta!"
    CAMPOS_EM_BRANCO = "Preencha todos os campos!"
    EMAIL_EM_BRANCO = "Preencha o campo de email!"
    SENHA_EM_BRANCO = "Preencha o campo de senha!"
    EMAIL_MALFORMADO = "Email inválido!"
    EMAIL_COM_ESPACO = "Email inválido!"

# Dados de teste
class Dados:
    EMAIL_INVALIDO = "123"
    EMAIL_NAO_CADASTRADO = "naoexiste@email.com"
    EMAIL_VALIDO = "nataliatheodorico@tamandua.org.br"
    SENHA_CORRETA = "123456"
    SENHA_INCORRETA = "senha_errada"
    SENHA = "qualquer123"
    EMAIL_COM_ESPACO = "teste @email.com"

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
    
    def obter_mensagem_erro(self, mensagem_esperada):
        """Obtém a mensagem de erro específica"""
        xpath = f"//*[contains(text(), '{mensagem_esperada}')]"
        erro = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        return erro.text.strip()

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