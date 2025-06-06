num = int(input("Enter the number: "))

is_negative = num < 0
if is_negative:
    num = abs(num)

rev = 0
while num != 0:
    digit = num % 10
    rev = (rev * 10) + digit
    num = num // 10

if is_negative:
    rev = -rev
    
print(num)
print(rev)