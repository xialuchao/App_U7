#coding = utf-8
__author__ = 'shylock'
#encoding = utf-8
import unittest
from HTML import HTMLTestRunner
from Lib.action.settingsaction import *
from Lib.action.calculatoraction import *
import os
import sys
import time
#get time
now = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
day = time.strftime('%Y-%m-%d',time.localtime(time.time()))
#all of the path
screenshot = '../ScreenShot/' + now +'.png'  #error screenshot path
resultpath = '../Result/' + day    #xml result folder
filename = resultpath + '/' + now + '_result.html'  #xml result path
logpath = '../Log/'+ now + '.txt'
#export the log into folder



class Testing(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'IRDMTSG6FYT89SRC'
        desired_caps['appPackage'] = 'com.android.launcher3'
        desired_caps['appActivity'] = '.Launcher'
        self.dr = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.dr.quit()

    def test_settings_case1(self):
        print 'setting case 1 is starting...'
        setting_case1(self)

    def test_settings_case2(self):
        print 'setting case 2 is starting...'
        setting_case2(self)

    def test_settings_case3(self):
        print 'setting case 3 is starting...'
        setting_case3(self)

    def test_calc_case1(self):
        print 'calculator case 1 is starting...'
        calc_case1(self)

    def test_calc_case2(self):
        print 'calculator case 2 is starting...'
        calc_case2(self)

            # self.dr.get_screenshot_as_file(screenshot)







if __name__ == '__main__':
    # log  = open(logpath,'w')
    # sys.stdout = log
    # sys.path.append(os.path.join(os.path.dirname(os.path.realpath(sys.argv[0]))))


    if os.path.exists(resultpath):
        fp = file(filename,'wb')
        #def test reporter
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Appium reporter',description='testcase')
        #run testcase
        suite = unittest.TestLoader().loadTestsFromTestCase(Testing)
        runner.run(suite)
        fp.close()

    else:
        os.mkdir(resultpath)
        fp = file(filename,'wb')
        #def test reporter
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Appium reporter',description='testcase')
        #run testcase
        suite = unittest.TestLoader().loadTestsFromTestCase(Testing)
        runner.run(suite)
        fp.close()
    # log.close()