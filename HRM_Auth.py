from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest 
import time
class OrangeHRMlLogIn(unittest.TestCase):
	def setUp (self):
		self.driver = webdriver.Chrome()
		driver = self.driver
		driver.get ("https://opensource-demo.orangehrmlive.com/")
		self.userName = driver.find_element_by_id('txtUsername')
		self.passWord = driver.find_element_by_id('txtPassword')

	def test_login_with_valid_data_then_return_success(self):
		self.userName.clear()
		self.userName.send_keys("Admin")
		self.passWord.clear()
		self.passWord.send_keys("admin123")
		self.passWord.send_keys(Keys.RETURN)

		welcomeAdmin = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "welcome")))

		assert "Welcome Admin" in self.driver.page_source

	def test_login_invalid_data (self):
		self.userName.clear()
		self.userName.send_keys("Admin1")
		self.passWord.clear()
		self.passWord.send_keys("admin123")
		self.passWord.send_keys(Keys.RETURN)

		element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "spanMessage")))

		assert "Invalid credentials" in self.driver.page_source

	def test_login_SQL_Injection(self):
		self.userName.clear()
		self.userName.send_keys("1=1")
		self.passWord.clear()
		self.passWord.send_keys("1=1")
		self.passWord.send_keys(Keys.RETURN)

		element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "spanMessage")))

		assert "Invalid credentials" in self.driver.page_source

	def tearDown(self):
		self.driver.close()

class OrangeHRMlLogout(unittest.TestCase):
	def setUp (self):
		self.driver = webdriver.Chrome()
		driver = self.driver
		driver.get ("https://opensource-demo.orangehrmlive.com/")
		self.userName = driver.find_element_by_id('txtUsername')
		self.passWord = driver.find_element_by_id('txtPassword')

	def test_logout_successfully(self):
		self.userName.clear()
		self.userName.send_keys("Admin")
		self.passWord.clear()
		self.passWord.send_keys("admin123")
		self.passWord.send_keys(Keys.RETURN)

		welcomeAdmin = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "welcome")))
		welcomeAdmin.click() 

		logOut = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Logout"))).click()

		logInAdmin = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "logInPanelHeading")))
        
		assert "LOGIN Panel" in self.driver.page_source

	def tearDown(self):
		self.driver.close()
if __name__ == "__main__":
    unittest.main()