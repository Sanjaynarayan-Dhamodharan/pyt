# Dictionary = A changeable, unordered collection of unique key:value pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC' ,
          'India':'New Delhi',
          'China':'Beijing',
          'Russia':'Moscow'}

#print(capitals['Russia'])
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())
#capitals.clear()

capitals.pop('China')
capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Washington'})

for key,value in capitals.items():
    print(key,value)
