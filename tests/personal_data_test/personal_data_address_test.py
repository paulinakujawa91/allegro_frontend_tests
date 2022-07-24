import pytest
from pages.personal_data_page.personal_data_page_address import PersonalDataPageAddress
from tests import const


@pytest.mark.usefixtures('setup')
class TestPersonalDataPageAddress:

    def test_set_address_successful(self):
        personal_data_page = PersonalDataPageAddress(self.driver)
        personal_data_page.log_in(const.email, const.password)
        personal_data_page.skip_2fa()
        personal_data_page.settings_page()
        personal_data_page.set_address_successful(const.street, const.post_code, const.city, const.voivodeship, const.country)
        assert personal_data_page.is_saved_address(const.street, const.post_code, const.city, const.voivodeship, const.country)

    def test_set_address_cancelled(self):
        personal_data_page = PersonalDataPageAddress(self.driver)
        personal_data_page.log_in(const.email, const.password)
        personal_data_page.skip_2fa()
        personal_data_page.settings_page()
        personal_data_page.set_address_cancelled(const.street, const.post_code, const.city, const.voivodeship, const.country)
        assert personal_data_page.is_cancelled_address(const.street, const.post_code, const.city, const.voivodeship, const.country)








