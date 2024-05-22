# str.format() = optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

#print("The "+animal+" jumped over the "+item)
#print("The {} jumped over the {}".format(animal,item))
#print("The {0} jumped over the {1}".format(animal,item)) #positional argument
#print("The {animal} jumped over the {animal}".format(animal="dog",item="milk")) # keywoard argument

#text = "The {} jumped over the {}"
#print(text.format(animal,item))

#name = "Bro"

#print("Hello, I am {}".format(name))
#print("Hello, I am {:10}. Nice to meet you".format(name)) # Spaces are added with colons
#print("Hello, I am {:<10}. Nice to meet you".format(name)) # Left align
#print("Hello, I am {:>10}. Nice to meet you".format(name)) # Right align
#print("Hello, I am {:^10}. Nice to meet you".format(name)) # Center align

number = 1000

print("The number pi is {:.3f}".format(number)) # number after period represents number of digits after decimal point. f is for floating point number
print("The number is {:,}".format(number)) # Shows up with comma in every thousands place
print("The number is {:b}".format(number)) # Shows up in Binary
print("The number is {:E}".format(number)) # Shows up in scientific notation
