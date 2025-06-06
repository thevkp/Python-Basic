#variables: containers or named memory locations
#Dynamic Typing: automatically determines data types by interpreter
#Dynamic binding: data types can be changed anywhere in the program
#Python Does not support variable declaration
#To solve this use declare variable and assign 'None' to it

name = input("Enter Your Name: ")
print(name)

age = int(input("Enter your age: "))
print(age)

a = int(input("Enter first num: "))
b = int(input("Enter second number: "))

c = a + b
print(a + b)

#Dynamic binding
num = 5
print(num)
num = "Nitish"
print(num)

var1,var2,var3 = 1,2,3
print(var1, var2, var3)

num1 = num2 = num3 = 5
print(num1,num2,num3)

#swap variable
var1,var2 = var2,var1
print(var1,var2)


fnum = input("Enter first num: ")
snum = input("Enter second num: ")
print(fnum, snum)

result = fnum + snum
print(result)

result = int(fnum) + int(snum)
print(result)