import matplotlib.pyplot as plt
import numpy as np
# y=sinx+x^2
x = np.linspace(0, 2*np.pi)
y = np.sin(x) +x**2

plt.plot(x, y)
plt.show()
