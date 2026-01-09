
# #shape Area calculatio
# # from abc import ABC, abstractmethod

# # class Shape(ABC):
    
# #     def area(self):
# #         pass

# # class Circle(Shape):
# #     def __init__(self, r):
# #         self.r = r
# #     def area(self):
# #         return 3.14 * self.r * self.r


# # c=Circle(5)
# # result=c.area()
# # print(result)





# # from abc import ABC, abstractmethod

# # class Car(ABC):
# #     @abstractmethod
# #     def start(self):
# #         pass

# # class Tesla(Car):
# #     def start(self):
# #         return "Tesla starts with a button"

# # class Suzuki(Car):
# #     def start(self):
# #         return "Suzuki starts with a key"


# # t=Tesla()
# # print(t.start())


# from abc import ABC ,abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass 
# class Circle(Shape):
    
        
#     def area(self,radius ):
#         return 3.14* radius 


# print(Circle().area(5))



#atm
# from abc import ABC, abstractmethod

# class ATM(ABC):
#     @abstractmethod
#     def withdraw(self):
#         pass

# class NepalATM(ATM):
#     def withdraw(self):
#         return "Cash withdrawn"

# c=NepalATM()
# print(c.withdraw(56000))



# from abc import ABC, abstractmethod

# class ATM(ABC):
#     @abstractmethod
#     def withdraw(self, amount):
#         pass

# class NepalATM(ATM):
#     def withdraw(self, amount):
#         return "withdrawn successfully"

# c = NepalATM()
# print(c.withdraw(56000))   



#creste a coffee machine abstract class with abstractmethod make_coffee, crate two sub classes of coffeemachine :lattemachine and mochaMachine ,
#implement abstractmethod make_coffee in lattemachine and mochamachine ,
#create instance of lattemachine and mochamachine , call make_coffee on both instances 



from abc import ABC, abstractmethod

class CoffeeMachine(ABC):
    def make_coffee(self):
        pass


class LatteMachine(CoffeeMachine):
    def make_tea(self):
        return "Latte is ready"


class MochaMachine(CoffeeMachine):
    def make_milk_tea(self):
        return "Mocha is ready"



latte = LatteMachine()
mocha = MochaMachine()

print(latte.make_tea())
print(mocha.make_milk_tea())



















































































































































































































































































































































































































































































