a = 5
b = a
print(a)
print(b)
b += 1
print(a)
print(b)

l1 = [1,2]
l2 = l1 # l2 is a reference variable 
print(l1, l2)
l2.append(5)
print(l1,l2)