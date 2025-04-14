# 🚀 Primeiros Passos

Este guia fornece uma introdução rápida ao framework de automação do CurtaON, ajudando você a começar a usar e desenvolver testes.

## Estrutura do Projeto

O framework segue uma estrutura organizada:

```
curtaON-automacoes/
├── docs/                    # Documentação
├── reports/                 # Relatórios de execução
├── src/                     # Código fonte
│   ├── config/             # Configurações
│   ├── data/               # Dados de teste
│   ├── pages/              # Page Objects
│   └── utils/              # Utilitários
├── tests/                  # Testes
│   ├── test_cases/        # Casos de teste
│   └── conftest.py        # Configurações do pytest
```

## Executando Testes

### Executar Todos os Testes

```bash
pytest tests/
```

### Executar um Teste Específico

```bash
pytest tests/test_cases/test_email_formato_invalido_improved.py -v
```

### Executar com Relatório HTML

```bash
pytest --html=reports/report.html
```

## Criando um Novo Teste

### 1. Identifique a Página

Primeiro, identifique qual página você precisa automatizar. Se já existir um Page Object para ela, use-o. Caso contrário, crie um novo.

### 2. Crie ou Use um Page Object

Os Page Objects encapsulam a lógica de interação com as páginas. Exemplo:

```python
# src/pages/login_page.py
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TestConfig.TIMEOUT_PADRAO)

    def acessar_site(self):
        self.driver.get(TestConfig.URL_BASE)
        return self

    def fazer_login(self, email, senha):
        self.preencher_email(email)
        self.preencher_senha(senha)
        self.clicar_botao_login()
        return self
```

### 3. Crie um Caso de Teste

Crie um arquivo de teste na pasta `tests/test_cases/`:

```python
# tests/test_cases/test_novo_caso.py
import pytest
from src.utils.test_logger import TestLogger
from src.utils.screenshot_manager import ScreenshotManager
from src.config.test_config import TestConfig
from src.data.test_data import TestData

class TestNovoCaso:
    def setup_method(self):
        self.logger = TestLogger.setup_logger("novo_caso")
        self.logger.info("🚀 INICIANDO TESTE: NOVO CASO")

    def test_novo_caso(self, driver, login_page):
        try:
            # Executa o fluxo
            login_page.acessar_site().fazer_login(
                TestData.Login.EMAIL_VALIDO,
                TestData.Login.SENHA_VALIDA
            )

            # Validação
            assert "Bem-vindo" in driver.page_source

            # Registra sucesso
            ScreenshotManager.take_screenshot(driver, "novo_caso", True)
            self.logger.info("✅ TESTE APROVADO")

        except Exception as e:
            ScreenshotManager.take_screenshot(driver, "novo_caso", False)
            self.logger.error(f"❌ TESTE REPROVADO: {str(e)}")
            raise
```

## Boas Práticas

1. **Use Page Objects**: Encapsule a lógica de interação com as páginas
2. **Separe Dados de Código**: Use classes de dados para armazenar dados de teste
3. **Faça Logs Detalhados**: Use o sistema de logging para registrar o que acontece
4. **Capture Screenshots**: Capture screenshots em caso de sucesso e erro
5. **Use Fixtures**: Aproveite as fixtures do pytest para configuração
6. **Documente seu Código**: Use docstrings e comentários para explicar o código

## Próximos Passos

- Explore os testes existentes para entender como eles funcionam
- Leia a documentação completa na pasta `docs/`
- Experimente criar seus próprios testes
- Contribua com melhorias para o framework
