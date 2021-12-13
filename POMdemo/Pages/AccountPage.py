import time


class AccountPage:

    def __init__(self, driver):
        self.driver = driver

        self.homepage_Link = "parabank.parasoft.com"
        self.home_logo_className = "logo"

        ### Left Header ###
        self.solutions_button_cssSelector = "#headerPanel > ul.leftmenu > li:nth-child(1) > a"
        self.aboutus_button_cssSelector = "#headerPanel > ul.leftmenu > li:nth-child(2) > a"
        self.services_button_cssSelector = "#headerPanel > ul.leftmenu > li:nth-child(3) > a"
        self.products_button_cssSelector = "#headerPanel > ul.leftmenu > li:nth-child(4) > a"
        self.locations_button_cssSelector = "#headerPanel > ul.leftmenu > li:nth-child(5) > a"

        ### Right Header ###
        self.homepagelogo_button_cssSelector = "#headerPanel > ul.button > li.home > a"
        self.aboutuslogo_button_cssSelector = "#headerPanel > ul.button > li.aboutus > a"
        self.constactlogo_button_cssSelector = "#headerPanel > ul.button > li.contact > a"

        ### Account Services ###
        self.newacc_button_cssSelector = "#leftPanel > ul > li:nth-child(1) > a"
        self.accoverview_button_cssSelector = "#leftPanel > ul > li:nth-child(2) > a"
        self.transferfunds_button_cssSelector = "#leftPanel > ul > li:nth-child(3) > a"
        self.billpay_button_cssSelector = "#leftPanel > ul > li:nth-child(4) > a"
        self.findtransactions_button_cssSelector = "#leftPanel > ul > li:nth-child(5) > a"
        self.updatecontactinfo_button_cssSelector = "#leftPanel > ul > li:nth-child(6) > a"
        self.reqloan_button_cssSelector = "#leftPanel > ul > li:nth-child(7) > a"
        self.logout_button_cssSelector = "#leftPanel > ul > li:nth-child(8) > a"

        ### OPEN NEW ACCOUNT ###
        self.newacctype_selector_id = "type"
        self.existingaccount_selector_id = "fromAccountId"
        self.newaccount_button_cssSelector = "#rightPanel > div > div > form > div > input"
        ### ACCOUNTS OVERVIEW ###
        self.accounts_table_id = "accountTable"
        ### TRANSFER FUNDS ###
        self.amount_box_id = "amount"
        self.fromaccount_selector_cssSelector = "#rightPanel > div > div:nth-child(1) > form > table > tbody > tr:nth-child(13) > td:nth-child(2) > select"
        self.toaccount_selector_id = "toAccountId"
        self.transfersubmit_button_cssSelector = "#rightPanel > div > div > form > div:nth-child(4) > input"
        ### BILL PAYMENT SERVICE ###
        self.payeename_box_cssSelector = "#rightPanel > div > div:nth-child(1) > form > table > tbody > tr:nth-child(1) > td:nth-child(2) > input"
        self.address_box_cssSelector = "#rightPanel > div > div:nth-child(1) > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > input"
        self.city_box_cssSelector = "#rightPanel > div > div:nth-child(1) > form > table > tbody > tr:nth-child(3) > td:nth-child(2) > input"
        self.state_box_cssSelector = "#rightPanel > div > div:nth-child(1) > form > table > tbody > tr:nth-child(4) > td:nth-child(2) > input"
        self.zipcode_box_cssSelector = "#rightPanel > div > div:nth-child(1) > form > table > tbody > tr:nth-child(5) > td:nth-child(2) > input"
        self.phone_box_xPath = "/html/body/div[1]/div[3]/div[2]/div/div[1]/form/table/tbody/tr[6]/td[2]/input"
        self.account_box_cssSelector = "#rightPanel > div > div:nth-child(1) > form > table > tbody > tr:nth-child(8) > td:nth-child(2) > input"
        self.verifyacc_box_cssSelector = "#rightPanel > div > div:nth-child(1) > form > table > tbody > tr:nth-child(9) > td:nth-child(2) > input"
        self.ammount_box_cssSelector = "#rightPanel > div > div:nth-child(1) > form > table > tbody > tr:nth-child(11) > td:nth-child(2) > input"
        self.fromaccount_selector_id = "fromAccountId"
        self.sendbillpay_button_cssSelector = "#rightPanel > div > div:nth-child(1) > form > table > tbody > tr:nth-child(14) > td:nth-child(2) > input"
        ### FIND TRANSACTIONS ###
        self.account_selector_id = "accountId"
        self.transactionid_box_id = "criteria.transactionId"
        self.findbytransacid_button_cssSelector = "#rightPanel > div > div > form > div:nth-child(5) > button"
        self.transacdate_box_id = "criteria.onDate"
        self.findbydate_button_cssSelector = "#rightPanel > div > div > form > div:nth-child(9) > button"
        self.transacfromdate_box_id = "criteria.fromDate"
        self.transactodate_box_id = "criteria.toDate"
        self.findbydaterange_button_cssSelector = "#rightPanel > div > div > form > div:nth-child(13) > button"
        self.transacamount_box_id = "criteria.amount"
        self.findbyamount_button_cssSelector = "#rightPanel > div > div > form > div:nth-child(17) > button"
        ### UPDATE CONTACT INFO ###
        self.firstname_textbox_id = "customer.firstName"
        self.lastname_textbox_id = "customer.lastName"
        self.address_textbox_id = "customer.address.street"
        self.city_textbox_id = "customer.address.city"
        self.state_textbox_id = "customer.address.state"
        self.zipcode_textbox_id = "customer.address.zipCode"
        self.phonenumber_textbox_id = "customer.phoneNumber"
        ### REQUEST LOAN ###
        self.loanamount_box_id = "amount"
        self.downpayment_box_id = "downPayment"
        self.fromaccount_selector_id = "fromAccountId"
        self.loansubmit_button_cssSelector = "#rightPanel > div > div > form > table > tbody > tr:nth-child(4) > td:nth-child(2) > input"

        ### BUTTOM OF PAGES ###
        self.homepagelink_button_cssSelector = "#footerPanel > ul:nth-child(1) > li:nth-child(1) > a"
        self.aboutuslink_button_cssSelector = "#footerPanel > ul:nth-child(1) > li:nth-child(2) > a"
        self.serviceslink_button_cssSelector = "#footerPanel > ul:nth-child(1) > li:nth-child(3) > a"
        self.productslink_button_cssSelector = "#footerPanel > ul:nth-child(1) > li:nth-child(4) > a"
        self.locationslink_button_cssSelector = "#footerPanel > ul:nth-child(1) > li:nth-child(5) > a"
        self.forumlink_button_cssSelector = "#footerPanel > ul:nth-child(1) > li:nth-child(6) > a"
        self.sitemaplink_button_cssSelector = "#footerPanel > ul:nth-child(1) > li:nth-child(7) > a"
        self.contactuslink_button_cssSelector = "#footerPanel > ul:nth-child(1) > li:nth-child(8) > a"

    def goto_homepageagain(self):
        self.driver.find_element_by_css_selector(self.homepagelogo_button_cssSelector).click()

    def goto_and_printout_aboutus(self):
        self.driver.find_element_by_css_selector(self.aboutuslogo_button_cssSelector).click()
        time.sleep(3)
        textarea = self.driver.find_element_by_id("rightPanel")
        print(textarea.text)
        time.sleep(1)
        self.driver.find_element_by_css_selector(self.homepagelogo_button_cssSelector).click()

    def open_new_account(self, accounttype, existingaccount):
        self.driver.find_element_by_css_selector(self.newacc_button_cssSelector).click()
        time.sleep(1)
        newacc_title = self.driver.find_element_by_css_selector("#rightPanel > div > div > h1")
        if newacc_title.text == "Open New Account":
            self.driver.find_element_by_id(self.newacctype_selector_id).send_keys(accounttype)
            time.sleep(1)
            self.driver.find_element_by_id(self.existingaccount_selector_id).send_keys(existingaccount)
            time.sleep(1)
            self.driver.find_element_by_css_selector(self.newaccount_button_cssSelector).click()
            time.sleep(3)
            acc_open_title = self.driver.find_element_by_css_selector("#rightPanel > div > div > h1")
            if acc_open_title.text == "Account Opened!":
                newacc_info_box = self.driver.find_element_by_css_selector("#rightPanel > div > div")
                print(newacc_info_box.text)
                print("\n'Open New Account Test' is Successful!")
                time.sleep(3)
                self.driver.get("https://parabank.parasoft.com")
            else:
                print("\nTest Failed!")
                time.sleep(3)
                self.driver.get("https://parabank.parasoft.com")
        else: self. driver.get("https://parabank.parasoft.com")

    def accounts_overview(self):
        self.driver.find_element_by_css_selector(self.accoverview_button_cssSelector).click()
        time.sleep(1)
        accounts_table = self.driver.find_element_by_id(self.accounts_table_id)
        first_account_line = self.driver.find_element_by_css_selector("#accountTable > tbody > tr:nth-child(1)")
        if len(first_account_line.text) > 0:
            print(accounts_table.text)
            print("\n'Review Accounts Test' is Successful!")
            time.sleep(3)
            self.driver.get("https://parabank.parasoft.com")
        else:
            print("\nTest Failed!")
            time.sleep(3)
            self.driver.get("https://parabank.parasoft.com")

    def transfer_funds(self, amount1, fromaccount, toaccount):
        self.driver.find_element_by_css_selector(self.transferfunds_button_cssSelector).click()
        time.sleep(1)
        self.driver.find_element_by_id(self.amount_box_id).send_keys(amount1)
        time.sleep(1)
        self.driver.find_element_by_id(self.fromaccount_selector_id).send_keys(fromaccount)
        time.sleep(1)
        self.driver.find_element_by_id(self.toaccount_selector_id).send_keys(toaccount)
        time.sleep(1)
        self.driver.find_element_by_css_selector(self.transfersubmit_button_cssSelector).click()
        time.sleep(1)
        transfer_title = self.driver.find_element_by_css_selector("#rightPanel > div > div > h1")
        if transfer_title.text == "Transfer Complete!":
            transfer_info_table = self.driver.find_element_by_css_selector("#rightPanel > div > div")
            print(transfer_info_table.text)
            print("\n'Transfer Funds Test' is Successful!")
            time.sleep(3)
            self.driver.get("https://parabank.parasoft.com")
        else:
            print("\nTest Failed!")
            time.sleep(3)
            self.driver.get("https://parabank.parasoft.com")

    def bill_pay(self, payeename, address, city, state, zipcode, phone, account, verifyaccount, amount2, fromaccount):
        self.driver.find_element_by_css_selector(self.billpay_button_cssSelector).click()
        time.sleep(1)
        driver = self.driver
        submitbutton = self.driver.find_element_by_css_selector(self.sendbillpay_button_cssSelector)
        driver.execute_script("arguments[0].scrollIntoView();", submitbutton)
        self.driver.find_element_by_css_selector(self.payeename_box_cssSelector).send_keys(payeename)
        time.sleep(1)
        self.driver.find_element_by_css_selector(self.address_box_cssSelector).send_keys(address)
        time.sleep(1)
        self.driver.find_element_by_css_selector(self.city_box_cssSelector).send_keys(city)
        time.sleep(1)
        self.driver.find_element_by_css_selector(self.state_box_cssSelector).send_keys(state)
        time.sleep(1)
        self.driver.find_element_by_css_selector(self.zipcode_box_cssSelector).send_keys(zipcode)
        time.sleep(1)
        self.driver.find_element_by_xpath(self.phone_box_xPath).send_keys(phone)
        time.sleep(1)
        self.driver.find_element_by_css_selector(self.account_box_cssSelector).send_keys(account)
        time.sleep(1)
        self.driver.find_element_by_css_selector(self.verifyacc_box_cssSelector).send_keys(verifyaccount)
        time.sleep(1)
        self.driver.find_element_by_css_selector(self.ammount_box_cssSelector).send_keys(amount2)
        time.sleep(1)
        self.driver.find_element_by_css_selector(self.fromaccount_selector_cssSelector).send_keys(fromaccount)
        time.sleep(1)
        submitbutton.click()
        time.sleep(3)
        billpay_title = self.driver.find_element_by_css_selector("#rightPanel > div > div:nth-child(2) > h1")
        if billpay_title.text == "Bill Payment Complete":
            billpayinfo_table = self.driver.find_element_by_css_selector("#rightPanel > div > div:nth-child(2)")
            print(billpayinfo_table.text)
            print("\n'Bill Payment Test' is Successful!")
            time.sleep(3)
            self.driver.get("https://parabank.parasoft.com")
        else:
            print("\nTest Failed!")
            
            time.sleep(3)
            self.driver.get("https://parabank.parasoft.com")

    def find_transactionbyid(self, transferacc, transaction_id):
        self.driver.find_element_by_css_selector(self.findtransactions_button_cssSelector).click()
        time.sleep(1)
        self.driver.find_element_by_id(self.account_selector_id).send_keys(transferacc)
        time.sleep(1)
        self.driver.find_element_by_id(self.transactionid_box_id).send_keys(transaction_id)
        time.sleep(1)
        self.driver.find_element_by_css_selector(self.findbytransacid_button_cssSelector).click()
        time.sleep(1)
        transactionresults_title = self.driver.find_element_by_css_selector("#rightPanel > div > div > h1")
        if transactionresults_title.text == "Transaction Results":
            transactions_table = self.driver.find_element_by_id("transactionTable")
            print(transactions_table.text)
            print("\n'Find Transactions by ID' Test is Successful!")
            time.sleep(3)
            self.driver.get("https://parabank.parasoft.com")
        else:
            print("\nTest Failed!")
            
            time.sleep(3)
            self.driver.get("https://parabank.parasoft.com")

    def find_transactionbydate(self, transferacc, bydate):
        self.driver.find_element_by_css_selector(self.findtransactions_button_cssSelector).click()
        time.sleep(1)
        self.driver.find_element_by_id(self.account_selector_id).send_keys(transferacc)
        time.sleep(1)
        self.driver.find_element_by_id(self.transacdate_box_id).send_keys(bydate)
        time.sleep(1)
        self.driver.find_element_by_css_selector(self.findbydate_button_cssSelector).click()
        time.sleep(1)
        transactionresults_title = self.driver.find_element_by_css_selector("#rightPanel > div > div > h1")
        if transactionresults_title.text == "Transaction Results":
            transactions_table = self.driver.find_element_by_id("transactionTable")
            print(transactions_table.text)
            print("\n'Find Transactions by Date' Test is Successful!")
            time.sleep(3)
            self.driver.get("https://parabank.parasoft.com")
        else:
            print("\nTest Failed!")
            
            time.sleep(3)
            self.driver.get("https://parabank.parasoft.com")

    def find_transactionfromdatetodate(self, transferacc, fromdate, todate):
        self.driver.find_element_by_css_selector(self.findtransactions_button_cssSelector).click()
        time.sleep(1)
        self.driver.find_element_by_id(self.account_selector_id).send_keys(transferacc)
        time.sleep(1)
        self.driver.find_element_by_id(self.transacfromdate_box_id).send_keys(fromdate)
        time.sleep(1)
        self.driver.find_element_by_id(self.transactodate_box_id).send_keys(todate)
        time.sleep(1)
        self.driver.find_element_by_css_selector(self.findbydaterange_button_cssSelector).click()
        time.sleep(1)
        transactionresults_title = self.driver.find_element_by_css_selector("#rightPanel > div > div > h1")
        if transactionresults_title.text == "Transaction Results":
            transactions_table = self.driver.find_element_by_id("transactionTable")
            print(transactions_table.text)
            print("\n'Find Transactions by Date Range' Test is Successful!")
            time.sleep(3)
            self.driver.get("https://parabank.parasoft.com")
        else:
            print("\nTest Failed!")
            
            time.sleep(3)
            self.driver.get("https://parabank.parasoft.com")

    def find_transactionbyamount(self, transferacc, transferamount):
        self.driver.find_element_by_css_selector(self.findtransactions_button_cssSelector).click()
        time.sleep(1)
        self.driver.find_element_by_id(self.account_selector_id).send_keys(transferacc)
        time.sleep(1)
        self.driver.find_element_by_id(self.transacamount_box_id).send_keys(transferamount)
        time.sleep(1)
        self.driver.find_element_by_css_selector(self.findbyamount_button_cssSelector).click()
        time.sleep(1)
        transactionresults_title = self.driver.find_element_by_css_selector("#rightPanel > div > div > h1")
        if transactionresults_title.text == "Transaction Results":
            transactions_table = self.driver.find_element_by_id("transactionTable")
            print(transactions_table.text)
            print("\n'Find Transactions by Amount' Test is Successful!")
            time.sleep(3)
            self.driver.get("https://parabank.parasoft.com")
        else:
            print("\nTest Failed!")
            
            time.sleep(3)
            self.driver.get("https://parabank.parasoft.com")

    def update_contactinfo(self, newname, newlastname, newaddress, newcity, newstate, newzipcode, newphone):
        self.driver.find_element_by_css_selector(self.updatecontactinfo_button_cssSelector).click()
        time.sleep(1)
        self.driver.find_element_by_id(self.firstname_textbox_id).clear()
        self.driver.find_element_by_id(self.firstname_textbox_id).send_keys(newname)
        time.sleep(1)
        self.driver.find_element_by_id(self.lastname_textbox_id).clear()
        self.driver.find_element_by_id(self.lastname_textbox_id).send_keys(newlastname)
        time.sleep(1)
        self.driver.find_element_by_id(self.address_textbox_id).clear()
        self.driver.find_element_by_id(self.address_textbox_id).send_keys(newaddress)
        time.sleep(1)
        self.driver.find_element_by_id(self.city_textbox_id).clear()
        self.driver.find_element_by_id(self.city_textbox_id).send_keys(newcity)
        time.sleep(1)
        self.driver.find_element_by_id(self.state_textbox_id).clear()
        self.driver.find_element_by_id(self.state_textbox_id).send_keys(newstate)
        time.sleep(1)
        self.driver.find_element_by_id(self.zipcode_textbox_id).clear()
        self.driver.find_element_by_id(self.zipcode_textbox_id).send_keys(newzipcode)
        time.sleep(1)
        self.driver.find_element_by_id(self.phonenumber_textbox_id).clear()
        self.driver.find_element_by_id(self.phonenumber_textbox_id).send_keys(newphone)
        time.sleep(2)
        submitbutton = self.driver.find_element_by_css_selector("#rightPanel > div > div > form > table > tbody > tr:nth-child(8) > td:nth-child(2) > input")
        submitbutton.click()
        time.sleep(3)
        updateinfo_title = self.driver.find_element_by_css_selector("#rightPanel > div > div > h1")
        if updateinfo_title.text == "Update Profile":
            update_infotable = self.driver.find_element_by_css_selector("#rightPanel > div > div > p")
            print(update_infotable.text)
            print("\n'Info Update Test' is Successful!")
            time.sleep(3)
            self.driver.get("https://parabank.parasoft.com")
        else:
            print("\nTest Failed!")
            
            time.sleep(3)
            self.driver.get("https://parabank.parasoft.com")

    def request_loan(self, loanamount, downpayment, fromaccount):
        self.driver.find_element_by_css_selector(self.reqloan_button_cssSelector).click()
        time.sleep(1)
        self.driver.find_element_by_id(self.loanamount_box_id).send_keys(loanamount)
        time.sleep(1)
        self.driver.find_element_by_id(self.downpayment_box_id).send_keys(downpayment)
        time.sleep(1)
        self.driver.find_element_by_id(self.fromaccount_selector_id).send_keys(fromaccount)
        time.sleep(2)
        loan_request_title = self.driver.find_element_by_css_selector("#rightPanel > div > div > h1")
        if loan_request_title.text == "Loan Request Processed":
            loan_request_table = self.driver.find_element_by_css_selector("#rightPanel > div > div > table")
            print(loan_request_table.text)
            print("\n'Bill Payment Test' is Successful!")
            time.sleep(3)
            self.driver.get("https://parabank.parasoft.com")
        else:
            print("\nTest Failed!")
            
            time.sleep(3)
            self.driver.get("https://parabank.parasoft.com")

    def logout_action(self):
        self.driver.find_element_by_css_selector(self.logout_button_cssSelector).click()
        time.sleep(2)
        loging_button = self.driver.find_element_by_css_selector("#loginPanel > p:nth-child(2) > a")
        if len(loging_button.text) > 0:
            print("You successfully logged out!")
        else:
            print("Test failed!")