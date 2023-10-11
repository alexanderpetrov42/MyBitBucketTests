from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageBase:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.open()

    def click(self, xpath):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, xpath))).click();

    def is_element_present(self, by, elem):
        try:
            self.driver.find_element(by, elem)
            return True
        except NoSuchElementException:
            return False

    def fill_the_field(self, elem, value):
        self.driver.find_element(elem).clear()
        self.driver.find_element(elem).send_keys(value)