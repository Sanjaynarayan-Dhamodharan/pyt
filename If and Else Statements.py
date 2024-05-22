age = int(input("How old are you?: "))

if age == 15:
    print("You are my age!")
elif age >= 100:
    print("You are too old!")
elif age == 0:
    print("You are not born at the moment!")
else:
    print("You are " + str(age) + " years old")