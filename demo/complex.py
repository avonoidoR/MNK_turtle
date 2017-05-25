#!/usr/bin/python

import unittest
class ComplexCartesian(object):
    def __init__(self,re,im):
        self.re = re
        self.im = im

    def __repr__(self):
        return 'ComplexCartesian({},{})'  .format(self.re,self.im)

    def __add__(self,other):
        return ComplexCartesian(self.re+other.re, self.im+other.im)


class UnittestComplex(unittest.TestCase):
    def test_Complex(self):
        num = ComplexCartesian(2.73, -12.14)
        self.assertEqual(num.re, 2.73)
        self.assertEqual(num.im, -12.14)

    def test_reprComplex(self):
        num = ComplexCartesian(2.73, -12.13)
        self.assertEqual(repr(num),'ComplexCartesian(2.73,-12.13)')

    def test_addComplex(self):
        num1=ComplexCartesian(2.72, -12.12)
        num2=ComplexCartesian(-2.72, 12.12)
        num=num1+num2
        self.assertAlmostEqual(num.re, 0)
        self.assertAlmostEqual(num.im, 0)
            
        
if __name__=='__main__':
    unittest.main()
