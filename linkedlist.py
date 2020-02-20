

class Linkedlist:
    e = 0
    nextL = None;

    def __init__(self, x, n = None):
        self.e = x
        self.nextL = n

    def append(self,x):
        while(self.nextL):
            self = self.nextL
        n = Linkedlist(x, None)
        self.nextL = n

    def count(self):
        c = 0
        while(self):
            self = self.nextL
            c += 1
        return c

    def tostring(self):
        s = "[ "
        while self.nextL:
            s += str(self.e)
            s += "; -]--->[ "
            self = self.nextL
        s += str(self.e)
        s += "; X]"
        return s


L = Linkedlist(5)
L.append(3)
L.append(4)
L.append(6)
L.append(1)



print(L.tostring(),'\n', L.count())

