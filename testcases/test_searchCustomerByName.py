import time
import pytest
from pageobjects.LoginPage import Loginpage
from pageobjects.AddcustomerPage import AddCustomer
from pageobjects.SearchCustomerPage import SearchCustomer
from utilities.readproperties import readconfig
from utilities.customLogger import logGen


class Test_SearchCustomerByName_005:
    baseURL = readconfig.getapplicationURL()
    username = readconfig.getuserEmail()
    password = readconfig.getPassword()
    logger = logGen.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("************* SearchCustomerByName_005 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Name **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        time.sleep(2)

        self.logger.info("************* searching customer by Name **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("siva")
        searchcust.setLastName("abhi")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("siva abhi")

        assert True == status
        self.logger.info("***************  TC_SearchCustomerByName_005 Finished  *********** ")
        self.driver.close()
