for i in range(1, 5):
    for j in range(1, i + 1):
        print(j,end="")
    for k in range(i - 1, 0, -1):
        print(k,end="")
    print()


for i in range(1, 5):
    for s in range(i + 1, 5):
        print(" ",end="")
    for j in range(1, i + 1):
        print(j,end="")
    for k in range(i - 1, 0, -1):
        print(k,end="")
    print()
