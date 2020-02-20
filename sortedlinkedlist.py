class Sortedlinkedlist:
    e = 0
    nextL = None;

    def __init__(self, x, n = None, new = True):
        if new:
            self.e = None
            self.nextL = Sortedlinkedlist(x, n, False)
        else:
            self.e = x
            self.nextL = n.nextL if n else n 
        

    def add(self,x):
        while(self.nextL):
            self = self.nextL
        n = Sortedlinkedlist(x, None, false)
        self.nextL = n

    def count(self):
        c = 0
        while(self.nextL):
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

L = Sortedlinkedlist(10)

print(L.tostring(), '\n', L.count())
