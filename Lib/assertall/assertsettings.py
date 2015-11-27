#coding = utf-8

__author__ = 'shylock'
from appium import webdriver


def assertmobiledataon(self):
    MobileSwitch = self.dr.find_element_by_class_name('android.widget.Switch').text
    self.assertEqual(MobileSwitch,'ON')

def assertnetworkstatus(self,statusnum):
    status = self.dr.network_connection
    self.assertEqual(status,statusnum)
    ##