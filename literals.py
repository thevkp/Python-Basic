#literals: values stored in variables

a = 0b1000 #Binary Literal
print(a)

b = 100 #Decimal Literal
print(b)

c = 0o310 #Octal Literal
print(c)

d = 0xf #Hexadecimal Literal
print(d)

e = 10.5 #Float Literal
print(e)

f = 10e2 #Float Literal in Scientific Notation
print(f)

x = 3.14j #Complex Literal
print(x)
print(x, x.imag, x.real)

fstring = "This is a string" #String Literal
print(fstring)
sstring = 'This is also a string' #String Literal
print(sstring)

unicode = u"\U0001f600\U0001F606\U0001F923\U0001F922" #Unicode Literal
print(unicode) 

isBool = True #Boolean Literal
print(isBool)

ans = isBool + 4
print(ans)

a = None # None Literal
print(a)