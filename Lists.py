#List = used to store multiple items in a single variable

food = ["Pizza", "Pork", "Meat", "Spaghetti"]

food [0] = "Sushi"

#print(food[0])
food.append("ice cream")
food.remove("Meat")
food.pop()
food.insert(0,"cake")
food.sort()
#food.clear()
for x in food:
    print(x)
