import pytest
from selenium.webdriver.common.by import By
from base_test import BaseTest

class TestInvalidLogin(BaseTest):
    """Teste de login com e-mail e senha incorretos"""

    def __init__(self):
        super().__init__("teste_login_negativo")

    def test_invalid_login(self):
        """Executa o teste de login inválido"""
        try:
            logging.info("=" * 60)
            logging.info("🚀 INICIANDO TESTE NEGATIVO DE LOGIN")
            logging.info("=" * 60)

            # 1. Acessa o site
            self.driver.get("https://curtaon.com.br")
            logging.info("🌐 Site carregado")

            # 2. Clica no botão 'Entrar'
            self.click_element(
                By.ID, 
                "header_MenuCurtaoOn_btnLoginModalEntrar",
                "Botão 'Entrar'"
            )

            # 3. Clica em 'E-mail'
            self.click_element(
                By.ID, 
                "btn-login-email",
                "Botão 'E-mail'"
            )

            # 4. Preenche e-mail inválido
            self.fill_field(
                By.ID, 
                "txtUsuarioHeader", 
                "email_invalido@teste.com",
                "Campo de e-mail"
            )

            # 5. Preenche senha inválida
            self.fill_field(
                By.ID, 
                "txtPassHeader", 
                "senha_invalida",
                "Campo de senha"
            )

            # 6. Clica no botão de login
            self.click_element(
                By.ID, 
                "btnLoginModalHeader",
                "Botão de login"
            )

            # 7. Verifica mensagem de erro
            try:
                self.wait_for_element(
                    By.CSS_SELECTOR, 
                    ".alert-danger",
                    timeout=10
                )
                logging.info("🎯 Mensagem de erro encontrada!")
            except TimeoutException:
                logging.error("❌ Mensagem de erro não encontrada")
                raise

            # Salva screenshot de sucesso
            self.save_screenshot("aprovado")
            logging.info("✅ TESTE APROVADO: Login inválido detectado corretamente!")

        except Exception as e:
            logging.error("❌ TESTE REPROVADO: Erro no fluxo de login inválido")
            logging.error(str(e))
            
            # Salva screenshot de erro
            self.save_screenshot("erro")
            pytest.fail(f"Falha no teste de login inválido: {str(e)}")

        finally:
            self.cleanup()

def test_invalid_login():
    """Função de teste para compatibilidade com pytest"""
    test = TestInvalidLogin()
    test.setup_driver()
    test.test_invalid_login() 