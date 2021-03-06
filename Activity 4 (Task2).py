a = [1,2,5,7,9]
b = [1,3,10,3,2]
c = []

print('Given vectors: a = ', a, 'b = ', b)
print('Inner Product of two vectors: (a * b)')
for i in range(len(a)):
    product1 = a[i] * b[i]
    print(a[i], '*', b[i], '=', product1, '+')
    c.append(product1)
print('(a * b) = ',c)
print('The sum of all numbers :', sum(c))
print('#'*64)
##########################################
d = [1,8,3,0,9 ]
e = [2,3,10,3,8]
f = []

print('Given vectors: d = ', d, 'e = ', e)
print('Inner Product of two vectors: (d * e)')
for i in range(len(d)):
    product2 = d[i] * e[i]
    print(d[i], '*', e[i], '=', product2, '+')
    f.append(product2)
print('(d * e) = ',f)
print('The sum of all numbers :', sum(f))
print('#'*64)
##########################################
g = [4,8,5,1,9 ]
h = [8,9,5,2,1]
j = []

print('Given vectors: g = ', g, 'h = ', h)
print('Inner Product of two vectors: (g * h)')
for i in range(len(g)):
    product3 = g[i] * h[i]
    print(d[i], '*', e[i], '=', product3, '+')
    j.append(product3)
print('(g * h) = ',j)
print('The sum of all numbers :', sum(j))

