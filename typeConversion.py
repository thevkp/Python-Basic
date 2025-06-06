#type conversion creates a new variable and copies the old value with new type
# as most primitve types are immutable int Python

a = 5
print(type(a))
b = float(a)
print(type(a))
print(type(b))

fnum = input("Enter first num: ")
print(type(fnum))

