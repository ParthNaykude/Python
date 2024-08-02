#Palimdrome

list1 = [1,2,1]
list2 = [ 1,2,3]

copy_list1= list1.copy()
copy_list1.reverse()

if(copy_list1 == list1) : 

        print("The List 1 is Palimdrome")
else : 
        print("Not Palimdrome")
        
copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2) :
    
    print("The list2 is Palimdrome ")
    
else : 
    print ("list2 is Not Palimdrome")