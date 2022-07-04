from selenium.webdriver.common.by import By


class ConsentPageLocators:
    consent_button = (By.XPATH, "//button[contains(., 'Ok, zgadzam się')]")


class HomePageLocators:
    arrow_head_button = (By.XPATH, "//div[@data-dropdown-id='user_dropdown']/button")
    login_button = (By.XPATH, '//a[@data-analytics-click-value="login-button"]')


class LoginPageLocators:
    login = (By.ID, 'login')
    password = (By.ID, 'password')
    login_button = (By.XPATH, "//button[contains(., 'Zaloguj się')]")
    login_span = (By.XPATH, "//div[contains(., 'Pomóż nam chronić Twoje konto')]")
    error_message = (By.XPATH, "//div[contains(., 'Login, e-mail lub hasło są nieprawidłowe')]")