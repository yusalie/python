# creates function
def even_or_odd(num):
    print("it is:")


# asks user input
_num = int(input("which number would you like to type?"))

#calls function
initEO = even_or_odd(_num)

# calculation
_modNum = _num%2

#output
if  _modNum == 0:
    print(_num, "is even")
if _modNum != 0:
    print(_num, "is not even")