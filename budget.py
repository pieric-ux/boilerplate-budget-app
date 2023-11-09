import math

class Category:

  # When objects are created, they are passed in the name of the category.
  # The class should have an instance variable called ledger that is a list.
  def __init__(self, name):
    self.name = name
    self.ledger = []

  # The class should also contain the following methods:

  # A deposit method that accepts an amount and description.
  # If no description is given, it should default to an empty string.
  # The method should append an object to the ledger list in the form of
  # {"amount": amount, "description": description}.
  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  # A withdraw method that is similar to the deposit method,
  # but the amount passed in should be stored in the ledger as a negative number.
  # If there are not enough funds, nothing should be added to the ledger.
  # This method should return True if the withdrawal took place, and False otherwise.
  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False
    
  # A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
  def get_balance(self):
    balance = 0
    for transaction in self.ledger:
      balance += transaction["amount"]
    return balance
  
  # A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
  def transfer(self, amount, destination):
    if self.withdraw(amount, "Transfer to " + destination.name):
      destination.deposit(amount, "Transfer from " + self.name)
      return True
    else:
      return False

  # A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
  def check_funds(self, amount):
    return self.get_balance() >= amount

  # *************Food*************
  # initial deposit        1000.00
  # groceries               -10.15
  # restaurant and more foo -15.89
  # Transfer to Clothing    -50.00
  # Total: 923.96
  def __str__(self):
    output = self.title() + '\n'
    output += self.ledger_str()
    output += self.total()
    return output

  # A title line of 30 characters where the name of the category is centered in a line of * characters.
  def title(self):
    space = (30 - len(self.name)) // 2
    output = '*' * space + self.name + '*' * space
    return output
    
  # A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
  def ledger_str(self):
    output = ''
    for transaction in self.ledger:
      output += f'{transaction["description"][:23]:23}' + f'{transaction["amount"]:7.2f}' + '\n'
    return output
  
  # A line displaying the category total.
  def total(self):
    output = f'Total:{self.get_balance():7.2f}'
    return output

# The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says "Percentage spent by category".
# This function will be tested with up to four categories.
# Look at the example output below very closely and make sure the spacing of the output matches the example exactly.

#Percentage spent by category
#100|          
# 90|          
# 80|          
# 70|          
# 60| o        
# 50| o        
# 40| o        
# 30| o        
# 20| o  o     
# 10| o  o  o  o
#  0| o  o  o  o
#    -----------
#     F  C  A  T
#     o  l  u  e
#     o  o  t  s
#     d  t  o  t
#        h     
#        i     
#        n     
#        g
def create_spend_chart(categories):
  output = 'Percentage spent by category\n'
  names = []
  spent_categories = []
  percentages = []
  
  for category in categories:  
    spent_category = 0
    names.append(tuple(category.name))
    
    for transaction in category.ledger:
      if transaction['amount'] < 0:
        spent_category += transaction['amount']
    spent_categories.append(spent_category)    
  total_spent = sum(spent_categories)
  
  for spent in spent_categories:
    percentages.append(10 * math.floor(abs((spent / total_spent) * 100)/10))
    
  for row in range(100, -1 , -10):
    output += f'{row:>3}| '
    for percentage in percentages:
      if row > percentage:
        output += f' '*3
      else:
        output += f'o' + ' '*2
    output += '\n'

  output += f' '*4 + f'-' + f'---'*len(categories) + '\n'

  for row in range(max(len(name) for name in names)):
    output += f' '* 5
    for name in names:
      if row < len(name):
        output += f'{name[row]}  '
      else:
        output += f' '*3
    if row < (max(len(name) for name in names) - 1):
      output += '\n'
        
  return output
