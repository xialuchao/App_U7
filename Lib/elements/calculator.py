#coding = utf-8
__author__ = 'shylock'

from appium import webdriver


def one(self):
    self.dr.find_element_by_id('com.android.calculator2:id/digit_1').click()
    print 'click 1'

def two(self):
    self.dr.find_element_by_id('com.android.calculator2:id/digit_2').click()
    print 'click 2'

def three(self):
    self.dr.find_element_by_id('com.android.calculator2:id/digit_3').click()
    print 'click 3'

def four(self):
    self.dr.find_element_by_id('com.android.calculator2:id/digit_4').click()

def five(self):
    self.dr.find_element_by_id('com.android.calculator2:id/digit_5').click()
    print 'click 5'

def six(self):
    self.dr.find_element_by_id('com.android.calculator2:id/digit_6').click()

def seven(self):
    self.dr.find_element_by_id('com.android.calculator2:id/digit_7').click()
    print 'click 7'

def eight(self):
    self.dr.find_element_by_id('com.android.calculator2:id/digit_8').click()

def nine(self):
    self.dr.find_element_by_id('com.android.calculator2:id/digit_9').click()
    print 'click 9'

def zero(self):
    self.dr.find_element_by_id('com.android.calculator2:id/digit_0').click()

def Dot(self):
    self.dr.find_element_by_id('com.android.calculator2:id/dec_point').click()

def Del(self):
    self.dr.find_element_by_id('com.android.calculator2:id/del').click()

def Div(self):#/
    self.dr.find_element_by_id('com.android.calculator2:id/op_div').click()

def Mul(self):#x
    self.dr.find_element_by_id('com.android.calculator2:id/op_mul').click()

def Sub(self):#-
    self.dr.find_element_by_id('com.android.calculator2:id/op_sub').click()

def Add(self):#+
    self.dr.find_element_by_id('com.android.calculator2:id/op_add').click()
    print 'click +'

def Dot(self):
    self.dr.find_element_by_id('com.android.calculator2:id/dec_point').click()

def equal(self):
    self.dr.find_element_by_id('com.android.calculator2:id/eq').click()
    print 'click ='

def swipeleft(self):
    self.dr.swipe(1024,1290,280,1290)

def swiperight(self):
    self.dr.swipe(280,1290,1024,1290)

def sin(self):
    self.dr.find_element_by_id('com.android.calculator2:id/fun_sin').click()
    print 'click sin'

def cos(self):
    self.dr.find_element_by_id('com.android.calculator2:id/fun_cos').click()

def tan(self):
    self.dr.find_element_by_id('com.android.calculator2:id/fun_tan').click()

def ln(self):
    self.dr.find_element_by_id('com.android.calculator2:id/fun_ln').click()

def log(self):
    self.dr.find_element_by_id('com.android.calculator2:id/fun_log').click()

def fact(self):#!
    self.dr.find_element_by_id('com.android.calculator2:id/op_fact').click()

def pi(self):#pai
    self.dr.find_element_by_id('com.android.calculator2:id/const_pi').click()

def e(self):
    self.dr.find_element_by_id('com.android.calculator2:id/const_e').click()

def pow(self):#^
    self.dr.find_element_by_id('com.android.calculator2:id/op_pow').click()

def lparen(self):#(
    self.dr.find_element_by_id('com.android.calculator2:id/lparen').click()

def rparen(self):
    self.dr.find_element_by_id('com.android.calculator2:id/rparen').click()

def sqrt(self):
    self.dr.find_element_by_id('com.android.calculator2:id/op_sqrt').click()



