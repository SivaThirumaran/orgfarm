import pytest
from selenium import webdriver
from pageobj.loginpage import zipcodepage
from utilities.read_properties import Readconfig
from utilities.customlogger import LogGen
import time


class Test_001_Zipcode:
    baseurl = Readconfig.getapplicationURL()
    email = Readconfig.getemail()
    password = Readconfig.getpassword()
    pincode = Readconfig.getpincode()
    logger=LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepageTitle(self,setup):

        self.logger.info("********* Test_001_Zipcode *********")
        self.logger.info("********* verify home page *********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.zp=zipcodepage(self.driver)
        self.zp.clicksignin()
        time.sleep(2)
        self.zp.clickloginwithpw()
        time.sleep(2)
        self.zp.setemail(self.email)
        self.zp.setpassword(self.password)
        time.sleep(2)
        self.zp.clicksign()
        time.sleep(2)
        act_title=self.driver.title
        
        if act_title=="OrgFarm":
            assert True
            self.driver.close()
            self.logger.info("********* Title passed *********")
        else:
            self.driver.save_screenshot(".\\screenshot\\"+"test_homepageTitle.png")
            self.driver.close()
            self.logger.error("********* Title failed *********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_pincode(self,setup):

        self.logger.info("********* Test_001_Zipcode *********")
        self.logger.info("********* verifying pincode *********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.zp=zipcodepage(self.driver)
        time.sleep(2)
        self.zp.setpincode(self.pincode)
        time.sleep(2)
        self.zp.clicksubmit()
        time.sleep(2)
        act_title=self.driver.title

        if act_title=="Standard Delivery - OrgFarm":
            assert True
            self.driver.close()
            self.logger.info("********* Title passed *********")
        else:
            self.driver.save_screenshot(".\\screenshot\\"+"test_pincode.png")
            self.driver.close()
            self.logger.error("********* Title failed *********")
            assert False

