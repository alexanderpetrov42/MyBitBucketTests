import unittest

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from base.page_base import PageBase
from locators.locators import NavPageLocators


class NavPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    def switch_to_bitbucket(self):
        self.driver.find_element(*NavPageLocators.switch_to_bitbucket).click()

