import matplotlib.pyplot as plt
import numpy as np

x = np.arange(start=0, stop=21, step=1)
y = np.median(x)
z = np.std(x)
w = np.var(x)
print(x)
print(y)
print(z)
print(w)

num = [0.5,0.7,1.,1.2,1.3,2.1]
bins = [0,1,2,3]

grph = plt.hist(num, bins=bins, orientation='vertical', edgecolor='black')
plt.show()

