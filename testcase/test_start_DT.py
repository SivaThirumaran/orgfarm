import pytest
from selenium import webdriver
from pageobj.loginpage import zipcodepage
from utilities.read_properties import Readconfig
from utilities.customlogger import LogGen
from utilities import XLutils
import time


class Test_003_DDT_Zipcode:
    baseurl = Readconfig.getapplicationURL()
    path=".//testdata/zipcode.xlsx"
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_pincode_DT(self,setup):
        self.logger.info("********* Test_003_DDT_Zipcode *********")
        self.logger.info("********* verify home page *********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.zp=zipcodepage(self.driver)

        self.rows = XLutils.getRowCount(self.path,'Sheet1')
        print("Number of rows in excel:", self.rows)

        lst_status = []

        for r in range(2, self.rows+1):
            self.zipcode = XLutils.readData(self.path, 'Sheet1', r, 1)
            self.exp = XLutils.readData(self.path, 'Sheet1', r, 2)

            self.zp.setpincode(self.zipcode)
            time.sleep(3)
            self.zp.clicksubmit()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Standard Delivery - OrgFarm"



            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("**** Passed ****")
                    self.zp.clickLocation()
                    time.sleep(5)
                    self.zp.clickCHGlocation();
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("**** Failed ****")
                    self.zp.clickCLOSEbutton();
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("**** Failed ****")
                    self.zp.clickLocation()
                    time.sleep(5)
                    self.zp.clickCHGlocation();
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("**** Passed ****")
                    self.zp.clickCLOSEbutton();
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("**** Login DDT test Passed ****")
            self.driver.close()
            assert True

        else:
            self.logger.info("**** Login DDT test Failed ****")
            self.driver.close()
            assert False

        self.logger.info("**** End of Login DDT Test ****")
        self.logger.info("**** Completed LoginDDT 003 ****");



