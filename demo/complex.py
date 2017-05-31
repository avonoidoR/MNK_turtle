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

    def __reduce__(self,other):
        return ComplexCartesian(self.re-other.re, self.im-other.im)

    

class ComplexPolar(object):
    def __init__(self,mod,phase):
        self.mod = mod
        self.phase = phase

    def __repr__(self):
        return 'ComplexPolar({}*e**i*{})' .format(self.mod,self.phase)

    def __mul__(self,other):
        return ComplexPolar(self.mod*other.mod, self.phase+other.phase)



class UnittestComplexCartesian(unittest.TestCase):
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
        
    def test_reduceComplex(self):
        num1=ComplexCartesian(2.72, -12.12)
        num2=ComplexCartesian(-2.72, 12.12)
        num=num1-num2
        self.assertAlmostEqual(num.re, 5.44)
        self.assertAlmostEqual(num.im, -24.24)
    

class UnittestComplexPolar(unittest.TestCase):
    def test_Complex(self):
        num=ComplexPolar(2.73, 30)
        self.assertEqual(num.mod, 2.73)
        self.assertEqual(num.phase, 30)

    def test_reprComplex(self):
        num=ComplexPolar(2.73, 30)
        self.assertEqual(repr(num), 'ComplexPolar(2.73*e**i*30)')

    def test_addComplex(self):
        num1=ComplexPolar(2, -30)
        num2=ComplexPolar(2, 30)
        num=num1*num2
        self.assertAlmostEqual(num.mod, 4)
        self.assertAlmostEqual(num.phase, 0)
        
        
if __name__=='__main__':
    unittest.main()
