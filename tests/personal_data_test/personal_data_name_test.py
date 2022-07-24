import pytest
from pages.personal_data_page.personal_data_page_name import PersonalDataPageName
from tests import const


@pytest.mark.usefixtures('setup')
class TestSetPersonalDataPageName:

    def test_set_name_successful(self):
        personal_data_page = PersonalDataPageName(self.driver)
        personal_data_page.log_in(const.email, const.password)
        personal_data_page.skip_2fa()
        personal_data_page.settings_page()
        personal_data_page.set_name_data_successful(const.first_name,const.last_name)
        assert personal_data_page.is_saved_name_data(const.first_name,const.last_name)

    def test_set_name_cancelled(self):
        personal_data_page = PersonalDataPageName(self.driver)
        personal_data_page.log_in(const.email, const.password)
        personal_data_page.skip_2fa()
        personal_data_page.settings_page()
        personal_data_page.set_name_data_cancelled(const.first_name,const.last_name)
        assert personal_data_page.is_cancelled_name_data(const.first_name,const.last_name)
