import matplotlib.pyplot as plt
import numpy as np
plt.figure(1)
x=np.linspace(0,1,1000)
plt.subplot(2,1,1)
plt.title('y=x^2 & y=x')
plt.xlabel("x")
plt.ylabel("y")
plt.xlim((0,1))
plt.ylim((0,1))
plt.xticks([0,0.3,0.6,1])
plt.yticks([0,0.5,1])
plt.plot(x,x**2)
plt.plot(x,x)
plt.legend(['y=x^2','y=x'])
plt.savefig('1.png')
plt.show()

