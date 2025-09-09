import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,7,100)
y1 = 2*x + 1
y2 = 2*x + 2
y3 = 2*x + 3

plt.plot(x,y1, color='red', marker='*', linestyle='--')
plt.plot(x,y2, color='blue', marker='*', linestyle='--')
plt.plot(x,y3, color='green', marker='*', linestyle='--')

plt.xlabel('x')
plt.ylabel('y')
plt.title("Draw the lines  y=2x+1,  y=2x+2,  y=2x+3")

plt.show()