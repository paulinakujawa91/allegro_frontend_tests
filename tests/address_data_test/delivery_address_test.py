import pytest
from pages.address_data_page.delivery_address import DeliveryAddressPage
from tests import const


@pytest.mark.usefixtures('setup')
class TestSetDeliveryAddress:

    def test_set_correct_delivery_address(self):
        delivery_first_name = "Tommasz"
        delivery_last_name = 'Nowak'
        delivery_company = 'XYZ'
        delivery_phone_number = '600600600'
        delivery_street = 'Akacjowa 19'
        delivery_post_code = '00-256'
        delivery_city = 'Kraków'
        delivery_country ='Polska'

        address_page = DeliveryAddressPage(self.driver)
        address_page.log_in(const.email, const.password)
        address_page.skip_2fa()
        address_page.settings_page()
        address_page.set_correct_delivery_address(delivery_first_name, delivery_last_name, delivery_company, delivery_phone_number, delivery_street, delivery_post_code, delivery_city, delivery_country)
        assert address_page.is_saved_delivery_address(delivery_first_name, delivery_last_name, delivery_company, delivery_phone_number, delivery_street, delivery_post_code, delivery_city, delivery_country)

    def test_set_delivery_address_cancelled(self):
        delivery_first_name = "Tommasgsgsgsgsgsgsgsz"
        delivery_last_name = 'Nohdhdjdjhdjhdjhdwak'
        delivery_company = 'XbdfhfhfhfhfhfYZ'
        delivery_phone_number = '600645600'
        delivery_street = 'Akacjjfjfjfjfowa 19'
        delivery_post_code = '00-444'
        delivery_city = 'Myszków'
        delivery_country = 'Polska'

        address_page = DeliveryAddressPage(self.driver)
        address_page.log_in(const.email, const.password)
        address_page.skip_2fa()
        address_page.settings_page()
        address_page.set_delivery_address_cancelled(delivery_first_name, delivery_last_name, delivery_company, delivery_phone_number, delivery_street, delivery_post_code, delivery_city, delivery_country)
        assert address_page.is_cancelled_delivery_address(delivery_first_name, delivery_last_name, delivery_company, delivery_phone_number, delivery_street, delivery_post_code, delivery_city, delivery_country)


