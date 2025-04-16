import numpy as np
import matplotlib.pyplot as plt

def eq1(x):
    return 0.5 * x + 0.5

def eq2(x):
    return -x + 2

xvalor = np.linspace(-1, 3, 100)

y = eq1(xvalor)
y2 = eq2(xvalor)

plt.figure('equação linear', figsize = (8,6))
plt.title('Equação Linear')
plt.xlabel('Equação 1 y = 0.5x + 0.5')
plt.ylabel('Equação 2 y = -x + 2')
plt.plot(xvalor, y, label = 'y = 0.5x + 0.5')
plt.plot(xvalor, y2, label = 'y = -x + 2')
plt.grid(True)
plt.scatter([1], [1], color = 'green', label = 'Solução')
plt.legend()

plt.show()