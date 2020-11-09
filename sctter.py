import matplotlib.pyplot as plt
import numpy as np

y = np.array([220,330,190,340,410,445,415])
x = np.array([14.2, 16.5, 11.8,15.3,18.8,22.5,19.5])

plt.plot(x,y, 'o')
plt.xlabel("Temperature(Degree Celsius)")
plt.ylabel("Soup Sale")
m, c = np.polyfit(x, y, 1)
y = m*x + c
plt.plot(x, y)
plt.show()