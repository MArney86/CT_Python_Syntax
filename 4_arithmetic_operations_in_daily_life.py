#Task 1: Grocery Store Math

price_bread, price_ham, price_cheddar = 4.99, 3.99, 2.79 #prices of our items
TAX_RATE = .0825 #tax rate of 8.25% in decimal form

subtotal = price_bread + price_ham + price_cheddar
grocery_total = subtotal + subtotal * TAX_RATE
print("Your grocery total for bread, ham, and cheddar is $" + str("{:.2f}".format(grocery_total))) #Total in 2 decimal place precision for monetary values

#Task 2: Bank Interest

INTEREST_RATE = .092 #annual percent interest of 9.2% in decimal format
account_principle = 120432 #our account principle
time_period = 1 #our time period in years

total_with_interest = float(account_principle) * INTEREST_RATE * float(time_period)

print("Your total after " + str("{:.2f}".format(time_period)) + " year(s) is $" + str("{:.2f}".format(total_with_interest)))