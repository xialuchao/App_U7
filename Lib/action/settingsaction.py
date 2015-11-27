__author__ = 'shylock'

from Lib.basefun import *
from Lib.elements.settings import *
from Lib.assertall.assertsettings import *

def setting_case1(self):
    StartSettings(self)
    clickDataUsage(self)
    clickMobile(self)
    clickMobileData(self)
    assertmobiledataon(self)
    assertnetworkstatus(self,4)
    print'assert the network is on'
    closeMobileData(self)

def setting_case2(self):
    StartSettings(self)
    clickDisplay(self)
    clickBrighnessLevel(self)
    chooseminibright(self)
    choosemaxbright(self)
    choosemidbright(self)

def setting_case3(self):
    StartSettings(self)
    findelement(self,'Battery')
    clickPowerSaving(self)


