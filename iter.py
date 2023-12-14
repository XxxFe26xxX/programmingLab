
class Iter:
    
    def __init__(self,a,b):
        #a = primo, b = ultimo
        self.a = a
        self.b = b

    def __iter__(self):
        self.x = self.a
        return self
    
    def __next__(self):
        if(self.a<=self.b):
            self.x = self.x+1
            return self.x-1
        #else stoppa la iterazione
        else:
            raise StopIteration
 
print(Iter(1,10))