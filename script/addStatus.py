import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestUser(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_add(self): 
        # LOGIN
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(3)
        browser.find_element(By.ID, "txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID, "txtPassword").send_keys("admin123") 
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click()
        time.sleep(1)

        # ADD
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/admin/employmentStatus")
        browser.find_element(By.ID,"btnAdd").click() 
        browser.find_element(By.ID, "empStatus_name").send_keys("Probition")
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(1)

        # CHECK
        welcome_act = browser.find_element(By.XPATH,"//form/div[2]").text
        welcome_exp = 'Successfully Saved'
        self.assertIn(welcome_exp, welcome_act)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()