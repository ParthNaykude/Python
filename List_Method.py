#List_Method
list = [2 , 1 , 3 , 5]
print("original list : ",list)
list.append(9)                            # Add elements in list 
print("\nAppended List")
print(list)

list.sort()                               #Sorting List in asending array 
print("\n Sorted List  ; ")
print(list)

fruits = [ "Mango" , "Banana" , "Apple" , "Litchi" ]
fruits.sort(reverse = True)                #Desending Sorting
print("\n Sorted List of Fruits : ")
print(fruits)

list.reverse()                            #Reversing the list
print("\n Reversing the list : ")
print(list)

list.insert(2 , 90)                       # Adding element in index 
print("\n the element 90 is added to list at 2 pos")
print(list)


list.remove(5)                             #remove the element
print("\n Removing the element of index 1 : ")
print(list)