from selenium import webdriver
import unittest
import time
from Samples.POMdemo.Pages.HomePage import HomePage
from Samples.POMdemo.Pages.AccountPage import AccountPage


class AccountServicesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_accountpage(self):
        username = "testfreeguy3"
        password = "123TEST"
        accounttype = "SAVINGS"
        existingaccount = "21780"
        amount1 = "100"
        fromaccount = "21780"
        toaccount = "23001"
        payeename = "ERENÇO"
        address = "M. Kemal Bulevard, Cumhuriyet Sk N. 3/5"
        city = "Eskişehir"
        state = "Turkey"
        zipcode = "11111"
        phone = "+908889993355"
        amount2 = "10"
        account = "123"
        verifyaccount = "123"
        transferacc = "21780"
        transaction_id = "25021"
        bydate = "12-13-2021"
        fromdate = "12-10-2021"
        todate = "12-13-2021"
        transferamount = "10"
        newname = "NEWTEST1"
        newlastname = "MAN"
        newaddress = "Coruscant Center, Jedi Temple N 42"
        newcity = "Coruscant"
        newstate = "Starz"
        newzipcode = "423131"
        newphone = "+1 99 88 123 42"
        loanamount = "10000"
        downpayment = "1500"

        driver = self.driver
        driver.get("https://parabank.parasoft.com")
        time.sleep(3)

        homepage = HomePage(driver)
        accountpage = AccountPage(driver)

        # homepage.goto_homepageagain()
        # homepage.goto_and_printout_aboutus()
        # homepage.goto_forgotlogin()
        # homepage.goto_registerpage()
        homepage.login_action(username, password)
        accountpage.open_new_account(accounttype, existingaccount)
        accountpage.accounts_overview()
        accountpage.transfer_funds(amount1, fromaccount, toaccount)
        accountpage.bill_pay(payeename, address, city, state, zipcode, phone, account, verifyaccount, amount2, fromaccount)
        accountpage.find_transactionbyid(transferacc, transaction_id)
        accountpage.find_transactionbydate(transferacc, bydate)
        accountpage.find_transactionfromdatetodate(transferacc, fromdate, todate)
        accountpage.find_transactionbyamount(transferacc, transferamount)
        accountpage.update_contactinfo(newname, newlastname, newaddress, newcity, newstate, newzipcode, newphone)
        accountpage.request_loan(loanamount, downpayment, fromaccount)
        accountpage.logout_action()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed!")