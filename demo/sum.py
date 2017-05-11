#!/usr/bin/python

import unittest

def sum_integers(n):
    p=0
    for t in range(n+1):
        p=p+t
    return p

   # p=1
   # x=0
   # while p<n+1:
       # x=x+p
       # p=p+1
   # return x
        

class TestSum(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(sum_integers(1),1)

    def test_unit_val1(self):
        self.assertEqual(sum_integers(5),15)

    def test_unit_val2(self):
        self.assertEqual(sum_integers(100),5050)

    def test_unit_val3(self):
        self.assertEqual(sum_integers(20),210)

if __name__=='__main__':
    unittest.main()
