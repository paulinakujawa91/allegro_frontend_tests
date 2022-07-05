import random
import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures('setup')
class TestOpenLoginPage:

    def test_log_in_correct_data(self):
        login_page = LoginPage(self.driver)
        login_page.log_in('nikitasobczak17@gmail.com','Moje1234!')
        assert login_page.is_login_successfuly()

    def test_log_in_invalid_login(self):
        invalid_email = str(random.randint(0,1000)) + 'test@gmail.com'
        login_page = LoginPage(self.driver)
        login_page.log_in(invalid_email,'Moje1234!')
        msg= 'Login, e-mail lub hasło są nieprawidłowe'
        assert msg in login_page.get_error_message()

    def test_log_in_invalid_password(self):
        invalid_password = str(random.randint(0,1000)) + 'Moje1234!'
        login_page = LoginPage(self.driver)
        login_page.log_in('nikitasobczak17@gmail.com', invalid_password)
        msg = 'Login, e-mail lub hasło są nieprawidłowe'
        assert msg in login_page.get_error_message()
