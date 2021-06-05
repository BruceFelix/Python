# Assignment #7:
 
Motorola is struggling with their Phone book for saving individual contacts on their mobile phone and tablets. So far so good, but not very well designed as the demand needs it to be more robust and user friendly. You are the brand-new Python Guru hired to help on this project to come in and rescue the situation. Without your new design the company will lose a lot of customers to her competitors like Apple and Samsung.
 
You want to use Python Programming language to design the code using Python Dictionary and Files Processing for permanently storing the individual contacts in a text file.
 
The phonebook needs to accept the following, but through a Python dictionary:
a) 	First Name
b)	Middle Initial
c) 	Last Name
d)	Mailing Address
e)	City, Country (State), Zip Code
f)  	Email Address
g) 	Phone Number
 
Once the above input is entered, please insert them into a file called contacts.txt. Use the following method for opening the contacts.txt for reading/writing.
 
with open("contacts.txt") as file: # Use file to refer to the file object
 
   data = file.read()
 
   do something with data
 
Opens contacts.txt in write mode
with open('contacts.txt', 'w') as file:  # Use file to refer to the file object
 
	file.write('Mandela')
 
Notice that we didn’t have to write “file.close()”. That will automatically be called when you use the with open for this operation.
Make the Menu to be able to INSERT new contacts, EDIT existing contacts, DELETE unwanted Contacts, Update an existing Contact(s).

 ![image](https://user-images.githubusercontent.com/44478872/120902790-01348c80-c64b-11eb-9a44-d868551b2b2d.png)

You may wanna use a menu driven function to accomplish this feat. In your arsenal are the IF…ELSE…ELIF, input(), print(), Dictionary, and use Python functions.
 This program is due in 7 days from today. Good luck and good job. Consult with your Kamkunji in case of any questions.
 
