#Exception = events detected during execution that interrupt flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
    print(result)
except ZeroDivisionError as e:
    print(e)
    print("That aint it chief")
except ValueError as e:
    print(e)
    print("Bro nahhhh")
except Exception as e:
    print(e)
    print("fr bruh?")
else:
    print(result)
finally:
    print("YEs yes yes yes")


