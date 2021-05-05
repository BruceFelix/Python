#Enter the price of the House you wish to Buy
print("Enter the house price")
price = float(input())

#Enter the credit score
print("Enter the credit score")
CreditScore = float(input())

#Enter the first name
print("Enter the first name")
first_name = input()

#Enter the last name
print("Enter the last name")
last_name = input()

full_name = first_name + " " + last_name

#Enter the email
print("Enter the email address")
email = input()

#Enter the phone number
print("Enter the phone number")
phone = input()

#Enter the mailing
print("Enter the mailing address")
address = input()

#Enter the mailing city address
print("Enter the City")
city = input()

#Enter your Current State
print("Enter your State")
state = input()
#Enter the mailing zip code
print("Enter the zip code")
zipcode = input()

#Quality for loans with the best interest rates
if CreditScore >= 780 and CreditScore <= 850:
    credit_status = "Excelent Credit"
    #print("Zero Down payment")
    downPayment = 0.0 * price

#Usuallt quality for loans with the best interest rates
elif CreditScore >= 740 and CreditScore <= 779:
    credit_status = "Very Good"
    downPayment = 0.2 * price

#May face slightly higher loan interest rates
elif CreditScore >= 720 and CreditScore <= 739:
    credit_status = "Above average"
    downPayment = 0.3 * price

#May qualify for most loans of higher interest rates
elif CreditScore >= 680 and CreditScore <=719:
    credit_status = "Average"
    downPayment = 0.6 * price

#May qualify for most loans at significant higher interest rates
elif CreditScore >=620 and CreditScore <= 679:
    credit_status = "Below Average"
    downPayment = 0.18 * price

# Usually has some credit issues; will probably not qualify for most loans
elif CreditScore >= 580 and CreditScore <= 619:
    credit_status = "Poor Credit Score"
    downPayment = 0.20 * price 

#Facing extreme credit issue
elif CreditScore < 520:
    credit_status = "Poor Credit Score"
    downPayment = 0.25 * price

else:
    print("You have a bad credit score")


print("==========================================================")
print("OUTPUT OF THE PROGRAM")
print("==========================================================")

print("First Name: " + full_name)
print("Physical Address: " + address)
print("City: %s State: %s Zipcode: %s" %(city, state, zipcode ))

print("New House Price: "+ str(price))
print("Down Payment: "+ str(downPayment))
print("Credit score: "+ str(CreditScore))
print("Credit Status: " + str(credit_status)) 

print("CONGRATULATIONS - YOU NOW OWN YOUR DREAM HOME - " + full_name + " & "  + " Lucy " + last_name )

print("==========================================================")