for i in range(1, 5):
    for j in range(1, 5):
        print('*', end="")
    print()

print()

for i in range(0, 5):
    for j in range(i, 5):
        print('*', end="")
    print()
print()

for i in range(0, 5):
    for s in range(0, i):
        print(" ",end="")
    for j in range(i, 5):
        print("*",end="")
    print()


for i in range(0, 5):
    for j in range(0, i + 1):
        print("*",end="")
    print()
    
for i in range(0, 5):
    for s in range(1, 5 - i):
        print(" ",end="")
    for j in range(0, i + 1):
        print("*",end="")
    print()
    
print()
for i in range(0, 5):
    for s in range(0, i):
        print(" ",end="")
    for j in range(i, 5):
        print("*",end="")
    print()
    
for i in range(0, 5):
    for j in range(1, i + 1):
        print(1 * j,end="")
    print()
