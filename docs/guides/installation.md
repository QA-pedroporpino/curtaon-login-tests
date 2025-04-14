# 🔧 Guia de Instalação

Este guia fornece instruções detalhadas para instalar e configurar o framework de automação do CurtaON.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git
- Chrome WebDriver compatível com sua versão do Chrome

## Instalação

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/curtaON-automacoes.git
cd curtaON-automacoes
```

### 2. Crie um Ambiente Virtual

É recomendado usar um ambiente virtual para isolar as dependências do projeto:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o WebDriver

O framework utiliza o Selenium WebDriver para automação. Você pode:

- Baixar o ChromeDriver manualmente e adicionar ao PATH
- Ou usar o webdriver-manager (já incluído nas dependências)

### 5. Configure Variáveis de Ambiente (Opcional)

Crie um arquivo `.env` na raiz do projeto para configurar variáveis de ambiente:

```
BASE_URL=https://curtaon.com.br
TIMEOUT=10
HEADLESS=False
```

## Verificação da Instalação

Para verificar se a instalação foi bem-sucedida, execute:

```bash
pytest tests/test_cases/test_email_formato_invalido_improved.py -v
```

Se tudo estiver configurado corretamente, o teste será executado e você verá os resultados no terminal.

## Solução de Problemas

### Erro: ChromeDriver não encontrado

Se você encontrar um erro relacionado ao ChromeDriver, verifique se:

1. O ChromeDriver está instalado e no PATH
2. A versão do ChromeDriver é compatível com sua versão do Chrome

### Erro: Módulos não encontrados

Se você encontrar erros de importação, verifique se:

1. O ambiente virtual está ativado
2. Todas as dependências foram instaladas corretamente

### Erro: Elementos não encontrados

Se os testes falharem porque elementos não são encontrados, verifique se:

1. A URL base está correta
2. Os seletores ainda são válidos (a aplicação pode ter mudado)
3. O site está acessível
