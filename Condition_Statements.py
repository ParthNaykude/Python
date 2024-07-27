#Condition_Statement

print("check the Traffic light ")
colour= input("Colour is (Red , Yellow , Green) : ")

if(colour=="Red" or "red"):
    print("Stop")
    
elif(colour=="Yellow" or "yellow"):          #Multiple elseif can be added
    print("you are less than 17")
    
elif(colour=="Green" or "green" ):
    print("You can go")

else:
    print("Enter the correct colour")