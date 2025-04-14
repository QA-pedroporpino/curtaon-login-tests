# 📚 Documentação do CurtaON Automações

Este diretório contém documentação detalhada sobre o framework de automação.

## 📋 Conteúdo

- [Arquitetura](architecture.md) - Visão geral da arquitetura do framework
- [Guias](guides/) - Guias de uso e contribuição
- [API](api/) - Documentação da API do framework
- [Exemplos](examples/) - Exemplos de uso

## 🏗️ Arquitetura

O framework segue uma arquitetura baseada em Page Objects, com separação clara entre:

- **Page Objects**: Representam as páginas da aplicação
- **Test Cases**: Contêm os casos de teste
- **Utils**: Utilitários para logging, screenshots, etc.
- **Config**: Configurações do framework
- **Data**: Dados de teste

## 🔧 Guias

- [Instalação](guides/installation.md)
- [Primeiros Passos](guides/getting-started.md)
- [Contribuição](guides/contributing.md)
- [Padrões de Código](guides/code-standards.md)

## 📊 Relatórios

Os relatórios são gerados automaticamente após cada execução de teste e incluem:

- Screenshots de sucesso e erro
- Logs detalhados
- Relatório HTML com resultados
