import math


class Unumber(object):
    
    def __init__(self, value, unit = ""):
        self.value = value
        self.unit = unit
    
    def __str__(self):
        return str(self.value) + self.unit

    def __lt__(self,other):
        pass

    def __le__(self,other):
        pass

    def __eq__(self,other):
        pass

    def __ne__(self,other):
        pass

    def __gt__(self,other):
        pass
    
    def __ge__(self,other):
        pass

    def __add__(self,other):
        pass
    
    def __sub__(self,other):
        pass
    
    def __mul__(self,other):
        pass
    
    def __floordiv__(self,other):
        pass
    
    def __mod__(self,other):
        pass
    
    def __pow__(self,other):
        pass
    
    def __lshift__(self,other):
        pass
    
    def __rshift__(self,other):
        pass
    
    def __and__(self,other):
        pass
    
    def __xor__(self,other):
        pass
    
    def __or__(self,other):
        pass

    def __iadd__(self,other):
        pass
    
    def __isub__(self,other):
        pass
    
    def __imul__(self,other):
        pass
    
    def __ifloordiv__(self,other):
        pass
    
    def __imod__(self,other):
        pass
    
    def __ipow__(self,other):
        pass
    
    def __ilshift__(self,other):
        pass
    
    def __irshift__(self,other):
        pass
    
    def __iand__(self,other):
        pass
    
    def __ixor__(self,other):
        pass
    
    def __ior__(self,other):
        pass
    
if __name__ == "__main__":
    n = Unumber(2,"ms")
    print (n)
    
