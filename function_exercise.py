# Exercise 1
# Defines function
def name_and_age(_name, _age):
    #prints result
    return print(_name, _age)

# gets input from user
name_and_age(input("enter your name:\n"), int(input("enter your age:\n")))

# exercise 3
# Defines function
def calc(num1, num2):
    #Calculation
    sum_add = num1 + num2
    sum_sub = num1 - num2
    #Prints result
    return print("The added number is:", sum_add, "\n", "The subtraction is:", sum_sub)

#Gets user input
calc(int(input("first number:\n")), int(input("second number:\n")))

# exercise 2
# Defines function
def list_output(*args):
    # gets result
    return print("The result(s) are:\n",*args)

# gets user input
list_output(input("enter numbers or strings\n"))

# exercise 4
# creates function
def employee_name():
    return
