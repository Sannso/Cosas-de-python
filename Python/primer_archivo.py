print ("Tests")

first_list=["1", "2", "3", "4", "5"]

print (first_list[0:3])

sublist=first_list[1:4]
print (sublist)

first_list.extend(sublist)
print (first_list)
