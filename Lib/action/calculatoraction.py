#coding = utf-8
__author__ = 'shylock'
from Lib.elements.calculator import *
from Lib.assertall.assertcalc import assertrecult
from Lib.basefun import StartCalculator

def calc_case1(self):
    StartCalculator(self)
    one(self)
    two(self)
    three(self)
    Add(self)
    five(self)
    seven(self)
    nine(self)
    equal(self)##123+579
    assertrecult(self,'702')

def calc_case2(self):
    StartCalculator(self)
    swipeleft(self)
    sin(self)
    pi(self)
    swiperight(self)
    Div(self)
    two(self)
    swipeleft(self)
    rparen(self)
    swiperight(self)
    equal(self)
    assertrecult(self,'1')