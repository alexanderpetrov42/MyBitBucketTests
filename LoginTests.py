import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import allure
import pytest
from allure_commons.types import AttachmentType

from pages.login_page import LogInPage
from pages.nav_page import NavPage
class testSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.close()

    @allure.title("Python.org test")
    @allure.description("Check search on python.org")
    def test_search(self):
        self.loginpage = LogInPage(self.driver)
        self.loginpage.open_page_and_search(self)
        assert "https://www.python.org/search/?q=getting+started+with+python&submit=" == self.driver.current_url

    @allure.title("Home page - smoke test")
    @allure.description("Check login with valid data")
    def test_login_with_valid_data_bitbucket(self):
        self.loginpage = LogInPage(self.driver)
        self.loginpage.login(self)

        with allure.step("Check if we are logged in"):
            try:
                self.assertTrue(self.loginpage.is_logged_in());
            except AssertionError as e:
                allure.attach(body=self.driver.get_screenshot_as_png(),
                              name="screenshot_image")
                raise AssertionError('We are not logged in')

    def create_bitbucket_repo(self):
        self.navpage = NavPage(self.driver)
        self.loginpage.login(self)
        self.navpage.switch_to_bitbucket()

    if __name__ == "__main__":
        unittest.main()