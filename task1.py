userfruits = int(input(" how many your favorite fruits:"))
listfruits = []

for i in range(userfruits):
    fruits = input ("Enter fruits: ")
    listfruits.append(fruits)
    print (listfruits)

    if fruits == "apple":
       print("happy eating")
    elif fruits == "banana":
        break
    