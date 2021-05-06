"""
Motorola is struggling with their Phone book for saving individual contacts on their mobile
phone and tablets. So far so good, but not very well designed as the demand needs it to be
more robust and user friendly. You are the brand-new Python Guru hired to help on this project
to come in and rescue the situation. Without your new design the company will lose a lot of
customers to her competitors like Apple and Samsung.
"""
import json, re
#####################################################
#Variables
phonebook = {
    "First Name" : " ",
    "Middle Initial" : " ",
    "Last Name" : " ",
    "Mailing Address" : " ",
    "City, Country(State), Zip Code" : " ",
    "Email Address" : " ",
    "Phone Number with 10 digits" : " "
}
######################################################
#functions
def menu():
    """
    List a menu for a user to choose from
    """
    print(
        """
        1. List Phone Numbers
        2. Add a Contact
        3. Remove a Contact
        4. Update a Contact 
        5. Lookup a Contacts by Number
        Q. Quit
        """
        )
def get_dict_values():
    """
    Iterates through the phonebook dictionary to enter values to the respective keys
    """
    for key, value in phonebook.items():
        print("Enter ",key)
        value = input()
        phonebook[key] = value
    return phonebook
def add_contact():
    """
    Called to add another contact in the phonebook
    """
    contact_details = get_dict_values()#gets the dictionary added in the add_contact function and stores it
    with open('contacts.txt', 'a') as file:
        file.write((json.dumps(contact_details)) + '\n' ) #updates the dictionary stored in contact_details into the contact.txt
def prompt_the_user():
    """
    Asks the user to either add a new contact or not
    """
    while True:
        print("Do you want to add a contact?")
        choice = input("Enter yes or no:\n ").upper()
        if choice == "YES":
            add_contact()
        elif choice == "NO":
            print("proceed to our menu")
            break
        else:
            print("Please choose a valid choice")
######################################################
#main body
prompt_the_user()
while True:
    """
    The while loop iterates throught the given options and returns valid options
    """
    menu()# displays the menu
    option = input("Type in a number (1-5 or Q):").upper()#the upper is to convert values to capital letters
    if option == "1":
        with open("contacts.txt", 'r') as numbers:#opens the .txt file
            as_a_list = numbers.read()
            phone_number_regex = re.compile(r'\d\d\d\d\d\d\d\d\d\d')#searches for a number with 10 digits
            mo = phone_number_regex.findall(as_a_list)# stores all values found in the file
            print(mo)
    elif option == "2":#basically adds another value
        add_contact()
    elif option == "3": #this option deletes values from our storage
        with open('contacts.txt', 'r') as contact_file:# opens the file and stores the values in a list 
            contact_list = []
            for line in contact_file:
                new_contact = eval(line)
                contact_list.append(new_contact)
        counter = 1 
        for contact in contact_list:# highlights the names and phonenumber of the dictonaries and adds an index before the values
            print( counter,contact["First Name"] + " " + contact["Last Name"] + " " + contact["Phone Number with 10 digits"])
            counter +=1        
        while True:#intends to delete the choosen value
            selection = input("Enter a number to choose the contact to delete: ") 
            if int(selection):
                if 0 < int(selection) <= (counter):
                    del contact_list[int(selection)-1]
                    break               
                else:
                    print("Error number not within range")
            else:
                print("Error entry not a number.") 

        with open('contacts.txt','w') as file:#updates the new values after the choosen value has been deleted
            for line in contact_list:
                file.write((str(line)) + "\n")
    elif option == "4":# chooses the value to be updated and deletes it then the user enters the correct values
        with open('contacts.txt', 'r') as contact_file:
            contact_list = []
            for line in contact_file:
                new_contact = eval(line)
                contact_list.append(new_contact)
        counter = 1 
        for contact in contact_list:
            print( counter,contact["First Name"] + " " + contact["Last Name"] + " " + contact["Phone Number with 10 digits"])
            counter +=1
        while True:
            selection = input("Enter a number to choose the contact to update: ") 
            if int(selection):
                if 0 < int(selection) <= (counter):# highlights the names and phonenumber of the dictonaries and adds an index before the values
                    print("This contact will be updated which requires you re-enter it ")
                    print(contact_list[int(selection)-1])
                    del contact_list[int(selection)-1]
                    with open('contacts.txt','w') as file:
                        for line in contact_list:
                            file.write((str(line)) + "\n")
                    add_contact()
                    break               
            else:
                print("Error number not within range")
    elif option == "5":#searches for the number the user wants. 
        #the constraint is the value has to have 10 digits
        number = input("Enter the number you are looking for: ")
        with open("contacts.txt", 'r') as numbers:
            as_a_list = numbers.read()
            phone_number_regex = re.compile(r'\d\d\d\d\d\d\d\d\d\d')
            result = phone_number_regex.findall(as_a_list)
            if number in result:
                print(number)
            else:
                print("The number is not available")
    elif option == "Q":#breaks the loop and exits the application
        break
    else:
        print("Please choose another value")
        

  