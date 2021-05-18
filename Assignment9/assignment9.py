###################################################################################
#Program name: Assignment 9
#Program description: Billing program for  Kenya power and Lighting company
#Programmer: Bruce Felix Macharia /aspiring PYTHONISTA
###################################################################################
#imports
from getpass import getpass
from mysql.connector import connect, Error
import json
#******************************************************************

#******************************************************************
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
def new_customer():
    print("Kindly enter Customer's First name: ")
    first_name = input()
    print("Kinldy enter Customer's Middle name: ")
    middle_name = input()
    print("Kindly enter Customer's Lastname: ")
    last_name = input()
    full_name = first_name +" " + middle_name+ " " + last_name# Forming his name in full
    print("Enter "+first_name +"'s" + " the billing address and County ")
    address = input("Address: ")
    county = input("County: ")
    town = input("Enter Customer's Town : ")
    place = get_area(town)
    kilowatt = float(input("What's their bill this month: " ))
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
    with open("bill.txt", "a+") as file:
        file.seek(0) # Move read cursor to the start of file.
        data = file.read(100)#if the file is not empty then append "\n"
        if len(data) > 0:
            file.write("\n")
        file.write(json.dumps(details))#Append text at the end of the file
    return details
def database(details):
    try:
        with connect(
            host = "localhost",
            user = getpass("Enter username: "),
            password = getpass("Enter password: "),#obscures the input
            # database = input("Enter database: ")
        ) as connection:
            pass
    except Error as e:
        print(e)
        #create a table if it is not there
    #     table = """
    #     CREATE TABLE IF NOT EXISTS People(
    #         personID int  PRIMARY KEY NOT NULL AUTO_INCREMENT,
    #         first_name VARCHAR(50) NOT NULL,
    #         middle_name VARCHAR(50) NOT NULL,
    #         last_name VARCHAR(50) NOT NULL,
    #         address int NOT NULL,
    #         town VARCHAR(50) NOT NULL,
    #         county VARCHAR(50) NOT NULL,
    #         consumption VARCHAR(50) NOT NULL,
    #         bill int NOT NULL
    #     )"""
    #     #then append values
    #     cursor = connection.cursor()
    #     cursor.execute(table)
    #     # print("Table is created")
    #     sql = """
    #         INSERTING INTO People (personID, first_name, middle_name, last_name,
    #         address, town, county, consumption,bill)
    #         VALUES(%s,%s,%s,%s,%s,%s,%f,%f)""" , (first_name, middle_name,last_name
    #         ,address, town, county, kilowatt, bill)
    #     cursor.execute(sql)
    #     print("records inserted")
    #     connection.commit()
    #     #Display the the data  
    #     people =cursor.execute("SELECT * FROM People")
    #     print(people)
    #     cursor.close()
    #     connection.close()
    #     print("MySQL connection is closed")
    # except Error as e: 
    #     print("Error while connecting to MySQL: {}" .format(e))
###########################################################################
#Main
details = new_customer()
database(details)
while True:
    print("__________________________________________________________")
    print("_________________________ MENU____________________________\nChoose")
    print("Generate customer bill - 1")
    print("View database and bill.txt - 2")
    # print("View bill.txt file - 3 ")
    print("QUIT - 3")
    choice = input()
    if choice == "1":
        new_customer()
    elif choice == "2":
        with open("bill.txt", "r") as read_file:
            print(read_file.read())
    elif choice == "3":
        print("Quiting Application")
        break
    else:
        print("Choose valid choice")




