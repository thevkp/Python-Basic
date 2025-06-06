lst = []
for i in range(0, 5):
    num = int(input())
    lst.append(num)
    
print(lst)

min = lst[0]
for i in range(len(lst)):
    if lst[i] < min:
        min = lst[i]

print(min)