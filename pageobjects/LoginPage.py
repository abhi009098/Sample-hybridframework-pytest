from selenium.webdriver.common.by import By



class Loginpage:
    textbox_username_css = "input.email"
    textbox_password_css = "input.password"
    button_login_css = "button[type='submit']"
    logout_xpath = "(//a[normalize-space()='Logout'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_username_css).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_username_css).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_password_css).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_password_css).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_login_css).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_xpath).click()

    def clear_text(self):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_username_css).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_password_css).clear()
