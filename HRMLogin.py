from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest 
import time
class OrangeHRMlLogIn(unittest.TestCase):
	def setUp (self):
		self.driver = webdriver.Chrome()
	def test_login_valid_data(self):
		driver = self.driver
		driver.get ("https://opensource-demo.orangehrmlive.com/")
		elem = driver.find_element_by_id('txtUsername')
		elem.clear()
		elem.send_keys("Admin")
		elem.send_keys(Keys.RETURN)
		elem = driver.find_element_by_id('txtPassword')
		elem.clear()
		elem.send_keys("admin123")
		elem.send_keys(Keys.RETURN)
		time.sleep(5)
		assert "Welcome Admin" in driver.page_source
		elem = driver.find_element_by_id('welcome')
		elem.click ()
		time.sleep(5)
		elem = driver.find_element_by_partial_link_text("Logout").click()
		assert "LOGIN Panel" in driver.page_source

	def test_login_invalid_data (self):
		driver = self.driver
		driver.get ("https://opensource-demo.orangehrmlive.com/")
		elem = driver.find_element_by_id('txtUsername')
		elem.clear()
		elem.send_keys("Admin1")
		elem.send_keys(Keys.RETURN)
		elem = driver.find_element_by_id('txtPassword')
		elem.clear()
		elem.send_keys("admin123")
		elem.send_keys(Keys.RETURN)
		time.sleep(5)
		assert "Invalid credentials" in driver.page_source
	def test_login_SQL_Injection(self):
		driver = self.driver
		driver.get ("https://opensource-demo.orangehrmlive.com/")
		elem = driver.find_element_by_id('txtUsername')
		elem.clear()
		elem.send_keys("1=1")
		elem.send_keys(Keys.RETURN)
		elem = driver.find_element_by_id('txtPassword')
		elem.clear()
		elem.send_keys("1=1")
		elem.send_keys(Keys.RETURN)
		time.sleep(5)
		assert "Invalid credentials" in driver.page_source

	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
    unittest.main()