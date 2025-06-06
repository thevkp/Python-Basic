for i in range(1, 10):
    if i == 5:
        break
    print(i)
    
lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))

for i in range(lower, upper + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
        