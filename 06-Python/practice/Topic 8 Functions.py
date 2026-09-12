# function = A block of reusable code
#            pace () after the function name to invokate it.

#def happy_birthday():
#    print("Happy birthday to you!")
#   print("You are old!")
#    print("Happy birthday to you!")
#    print() 

#happy_birthday()
#happy_birthday()
#happy_birthday()3


#def happy_birthday(name, age):
#    print(f"Happy birthday to {name}!")
#    print(f"You are {age} years old!")
#    print("Happy birthday to you!")
#    print() 

#happy_birthday("Cesar", "20")
#happy_birthday("David", "30")


#def display_invoice(username, amount, due_date):
#    print(f"Hello {username}.")
#    print(f"Your bill of ${amount:.2f} is due: {due_date}")

#display_invoice("Cesar Guerra", 135.29, "07/09")



# return = statement used to end a function
#          and send a result back to the caller


#def add(x, y):
#    z = x + y
#    return z

#def subtract(x, y):
#    z = x - y
#    return z

#def multiply(x, y):
#    z = x * y
#    return z

#def divide(x, y):
#    z = x / y
#    return z

#print(add(10, 20))
#print(subtract(10, 20))
#print(multiply(10, 20))
#print(divide(10, 20))



def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("cesar", "guerra")

print(full_name)