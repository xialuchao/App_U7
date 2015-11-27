#coding = utf-8
__author__ = 'shylock'
from appium import webdriver
from time import sleep

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

def findApp(self,app):
    self.dr.find_element_by_accessibility_id('Apps').click()
    a = 1
    while a < 10:
        list = self.dr.find_elements_by_class_name("android.widget.TextView")
        for i in range(len(list)):
            if list[i].text == app:
                list[i].click()
                return
        self.dr.swipe(555,222,222,222)
        a = a + 1


def findElement(self,element):
    a = 1
    while a < 10:
        list = self.dr.find_elements_by_class_name("android.widget.TextView")
        for i in range(len(list)):
            if list[i].text == element:
                list[i].click()
                return
        self.dr.swipe(540,1900,540,0)
        a = a + 1


def findelement(self,element):
    a = 1
    while a < 10:
        list = self.dr.find_elements_by_class_name("android.widget.TextView")
        for i in range(len(list)):
            if list[i].text == element:
                print element
                self.dr.find_element_by_name(element).click()
                return
        sleep(1)
        self.dr.swipe(540,1900,540,0)
        a = a + 1



##start activity
def StartSettings(self):
    self.dr.start_activity('com.android.settings','.Settings')

def StartCalculator(self):
    self.dr.start_activity('com.android.calculator2','.Calculator')
