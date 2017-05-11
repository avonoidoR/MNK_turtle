#!/usr/bin/python

import unittest
import operator
import functools

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
        
        
        

class TestGcd(unittest.TestCase):
    def test_gcd1(self):
        self.assertEqual(gcd(3,5),1)

    def test_gcd2(self):
        self.assertEqual(gcd(5,0),5)

    def test_gcd3(self):
        self.assertEqual(gcd(121,22),11)

    def test_gcd4(self):
        self.assertEqual(gcd(1001,14),7)

    
    def test_gcd5(self):
        self.assertEqual(gcd(0,5),5)

class Frac(object):
    def __init__(self,num,denum):
        nod=gcd(num,denum)
        self.numerator=num/nod
        self.denumerator=denum/nod

    def __eq__(self,other):
        return self.numerator==other.numerator and self.denumerator==other.denumerator

    def __add__(self,other):
        a=self.numerator*other.denumerator+self.denumerator*other.numerator
        b=self.denumerator*other.denumerator
        c=gcd(a,b)
        return Frac(a//c,b//c)
        
        

class TestFrac(unittest.TestCase):
    def test_frac1(self):
        a=Frac(1,2)

    def test_frac2(self):
        a=Frac(4,8)
        b=Frac(1,2)
        self.assertEqual(a,b)

    def test_sum_frac(self):
        a=Frac(1,2)
        b=Frac(1,3)
        self.assertEqual(a+b,Frac(5,6))
    

if __name__=='__main__':
    unittest.main()
