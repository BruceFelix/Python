###################################################################################
#Program name: Assignment 9
#Program description: Billing program for  Kenya power and Lighting company
#Programmer: Bruce Felix Macharia /aspiring PYTHONISTA
###################################################################################
#functions
def discount_given(kilowatt):
    """
    This function calculates the amount of discount to be given according to the kilowatts consumed
    It takes a float unit as a paramter Which is the kilowatts for that month. 
    """
    if 200 <= kilowatt <= 450:#for less than 451 to 200
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
    Shimoni,Takaungu,Thika,Vihiga,Voi,Wajir,Watamu,Webuye,Wote,Wundanyi""".split(",")#converts string to list

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

###########################################################################
print("Kindly enter your firstname: ")
first_name = input()
print("Kinldy enter your Middle name: ")
middle_name = input()
print("Kindly enter your Lastname: ")
last_name = input()
full_name = first_name + middle_name + last_name# Forming his name in full
print(first_name,"Enter your billing address and County ")
address = input("Address: ")
county = input("County: ")
town = input("Enter the Town you come from: ")
place = get_area(town)
kilowatt =( discount_given(float(input("What was your bill this month: "))))# calls the discount function and takes the input function as the parameter.
bill = monthly_bill(place,kilowatt)# calls the bill function to get the gross bill   
#4 4)	Print out a monthly receipt of the Kilowatts consumed, taxes paid, whether it is residential, or an industrial.
#  Format your output as you would see it on your electric bill at home.
print("################################################################################")
print("\tCustomer Details and total bill")
print("Name:",full_name)
print("Connection type is: ",place)
print("From",address,town,county)
print("Total bill",bill)
print("#######################################################################################")

