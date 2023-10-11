from selenium.webdriver.common.by import By


class LoginPageLocators:
    user_text_field = (By.NAME, "username")
    submit_user_button = (By.XPATH, "//button[@type=\"submit\"]")
    password_text_field = (By.NAME, "password")
    submit_login_button = (By.ID, "login-submit")
    profile_button = (By.XPATH, "//header/div/div[4]")
    logout_button = (By.XPATH, "//span[text()=\"Log out\"]")

class NavPageLocators:
    switch_to_bitbucket = (By.XPATH, "//button[@role=\"presentation\"]")


