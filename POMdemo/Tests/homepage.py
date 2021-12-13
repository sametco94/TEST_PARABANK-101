from selenium import webdriver
import unittest
import time
from Samples.POMdemo.Pages.HomePage import HomePage


class HomePageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_homepage(self):
        driver = self.driver
        driver.get("https://parabank.parasoft.com")
        time.sleep(3)

        homepage = HomePage(driver)

        username = "testfreeguy1"
        password = "123TEST"

        # homepage.goto_homepageagain()
        # homepage.goto_and_printout_aboutus()
        # homepage.goto_forgotlogin()
        # homepage.goto_registerpage()
        homepage.login_action(username, password)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed!")