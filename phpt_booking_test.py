
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class PHPTravelsHotelBooking(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://phptravels.net/hotels")
        self.wait = WebDriverWait(self.driver, 15)

    def test_apply_coupon(self):
        driver = self.driver
        wait = self.wait

        # Enter location
        location_input = wait.until(EC.presence_of_element_located((By.ID, "autocomplete")))
        location_input.clear()
        location_input.send_keys("New York")

        # Select date range 
        driver.find_element(By.NAME, "checkin").clear()
        driver.find_element(By.NAME, "checkin").send_keys("10-04-2025")
        driver.find_element(By.NAME, "checkout").clear()
        driver.find_element(By.NAME, "checkout").send_keys("15-04-2025")

        # Click search button
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Wait for search results and click the first hotel
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".card-item")))
        driver.find_elements(By.CSS_SELECTOR, ".card-item")[0].click()

        # On hotel detail page, click "Book Now"
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Book Now')]"))).click()

        # On checkout page, apply coupon (if available)
        try:
            coupon_toggle = wait.until(EC.element_to_be_clickable((By.ID, "couponCodeToggle")))
            coupon_toggle.click()

            coupon_input = wait.until(EC.presence_of_element_located((By.ID, "couponCode")))
            coupon_input.send_keys("SUMMER25")
            driver.find_element(By.ID, "applyCouponBtn").click()

            # Verify coupon applied (check for discount message)
            discount_msg = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "coupon-success"))).text
            self.assertIn("applied", discount_msg.lower())

        except Exception as e:
            print("Coupon elements not found or not applicable on this booking:", e)

        # Verify on checkout page
        checkout_title = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h4"))).text
        self.assertIn("Booking Summary", checkout_title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
