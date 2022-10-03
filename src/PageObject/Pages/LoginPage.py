from ..Locates import Locator
from selenium.webdriver.common.by import By
import sys

sys.path.append(sys.path[0] + "/....")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())


class Login(object):
    def __init__(self, driver):
        self.driver = driver
        self.email = driver.find_element(By.XPATH, Locator.email)
        self.password = driver.find_element(By.XPATH, Locator.password)
        self.submit = driver.find_element(By.ID, Locator.submit)

    def getEmailText(self):
        return self.search_text

    def getPasswordText(self):
        return self.search_text

    def getSubmit(self):
        return self.submit
