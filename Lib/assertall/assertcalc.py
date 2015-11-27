#coding = utf-8
__author__ = 'shylock'

def assertrecult(self,res):
    result = self.dr.find_element_by_id('com.android.calculator2:id/formula').text
    print result
    self.assertEqual(result , res)


