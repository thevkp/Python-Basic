lst = [1,2,3,4,5]

i = 0
while i < len(lst):
    print(lst[i], end=" ")
    i += 1
print()
    
tup = (1,2,3,4,5)
i = 0
while i < len(tup):
    print(tup[i], end=" ")
    i += 1
print()

my_set = {1,1,2,2,4,4,5,5,3}
# iterator = iter(my_set) #iterating over set using while loop is recommended
# while i < len(my_set):
#     print(my_set[i])
#     i += 1  

for num in my_set:
    print(num, end=" ")
print()



for i in "Magadh":
    print(i, end=" ")
print()


for i in range(1, 10, 2):
    print(i, end=" ")
print()

for i in range(0, 10, 2):
    print(i, end=" ")
print()
    
for i in range(10, 0, -1):
    print(i, end=" ")
print()