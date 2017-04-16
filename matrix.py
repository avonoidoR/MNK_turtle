class Matrix(object):
    def __init__(self, data):
        if type(data) == list and type(data[0]) == list:
            self.dat = data

    def get(self, p, q):
        return self.dat[p][q]

    def set(self, p, q, val):
        self.dat[p][q] = val
