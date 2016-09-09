import unittest
import sys,os
import HTMLTestRunner
import Account_Check_Chrome
import Exchange_Test_Chrome
import IndexOTC_Test_Chrome
import OptionEx_Test_Chrome
import OptionOTC_Test_Chrome
import WatchList_Test_Chrome
import TradeInfo_Check_Chrome
import UserDetail_Check_Chrome

class TestSuite(unittest.TestCase):
    
    suite=unittest.TestLoader().loadTestsFromTestCase(WatchList_Test_Chrome.WatchList_Test_Chrome) 
    '''
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(IndexOTC_Test_Chrome.IndexOTC_Test_Chrome)) 
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Exchange_Test_Chrome.Exchange_Test_Chrome))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(OptionOTC_Test_Chrome.OptionOTC_Test_Chrome))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(OptionEx_Test_Chrome.OptionEx_Test_Chrome))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Account_Check_Chrome.Account_Check_Chrome))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TradeInfo_Check_Chrome.TradeInfo_Check_Chrome))
    
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(UserDetail_Check_Chrome.UserDetail_Check_Chrome))
    '''
    
    outfile = open("E:\\DoNetStudy\\AutoUIPython\\TestReport.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='ci.shzdtech.com Test Report', description='UI Test Report - Chrome' )
    runner.run(suite)
    outfile.close()

