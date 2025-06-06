email = input("Enter your email: ")
password = input("Enter your password: ")

# Store the PIN as a string for proper comparison
pin = "123"

if email == 'vk@gmail.com' and password == str(pin):
    print("You are logged in now.")
elif email == 'vk@gmial.com' and password != str(pin):
    print("Wrong Password")
else:
    print("User Not Found.")

    