"""
#39.WAP that displays for inserting and deleting......
list1=eval[input("Enter a list")]
print("menu")
print("1:insert")
print("2:delete")
choice=eval(input("enetr your choice"))
if(choice==1):
     index=eval(input("enter the index"))
     element=eval[input("enter the element")]
     list1.insert(index,element)
     print(list1)
elif(choice==2) :
     print("submenu")
     print("1.Using Value")
     print("2.Using index")
     print("3.Using list slice")
     del_choice=eval(input("Enter your choice"))
     if(del_choice==1):
         ele1=eval(input("enter an element"))
         list1.remove(ele1)
         print(list1)
     elif(del_choice==3) :
         index1=eval(input("Enetr index"))
         list1.pop(index1)
         print(list1)
     elif(del_choice==3) :
         start_index=eval(input("Enter start index"))
         end_index=eval(input("Enter end index"))
         del list1(start_index,end_index)
         print(list1)
        
        
"""
"""
#40
list1=eval(input("Enter a list"))
m=min(list1)
i=list1.index(m)
print("minimum",m)
print("index of minimum elements",i)

"""
 #41
 """
list1=eval(input("Enter a list"))
search=input("Enter an element you want to search")
if search in list1:
   print ("element found")
   
else :
 print("element not found")

"""

