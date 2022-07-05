import pytest
from selenium import webdriver

driverpath = r'C:\Users\Tomek_2\Desktop\kursy_udemy\SELENIUM\chromedriver.exe'

@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(driverpath)
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()