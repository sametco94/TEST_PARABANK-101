from selenium import webdriver
import unittest
import time
from Samples.POMdemo.Pages.HomePage import HomePage
from Samples.POMdemo.Pages.RegisterPage import RegisterPage


class RegisterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_register(self):
        firstname = "TEST"
        lastname = "FREEGUY"
        address = "Mustafar Avenue, Hoth Street N 42"
        city = "Central"
        state = "Wisconsin"
        zipcode = "4242"
        phone = "+905371112233"
        ssn = "420420420"
        username = "testfreeguy3"
        password = "123TEST"
        repassword = "123TEST"

        driver = self.driver
        driver.get("https://parabank.parasoft.com")
        time.sleep(3)

        homepage = HomePage(driver)
        registerpage = RegisterPage(driver)

        homepage.goto_registerpage()
        registerpage.fillin_and_submit(firstname, lastname, address, city, state, zipcode, phone, ssn, username, password, repassword)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test is completed!")