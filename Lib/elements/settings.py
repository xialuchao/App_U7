#coding = utf-8

__author__ = 'shylock'


from appium import webdriver
from Lib.basefun import findElement,setUp
from Lib.assertall.assertsettings import *


#first page
def clickDataUsage(self):
    self.dr.find_element_by_name('Data usage').click()

def clickSoundAndNotification(self):
    self.dr.find_element_by_name('Sound & notification').click()

def clickDisplay(self):
    self.dr.find_element_by_name('Display').click()







#the second page
def clickCellular(self):
    self.dr.find_elements_by_class_name(self,'android.widget.LinearLayout')[1].click()

def clickMobile(self):
    self.dr.find_element_by_name('Mobile').click()

def clickMobileData(self):
    MobileSwitch = self.dr.find_element_by_class_name('android.widget.Switch').text
    if MobileSwitch == 'OFF':
        print 'the mobile switch status is off'
        assertnetworkstatus(self,0)
        print 'assert the network is off'
        self.dr.find_element_by_class_name('android.widget.Switch').click()
        print 'the mobile switch status is on'
    elif MobileSwitch == 'ON':
        print 'the mobile switch status is on'

def closeMobileData(self):
    self.dr.find_element_by_class_name('android.widget.Switch').click()
    self.dr.find_element_by_id('android:id/button1').click()
    print 'close the mobile data'

def clickBrighnessLevel(self):
    self.dr.find_element_by_name('Brightness level').click()

def chooseminibright(self):
    print 'click the mini bright'
    self.dr.tap([(215,225)])

def choosemidbright(self):
    print 'click the mid bright'
    self.dr.tap([(525,225)])

def choosemaxbright(self):
    print 'click the max birght'
    self.dr.tap([(815,225)])


#battery
def clickPowersaving(self):
    self.dr.find_element_by_name('Intelligent power saving standby')
