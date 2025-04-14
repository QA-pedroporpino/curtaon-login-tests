# 🧪 Testes Automatizados do CurtaON!

Este diretório contém os testes automatizados para o site CurtaON!.

## 📋 Testes Disponíveis

### 1. Teste de Logo no Google

`test_logo_google.py`

- **Objetivo**: Verificar se o logo antigo do tamanduá ainda está sendo exibido nos resultados do Google
- **Como funciona**:
  - 🔍 Faz uma busca por "CurtaOn" no Google
  - 📸 Captura screenshots em cada etapa
  - 🚨 Alerta se encontrar o logo antigo do tamanduá
  - ✨ Confirma se o novo logo está sendo exibido corretamente

### 2. Teste de Login

`test_login_valido_otimizado.py`

- **Objetivo**: Validar o fluxo completo de login
- **Como funciona**:
  - 🔑 Testa login com credenciais válidas
  - ✅ Verifica redirecionamento após login
  - 📸 Captura screenshots em caso de erro
  - 🚨 Reporta problemas encontrados

## 🛠️ Como Executar os Testes

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Execute os testes:

```bash
# Teste do Logo
python test_logo_google.py

# Teste de Login
python test_login_valido_otimizado.py
```

## 📸 Screenshots

### 📁 Localização

Todos os screenshots são salvos automaticamente na pasta `test_screenshots/` dentro do diretório do teste. O caminho completo é mostrado nos logs quando um screenshot é salvo.

### 📝 Nomenclatura

Os screenshots seguem o padrão:

- `teste_logo_*` - Screenshots do teste de logo
- `teste_login_*` - Screenshots do teste de login

Cada arquivo inclui:

- Nome do teste
- Nome do passo
- Timestamp (para evitar sobrescrita)

Exemplo: `teste_logo_resultados_busca_20240315_143022.png`

### 🔍 Como Encontrar

1. Procure pela mensagem "📁 Pasta de screenshots:" no início do teste
2. Ou procure por "📂 Caminho completo:" após cada screenshot salvo
3. Os screenshots são salvos em:
   ```
   C:\Projects\curtaON!automacoes\tests\test_cases\test_screenshots\
   ```

## 🔍 Logs

Os testes geram logs detalhados com emojis para facilitar o entendimento:

- 🌐 Navegação web
- 🔍 Busca e análise
- ⌨️ Digitação
- 📸 Screenshots
- ✅ Sucesso
- ❌ Erros
- 🚨 Alertas importantes
- 📝 Informações detalhadas
- 👋 Finalização
- ⚠️ Avisos
- ✨ Resultados positivos

## 🤝 Contribuindo

Para adicionar novos testes:

1. Crie um novo arquivo `test_*.py`
2. Importe o `ScreenshotManager` do módulo `utils`
3. Siga o padrão de logs com emojis
4. Use o `ScreenshotManager` para salvar screenshots
5. Atualize este README com as informações do novo teste

## 📝 Notas

- Os testes são executados em modo headless para evitar interferência visual
- Configurações anti-reCAPTCHA estão implementadas
- Screenshots são salvos com timestamp para evitar sobrescrita
- Todos os screenshots são centralizados na pasta `test_screenshots/`
- O caminho completo dos screenshots é mostrado nos logs
