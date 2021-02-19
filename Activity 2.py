import numpy as np
import matplotlib.pyplot as plt
import matplotlib

Vector1 = np.array([-10, -20])
Vector2 = np.array([-10, 15])
Vector3 = np.array([8, 0])
Vector4 = np.array([-10, 0])
Vector5 = np.array([4.5, 4])

#Addition and Subtraction
Subtraction = np.subtract(Vector1, Vector2)
Addition = np.add(np.subtract(Vector1, Vector2), Vector3)
print('#'*64)
print('Subtracting Vector1 and Vector2 is equal to', Subtraction,
      '\nAdding', Subtraction, 'to Vector3 is equal to', Addition)

#Multiplication and Division
Divide = np.divide(Vector1, Vector2)
Multiply = np.multiply(np.divide(Vector1, Vector2), Vector4)
print('#'*64)
print('Dividing Vector1 and Vector2 is equal to', Divide,
      '\nMultiplying', Divide, 'to Vector4 is equal to', Multiply)

#Squarring and Square root
Square = np.square(Vector5)
Square_root = np.sqrt(np.square(Vector5))
print('#'*64)
print('The Square of Vector5 is equal to', Square,
      '\nThe Square Root of', Square, 'is equal to', Square_root)


#Summation
Summation = np.sum(Vector5)
print('#'*64)
print('The Summation of Vector5 is equal to', Summation)


#Visualizing Data
print('#'*64)
plt.title('Visualization of Data')
plt.xlim(-60, 60)
plt.ylim(-60, 60)

#Vector
plt.scatter(Vector1[0], Vector1[1], label='Vector1', c='Yellow')
plt.scatter(Vector2[0], Vector2[1], label='Vector2', c='Olivedrab')
plt.scatter(Vector3[0], Vector3[1], label='Vector3', c='Yellowgreen')
plt.scatter(Vector4[0], Vector4[1], label='Vector4', c='darkolivegreen')
plt.scatter(Vector5[0], Vector5[1], label='Vector5', c='greenYellow')

#Results
plt.scatter(Addition[0],      Addition[1],         label='Addition',          c='teal')
plt.scatter(Subtraction[0],   Subtraction[1],      label='Subtraction',       c='cyan')
plt.scatter(Divide[0],        Divide[1],           label='Division',          c='cadetblue')
plt.scatter(Multiply[0],      Multiply[1],         label='Multiplication',    c='powderblue')
plt.scatter(Square[0],        Square[1],           label='Square',            c='deepskyblue')
plt.scatter(Square_root[0],   Square_root[1],      label='Squareroot',        c='skyblue')

#Resultant Vector
plt.quiver(Vector2[0], Vector2[1], Vector1[0], Vector1[1], angles='xy', scale_units='xy', scale=1, color='Pink')
plt.quiver(-20, -5, Vector4[0], Vector4[1], angles='xy', scale_units='xy', scale=1, color='red')
Vector6 = Vector1 + Vector4
plt.quiver(Vector2[0], Vector2[1], Vector6[0], Vector6[1], angles='xy', scale_units='xy', scale=1, color='blue')


R_mag = np.sqrt(np.sum(Vector1**2+Vector4**2)) ##Euclidean Distance / Euclidean Norm
rise = Vector6[1]
run = Vector6[0]
slope = rise/run
print('The slope is: ',slope)



plt.grid()
plt.legend()
plt.show()
















