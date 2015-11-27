#coding = utf-8
__author__ = 'shylock'
from appium import webdriver
from Lib.basefun import *
from appium.webdriver.connectiontype import ConnectionType


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'IRDMTSG6FYT89SRC'
desired_caps['appPackage'] = 'com.android.launcher3'
desired_caps['appActivity'] = '.Launcher'
dr = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

#dr.find_element_by_accessibility_id('Apps').click()
dr.start_activity('com.android.deskclock','.DeskClock')
dr.find_element_by_accessibility_id('Alarm').click()
dr.find_element_by_id('com.android.deskclock:id/fab')







