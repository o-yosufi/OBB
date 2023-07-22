x = 505 
y = 500 + 5

print(x,y)
#
x == y
x is y
print(id(x))
print(id(y))
#
x = 200
y = 100
print(x is not y)
a = [5, 6, 7, 1, 9]
c = [5, 6, 7, 1, 9]
a = c
print(a is c)