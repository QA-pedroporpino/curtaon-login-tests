# 📝 Padrões de Código

Este documento descreve os padrões de código adotados no framework de automação do CurtaON. Seguir estes padrões ajuda a manter o código consistente, legível e fácil de manter.

## Estilo Python

### PEP 8

Seguimos o estilo PEP 8 para Python. Alguns pontos importantes:

- Use 4 espaços para indentação (não tabs)
- Limite o comprimento das linhas a 79 caracteres
- Use espaços em branco para melhorar a legibilidade
- Use nomes descritivos para variáveis, funções e classes

### Docstrings

Use docstrings para documentar módulos, classes e funções:

```python
def fazer_login(self, email, senha):
    """
    Realiza o processo de login com email e senha.

    Args:
        email (str): Email do usuário
        senha (str): Senha do usuário

    Returns:
        self: Permite encadeamento de métodos
    """
    self.preencher_email(email)
    self.preencher_senha(senha)
    self.clicar_botao_login()
    return self
```

### Comentários

Use comentários para explicar o "porquê" e não o "o quê":

```python
# Não faça isso:
# Preenche o campo de email
email_field.send_keys(email)

# Faça isso:
# Usa o email de teste para validar o fluxo de login
email_field.send_keys(TestData.Login.EMAIL_VALIDO)
```

## Estrutura de Arquivos

### Nomes de Arquivos

- Use nomes em minúsculas com underscores: `login_page.py`
- Use prefixos para indicar o tipo: `test_login.py`
- Evite nomes genéricos: `utils.py` → `screenshot_manager.py`

### Organização de Imports

Organize os imports na seguinte ordem:

1. Imports da biblioteca padrão
2. Imports de bibliotecas de terceiros
3. Imports locais do projeto

Exemplo:

```python
import os
import time
import logging

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from src.config.test_config import TestConfig
from src.data.test_data import TestData
```

## Page Objects

### Estrutura de Classe

```python
class LoginPage:
    """Page Object para a página de login."""

    def __init__(self, driver):
        """
        Inicializa o Page Object.

        Args:
            driver: Instância do WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, TestConfig.TIMEOUT_PADRAO)

    def acessar_site(self):
        """Acessa o site do CurtaON."""
        self.driver.get(TestConfig.URL_BASE)
        return self

    def fazer_login(self, email, senha):
        """
        Realiza o processo de login.

        Args:
            email (str): Email do usuário
            senha (str): Senha do usuário

        Returns:
            self: Permite encadeamento de métodos
        """
        self.preencher_email(email)
        self.preencher_senha(senha)
        self.clicar_botao_login()
        return self
```

### Métodos de Ação

- Use verbos para nomes de métodos: `clicar_botao`, `preencher_campo`
- Retorne `self` para permitir encadeamento de métodos
- Separe ações complexas em métodos menores

## Testes

### Estrutura de Teste

```python
class TestLogin:
    """Testes relacionados ao login."""

    def setup_method(self):
        """Setup executado antes de cada método de teste."""
        self.logger = TestLogger.setup_logger("login")

    def test_login_sucesso(self, driver, login_page):
        """
        Testa o login com credenciais válidas.

        Verifica se o usuário é redirecionado para a página inicial após o login.
        """
        try:
            # Arrange
            email = TestData.Login.EMAIL_VALIDO
            senha = TestData.Login.SENHA_VALIDA

            # Act
            login_page.acessar_site().fazer_login(email, senha)

            # Assert
            assert "Bem-vindo" in driver.page_source

            # Registra sucesso
            ScreenshotManager.take_screenshot(driver, "login_sucesso", True)
            self.logger.info("✅ TESTE APROVADO")

        except Exception as e:
            # Registra falha
            ScreenshotManager.take_screenshot(driver, "login_sucesso", False)
            self.logger.error(f"❌ TESTE REPROVADO: {str(e)}")
            raise
```

### Padrões de Nomeação

- Use prefixo `test_` para métodos de teste
- Use nomes descritivos que indiquem o que está sendo testado
- Agrupe testes relacionados em classes

### Organização de Testes

- Siga o padrão AAA (Arrange, Act, Assert)
- Separe a preparação, ação e verificação
- Use comentários para indicar cada seção

## Logging

### Níveis de Log

- `DEBUG`: Informações detalhadas para depuração
- `INFO`: Informações gerais sobre o progresso
- `WARNING`: Avisos sobre situações inesperadas
- `ERROR`: Erros que não impedem a execução
- `CRITICAL`: Erros críticos que impedem a execução

### Mensagens de Log

- Use mensagens claras e descritivas
- Inclua informações relevantes: valores, IDs, etc.
- Use emojis para melhor visualização: ✅, ❌, 🚀, etc.

## Tratamento de Erros

### Try/Except

Use try/except para capturar e tratar erros específicos:

```python
try:
    # Código que pode gerar erro
    elemento = driver.find_element(By.ID, "elemento")
except NoSuchElementException:
    # Tratamento específico
    self.logger.error("Elemento não encontrado")
    raise
except Exception as e:
    # Tratamento genérico
    self.logger.error(f"Erro inesperado: {str(e)}")
    raise
```

### Assertions

Use assertions para validar condições:

```python
assert "Bem-vindo" in driver.page_source, "Mensagem de boas-vindas não encontrada"
```

## Configuração

### Constantes

Use classes para agrupar constantes relacionadas:

```python
class TestConfig:
    """Configurações do framework."""

    # URLs
    URL_BASE = "https://curtaon.com.br"

    # Timeouts
    TIMEOUT_PADRAO = 10
    TIMEOUT_LONGO = 15

    # Seletores
    class Seletores:
        BOTAO_ENTRAR = "header_MenuCurtaoOn_btnLoginModalEntrar"
        CAMPO_USUARIO = "txtUsuarioHeader"
```

## Dados de Teste

### Organização

Use classes para agrupar dados relacionados:

```python
class TestData:
    """Dados de teste."""

    # Dados de login
    class Login:
        EMAIL_VALIDO = "usuario@exemplo.com"
        SENHA_VALIDA = "senha123"
        EMAIL_INVALIDO = "123"
```

## Conclusão

Seguir estes padrões ajuda a manter o código consistente, legível e fácil de manter. Eles são baseados em boas práticas de desenvolvimento Python e automação de testes.
