number = 0
while number < 100:
    number = number +1
    if number%3 == 0:
        print("fizz")
    elif number%5 == 0:
        print("buzz")
    elif number%3 == 0 and number%5 ==0:
        print("fizzbuzz")
    else:
        print(number)