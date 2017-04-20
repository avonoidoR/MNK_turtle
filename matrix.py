#!/usr/bin/python3

import unittest

class Matrix(object):
    def __init__(self, data):
        if type(data) == list and type(data[0]) == list:
            self.dat = data

    def get(self, p, q):
        return self.dat[p][q]

    def set(self, p, q, val):
        self.dat[p][q] = val

    def height(self):
        return len(self.dat)

    def width(self):
        return len(self.dat[0])

class TestMatrixConstruction(unittest.TestCase):
    def test_create_by_matrix(self):
        m = Matrix([[11, 12], [21, 22], [31, 32]])
        self.assertEqual(m.width(), 2)
        self.assertEqual(m.height(), 3)
        self.assertEqual(m.get(0, 0), 11)

if __name__ == '__main__':
    unittest.main() 
