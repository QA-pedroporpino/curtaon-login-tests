class TestConfig:
    # URLs
    URL_BASE = "https://curtaon.com.br"
    
    # Timeouts
    TIMEOUT_PADRAO = 10
    TIMEOUT_LONGO = 15
    
    # Diretórios
    DIR_SCREENSHOTS = "screenshots"
    DIR_LOGS = "logs"
    
    # Seletores
    class Seletores:
        BOTAO_ENTRAR = "header_MenuCurtaoOn_btnLoginModalEntrar"
        BOTAO_EMAIL = "btn-login-email"
        CAMPO_USUARIO = "txtUsuarioHeader"
        CAMPO_SENHA = "txtPassHeader"
        BOTAO_LOGIN = "btnLoginModalHeader"
        MENSAGEM_ERRO = "//*[contains(text(), 'Email inválido!')]"
    
    # Mensagens
    class Mensagens:
        EMAIL_INVALIDO = "Email inválido!"
        CAMPOS_OBRIGATORIOS = "campos email e senha são obrigatórios"
        EMAIL_SENHA_INCORRETOS = "e-mail ou senha incorretos" 