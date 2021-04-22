from selenium import webdriver
class zipcodepage:
    button_signin_xpath="/html/body/div[2]/div[2]/div/div/div/div/div[1]/p/a"
    button_login_with_pw_xpath="//*[@id='login-form']/div/div[2]/div/a"
    textbox_email_name="email"
    textbox_password_name="password"
    button_sign_name="login"
    textbox_pincode_id="searchTextField"
    button_start_xpath="//*[@id='submit']"
    button_Account_xpath="/html/body/div[2]/div[1]/div/div/div[2]/div/div"
    button_Logout_xpath="/html/body/div[2]/div[1]/div/div/div[2]/div/div/ul/li[10]"
    button_Location_xpath="//*[@id='sticky-wrapper']/div/div[1]/div[2]/div[3]/a[1]"
    button_CHGLocation_xpath="//*[@id='useraddress-popup']/div/div/div/div/div/div/a"
    button_CLRpincode_name="zipcode"
    button_CLOSEbutton_xpath="/html/body/div[12]/div[7]/div/button"


    def __init__(self,driver):
        self.driver=driver

    def clicksignin(self):
        self.driver.find_element_by_xpath(self.button_signin_xpath).click()

    def clickloginwithpw(self):
        self.driver.find_element_by_xpath(self.button_login_with_pw_xpath).click()

    def setemail(self,email):
        self.driver.find_element_by_name(self.textbox_email_name).send_keys(email)

    def setpassword(self,password):
        self.driver.find_element_by_name(self.textbox_password_name).send_keys(password)

    def clicksign(self):
        self.driver.find_element_by_name(self.button_sign_name).click()

    def setpincode(self,pincode):
        self.driver.find_element_by_id(self.textbox_pincode_id).clear()
        self.driver.find_element_by_id(self.textbox_pincode_id).send_keys(pincode)

    def clicksubmit(self):
        self.driver.find_element_by_xpath(self.button_start_xpath).click()

    def clickAccount(self):
        self.driver.find_element_by_xpath(self.button_Account_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.button_Logout_xpath).click()

    def clickLocation(self):
        self.driver.find_element_by_xpath(self.button_Location_xpath).click()

    def clickCHGlocation(self):
        self.driver.find_element_by_xpath(self.button_CHGLocation_xpath).click()

    def clickCLRpincode(self):
        self.driver.find_element_by_name(self.button_CLRpincode_name).clear()

    def clickCLOSEbutton(self):
        self.driver.find_element_by_xpath(self.button_CLOSEbutton_xpath).click()

    def clearEmail(self):
        self.driver.find_element_by_name(self.textbox_email_name).clear()

    def clearPassword(self):
        self.driver.find_element_by_name(self.textbox_password_name).clear()


