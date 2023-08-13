###########Nada###################
contact = {}
def dislay():
 print("\n\t\tName\t|\tNumber")
 print("-----"*8)
 for key , value in contact.items() :
     print(f"\t\t{key}\t|\t{value}")
print(" \t\t\t**********        Nada          **********")
print(" \t\t\t********** Hello in Contact Book **********")
while True :
 print("\n\t\t\t\t      1.Add new contact\n\t\t\t\t      2.Search contact\n\t\t\t\t      3.Display contact\n\t\t\t\t      4.deleted contact\n\t\t\t\t      5.Update contact\n\t\t\t\t      6.Exit")
 choise= int(input("\t\t\t\t   Please Enter The Number : "))
 if choise == 1 :
        user = input("Enter your Name : ")
        phone = input("Entr your Number : ")
        contact[user] = phone
 elif choise == 2 :
    search_name=str(input("Enter contact Name : "))
    if search_name in contact :
     print(f"The number for {search_name} is {contact[search_name]}")  
    else :
        print("Is Not Found")
 elif choise == 3 :
    if not contact :
        print("the contact is empty")
    else :
        dislay()
        
 elif choise==4:
   deleted_word = input("Enter the Name to be deleted : ")
   if deleted_word in contact :
    confirm=print(f"Are You sure to delete this contacts {contact[deleted_word] } y/n ?").lower
    if confirm == 'y' :
     data= contact.pop(deleted_word)
     print(data)
     dislay()
 elif choise==5:
   edite_word = input("Enter the Name to be edited : ")
   if edite_word in contact :
    phone = input("Entr your Number : ")
    contact[edite_word] = phone  
    dislay()  
   else:
    print(" Name is not found in contact book ")

 else:
    break 


