class Account:
     def __init__(self, number, holder, balance, limit):
         self.__number = number
         self.__holder = holder
         self.__balance = balance
         self.__limit = limit

     def extract(self):
         print("Balance is {} the {}'s account".format(self.__balance, self.__holder))
     
     def deposit(self, value):
         self.__balance += value

     def __takeout(self, available):
          return available <= (self.__balance + self.__limit)

     def plunder(self, value):
          if(self.__takeout(value)):
               self.__balance -= value
          else:
               print("The value {} has passed the limit".format(value))

     def transfer(self, value, destiny):
         self.plunder(value)
         destiny.deposit(value)

     def get_balance(self):
         return self.__balance

     def get_holder(self):
         return self.__holder

     @property
     def limit(self):
         return self.__limit

     @limit.setter
     def limit(self, limit):
         self.__limit = limit
    
     @staticmethod
     def cdbank():
         return "001"