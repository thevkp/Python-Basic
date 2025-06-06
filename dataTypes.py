# Python can handle large integers
print(8)
print(2e10)
print(1e309)


#Decimal/float
print(5.5)
print(8 / 3)

#Text/String
print("Hello, World!")

#Complex
print(5 + 6j)

#List roughly C array: Mutable
lst = [1,2,3,4,5]
print(lst)
lst[3] = 88
print(lst)

#Tupe-> collection of objects(immutable), syntax: tup = (ele1, ele2,...)
tup =(1,2,3,4,5)
print(tup)
# tup[0] = -1 #will throw erro


#sets: using curly braces '{}': omitts duplicate values, mutable, no assignment
my_set = {1,2,3,4,5,4,5}
print(my_set)
# my_set[3] = 33 # throws error
my_set.add(33) #adds 33 to the last 
print(my_set)


#Dictionary: collection of key-value pairs, mutable, supports assignment
my_dict = {'Name':'Nitish', 'Age':27}
print(my_dict)
print(my_dict['Name'])
print(my_dict['Age'])
my_dict['Gender'] = "Male"
print(my_dict)

my_dict['Weight'] = 75
print(my_dict)

print(id(my_dict))
print(id(my_set))
print(id(lst))
print(id(lst[0]))


print(type([1,2,3]))