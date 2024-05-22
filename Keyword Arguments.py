# Arguments preceded by an identifier when we pass them to a function. The order of the arguments doesn't matter, unlike positional arguments. Python knows the naes of thearguments that our function recieves.

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello(first="John",last="Cena",middle="Randy")

