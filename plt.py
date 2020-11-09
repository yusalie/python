import matplotlib.pyplot as plt
import numpy as np


names = ['College1', 'College2']
marksA = [10,20,5,30,100,11,8,48,69,4,41,45,66,89]
marksB = [4,70,54,7,48,48,64,8,64,80,96,84,98,40]
marks = [marksA, marksB]
plt.boxplot(marks)
plt.xlabel("college")

plt.ylabel("marks")

plt.show()

labels = 'Burgers', 'Hotdogs', 'Sandwhich', 'Sushi'
sizes = [37,56,77,99]
explode = (0, 0.1, 0, 0)  #

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

plt.show()


x = np.array([45,4,54,54,80,78,2,84,45,19, -20])
y = np.array([5,0,48,6,48,44,5,63,220,66, 0])
plt.plot(x,y, 'o')
plt.xlabel("Temp")
plt.ylabel("Drinks")
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x* + b)
plt.show()


