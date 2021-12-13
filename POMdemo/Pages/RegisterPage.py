import time


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

        self.firstname_textbox_id = "customer.firstName"
        self.lastname_textbox_id = "customer.lastName"
        self.address_textbox_id = "customer.address.street"
        self.city_textbox_id = "customer.address.city"
        self.state_textbox_id = "customer.address.state"
        self.zipcode_textbox_id = "customer.address.zipCode"
        self.phonenumber_textbox_id = "customer.phoneNumber"
        self.ssn_textbox_id = "customer.ssn"
        self.username_textbox_id = "customer.username"
        self.password_textbox_id = "customer.password"
        self.repassword_textbox_id = "repeatedPassword"

        self.registerconfirm_button_xPath = "//*[@id='customerForm']/table/tbody/tr[13]/td[2]/input"

    def fillin_and_submit(self, firstname, lastname, address, city, state, zipcode, phone, ssn, username, password, repassword):
        self.driver.find_element_by_id(self.firstname_textbox_id).send_keys(firstname)
        self.driver.find_element_by_id(self.lastname_textbox_id).send_keys(lastname)
        self.driver.find_element_by_id(self.address_textbox_id).send_keys(address)
        self.driver.find_element_by_id(self.city_textbox_id).send_keys(city)
        self.driver.find_element_by_id(self.state_textbox_id).send_keys(state)
        self.driver.find_element_by_id(self.zipcode_textbox_id).send_keys(zipcode)
        self.driver.find_element_by_id(self.phonenumber_textbox_id).send_keys(phone)
        self.driver.find_element_by_id(self.ssn_textbox_id).send_keys(ssn)
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)
        self.driver.find_element_by_id(self.repassword_textbox_id).send_keys(repassword)
        time.sleep(2)

        self.driver.find_element_by_xpath(self.registerconfirm_button_xPath).click()
        time.sleep(2)
        test_textpanel = self.driver.find_element_by_id("rightPanel")
        print(test_textpanel.text)
