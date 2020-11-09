class Bus:
    def __init__(self, seats, color, driver):
        self.seats = seats
        self.color = color
        self.driver = driver


        
bus = Bus(int(input("Number of seats\n")), input("Color of bus\n"), input("name of driver\n"))

print("\n","driver: ", bus.driver, "\n","Color:", bus.color,"\n","Number of seats:", bus.seats)
