num = int(input("Enter the numbers: "))

fnum = num % 10
num = num // 10
print(num)

snum = num % 10
num = num // 10
print(num)

tnum = num % 10
num = num // 10
print(num)

sum = fnum + snum + tnum
print(sum)

num2 = int(input("Enter the number: "))

# sum2 = None
# for x in num2:
#     sum2 = x + sum2
# print(sum2)

sum3 = 0
while num2:
    digit = num2 % 10
    sum3 = sum3 + digit
    num2 = num2 // 10

print(sum3)

