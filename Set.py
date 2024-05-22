# set = collection which is unordered and unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup","knife"}

print(utensils.difference(dishes))
print(dishes.difference(utensils))
print(utensils.intersection(dishes))
utensils.update(dishes)
dishes.update(utensils)
utensils.add("napkin")
utensils.remove("fork")
#utensils.clear()

dinner_table = utensils.union(dishes)

for x in dinner_table:
    print(x)

