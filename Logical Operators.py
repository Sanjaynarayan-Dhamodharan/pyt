#logical operators (and, or) = used to check if two or more conditional statements are true.

temp= int(input("what is the weather like today?"))

if not(temp >= 0 and temp <= 30):
    print("Bro do not go outside it's too hot!")

elif not(temp > 30 or temp < 0):
    print("Damn it is normal temp outside")

if not(temp >= 0 and temp <= 30):
    print("It is too hot")