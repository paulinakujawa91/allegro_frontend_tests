import pytest
from pages.personal_data_page.personal_data_page_supouse_name import PersonalDataPageSpouseName
from tests import const


@pytest.mark.usefixtures('setup')
class TestPersonalDataPageSpouseName:

    def test_set_supouse_name_successful(self):
        personal_data_page = PersonalDataPageSpouseName(self.driver)
        personal_data_page.log_in(const.email, const.password)
        personal_data_page.skip_2fa()
        personal_data_page.settings_page()
        personal_data_page.set_spouse_name_successful(const.spouse_first_name, const.spouse_last_name)
        assert personal_data_page.is_saved_spouse_name(const.spouse_first_name, const.spouse_last_name)

    def test_set_supouse_name_cancelled(self):
        personal_data_page = PersonalDataPageSpouseName(self.driver)
        personal_data_page.log_in(const.email, const.password)
        personal_data_page.skip_2fa()
        personal_data_page.settings_page()
        personal_data_page.set_spouse_name_cancelled(const.spouse_first_name, const.spouse_last_name)
        assert personal_data_page.is_cancelled_spouse_name(const.spouse_first_name, const.spouse_last_name)
