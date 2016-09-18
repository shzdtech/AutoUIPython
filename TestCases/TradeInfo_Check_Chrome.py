import unittest
import csv
#import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
from itertools import count

class TradeInfo_Check_Chrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.mouse = webdriver.ActionChains(self.driver)
        self.driver.set_window_size(1120, 550)
        
    def test_url_TradeInfo(self):
        Data_Path=os.path.join(os.path.dirname(__file__), os.pardir, "data.csv")
        with open(Data_Path, 'rU') as UsersInfoFile:
                        reader=csv.reader(UsersInfoFile)
                        next(reader, None)  # skip the headers
                        for row in reader:
                            self.driver.get("https://ci.shzdtech.com/Account/Login")
                           
                            self.assertEqual(self.driver.title, "Log in-Universal Futures & Options (UFO)")
                            self.driver.find_element_by_xpath("//input[@id='UserName']").send_keys(row[0])
                            self.driver.find_element_by_xpath("//input[@id='Password']").send_keys(row[1])
                            self.driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()                          
                            self.assertEqual(self.driver.current_url, "https://ci.shzdtech.com/")
                            
                            men_menu = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'MyTrade')]")))
                            self.mouse.move_to_element(men_menu).click().perform()
                            fastrack = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Trade Info')]")))
                            fastrack.click()                         
                            self.assertEqual(self.driver.title, "Report-Universal Futures & Options (UFO)")
                                            
                            data_table = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@id='all_orders']")))
                            self.assertIsNotNone(data_table)
                            time.sleep(30)
                            goodsxpath="//td[contains(.,'"+row[6]+"')]"
                            count=len(self.driver.find_elements_by_xpath(goodsxpath))
                            self.assertEqual(count,2)
                           
                            Data_Path=os.path.join(os.path.dirname(__file__), os.pardir,'Snapshots/TradeInfo.jpg')
                            self.driver.get_screenshot_as_file(Data_Path)
                        
    def tearDown(self):
        self.driver.quit()
    
if __name__ == '__main__':
    unittest.main()