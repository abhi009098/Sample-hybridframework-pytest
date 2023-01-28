import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddCustomer:
    # Add customer Page
    lnkCustomers_menu_xpath = "(//a[@class='nav-link'])[21]"
    lnkCustomers_menuitem_xpath = "(//a[@class='nav-link']//p/following::i[contains(@class,'nav-icon far')]/following-sibling::p)[17]"
    btnAddnew_CSS = "a.btn.btn-primary"
    divAddCustomerinfotitle_CSS = "//div[text()='Customer info']"
    txtEmail_xpath = "//input[@type='email']"
    txtPassword_xpath = "//input[@type='password']"
    txtFirstName_CSS = "input[name='FirstName']"
    txtLastName_CSS = "input[name='LastName']"
    rdMaleGender_CSS = "input#Gender_Male"
    rdFeMaleGender_CSS = "input#Gender_Female"
    txtDob_CSS = "input[name='DateOfBirth']"
    txtCompanyName_CSS = "input[name='Company']"
    txtcustomerRoles_xpath = "(//div[@unselectable='on']//div)[2]"
    lstitemAdministrators_xpath = "//span[text()='Administrators']"
    lstitemForummoderators_xpath = "//span[text()='Forum Moderators']"
    lstitemRegistered_xpath = "//span[text()='Registered']"
    lstitemGuests_xpath = "//span[text()='Guests']"
    lstitemVendors_xpath = "//span[text()='Vendors']"
    drpmgrOfVendor_xpath = "//select[@class='form-control valid']"
    txtAdminContent_CSS = "#AdminComment"
    btnSave_CSS = "button[name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btnAddnew_CSS).click()

    def clickonCustomerInfoTitle(self):
        self.driver.find_element(By.CSS_SELECTOR, self.divAddCustomerinfotitle_CSS).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH,self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role == "Forum Moderators":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemForummoderators_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.CSS_SELECTOR, self.rdMaleGender_CSS).click()
        elif gender == 'Female':
            self.driver.find_element(By.CSS_SELECTOR, self.rdFeMaleGender_CSS).click()
        else:
            self.driver.find_element(By.CSS_SELECTOR, self.rdMaleGender_CSS).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.CSS_SELECTOR, self.txtFirstName_CSS).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.CSS_SELECTOR, self.txtLastName_CSS).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(By.CSS_SELECTOR, self.txtDob_CSS).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.CSS_SELECTOR, self.txtCompanyName_CSS).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(By.CSS_SELECTOR, self.txtAdminContent_CSS).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btnSave_CSS).click()
