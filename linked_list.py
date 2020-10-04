#Create a python menu driven program for:
#Create a link list of 5 nodes, take data from user.
#Insert an element in front, last and middle of the list.
#Delete a node from front, last and middle.
#Sort the list in ascending and descending order.
#Search a node from a sorted and unsorted list.
#Print the list.
#Count the number of nodes in the list.

#class Menu:

main_menu_input = 0
def main_menu():
  global main_menu_input
  print ("This is a python menu driven program for the following options:")
  print ("\n1.Create a linked list of 5 nodes and take data from the user.")
  print ("2.Insert an element in front, last and middle of the list.")
  print ("3.Delete a node from front, last and middle.")
  print ("4.Sort the list in ascending and descending order.")
  print ("5.Search a node from a sorted and unsorted list.")
  print ("6.Print the list.")
  print ("7.Count the number of nodes in the list.")
  main_menu_input = input("Enter your main menu value:")

main_menu()

numberList =[]
if int(main_menu_input) == 1:
  list_size = int(input("Enter the list size : "))
  print("\n")
  
  for i in range(0, list_size):
    print("Enter number at location", i, ":")
    item = int(input())
    numberList.append(item)
  main_menu()


if int (main_menu_input) == 6:
  print("User List is ", numberList)
  
