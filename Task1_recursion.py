def palindrome(pal):
    print("Thank you")

palin = input("type any sentence or number:\n")

initPal = palindrome(palin)

rev_pal = palin[::-1]
if palin == rev_pal:
    print(palin, "is palindrome")
elif rev_pal != palin:
    print(palin, "is not a palindrome")
