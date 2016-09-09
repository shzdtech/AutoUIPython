import unittest
import csv
#import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginTest_Chrome(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()       
        self.mouse = webdriver.ActionChains(self.driver)    
        self.driver.set_window_size(1120, 550)
        
    def test_Login(self):
        with open('E:\DoNetStudy\AutoUIPython\users.csv', 'rU') as UsersInfoFile:
                        reader=csv.reader(UsersInfoFile)
                        next(reader, None)  # skip the headers
                        for row in reader:
                            self.driver.get("http://ci.shzdtech.com/Account/Login")
                            #time.sleep(30)
                            self.assertEqual(self.driver.title, "Log in-Universal Futures & Options (UFO)")
                            self.driver.find_element_by_xpath("//input[@id='UserName']").send_keys(row[0])
                            self.driver.find_element_by_xpath("//input[@id='Password']").send_keys(row[1])
                            self.driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()                          
                            self.assertEqual(self.driver.title, "Universal Futures & Options Platform-Universal Futures & Options (UFO)")
                            self.assertEqual(self.driver.current_url, "http://ci.shzdtech.com/")
                            #time.sleep(30)                            
                            #self.driver.find_element_by_xpath("//span[contains(.,'Quotes ')]").click()
                            #self.driver.find_element_by_xpath("//span[contains(.,'Watch List ')]").click()
                            #span_element=self.driver.find_element_by_xpath("//span[contains(.,'Quotes ')]")
                            #self.mouse.move_to_element(span_element).click().perform()
                            #self.driver.get("http://ci.shzdtech.com/MarketData")
                            #self.driver.find_element_by_xpath("//span[contains(.,'Watch List ')]").click()
                            #time.sleep(30)
                            #self.assertEqual(self.driver.title, "Watch List-Universal Futures & Options (UFO)")
                            
                            #span_element=self.driver.find_element_by_xpath("//span[contains(.,'MyTrade')]")
                            #self.mouse.move_to_element(span_element).click().perform()
                            #self.driver.get("http://ci.shzdtech.com/MarketData")
                            #self.driver.find_element_by_xpath("//span[contains(.,'Log out')]").click()
                            #time.sleep(30)
                            #men_menu = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Quotes ')]")))
                            #self.mouse.move_to_element(men_menu).click().perform()
                            #fastrack = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Watch List ')]")))
                            #ActionChains(self.driver).move_to_element(fastrack).perform()
                            #fastrack.click()
                            #self.assertEqual(self.driver.title, "Watch List-Universal Futures & Options (UFO)")                                                       
                                                                    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()