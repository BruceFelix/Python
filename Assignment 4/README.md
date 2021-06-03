# Assignment #4:
 
YOU HAVE BEEN HIRED FINALLY BY THE 21st Century as a Senior Programmer and you've been tasked to help in revamping their credit rating and loan issuing system. Just remember, your job is to make things happen. As a Sr. Developer in Python Programming, all the lights and attention are turned towards you and there is a job to be done to deliver this critical system on time.
 
Your job is to design a simple program to allow the loan officer(s) to enter the customer particulars at the terminal and determine if a customer is creditworthy.
 
Based on their loan officer's entry, your system is required to get the best desired results as shown below in the OUTPUT.
 
Please, design a program to do the input entry, do the desired calculations and come up with the needed requirements and output them as needed.
Please consider all the needed variables. If you need to add any, please do add if need is there. Good luck.
 
 
#Enter the price of the House you wish to Buy
print("Enter the house price")
price = input()
 
#Enter the credit score
print("Enter the credit score")
CreditScore = input()
 
 
#Enter the first name
print("Enter the first name")
first_name = input()
 
#Enter the last name
print("Enter the last name")
last_name = input()
 
fullnames = first_name + " " + last_name
 
#Enter the email
print("Enter the email address")
email = input()
 
#Enter the phone number
print("Enter the phone number")
phone = input()
 
#Enter the mailing
print("Enter the mailing address")
mailing = input()
 
#Enter the mailing
print("Enter the City")
city = input()
 
#Enter the mailing
print("Enter the zip code")
zipcode = input()
 
#Qualify for loans with the best interest rates
CreditScore >= 780 AND 850
print "Excent Credit"
print("Zero Down Payment")
downPayment = 0.10 * price
 
#Usually qualify for loans with the best interest rates
CreditScore >= 740 AND 779
print("Very Good")
downPayment = 0.1 * price
 
#May face slightly higher loan Interest rates
CreditScore >= 720 AND 739
print("Above Average")
downPayment = 0.3 * price
 
#May qualify for most loans of higher interest rates
CreditScore >= 680 AND 719
print("Average")
downPayment = 0.6 * price
 
#May qualify for most loans at significant higher Interest rates
CreditScore >= 620 AND 679
print("Below Average")
downPayment = 0.18 * price
 
#Usually has some credit issues; will probably not qualify for most loans
CreditScore >= 580 AND 619
print("Poor Credit Score")
downPayment = 0.20 * price
 
 
#Facing extreme credit issue
CreditScore < 520
print("Poor Credit Score")
downPayment = 0.25 * price
 
==================================================================
OUTPUT OF THE PROGRAM
==================================================================
First Name: James Mutison Mutisya
Physical Address: 435 Hidden Special Place
City: Kalamzoo State: Michigan Zipcode: 49001
 
New House Price: 245,000.00
Down Payment: 20,000.00
Credit Score: 679
Credit Status: Below Average
 
CONGRATULATIONS - YOU NOW OWN YOUR DREAM HOME - James Mutison & Lucy Mutisya
==================================================================

