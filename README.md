<<<<<<< HEAD
# curtaon-login-tests
Testes automatizados de login da plataforma CurtaON usando Python e Selenium.   Automated login tests for CurtaON platform using Python and Selenium.
=======
# 🚀 CurtaON! Automações

Framework de automação de testes para o CurtaON utilizando Python, Selenium e Pytest.

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Executando os Testes](#-executando-os-testes)
- [Relatórios](#-relatórios)
- [Contribuição](#-contribuição)
- [Licença](#-licença)

## 🎯 Sobre o Projeto

Este projeto contém automações de testes para o CurtaON, focando em cenários de login e validações de formulários. O framework foi desenvolvido seguindo as melhores práticas de automação de testes e padrões de projeto como Page Objects.

## 🛠 Tecnologias Utilizadas

- Python 3.8+
- Selenium WebDriver
- Pytest
- Pytest-HTML (para relatórios)
- Logging
- Page Objects
- Fixtures

## 📁 Estrutura do Projeto

```
curtaON-automacoes/
├── docs/                    # Documentação do projeto
├── reports/                 # Relatórios de execução
├── src/                     # Código fonte
│   ├── config/             # Configurações
│   ├── data/               # Dados de teste
│   ├── pages/              # Page Objects
│   └── utils/              # Utilitários
├── tests/                  # Testes
│   ├── test_cases/        # Casos de teste
│   └── conftest.py        # Configurações do pytest
├── .gitignore
├── README.md
├── requirements.txt
└── setup.py
```

## ⚙️ Pré-requisitos

- Python 3.8 ou superior
- Chrome WebDriver
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/curtaON-automacoes.git
cd curtaON-automacoes
```

2. Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## 🚀 Executando os Testes

Para executar todos os testes:

```bash
pytest tests/
```

Para executar um teste específico:

```bash
pytest tests/test_cases/test_email_formato_invalido_improved.py -v
```

Para executar com relatório HTML:

```bash
pytest --html=reports/report.html
```

## 📊 Relatórios

Os relatórios são gerados automaticamente na pasta `reports/` após cada execução. Incluem:

- Screenshots de sucesso e erro
- Logs detalhados
- Relatório HTML com resultados

## 🤝 Contribuição

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

Seu Nome - [@seu-usuario](https://github.com/seu-usuario)

---

⌨️ com ❤️ por [Seu Nome](https://github.com/seu-usuario) 😊
>>>>>>> 524422f (subindo os testes de login do CurtaON)
