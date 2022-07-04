import random

import pytest

from pages.consent_page import ConsentPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures('setup')
class TestOpenLoginPage:

    def test_open_consent_page(self):
        consent_page = ConsentPage(self.driver)
        consent_page.open_page()
        consent_page.accept_consent()

    def test_open_home_page(self):
        consent_page = ConsentPage(self.driver)
        consent_page.open_page()
        consent_page.accept_consent()
        home_page = HomePage(self.driver)
        home_page.open_home_page()

    def test_log_in_passed(self):
        consent_page = ConsentPage(self.driver)
        consent_page.open_page()
        consent_page.accept_consent()
        home_page = HomePage(self.driver)
        home_page.open_home_page()
        login_page = LoginPage(self.driver)
        login_page.log_in('nikitasobczak17@gmail.com','Moje1234!')
        assert login_page.get_login_span()

    def test_log_in_invalid_login(self):
        consent_page = ConsentPage(self.driver)
        consent_page.open_page()
        consent_page.accept_consent()
        home_page = HomePage(self.driver)
        home_page.open_home_page()
        invalid_email = str(random.randint(0,1000)) + 'test@gmail.com'
        login_page = LoginPage(self.driver)
        login_page.log_in(invalid_email,'Moje1234!')
        msg= 'Login, e-mail lub hasło są nieprawidłowe'
        assert msg in login_page.get_error_message()

    def test_log_in_invalid_password(self):
        consent_page = ConsentPage(self.driver)
        consent_page.open_page()
        consent_page.accept_consent()
        home_page = HomePage(self.driver)
        home_page.open_home_page()
        invalid_password = str(random.randint(0,1000)) + 'Moje1234!'
        login_page = LoginPage(self.driver)
        login_page.log_in('nikitasobczak17@gmail.com', invalid_password)
        msg = 'Login, e-mail lub hasło są nieprawidłowe'
        assert msg in login_page.get_error_message()
