import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestNas(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_addNas(self): 
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
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewSkills")
        browser.find_element(By.ID,"btnAdd").click()
        browser.find_element(By.ID, "skill_name").send_keys("Katalon")
        browser.find_element(By.ID, "skill_description").send_keys("For automation Testing")
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