num1 = int(input("Enter first number: "))
num2 =int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

max1 = num1
if num1 < num2:
    max1 = num2

# max = num3
# if max < num3:
#     max = num3
    
# print(max)

if num1 < num2 and num2 < num3:
    print('Smallest:', num1)
    
min = num1
for i in range(1, 3):
    if num2 < min:
        min = num2
    elif num3 < min:
        min = num3
print(min)



