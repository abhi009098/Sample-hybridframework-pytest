import time



import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobjects.LoginPage import Loginpage
from utilities.readproperties import readconfig
from utilities.customLogger import logGen
from utilities import excelutils


class Test_002_DDT_Login:
    baseurl = readconfig.getapplicationURL()
    # path = "D:\\LoginData.xlsx"
    path = "C:\\Users\\abhi0\\PycharmProjects\\hybridframework\\testdata\\Excel\\LoginData.xlsx"

    logger = logGen.loggen()
    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("**************** Test_002_DDT_login test **********************")
        self.logger.info("**************** Verifying Login DDT test **********************")
        self.driver = setup  # webdriver.Chrome() will get from conftest.py file
        self.driver.get(self.baseurl)
        self.lp = Loginpage(self.driver)
        # self.lp.clear_text()
        self.rows = excelutils.get_row_count(self.path, 'Sheet1')
        print("Number of rows in excel:", self.rows)

        lst_status = []  # empty list variable

        for r in range(2, self.rows + 1):
            self.username = excelutils.read_cellData(self.path, 'Sheet1', r, 1)
            self.password = excelutils.read_cellData(self.path, 'Sheet1', r, 2)
            self.exp = excelutils.read_cellData(self.path, 'Sheet1', r, 3)

            self.lp.enter_username(self.username)
            self.lp.enter_password(self.password)
            self.lp.click_login()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*****passed******")
                    self.lp.click_logout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info('*****failed*********')
                    self.lp.click_logout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                # if self.exp == "Pass":
                #     self.logger.info("*****failed*********")
                #     self.lp.click_logout()
                #     lst_status.append("Fail")
                # elif self.exp == "Fail":
                #     self.logger.info("*****passed******")
                #     lst_status.append("Pass")
                #     self.logger.info("*****passed******")
                #     lst_status.append("Pass")
                if self.exp == "Fail":
                    self.logger.info("*****passed******")
                    lst_status.append("Pass")
                elif self.exp == "Pass":
                    self.logger.info('*****failed*********')
                    lst_status.append("Fail")

        if "Fail" not in lst_status:
            self.logger.info("********LOGINDATA TEST PASSED**********")
            assert True

        else:
            self.logger.info("********LOGINDATA TEST Failed**********")
            assert False

        self.logger.info("*********End of login DDT Test**********")
        self.logger.info("*********Completed Test_002_DDT_Login**********")


# class Test_002_DDT_Login:
#     def test_login_ddt(self):
#         self.baseurl = readconfig.getapplicationURL()
#         self.path = "C:\\Users\\abhi0\\PycharmProjects\\hybridframework\\testdata\\Excel\\LoginData.xlsx"
#         logger = logGen.loggen()
#
#         self.driver = setup
#         self.driver.get(self.baseurl)
#         self.lp = Loginpage(self.driver)
#
#         self.rows = excelutils.get_row_count(self.path, 'Sheet1')
#
#         lst_status = []
#
#         for r in range(2, self.rows + 1):
#             self.username = excelutils.read_cellData(self.path, 'Sheet1', r, 1)
#             self.password = excelutils.read_cellData(self.path, 'Sheet1', r, 2)
#             self.exp = excelutils.read_cellData(self.path, 'Sheet1', r, 3)
#
#             self.lp.enter_username(self.username)
#             self.lp.enter_password(self.password)
#             self.lp.click_login()
#             time.sleep(5)
#
#             act_title = self.driver.title
#             exp_title = "Dashboard / nopCommerce administration"
#
#             if act_title == exp_title:
#                 if self.exp == "Pass":
#                     lst_status.append("Pass")
#                 elif self.exp == "Fail":
#                     lst_status.append("Fail")
#
#             elif act_title != exp_title:
#                 if self.exp == "Fail":
#                     lst_status.append("Pass")
#                 elif self.exp == "Pass":
#                     lst_status.append("Fail")
#
#         if "Fail" not in lst_status:
#             assert True
#         else:
#             assert False
