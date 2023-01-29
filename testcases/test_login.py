import pytest
from selenium import webdriver
from pageobjects.LoginPage import Loginpage
from utilities.readproperties import readconfig
from utilities.customLogger import logGen


class Test_001_Login:
    baseurl = readconfig.getapplicationURL()
    username = readconfig.getuserEmail()
    password = readconfig.getPassword()
    logger = logGen.loggen()

    #@pytest.mark.regression
    def test_homepage_title(self, setup):
        self.logger.info("**************** Test_001_Login *******************")
        self.logger.info("**************** Verifying home page title **********************")
        self.driver = setup  # webdriver.Chrome() will get from conftest.py file
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**************** home page title passed **********************")

        else:
            self.driver.save_screenshot(
                "C:\\Users\\abhi0\\PycharmProjects\\hybridframework\\screenshots\\homepage_title.png")
            # time.sleep(3)
            self.driver.close()
            # self.logger.info("**************** home page title is failed **********************")
            self.logger.info("**************** home page title is failed **********************")
            assert False
    # @pytest.mark.sanity
    # @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("**************** Verifying login test **********************")
        self.driver = setup  # webdriver.Chrome() will get from conftest.py file
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp = Loginpage(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("**************** login test passed **********************")

        else:
            self.driver.save_screenshot(
                "C:\\Users\\abhi0\\PycharmProjects\\hybridframework\\screenshots\\login_title.png")
            # time.sleep(3)
            self.driver.close()
            self.logger.info("**************** login test failed **********************")
            assert False
