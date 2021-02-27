#Task 1

import numpy as np
import matplotlib.pyplot as plt

vectorA = np.array([3,2])
vectorB = np.array([3,-2])

scalar = np.arange(-3,3,1)

scalar1, scalar2 = np.meshgrid(scalar,scalar)
vectR = vectorA + vectorB
spanRx = scalar1 * vectorA[0] + scalar2 * vectorB[0]
spanRy = scalar1 * vectorA[1] + scalar2 * vectorB[1]
plt.scatter(spanRx,spanRy, s=10, alpha=0.75)

plt.xlim(-20,20)
plt.ylim(-20,20)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.grid()
plt.show()