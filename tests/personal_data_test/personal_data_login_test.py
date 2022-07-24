import pytest
from pages.personal_data_page.personal_data_page_login import PersonalDataPageLogin
from tests import const


@pytest.mark.usefixtures('setup')
class TestPersonalDataPageLogin:

    def test_set_login_successful(self):
        personal_data_page = PersonalDataPageLogin(self.driver)
        personal_data_page.log_in(const.email, const.password)
        personal_data_page.skip_2fa()
        personal_data_page.settings_page()
        personal_data_page.set_login_successful('LoginTestowy')
        assert personal_data_page.is_login_successfuly()

    def test_set_login_cancelled(self):
        personal_data_page = PersonalDataPageLogin(self.driver)
        personal_data_page.log_in(const.email, const.password)
        personal_data_page.skip_2fa()
        personal_data_page.settings_page()
        personal_data_page.set_login_cancelled('LoginCancelled')
        assert personal_data_page.is_cancelled_login('LoginCancelled')
