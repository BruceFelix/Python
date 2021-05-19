#Program name: Assignment 9
#Program description: Billing program for  Kenya power and Lighting company
#Programmer: Bruce Felix Macharia /aspiring PYTHONISTA
###################################################################################
#imports
from getpass import getpass # This module is used to hide the password and username for security purposes 
from mysql.connector import connect, Error, connection, cursor # importing the functions individually
import json # To convert the data 
#functions
def discount_given(kilowatt):
    """
    This function calculates the amount of discount to be given according to the kilowatts consumed
    It takes a float unit as a paramter Which is the kilowatts for that month. 
    """
    if 0 < kilowatt > 199:
        kilowatt = kilowatt
    elif 200 <= kilowatt <= 450:#for less than 451 to 200
        kilowatt = kilowatt * (97/100)
    elif 451 <= kilowatt <= 500:#for less than 501 to 451
        kilowatt = kilowatt * (95/100)
    elif 501 <= kilowatt <= 601:#for less than 602 to 501
        kilowatt = kilowatt * (93/100)
    elif 602 <= kilowatt <= 701:# for less than 702 to 602
        kilowatt = kilowatt * (91/100)
    elif 702 <= kilowatt <= 801: #for less than 802 to 702
        kilowatt = kilowatt * (88/100)
    elif kilowatt >= 802:# for greater than 802 or 802
        kilowatt = kilowatt * (95/100)
    return kilowatt # output when called results in kilowatts with a discount
def get_area(town):  
    """
    This function takes a string of Towns and converts them to list of towns.
    The the user enters the town they hail from and if it is in the list it is considered an urban center else rural area.
    The user is then asked to chose the connection type to determine if it is rural/residential etc
    """
    areas = """Baragoi,Bungoma,Busia,Butere,Dadaab,Diani Beach,Eldoret,Emali,Embu,Garissa,Gede,Hola,Homa Bay,Isiolo,Kitui,Kibwezi,Kajiado,Kakamega,
    Kakuma,Kapenguria,Kerich,Keroka ,Kiambu,Kisii,Kisumu,Kitale,Lamu,Langata,Litein,Lodwar,Lokichoggio,Londiani,Loyangalani,Machakos,Makindu,Malindi,
    Mandera,Maralal,Marsabit,Meru,Mombasa,Moyale,Mumias,Muranga,Mutomo,Nairobi,Naivasha,Nakuru,Namanga,Nanyuki,Naro Moru,Narok,Nyahururu,Nyeri,Ruiru,
    Shimoni,Takaungu,Thika,Vihiga,Voi,Wajir,Watamu,Webuye,Wote,Wundanyi""".split(",")#converts string to a list  of towns in Kenya

    if town in areas: #checks if town is in the list
        town = "urban"
    else:
        town = "rural"
    print("""Kindly choose if your connection type is 

            R - for a residential home
            L - for Light Industrial 
            H - Heavy Industrial
            Q - to quit the process
            """
        )
    type_area = input().upper()# Then forms a combination of area and connection type eg: Rural/Residential
    if type_area == "R" and town == "rural":
        resides = "Rural/Residential"
    elif type_area == "L" and town == "rural":
        resides= "Rural/Light Industrial"
    elif type_area == "H" and town == "rural":
        resides = "Rural/Heavy Industrial"
    elif type_area == "R" and town == "urban":
        resides = "Urban/Residential"
    elif type_area == "L" and town == "urban":
        resides = "Urban/Light Industrial"
    elif type_area == "H" and town == "urban":
        resides = "Urban/ Heavy Industrial"
    return resides # The resides is used as a parameter in bill calculation to return gross bill.
def monthly_bill(area,kilowatt):
    """
    This function calculates the gross bill according to the area where the customer is located.
    It is higher in the urban area.
    It also takes two parameters 
    1. the kilowatts in float unit
    2. The town to determine if it is rural or urban
    """
    if area == "Rural/Residential":
        bill = kilowatt * 10.0
        gross_bill = 110/100 * (bill)
    elif area == "Rural/Light Industrial":
        bill = kilowatt * 20.0
        gross_bill = 115/100 * (bill)
    elif area == "Rural/Heavy Industrial":
        bill = kilowatt * 27.0
        gross_bill = 115/100 * (bill)
    elif area ==  "Urban/Residential":
        bill = 104/100 *(kilowatt * 15.0)
        gross_bill = 110/100 * (bill)
    elif area ==  "Urban/Light Industrial":
        bill = 104/100 * (kilowatt * 23.0)
        gross_bill = 118/100 * (bill)
    elif area ==  "Urban/ Heavy Industrial":
        bill = 104/100 * (kilowatt * 30)
        gross_bill = 118/100 * (bill)
    return gross_bill
