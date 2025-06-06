fnum = int(input("First num: "))
snum = int(input("Second num: "))

op = input("enter the operation(symbol): ")

if op == '+':
    print(fnum + snum)
elif op == '-':
    print(fnum - snum)
elif op == '*':
    print(fnum * snum)
elif op == '/':
    print(fnum / snum)
else:
    print("Invalid Operation")