# Assignment 9
## Billing Applicatiion for Kenya power.
### NB!! To be used by management only.


## MENU
Upon running the application the User is prompted to choose from a given choices

### If they choose one
The generate bill/ update database function.
In this function the customers details are captured 
Th Total bill is also generated and the discount function and get area function is called.

#### Discount Function
This function gives a discount for the total power consumed.
#### Get area function
Gets to determine if the person is form a rural or urban area

##### Updates are made
After all details and calculation are made they are updated in the .txt file bill.txt file in this case and in the data base I have named bill

## IF the choose option 2
The database is opened and the details can be viewed from People's table

## If option 3  
The bill.txt is shown on the screen

## If option 4 
The application is ended


# Assignment #9:
You finally secured a permanent job with Kenya Power and Lighting Company (KPLC) as a Python and Database programmer. As a company, KPLC recently experienced exponential growth due to the Rural Electrification in Kenya. Alot of homes in Kenya, both in Urban and Rural areas got the KPLC services. It has been hectic with the old billing system and the consumption and billing has been accurate. As a new Programmer, there is lots of hope in the design of the system you are working on. The management and the higher echelons in the company cannot wait long to see the product.

The following are the charges for electricity per kilowatt. 
a)	1 Kilowatt of electricity is KE sh. 10.00 in Rural Area (residential)
b)	1 Kilowatt of electricity is KE sh. 15.00 in Urban Area (residential)
c)	1 Kilowatt of electricity is KE sh. 20.00 in Rural Area (Light Industrial)
d)	1 Kilowatt of electricity is KE sh. 23.00 in Urban Area (Light Industrial)
e)	1 Kilowatt of electricity is KE sh. 27.00 in Rural Area (Heavy Industrial)
f)	1 Kilowatt of electricity is KE sh. 30.00 in Urban Area (Heavy Industrial)


As a requirement:

1)	Your program needs to enter the customer’s name whether residential/urban/rural/light Industrial or Heavy Industrial.

2)	Need to input the Billing Address/ City/ Town and County

3)	Calculate the total cost per month of electricity consumed

4)	Print out a monthly receipt of the Kilowatts consumed, taxes paid, whether it is residential, or an industrial. Format your output as you would see it on your electric bill at home.

The following are the conditions for the charges and the billing for the KPLC company.
State VAT Tax (18%) charges on Industrial in Urban Areas
State VAT Tax (15%) charges on Industrial in Rural Areas
State VAT Tax (10%) charges on residential

Every city in the country charges a nominal tax of 4% on the total electricity consumed regardless. We call it city tax - 4%. 





Conditions:
 
a)	If monthly electric consumption is between 200kw and 450 kw then give a discount of 3%.
b)	If monthly electric consumption is between 451kw and 500 kw then give a discount of 5%.
c)	If monthly electric consumption is between 501kw and 601 kw then give a discount of 7%.
d)	If monthly electric consumption is between 602kw and 701 kw then give a discount of 9%.
e)	If monthly electric consumption is between 702kw and 801 kw then give a discount of 11%.
f)	If monthly electric consumption is over 802 kw and above then give a discount of 12%.

Create the program to routinely insert into the file (electricity.txt)  the details and routinely write the same into a MySQL database.

Make the Electricity.txt readable and be able to display the formatted output on the screen.

Make the Electricity MySQL database readable and be able to display the formatted output on the screen and archived records displayable and CRUD (Create/Read/Updated/Deleted).





