import math
num = int(input("Enter the number: "))

while num != -1:
    for i in range(2, math.ceil(math.sqrt(num))):
        if num % i == 0:
            print(f"{num} is not prime.")
            break
    else:
        print(f"{num} is prime.")
    num = int(input())