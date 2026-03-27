class car:
    def __init__(self,year,make,model,speed):
        self.__year=year
        self.__make=make
        self.__model=model
        self.__speed=speed
    def set_speed(self,speed):
        self.__speed=0 if speed<0 else speed
    def get_speed(self):
        return self.__speed    
    
c=car(2012,"Toyota","Innova",120)
# print(c.__year)
# print(c.year)
c.set_speed(999)
print(c._car__year)
print(c.get_speed())

class bank:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance=self.__balance+amount
    def wid(self,w_anount):
        if self.__balance>=w_anount:
            self.__balance=self.__balance-w_anount
            return True
        else:
            print("insufficient balance")    
    def get_balance(self):
        return self.__balance
b=bank(1000)
b.deposit(700)
b.wid(170)
print(b.get_balance())    




        