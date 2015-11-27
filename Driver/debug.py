#coding = utf-8
# __author__ = 'shylock'

from Lib.basefun import setUp,findApp
from Lib.action.calculatoraction import calc
from Lib.action.settingsaction import test_setting
from appium import webdriver

from time import sleep
import unittest
print 1

class Testing(unittest.TestCase):

    def test_test(self):
        test_setting(self)
        print 'suc'
if __name__ == '__main__':
    print 2
    suite = unittest.TestLoader().loadTestsFromTestCase(Testing)
    unittest.TextTestRunner(verbosity=2).run(suite)
