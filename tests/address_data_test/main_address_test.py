import pytest
from pages.address_data_page.main_address import MainAddressPage
from tests import const


@pytest.mark.usefixtures('setup')
class TestSetMainAddress:

    def test_set_main_address_succesful(self):
        address_page = MainAddressPage(self.driver)
        address_page.log_in(const.email, const.password)
        address_page.skip_2fa()
        address_page.settings_page()
        address_page.set_main_address_successful(const.street, const.code, const.city, const.voivodeship, const.country)
        assert address_page.is_saved_main_address()

    def test_set_main_address_cancelled(self):
        address_page = MainAddressPage(self.driver)
        address_page.log_in(const.email, const.password)
        address_page.skip_2fa()
        address_page.settings_page()
        address_page.set_main_address_cancelled(const.street, const.code, const.city, const.voivodeship, const.country)
        assert address_page.is_cancelled_main_address()

