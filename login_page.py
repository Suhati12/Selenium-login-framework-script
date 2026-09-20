from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://practicetestautomation.com/practice-test-login/"

        # Locators
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.submit_button = (By.ID, "submit")
        self.error_message = (By.ID, "error")
        self.success_heading = (By.TAG_NAME, "h1")

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(*self.username_input).clear()
        if username:
            self.driver.find_element(*self.username_input).send_keys(username)
        
        self.driver.find_element(*self.password_input).clear()
        if password:
            self.driver.find_element(*self.password_input).send_keys(password)
            
        self.driver.find_element(*self.submit_button).click()

    def get_error_message(self):
        wait = WebDriverWait(self.driver, 5)
        return wait.until(EC.visibility_of_element_located(self.error_message)).text

    def get_success_heading(self):
        wait = WebDriverWait(self.driver, 5)
        return wait.until(EC.visibility_of_element_located(self.success_heading)).text