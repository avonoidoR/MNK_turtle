import unittest

class Matrix(object):
    def __init__(self,dat):
        if type(dat)==list and type(dat[0])==list:
            self.dat=dat
        elif type(dat)==list:
            self.dat=[[t] for t in dat]

    def width(self):
        return len(self.dat[0])

    def height(self):
        return len(self.dat)

    def get(self,p,q):
        return self.dat[p][q]

class TestMatrix(unittest.TestCase):
    def test_init(self):
        mat=Matrix([[11,12],[21,22],[31,32]])
        self.assertEqual(mat.height(),3)
        self.assertEqual(mat.width(),2)
        self.assertEqual(mat.get(2,1),32)

    def test_vector_init(self):
        mat=Matrix([1,2,10,15])
        self.assertEqual(mat.height(),4)
        self.assertEqual(mat.width(),1)
        self.assertEqual(mat.get(2,0),10)

if __name__=='__main__':
    unittest.main()
    
        
