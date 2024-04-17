#Task 1: Value Swapping

variable_1 = 14 #first variable
variable_2 = 88 #second variable
test_value = variable_1 - 10 + variable_2 #simple test value to verify the correct swapping of our variable

variable_1, variable_2 = variable_2, variable_1 #swap operation

if test_value - variable_1 == variable_2 - 10 and test_value - variable_2  == variable_1 - 10: #verification test on our swap operation
    print("The variables were swapped correctly")
else:
    print("The variables did not swap correctly")