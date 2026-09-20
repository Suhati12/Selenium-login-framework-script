from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TablePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://practicetestautomation.com/practice-test-table/"

        # Locators
        self.python_radio = (By.XPATH, "//input[@type='radio' and @value='Python']")
        self.table_rows = (By.XPATH, "//table//tbody/tr")
        self.language_column = (By.XPATH, "//table//tbody/tr/td[3]")

    def open(self):
        self.driver.get(self.url)

    def filter_by_python(self):
        wait = WebDriverWait(self.driver, 5)
        radio = wait.until(EC.element_to_be_clickable(self.python_radio))
        radio.click()

    def get_displayed_languages(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_all_elements_located(self.table_rows))
        elements = self.driver.find_elements(*self.language_column)
        return [elem.text.strip() for elem in elements]