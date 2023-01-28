import pytest
import time

from selenium.webdriver.common.by import By

from pageobjects.LoginPage import Loginpage
from pageobjects.AddcustomerPage import AddCustomer
from utilities.readproperties import readconfig
from utilities.customLogger import logGen
import string
import random


class Test_003_AddCustomer:
    baseURL = readconfig.getapplicationURL()
    username = readconfig.getuserEmail()
    password = readconfig.getPassword()
    logger = logGen.loggen()  # Logger

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Add Customer Test **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddnew()

        self.logger.info("************* Providing customer info **********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        #self.addcust.setCustomerRoles("Administrators")
       # self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("siva")
        self.addcust.setLastName("abhi")
        self.addcust.setDob("5/29/1989")  # Format: D / MM / YYY
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("This is for testing.........")
        self.addcust.clickOnSave()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(
                "C:\\Users\\abhi0\\PycharmProjects\\hybridframework\\screenshots\\test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False


        self.logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
