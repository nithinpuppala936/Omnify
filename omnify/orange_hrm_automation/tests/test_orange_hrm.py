import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from pages.add_employee_page import AddEmployeePage
import time
from selenium.webdriver.chrome.service import Service

print("Test started...")
def test_orange_hrm_flow():
    print("Launching browser...")

    service = Service(r"C:\Users\puppa\OneDrive\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    print("Browser launched.")


    # Step 2: Login to OrangeHRM
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("Admin", "admin123")
    time.sleep(3)

    # Step 3: Navigate to PIM module
    dashboard = DashboardPage(driver)
    dashboard.navigate_to_pim()
    time.sleep(2)

    # Step 4: Go to Add Employee and add multiple employees
    pim_page = PIMPage(driver)
    pim_page.go_to_add_employee()
    time.sleep(2)

    add_employee = AddEmployeePage(driver)
    employees = [("John", "Doe"), ("Jane", "Smith"), ("Alice", "Brown"), ("Bob", "Jones")]

    for first, last in employees:
        add_employee.add_employee(first, last)
        time.sleep(2)
        pim_page.go_to_add_employee()
        time.sleep(2)

    # Step 5: Go to Employee List to verify employees
    pim_page.go_to_employee_list()
    time.sleep(3)

    # Step 6: Verify each employee is present in the list
    for first, last in employees:
        full_name = first + " " + last
    try:
        employee_element = driver.find_element(By.XPATH, f"//div[text()='{full_name}']")
        if employee_element:
            print(f"Name Verified: {full_name}")
    except Exception as e:
        print(f"Employee not found: {full_name}")

    


    # Step 7: Logout closing the browser
    print("Test complete. Employees added and verified.")
    driver.quit()
if __name__ == "__main__":
    test_orange_hrm_flow()

