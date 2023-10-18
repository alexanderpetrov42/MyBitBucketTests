import unittest
import allure

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from base.page_base import PageBase
from locators.locators import LoginPageLocators


class LogInPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Opening python website")
    def open_homepage_python(self, driver):
        driver.get("https://www.python.org")

    @allure.step("Opening page and searching")
    def open_page_and_search(self, driver):
        self.open_homepage_python(self.driver)
        assert ("Python" in self.driver.title)
        elem = self.driver.find_element(By.NAME, "q")
        elem.send_keys("getting started with python")
        elem.send_keys(Keys.RETURN)

    @allure.step("Logging in to bitbucket")
    def login(self, driver):
        self.driver.get("https://id.atlassian.com/login?application=bitbucket&amp;continue=https%3A%2F%2Fbitbucket.org%2Faccount%2Fsignin%2F%3FredirectCount%3D1%26next%3D%252F")
        self.driver.find_element(*LoginPageLocators.user_text_field).send_keys("testlogin@login.login")
        self.driver.find_element(*LoginPageLocators.submit_user_button).click()
        self.driver.find_element(*LoginPageLocators.password_text_field).send_keys("password")
        self.driver.find_element(*LoginPageLocators.submit_login_button).click()

    @allure.step("Logging in to bitbucket with invalid data")
    def login_invalid_data(self, driver):
        self.driver.get("https://id.atlassian.com/login?application=bitbucket&amp;continue=https%3A%2F%2Fbitbucket.org%2Faccount%2Fsignin%2F%3FredirectCount%3D1%26next%3D%252F")
        self.driver.find_element(*LoginPageLocators.user_text_field).send_keys("invalid_data@test.test")
        self.driver.find_element(*LoginPageLocators.submit_user_button).click()

    @allure.step("Checking if we are logged in")
    def is_logged_in(self, user=None):
            return self.is_element_present(*LoginPageLocators.profile_button)

    @allure.step("Switching to bitbucket")
    def switch_to_bitbucket(self):
        self.driver.find_element(*LoginPageLocators.switch_to_bitbucket).click()

