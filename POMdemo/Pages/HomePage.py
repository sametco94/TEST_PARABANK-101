import time

class HomePage:

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

        ### Customer Login ###
        self.username_textarea_cssSelector = "#loginPanel > form > div:nth-child(2) > input"
        self.password_textarea_cssSelector = "#loginPanel > form > div:nth-child(4) > input"
        self.login_button_cssSelector = "#loginPanel > form > div:nth-child(5) > input"
        self.forgotlogin_button_cssSelector = "#loginPanel > p:nth-child(2) > a"
        self.register_button_cssSelector = "#loginPanel > p:nth-child(3) > a"

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

    def goto_forgotlogin(self):
        self.driver.find_element_by_css_selector(self.forgotlogin_button_cssSelector).click()

    def goto_registerpage(self):
        self.driver.find_element_by_css_selector(self.register_button_cssSelector).click()

    def goto_and_printout_aboutus(self):
        self.driver.find_element_by_css_selector(self.aboutuslogo_button_cssSelector).click()
        time.sleep(3)
        textarea = self.driver.find_element_by_id("rightPanel")
        print(textarea.text)
        time.sleep(1)
        self.driver.find_element_by_css_selector(self.homepagelogo_button_cssSelector).click()

    def login_action(self, username, password):
        self.driver.find_element_by_css_selector(self.username_textarea_cssSelector).send_keys(username)
        self.driver.find_element_by_css_selector(self.password_textarea_cssSelector).send_keys(password)
        time.sleep(1)
        self.driver.find_element_by_css_selector(self.login_button_cssSelector).click()
        time.sleep(1)
        AccountOverview = self.driver.find_element_by_css_selector("#rightPanel > div > div")
        HeadText = self.driver.find_element_by_css_selector("#rightPanel > div > div > h1").text
        if HeadText == "Accounts Overview":
            print(AccountOverview.text)
            print("'Login Test' Successful!")
        else:
            self.driver.find_element_by_css_selector(self.homepagelogo_button_cssSelector).click()
            print("Test UNsuccessful!")