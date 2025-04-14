import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
import os
import sys
from selenium.webdriver.support.ui import WebDriverWait
import time

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Importação do arquivo base_test.py
from tests.test_cases_improved.base_test import Config, Dados, Logger, Screenshot

class TestLoginValidoOtimizado:
    """
    🧪 Suite de testes para validação de login com credenciais válidas
    
    Esta suite contém testes que validam o fluxo completo de login no sistema CurtaON!,
    garantindo que usuários possam acessar a plataforma com suas credenciais.
    
    Atributos:
        driver: Instância do WebDriver
        login_page: Página de login com os métodos de interação
        logger: Sistema de logging personalizado
    
    Tags: 
        @smoke: Testes críticos que devem ser executados em cada build
        @regression: Testes completos para validação de regressão
    """
    
    @pytest.fixture(autouse=True)
    def setup_teardown(self, driver, login_page):
        """
        🔧 Configuração e limpeza do ambiente de teste
        
        Args:
            driver: Instância do WebDriver (injetada pelo pytest)
            login_page: Página de login (injetada pelo pytest)
        """
        self.driver = driver
        self.login_page = login_page
        self.logger = Logger.criar("login_valido_otimizado")
        
        # Setup
        self.logger.info("🔷" * 30)
        self.logger.info("🚀 INICIANDO TESTE: LOGIN VÁLIDO")
        self.logger.info("🔷" * 30)
        
        yield
        
        # Teardown
        self.logger.info("🔷" * 30)
        self.logger.info("🏁 FINALIZANDO TESTE: LOGIN VÁLIDO")
        self.logger.info("🔷" * 30)
    
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login_valido_fluxo_completo(self):
        """
        🎯 TC-001: Validação do fluxo completo de login com credenciais válidas
        
        Verifica se um usuário consegue realizar login com sucesso utilizando
        credenciais válidas, seguindo o fluxo completo desde o acesso ao site
        até o redirecionamento para a página principal.
        
        Passos do teste:
        1. Acessar o site do CurtaON
        2. Clicar no botão 'Entrar'
        3. Selecionar login por email
        4. Preencher credenciais válidas
        5. Validar redirecionamento
        
        Resultado esperado:
        - Usuário é redirecionado para a página principal após login bem-sucedido
        """
        try:
            # Acessa o site
            self.driver.get(self.login_page.URL)
            self.logger.info("Acessando o site")
            
            # Aguarda um tempo para evitar reCAPTCHA
            time.sleep(5)
            
            # Verifica se o modal de login já está aberto
            try:
                modal = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "header_MenuCurtaoOn_btnLoginModalEntrar"))
                )
                if modal.is_displayed():
                    self.logger.info("Modal de login já está aberto")
                else:
                    # Clica no botão "Entrar"
                    self.login_page.clicar_botao_entrar()
                    self.logger.info("Clicando no botão 'Entrar'")
            except TimeoutException:
                # Clica no botão "Entrar" se o modal não estiver visível
                self.login_page.clicar_botao_entrar()
                self.logger.info("Clicando no botão 'Entrar'")
            
            # 3️⃣ Preenchimento do formulário
            self.logger.info(f"✏️ Preenchendo formulário com email: '{Dados.EMAIL_VALIDO}'")
            self.login_page.fazer_login(Dados.EMAIL_VALIDO, Dados.SENHA_CORRETA)
            
            # 4️⃣ Validação do redirecionamento
            self.logger.info("⏳ Aguardando redirecionamento após login")
            self._validar_redirecionamento()
            
            # 5️⃣ Captura de evidência
            Screenshot.capturar(self.driver, "login_valido", True)
            self.logger.info("📸 Screenshot de sucesso capturado")
            
            # 6️⃣ Registro de sucesso
            self.logger.info("✅ TESTE APROVADO: Login realizado com sucesso")
            
        except TimeoutException as e:
            self.logger.error(f"⏰ Timeout ao aguardar elemento: {str(e)}")
            Screenshot.capturar(self.driver, "login_valido_timeout", False)
            raise
        
        except ElementClickInterceptedException as e:
            self.logger.error(f"🚫 Elemento não clicável (interceptado): {str(e)}")
            Screenshot.capturar(self.driver, "login_valido_click_error", False)
            raise
            
        except NoSuchElementException as e:
            self.logger.error(f"❌ Elemento não encontrado: {str(e)}")
            Screenshot.capturar(self.driver, "login_valido_element_error", False)
            raise
            
        except Exception as e:
            self.logger.error(f"💥 Erro inesperado durante o teste: {str(e)}")
            Screenshot.capturar(self.driver, "login_valido_erro", False)
            raise
    
    def _interagir_com_modal_login(self):
        """
        Método auxiliar para interagir com o modal de login
        Tenta identificar se o modal já está aberto antes de clicar no botão
        """
        self.logger.info("🔘 Verificando estado do modal de login")
        try:
            modal = self.driver.find_element(By.ID, "login-modal")
            if not modal.is_displayed():
                self.logger.info("🔘 Modal fechado, clicando no botão 'Entrar'")
                self.login_page.clicar_botao_entrar()
            else:
                self.logger.info("✅ Modal de login já está aberto")
        except NoSuchElementException:
            self.logger.info("🔘 Modal não encontrado, clicando no botão 'Entrar'")
            self.login_page.clicar_botao_entrar()
        
        self.logger.info("🔘 Clicando no botão 'E-mail'")
        self.login_page.clicar_botao_email()
    
    def _validar_redirecionamento(self):
        """
        Método auxiliar para validar o redirecionamento após o login
        Verifica se a URL mudou e aguarda um tempo para garantir o carregamento
        
        Raises:
            TimeoutException: Se o redirecionamento não ocorrer no tempo esperado
        """
        try:
            # Aguarda até que a URL mude para a página principal
            self.login_page.wait.until(
                lambda driver: driver.current_url != Config.URL
            )
            self.logger.info("✅ Redirecionamento confirmado")
            
            # Aguarda um tempo para garantir o carregamento completo
            time.sleep(2)
            self.logger.info("⏳ Aguardando estabilização da página")
            
        except TimeoutException:
            self.logger.error("❌ Redirecionamento não ocorreu no tempo esperado")
            raise

if __name__ == "__main__":
    # Configuração para execução direta
    import logging
    logging.basicConfig(level=logging.INFO)
    
    # Executa o teste
    pytest.main([__file__, "-v", "--capture=no"]) 