# HRManagementTest
This project includes some test cases for HRM site. Now it contains Auth test cases. 

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
  1- download python from here https://www.python.org/ and run it.
	2- download chrome driver from here http://selenium-python.readthedocs.io/installation.html.

### Running the tests
  1- open cmd and write this command line C:\Python35\Scripts\pip.exe install selenium by that selenium is installed.
	2- open a notepad and write your code then save it with .py extension.
	3- open .py file you just saved and run it using cmd with this command line **python filename.py** or right click on file and open with      IDLE then click run then choose run module.

### Snippet of Code

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
        
		assert "LOGIN Panel" in self.driver.page_source'''
