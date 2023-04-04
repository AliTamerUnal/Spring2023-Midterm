def g():
    h = 44

class A:
    def __init__(self, y) -> None:
        self.y = y
        
    i = 22

    g()

    def g(self):
        self.h = 66


a = A(33)

#print (a.y)    #Q4.1
#print (a.h)    #Q4.2
#print (h)      #Q4.3

a.g()

#Q4.4
