A = [-0.4, 4.3, -0.6]
B = [-0.2, 0.2,  1.0]
C = [-0.2, 2.1, -1.5]
A_Squared = []
B_Squared = []
C_Squared = []
X_addition = []
#(A**2 + B**2 + C**2)
for i in range(len(A)):
    A_square_key = A[i]* A[i]
    A_Squared.append(A_square_key)
print('A**2=                    ',A_Squared)

for i in range(len(B)):
    B_square_key = B[i]* B[i]
    B_Squared.append(B_square_key)
print('B**2=                    ',B_Squared)

for i in range(len(C)):
    C_square_key = C[i]* C[i]
    C_Squared.append(C_square_key)
print('C**2=                    ',C_Squared)

for i in range(len(A_Squared)):
    addition_key = A_Squared[i]+B_Squared[i]+C_Squared[i]
    X_addition.append(addition_key)
print('(A**2 + B**2 + C**2)=    ',X_addition)
X = X_addition

print('#'*64)
##########################
#(A*(B+A*B)/C)
A_Product = []
A_Product2 = []
A_Division = []
B_Addition = []

#A*B
for i in range(len(A)):
    A_product_key = A[i] * B[i]
    A_Product.append(A_product_key)
print('A*B =                    ', A_Product)
#B+(A*B)
for i in range(len(A)):
    A_Addition_key = A_Product[i] + B[i]
    B_Addition.append(A_Addition_key)
print('B+(A*B) =                ', B_Addition)
#A*(B+(A*B))
for i in range(len(A)):
    A_Product2_key = B_Addition[i] * A[i]
    A_Product2.append(A_Product2_key)
print('(A*(B+(A*B)) =           ', A_Product2)
#A*(B+(A*B))/C
for i in range(len(A)):
    A_Division_key = A_Product2[i] / C[i]
    A_Division.append(A_Division_key)
print('A*(B+(A*B))/C =          ',A_Division)
Y = A_Division
print('#'* 64)
##################################

A_sum = []
A_Linalg = []
for i in range(len(A)):
    A_sum_key = A[i]+ B[i]+ C[i]
    A_sum.append(A_sum_key)
print('A + B + C =               ',A_sum)

for i in range(len(A)):
    A_Linalg_square_key = A_sum[i] * A_sum[i]
    A_Linalg.append(A_Linalg_square_key)
print('||A + B + C||=           ',sum(A_Linalg)**(1/2))
Z = sum(A_Linalg)**(1/2)
##################################
print('#'*64)

DXY = []
EDZ = []
for i in range(len(A)):
    D = X[i] * Y[i]
    DXY.append(D)
print('(A**2 + B**2 + C**2)*(A*(B+A*B)/C) = ',DXY)

for i in range(len(A)):
    E = DXY[i] * Z
    EDZ.append(E)
print('(A**2 + B**2 + C**2)*(A*(B+A*B)/C)*||A + B + C||=',(EDZ))