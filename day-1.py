x =100
y = 200
# WRONG APPROCH
# x=y
# y=x

APPROCH-1
temp = x
x = y
y = temp


APPROCH-2
x,y = y,x

print(x)
print(y)
x = 34
print(id(x))
print(id(y))



dict = {1:"set", 2:10}
print(type(dict))


l = [1,2,3,4,5,67,7,7,7,8,65,45]
print(len(l))

print(8 in l)
print("index: " + str(l.index(7)))  # Corrected concatenation
print("count: " + str(l.count(7)))

print(l.index(8,6,12))

# removing elements
l.remove(7)
print(l)
l.pop()
print(l)
l.pop(3)
print(l)
print(l.pop(3))
print(l)

del l[3]
print(l)
del l[0:4]
print(l)


s = {1,2,3,5,4,6}
s1 = {6,7,8,9,0}
print(s | s1)
print(s.union(s1))
print(s & s1)
print(s.intersection(s1))
print(s - s1)
# print(s.difference(s2))

OutPuts:-


200
100
135453261464616
135453261466728
<class 'dict'>
12
True
index: 6
count: 3
9
[1, 2, 3, 4, 5, 67, 7, 7, 8, 65, 45]
[1, 2, 3, 4, 5, 67, 7, 7, 8, 65]
[1, 2, 3, 5, 67, 7, 7, 8, 65]
5
[1, 2, 3, 67, 7, 7, 8, 65]
[1, 2, 3, 7, 7, 8, 65]
[7, 8, 65]
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
{6}
{6}
{1, 2, 3, 4, 5}





















