print ("Tests")

letra1 = "primera palabra "
letra2 = "segunda palabra \n"
combinados = letra1 + letra2
print(combinados)


first_list=["1", "2", "3", "4", "5"]

print(len(first_list))

for i in range(len(first_list)):
    if(i != 2):
        print(i)
    else:
        print("yo avia ponid0 mi doz aqui.jpg")


print(first_list[1:])
print(first_list[:4])
print(first_list[4:])

print (first_list[0:3])

sublist=first_list[1:4]
print (sublist)

first_list.extend(sublist)
print (first_list)
