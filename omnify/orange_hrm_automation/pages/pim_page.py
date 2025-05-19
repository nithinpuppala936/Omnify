from selenium.webdriver.common.by import By

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_employee_button = (By.LINK_TEXT, "Add Employee")
        self.employee_list_button = (By.LINK_TEXT, "Employee List")

    def go_to_add_employee(self):
        self.driver.find_element(*self.add_employee_button).click()

    def go_to_employee_list(self):
        self.driver.find_element(*self.employee_list_button).click()
