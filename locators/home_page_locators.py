from selenium.webdriver.common.by import By


class HomePageLocators:
    arrow_head_button = (By.XPATH, "//div[@data-dropdown-id='user_dropdown']/button")
    login_button = (By.XPATH, '//a[@data-analytics-click-value="login-button"]')