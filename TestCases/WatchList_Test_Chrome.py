import unittest
import csv
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class WatchList_Test_Chrome(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.mouse = webdriver.ActionChains(self.driver)
        self.driver.set_window_size(1120, 550)
    
    def test_WatchList_Buy(self):
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
                            self.assertEqual(self.driver.title, "Universal Futures & Options Platform-Universal Futures & Options (UFO)")
                            self.assertEqual(self.driver.current_url, "https://ci.shzdtech.com/")
                            
                            men_menu = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Quotes ')]")))
                            self.mouse.move_to_element(men_menu).click().perform()
                            fastrack = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Watch List ')]")))
                            fastrack.click()
                            self.assertEqual(self.driver.title, "Watch List-Universal Futures & Options (UFO)")                                                       
                           
                            data_table = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(.,'Watch List')]")))
                            self.assertIsNotNone(data_table)
                            
                            self.driver.implicitly_wait(30)
                            goodsxpath="//td[contains(.,'"+row[6]+"')]"
                            element=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, goodsxpath)))
                            element.click()
                            
                            element=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='marketdata-page']/body/div[4]/div[3]/div/input")))
                            element.clear()
                            element.send_keys(row[2])
                            self.driver.implicitly_wait(60)
                            
                            element=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='marketdata-page']/body/div[4]/div[4]/div/input")))
                            element.clear()
                            element.send_keys(row[3])
                            self.driver.implicitly_wait(60)
                            
                            Data_Path=os.path.join(os.path.dirname(__file__), os.pardir,'Snapshots/watchlistbuy.jpg')
                            self.driver.get_screenshot_as_file(Data_Path)

                            element=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='marketdata-page']/body/div[4]/div[5]/div[1]")))
                            element.click()
                            
                            time.sleep(5)
                            Data_Path=os.path.join(os.path.dirname(__file__), os.pardir,'Snapshots/watchlistafterbuy.jpg')
                            self.driver.get_screenshot_as_file(Data_Path)
                            
                            self.assertTrue(EC.presence_of_element_located((By.XPATH,"//div[contains(.,'Order sent successfully!')]")))
                            self.driver.quit()
                            
    def test_WatchList_Sell(self):
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
                            self.assertEqual(self.driver.title, "Universal Futures & Options Platform-Universal Futures & Options (UFO)")
                            self.assertEqual(self.driver.current_url, "https://ci.shzdtech.com/")
                            
                            men_menu = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Quotes ')]")))
                            self.mouse.move_to_element(men_menu).click().perform()
                            fastrack = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Watch List ')]")))
                            fastrack.click()
                            self.assertEqual(self.driver.title, "Watch List-Universal Futures & Options (UFO)")                                                       
                           
                            data_table = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(.,'Watch List')]")))
                            self.assertIsNotNone(data_table)
                            
                            self.driver.implicitly_wait(30)
                            goodsxpath="//td[contains(.,'"+row[6]+"')]"
                            #print(goodsxpath)
                            element=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, goodsxpath)))
                            element.click()
                            
                            element=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='marketdata-page']/body/div[4]/div[2]/span[2]")))
                            element.click()
                            
                            element=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='marketdata-page']/body/div[4]/div[3]/div/input")))
                            element.clear()
                            element.send_keys(row[4])
                            self.driver.implicitly_wait(60)
                            
                            element=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='marketdata-page']/body/div[4]/div[4]/div/input")))
                            element.clear()
                            element.send_keys(row[5])
                            self.driver.implicitly_wait(60)
                            
                            Data_Path=os.path.join(os.path.dirname(__file__), os.pardir,'Snapshots/watchlistsell.jpg')
                            self.driver.get_screenshot_as_file(Data_Path)
                            
                            element=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='marketdata-page']/body/div[4]/div[5]/div[1]")))
                            element.click()
                            
                            time.sleep(5)
                            Data_Path=os.path.join(os.path.dirname(__file__), os.pardir,'Snapshots/watchlistaftersell.jpg')
                            self.driver.get_screenshot_as_file(Data_Path)
                            
                            self.assertTrue(EC.presence_of_element_located((By.XPATH,"//div[contains(.,'Order sent successfully!')]")))
                            self.driver.quit()
    
    def tearDown(self):
        self.driver.quit()    
    
if __name__ == '__main__':
    unittest.main()