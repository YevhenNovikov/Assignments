a=3
b=5
swaps=b-a
b=b-swaps
a=a+swaps
print(a)
print(b)

a=3
b=5
c=a
a=b
b=c
print(a)
print(b)

a=3
b=5
a,b=b,a
print(a)
print(b)