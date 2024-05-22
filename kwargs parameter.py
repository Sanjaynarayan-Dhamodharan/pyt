# **kwargs - parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")
    #print("Hello "+kwargs['first']+" "+kwargs['last'])

hello(title= "Mr.", first="Barry", middlename= "Dude", last= "Benson")