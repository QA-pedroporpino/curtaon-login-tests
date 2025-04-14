# 🏗️ Arquitetura do Framework

## Visão Geral

O framework de automação do CurtaON segue uma arquitetura baseada em Page Objects, com uma clara separação de responsabilidades. Esta arquitetura foi projetada para ser:

- **Manutenível**: Fácil de atualizar quando a aplicação muda
- **Escalável**: Fácil de adicionar novos testes
- **Legível**: Fácil de entender o que cada parte faz
- **Reutilizável**: Evita duplicação de código

## Componentes Principais

### 1. Page Objects (`src/pages/`)

Os Page Objects encapsulam a lógica de interação com as páginas da aplicação. Cada página tem sua própria classe com métodos que representam ações que podem ser realizadas naquela página.

Exemplo:

```python
class LoginPage:
    def acessar_site(self):
        # Acessa o site
        return self

    def fazer_login(self, email, senha):
        # Realiza o login
        return self
```

### 2. Configurações (`src/config/`)

As configurações centralizam constantes, URLs, timeouts e outros parâmetros do framework. Isso facilita a manutenção, pois alterações precisam ser feitas em apenas um lugar.

Exemplo:

```python
class TestConfig:
    URL_BASE = "https://curtaon.com.br"
    TIMEOUT_PADRAO = 10
```

### 3. Dados de Teste (`src/data/`)

Os dados de teste separam os dados utilizados nos testes do código de teste em si. Isso facilita a manutenção e permite reutilizar os mesmos dados em diferentes testes.

Exemplo:

```python
class TestData:
    EMAIL_INVALIDO = "123"
    SENHA_PADRAO = "qualquer123"
```

### 4. Utilitários (`src/utils/`)

Os utilitários fornecem funcionalidades comuns como logging, captura de screenshots e outras funções auxiliares.

Exemplo:

```python
class ScreenshotManager:
    @staticmethod
    def take_screenshot(driver, name, success=True):
        # Captura screenshot
        return filename
```

### 5. Casos de Teste (`tests/test_cases/`)

Os casos de teste utilizam os Page Objects, configurações, dados e utilitários para implementar os cenários de teste.

Exemplo:

```python
def test_email_formato_invalido(self, driver, login_page):
    # Executa o teste
    login_page.fazer_login(TestData.EMAIL_INVALIDO, TestData.SENHA_PADRAO)
    # Valida o resultado
```

## Fluxo de Execução

1. O pytest inicia a execução dos testes
2. As fixtures do `conftest.py` são executadas, fornecendo o driver e os Page Objects
3. O teste é executado, utilizando os Page Objects para interagir com a aplicação
4. Os utilitários são utilizados para logging e captura de screenshots
5. Os resultados são registrados e relatórios são gerados

## Benefícios da Arquitetura

- **Separação de Responsabilidades**: Cada componente tem uma função específica
- **Reutilização de Código**: Evita duplicação de código
- **Manutenibilidade**: Facilita a manutenção quando a aplicação muda
- **Legibilidade**: Código mais limpo e fácil de entender
- **Escalabilidade**: Fácil de adicionar novos testes e funcionalidades
