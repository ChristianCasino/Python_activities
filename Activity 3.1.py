#Task 2
import numpy as np
import matplotlib.pyplot as plt

vectorA = np.array([2,0])
vectorB = np.array([2,-2])

A = np.arange(-4,4,1)
B = np.arange(-5,5,2)
C = np.arange(-6,6,3)

scalar1, scalar2 = np.meshgrid(A,A)
scalar3, scalar4 = np.meshgrid(B,B)
scalar5, scalar6 = np.meshgrid(C,C)
vectR = vectorA + vectorB


spanRx1 = scalar1 * vectorA[0] + scalar2 * vectorB[0]
spanRy1 = scalar1 * vectorA[1] + scalar2 * vectorB[1]

spanRx2 = scalar3 * vectorA[0] + scalar4 * vectorB[0]
spanRy2 = scalar3 * vectorA[1] + scalar4 * vectorB[1]

spanRx3 = scalar5 * vectorA[0] + scalar6 * vectorB[0]
spanRy3 = scalar5 * vectorA[1] + scalar6 * vectorB[1]

plt.scatter(spanRx1, spanRy1, s=10, alpha=0.75, color = 'blue')
plt.scatter(spanRx2, spanRy2, s=10, alpha=0.75, color = 'red')
plt.scatter(spanRx3, spanRy3, s=10, alpha=0.75, color = 'green')

plt.xlim(-50,50)
plt.ylim(-50,50)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.grid()
plt.show()