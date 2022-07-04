import pytest
from selenium import webdriver


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(r'C:\Users\Tomek_2\Desktop\kursy_udemy\SELENIUM\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()