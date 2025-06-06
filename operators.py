#Arithmetic Operators

print(5 + 6) #Addition operator

print(5 - 6) #Subtraction operator

print(5 * 6) #Product operator

print(5 / 2) #Float Division

print(5 // 2) #Integer Division return floor value of quotient(result)
print(6.3 // 3) #Will return 2.0 not 2.1

print(5 % 2) # Modulo Operator (return remainder)

print(5 ** 2) #Power operator 


#Relational Operator
print(5 == 4)
print( 5 != 4)

#Logical Operator
print(1 and 0)
print(1 and 1)

print(1 or 0)
print(1 or 1)

print(2 and 1)

#Bitwise Operator
print(2 & 1) #Bitwise 'AND'
print(2 ^ 1) #Bitwise 'XOR'
print(2 | 1) #Bitwise 'OR'

print(2 ^ 3)

#Membership Operators

#in/not in
print('D' in 'Delhi') #Returns True
print('Y' in 'Delhi') #Returns False
print('Y' not in 'Delhi') #Return True

lst = [1, 2, 3, 4, 5]
print(7 in lst)
if 7 in lst:
    print(7, "is present in lst")
else:
    print(7, "is not in lst")

