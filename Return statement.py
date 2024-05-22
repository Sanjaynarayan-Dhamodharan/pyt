# return statement = functions send python values/objects back to the caller
# these values/objects are known as the function's return value

def multiply(number1,number2):
    result = number1 * number2
    return result

#OR

def multiply(number1,number2):
    return number1 * number2

x = multiply(6,8)
print(x)
#print(multiply(6,8))