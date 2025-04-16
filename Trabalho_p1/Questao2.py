import numpy as np
import matplotlib.pyplot as plt

a = 2
b = 2
c = -6

delta = b**2 - 4*a*c

if delta >= 0:
    x1 = (-b + np.sqrt(delta)) / (2*a)
    x2 = (-b - np.sqrt(delta)) / (2*a)
    print(F'O valor de delta é {delta}, e suas raizes são {x1:.2f} e {x2:.2f}.')
else:
    print('Não há raiz real nessa equação.')

valorx = np.linspace(-4, 3, 100)
valory = a * valorx ** 2 + b * valorx + c

plt.figure('equação de segundo grau', figsize=(8, 6))
plt.title('Equação de Segundo Grau')
plt.xlabel = ('Eixo X')
plt.ylabel = ('Eixo Y')
plt.grid(True)
plt.plot(valorx, valory, label = f'y = {a}x² + {b}x + {c}')
plt.scatter([x1, x2], [0, 0], color = 'green', label = (f'Raízes: {x1:.2f} e {x2:.2f}'))
plt.legend()

plt.show()