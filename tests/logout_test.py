from pages.logout_page import LogoutPage
import pytest


@pytest.mark.usefixtures('setup')
class TestLogoutPage:
    def test_log_out(self):
        logout_page = LogoutPage(self.driver)
        logout_page.log_in('jan447370@gmail.com','Moje1234!')
        logout_page.skip_2fa()
        logout_page.log_out()
        assert logout_page.is_logout_successfull()
