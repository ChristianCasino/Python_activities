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
##########################################
k = [7,2,3,1,1 ]
l = [3,4,5,2,1]
m = []

print('Given vectors: k = ', k, 'l = ', l)
print('Inner Product of two vectors: (k * l)')
for i in range(len(k)):
    product4 = k[i] * l[i]
    print(k[i], '*', l[i], '=', product4, '+')
    m.append(product4)
print('(k * l) = ',m)
print('The sum of all numbers :', sum(m))
print('#'*64)
##########################################
n = [4,5,5,1,8 ]
o = [2,4,5,2,2]
p = []

print('Given vectors: n = ', n, 'o = ', o)
print('Inner Product of two vectors: (n * o)')
for i in range(len(n)):
    product5 = n[i] * o[i]
    print(n[i], '*', o[i], '=', product5, '+')
    p.append(product5)
print('(n * o) = ',p)
print('The sum of all numbers :', sum(p))

