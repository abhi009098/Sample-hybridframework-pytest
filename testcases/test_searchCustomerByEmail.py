import time
import pytest
from pageobjects.LoginPage import Loginpage
from pageobjects.AddcustomerPage import AddCustomer
from pageobjects.SearchCustomerPage import SearchCustomer
from utilities.readproperties import readconfig
from utilities.customLogger import logGen


class Test_SearchCustomerByEmail_004:
    baseURL = readconfig.getapplicationURL()
    username = readconfig.getuserEmail()
    password = readconfig.getPassword()
    logger = logGen.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("************* SearchCustomerByEmail_004 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Email **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("************* searching customer by emailID **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("uy1ph97b@gmail.com")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail("uy1ph97b@gmail.com")

        assert True == status
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")
        self.driver.close()
