from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_menu = (By.LINK_TEXT, "PIM")

    def navigate_to_pim(self):
        action = ActionChains(self.driver)
        pim_element = self.driver.find_element(*self.pim_menu)
        action.move_to_element(pim_element).click().perform()
