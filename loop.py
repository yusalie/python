import random

ranNUmber = random.randint(1,10)
print(ranNUmber)
guess = int(input("guess number"))
guessTaken = 0
while guessTaken <= 3:
    print("you have 3 guesses")
    if guess != ranNUmber:
        guessTaken + 1
        print("wrong")
    if guess != ranNUmber:
        guessTaken + 1
        print("you have ", (guessTaken+1), " guesses")
    if guess != ranNUmber:
        guessTaken + 1
        print("you have ", (guessTaken+1), " guesses")
    if guess == ranNUmber:
         ("print you win")
    if guessTaken ==3:
        print("you lose","the number was ", ranNUmber)
    break