import pytest
from selenium import webdriver
from pageobj.loginpage import zipcodepage
from utilities.read_properties import Readconfig
from utilities.customlogger import LogGen
from utilities import XLutils
import time
import pathlib
import modulefinder

class Test_002_DDT_Zipcode:
    baseurl = Readconfig.getapplicationURL()
    path=".//testdata/logindata.xlsx"
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_homepageTitle_ddt(self, setup):

        self.logger.info("********* Test_002_DDT_Zipcode *********")
        self.logger.info("********* verify home page *********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.zp = zipcodepage(self.driver)


        self.rows=XLutils.getRowCount(self.path,'Sheet1')
        print("Number of rows in excel:",self.rows)

        lst_status = []

        for r in range(2, self.rows+1):
            self.zp.clicksignin()
            time.sleep(2)
            self.zp.clickloginwithpw()
            time.sleep(2)
            self.Email = XLutils.readData(self.path, 'Sheet1', r, 1)
            self.Password = XLutils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLutils.readData(self.path, 'Sheet1', r, 3)

            self.zp.setemail(self.Email)
            time.sleep(2)
            self.zp.setpassword(self.Password)
            time.sleep(2)
            self.zp.clicksign()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "OrgFarm"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("****** Passed ******")
                    time.sleep(2)
                    self.zp.clickAccount()
                    time.sleep(2)
                    self.zp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Pass":
                    self.logger.info("**** Passed ****")
                    self.zp.clickAccount()
                    time.sleep(2)
                    self.zp.clickLogout()
                    lst_status.append("Pass")
            elif act_title != exp_title:
                if self.exp == "Fail":
                    self.logger.info("****** Failed ******")
                    time.sleep(2)
                    self.zp.clearEmail()
                    self.zp.clearPassword()
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("**** Passed ****")
                    time.sleep(2)
                    self.zp.clearEmail()
                    self.zp.clearPassword()
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("**** Login DDT test Passed ****")
            self.driver.close()
            assert True

        else:
            self.logger.info("**** Login DDT test Failed")
            self.driver.close()
            assert False

        self.logger.info("**** End of Login DDT Test ****")
        self.logger.info("**** Completed loginDDT_002 ****");






