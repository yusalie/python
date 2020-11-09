influ = 350.50
can = 400

checkV = input("cancer or flu\n")

consultfee = float(input("Enter fee\n"))

canfee = can + consultfee


if checkV == "flu":
    if consultfee > 600:
        cv = consultfee - (consultfee*(2/100))
        print(cv+influ)
    elif consultfee < 600:
        print(consultfee+influ)
if checkV == "cancer":
    if consultfee > 600:
        print("we cant help")
    elif consultfee < 600:
        print("your amount is:", canfee)

