import sys
import os
sys.path.append(sys.path[0] + "/../..")
from time import sleep
import unittest

from src.TestBase.WebDriverSetup import WebDriverSetup





class Login(WebDriverSetup):

    def test_login(self):

        driver = self.driver
        self.driver.get("http://www.localhost:3006/")
        self.driver.set_page_load_timeout(30)


if __name__ == '__main__':
    unittest.main()
