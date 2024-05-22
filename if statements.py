# if statement = a block of code that wille xecute if it's condition is true

age = int(input("how old are you?: "))

if age == 100:
    print("You are a century!")
elif age >= 18:
    print("Wow! You are so old...")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are too young!")

#Begin with if statement, if that is false, go to elif statement and if not that, then go to else statement. You can add more than one elif statement. equal to is ==. Order matters