num = 10
print("This is a number: " , num)
msg = "Hello, Class"
print("This is a string: ", msg)

user_input = input("Enter you name: ")
print("Your name is ", user_input)
user_input = input("Enter a number: ")
print("You entered: ", user_input)

print("Num variable is of type: ", type(num))
print("msg variable is of type: ", type(msg))

#try again to illustrate types
user_input = input("Enter you name: ")
print("user_input is: ", user_input, "and it's type is: ", type(user_input))
user_input = input("Enter a number: ")
print("user_input is: ", user_input, "and it's type is: ", type(user_input))

num = num + 1
print("Num is now: " , num)
msg = msg + ", how are you doing"
print("msg is now: ", msg)

name = input("Enter you name: ")
if (name == ""):
    msg = "Hello, Class"
else:
    msg = "Hello," + name
print(msg)

def greeting(name) -> str:
    if name == "":
        msg = "Hello, Class"
    else:
        msg = "Hello, " + name
    return msg

name = input("Enter you name (again): ")
greeting_msg = greeting(name)
print(greeting_msg)

#or you can print directly as well
print(greeting(name))