def generate_bill_update_database():
    #Capturing user data
    print("Enter customer's details first: ")
    print("Kindly enter Customer's First name: ")
    first_name = input()
    print("Kinldy enter Customer's Middle name: ")
    middle_name = input()
    print("Kindly enter Customer's Lastname: ")
    last_name = input()
    address = input("Address: ")
    county = input("County: ")
    town = input("Enter Customer's Town : ")
    kilowatt = float(input("What's their bill this month: " ))
    full_name = first_name +" " + middle_name+ " " + last_name# Forming his name in full
    print("Enter "+first_name +"'s" + " the billing address and County ")
    place = get_area(town)
    discount_given(kilowatt)
    bill = monthly_bill(place,kilowatt)# calls the bill function to get the gross bill   
    print("################################################################################")
    print("\tCustomer Details and total bill")
    print("________________________________________________________________________________")
    print("Name:",full_name)
    print("Connection type is: ",place)
    print("From",address,town,county)
    print("Electricty consumed",str(kilowatt))
    print("Total bill",bill)
    print("#######################################################################################")
    details = full_name + " " + place + " " + address + " " + town+ " " +  county+ " " +  str(kilowatt) + " " + str(bill)
    with open("bill.txt", "a+") as file:# updates the customer's details to this file
        file.seek(0) # Move read cursor to the start of file.
        data = file.read(100)#if the file is not empty then append "\n"
        if len(data) > 0:
            file.write("\n")
        file.write(json.dumps(details))#Append text at the end of the file

    try:# to ensure connection happens 
        connection = connect(
            host = "localhost",
            username = getpass("Enter username: "),# hides the username's name
            password = getpass("Enter password: "),#obscures the input
            database = "bill"
        )
    except Error as e:
        print(e)
    table = """
        CREATE TABLE IF NOT EXISTS People(
        personid INT  PRIMARY KEY AUTO_INCREMENT,
        first_name VARCHAR(50),
        middle_name VARCHAR(50),
        last_name VARCHAR(50),
        address VARCHAR(50),
        town VARCHAR(50),
        county VARCHAR(50),
        consumption INT
        )
        """# to create the table if it doesn't exist
    inserting_values = """
        INSERT INTO People(first_name, middle_name, last_name, address, town, county, consumption)
        VALUES(%s, %s, %s, %s, %s, %s, %s)
        """# this is to add the values to the People table
    values = (first_name, middle_name, last_name, address, town, county, kilowatt)
    cursor= connection.cursor() # creates the cursor object
    cursor.execute(table)# creates a table
    cursor.execute(inserting_values,values)#takes 2 parameters to append to the table
    connection.commit() # updatesthe database
    cursor.close()# closes the cursor object
    connection.close()# Terminates the database connection
    print("Records picked")
def view_database():
    """
    This function is used to view the records in the database.
    """
    try:
        connection = connect(
            host = "localhost",
            username = getpass("Enter username: "),
            password = getpass("Enter password: "),#obscures the input
            database = "bill"
        )
    except Error as e:
        print(e)
    cursor = connection.cursor()
    show_details = "SELECT * FROM People"
    cursor.execute(show_details)
    result = cursor.fetchall()
    print("\t Records")
    for row in result:
        print(row)
    cursor.close()
    connection.close()
####################################################
while True:
    print("__________________________________________________________")
    print("_________________________ MENU____________________________\nChoose")
    print("Generate customer bill and feed database -1")
    print("To view database - 2")
    print("View bill.txt file - 3 ")
    print("QUIT - 4")
    choice = input()
    if choice == "1":
        generate_bill_update_database()
    elif choice == "2":
        print("Presenting data from the database")
        view_database()
    elif choice == "3":
        print("This is the bill.txt file where data is stored")
        with open("bill.txt", "r") as read_file:
            print(read_file.read())
    elif choice == "4":
        print("Quiting Application")
        break
    else:
        print("Choose valid choice")




