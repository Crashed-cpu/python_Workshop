#OOPS WITH PYTHON
#fn overloading and pointer overloading 
#class in python
#in python private attributes not possible external modules is needeede 
#def__init__(self): #it is pointing itself
class xyz:
    def __init__(self):
        self.ABC = "123"

    def get(self):
            return self.ABC 
    
DECLARE_CLASS = xyz()
VALUE = DECLARE_CLASS.get()


print(VALUE)
#BANKING SYSTEM USER BALENCE = starting balendce 0 