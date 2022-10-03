import sys
import os
sys.path.append(sys.path[0] + "/../..")
from time import sleep
import unittest
from src.PageObject.Pages.LoginPage import Login as LoginPage
from src.TestBase.WebDriverSetup import WebDriverSetup

class Login(WebDriverSetup):

    def test_login(self):

        driver = self.driver
        self.driver.get("http://www.localhost:3006/")
        self.driver.set_page_load_timeout(30)
        loginPage =LoginPage(driver)
        loginPage.setEmailText("admin@gmail.com")
        loginPage.setPasswordText("admin@123")
        sleep(2)
        loginPage.submitForm()
        sleep(5)
        

   

if __name__ == '__main__':
    unittest.main()
