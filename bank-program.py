class Account:
  def __init__(self, name, startingBalance):
    self.__name = name 
    self.__balance = startingBalance
  
  @property
  def Name(self):
    return self.__name
  
  @property 
  def Balance (self):
    return self.__balance
 
  @Balance.setter
  def Balance (self, value):
    self.__balance = value 
  
  def print_account(self):
    print("%s $%.2f" % (self.__name, self.__balance))
  
  def withdraw (self, amount):
    if amount > 0 and amount <= self.__balance:
      self.__balance = self.__balance - amount
  
  def deposit(self, amount):
    if amount >0:
      self.__balance += amount 

test_account = Account("Naomi", 100.0)
while True:
  input_line = input("select an option [0:print, 1:withdraw, 2:deposit, 3:quit]:")
  option = int(input_line)
  if option == 0:
    test_account.print_account()
  if option == 1:
    line = input("Enter amount to withdraw:")
    amount = float(line)
    test_account.withdraw(amount)
  if option == 2:
    line = input("Enter amount to Deposit:")
    amount = float(line)
    test_account.deposit(amount) 
  if option == 3:
    print("Thank you")
    break 