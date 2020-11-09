# creates function
def palindrome(pal):
    print("Thank you")

# asks for user input
palin = input("type any sentence or number:\n")

# calls function
initPal = palindrome(palin)

#reverse input
rev_pal = palin[::-1]

#output answer
if palin == rev_pal:
    print(palin, "is palindrome")
elif rev_pal != palin:
    print(palin, "is not a palindrome")
