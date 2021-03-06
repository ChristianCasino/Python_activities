import numpy as np
import matplotlib.pyplot as plt

a = np.array([-0.4, 4.3, -0.6])
b = np.array([-0.2, 0.2,  1.0])
c = np.array([-0.2, 2.1, -1.5])

answer = ((np.square(a) + np.square(b) + np.square(c)) * (np.divide(np.multiply(a,(np.add(b, (np.multiply(a,b))))),c)))*(np.linalg.norm(a+b+c))
print('(A**2 + B**2 + C**2)*(A*(B+A*B)/C)*||A + B + C||=',answer)

plt.quiver(a[0], a[1], b[0], b[1], angles='xy', scale_units='xy', scale=1, color='green')
plt.quiver(a[0] + b[0], a[1] + b[1], c[0], c[1], angles='xy', scale_units='xy', scale=1, color='red')
d = b + c
plt.quiver(a[0], a[1], d[0], d[1] ,angles='xy', scale_units='xy', scale=1, color='blue')

R_mag = np.sqrt(np.sum(b**2+c**2))
rise = c[1]
run = c[0]
slope = rise/run
print('The slope is: ',slope)
plt.xlim(-5,9)
plt.ylim(4,7.5)
plt.grid()
plt.legend()
plt.show()

