import unittest
import csv
#import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class WatchList_Test_Chrome(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.mouse = webdriver.ActionChains(self.driver)
        self.driver.set_window_size(1120, 550)
      
    def test_WatchList(self):
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
                            
                            men_menu = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Quotes ')]")))
                            self.mouse.move_to_element(men_menu).click().perform()
                            fastrack = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Watch List ')]")))
                            fastrack.click()
                            self.assertEqual(self.driver.title, "Watch List-Universal Futures & Options (UFO)")                                                       
                           
                            data_table = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(.,'Watch List')]")))
                            self.assertIsNotNone(data_table)
                            
                            self.driver.implicitly_wait(30)
                            element=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td[contains(.,'cu1707')]")))
                            element.click()
                            self.driver.get_screenshot_as_file("E:\DoNetStudy\AutoUIPython\snapshot\WatchList.jpg")
                            self.driver.implicitly_wait(20)
                            
                            element=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(.,'Amount')]")))
                            element.find_element_by_class_name("number-container").clear()
                            element.send_keys(row[10])
                            self.driver.implicitly_wait(10)
                            self.driver.get_screenshot_as_file("E:\DoNetStudy\AutoUIPython\snapshot\WatchListbuy.jpg")
                            self.driver.find_element_by_xpath("//div[contains(.,'Make Order')]").click()
                            self.driver.implicitly_wait(10)
                                
    def tearDown(self):
        self.driver.quit()    
    
if __name__ == '__main__':
    unittest.main()