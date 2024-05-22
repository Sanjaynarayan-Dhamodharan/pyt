# Scope = The region that a variable is recognized. A variable is only available from inside the region it is created. A global and locally coped versions of a variable can be created.

name = "Bro" #Global scope (Available inside and outside of functions)
def display_name():
    name = "Code" #This is a local scope since it a available only inside this function
    print(name)

display_name()
print(name)