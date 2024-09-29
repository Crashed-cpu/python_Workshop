class xyz:
    def __init__(self):
        self.__balance__ = 0

    def deposit(self, amount):
        self.__balance__+= amount
        return True
    
    def withdraw(self, amount):
            if 0< amount <= self.__balance__:
                 self.__balance__-= amount
                 return True
            else:
                 return False
    def get(self):
         return self.__balance__


ABC = xyz()
print(ABC.get())
ABC.deposit(10000)
print(ABC.get())
ABC.withdraw(1000)
print(ABC.get())
ABC.withdraw(10000)
print(ABC.get())


#where can we use inheritance in this code? 
#we made new class saving and put interest transaction , savings account , simple interest 
