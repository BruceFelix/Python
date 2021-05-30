import csv 
from getpass import getpass
from mysql.connector import connect, Error, connection, cursor
from faker import Faker
 
record_count = 100
fake = Faker()

with open ('Employee_Records.csv',"r") as csv_file:
    """This is used to read from the csv file and store the values to be used later in a list
    The values will now be update in the database"""
    csvfile = csv.reader(csv_file, delimiter=',')
    all_values = []
    for row in csvfile:
        value =(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
        all_values.append(value)
 
try:# check if it is connected
    connection = connect( host = "localhost",username = getpass("Enter username: "), password = getpass("Enter password: "),database = "employee")
except Error as e:
        print(e)
cursor = connection.cursor()# creates an object cursor named cursor

#################################################
#funtions
def csv_file():
    """stores the values in the csv file"""
    with open('Employee_Records.csv', 'w', newline= '') as csvfile:
        fieldnames = ['First_Name', 'Last_Name', 'SSN', 'Email_address', 'Phone', 'Address', 'City', 'state', 'zipcode', 'country']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
    #
        for i in range(record_count):
         writer.writerow({
          'First_Name': fake.first_name(),
          'Last_Name': fake.last_name(),
          'SSN': fake.ssn(),
          'Email_address': fake.email(),
          'Phone': fake.phone_number(),
          'Address': fake.street_address(),
          'City': fake.city(),
          'state': fake.state(),
          'zipcode': fake.zipcode(),
          'country': fake.country()
      })
def display():
    """Used to display the values in the database"""
    show_details = "SELECT * FROM Employee_Records"
    cursor.execute(show_details)
    result = cursor.fetchall()
    print("\t\t Records")
    print("___________________________________________________________________________________________________________________________________________________________________")
    for row in result:
        print(row)
    connection.commit()
def csv_to_db():
    """Imports the values in the csv file to the database"""
    table = """
        CREATE TABLE IF NOT EXISTS Employee_Records(
            personid INT PRIMARY KEY AUTO_INCREMENT,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            ssn VARCHAR (100),
            email VARCHAR(100),
            phonenumber VARCHAR(100),
            address VARCHAR(100),
            city VARCHAR(50),
            state VARCHAR(50),
            zipcode VARCHAR(50),
            country VARCHAR(50)
        )
    """
    inserting_values = """INSERT INTO Employee_Records(first_name,last_name,ssn,email,phonenumber, address, city, state, zipcode, country)
            VALUES(%s, %s, %s, %s, %s, %s, %s,%s,%s,%s)
            """
    cursor.execute(table)
    cursor.executemany(inserting_values,all_values)
    connection.commit()
    print("Records imported")
def delete_record():
    """Deletes a record from the database"""
    display()
    print("Enter the Person Id of the record you want to delete: ")
    id = input()#gets the id of the value to be deleted
    delete = "DELETE FROM Employee_Records WHERE personid ={idno}".format(idno = id)# query to delete that record
    cursor.execute(delete)
    connection.commit()
    print("Record deleted")
def new_record():
    """Generates new records that will be inserted in the db instead of user input"""
    First_Name = fake.first_name()
    Last_name = fake.last_name()
    SSN = fake.ssn()
    Email_address =fake.email()
    Phone = fake.phone_number()
    Address = fake.street_address()
    City = fake.city()
    state = fake.state()
    zipcode = fake.zipcode()
    country = fake.country()
    values = (First_Name,Last_name,SSN,Email_address,Phone,Address,City,state,zipcode,country)
    return values
def insert_record():
    """Generated records in new record are updated in the db"""
    inserting_values = """INSERT INTO Employee_Records(first_name,last_name,ssn,email,phonenumber,address,city,state,zipcode,country)
            VALUES(%s, %s, %s, %s, %s, %s, %s,%s,%s,%s)
            """
    cursor.execute(inserting_values,new_record())
    connection.commit()
    print("Record insert")
def update_record():
    """Used to change the records of a specific ID"""
    display()
    print("Enter the Person Id of the record you want to update: ")
    id = input()
    records = list(new_record())
    First_Name = records[0]
    Last_name = records[1]
    SSN = records[2]
    Email_address = records[3]
    Phone = records[4]
    Address = records[5]
    City = records[6]
    state = records[7]
    zipcode= records[8]
    country =records[9]
    update = """UPDATE Employee_Records 
    SET first_name = %s ,last_name = %s ,ssn = %s ,email = %s ,phonenumber = %s ,address = %s ,city = %s ,state = %s ,zipcode = %s ,country= %s 
    WHERE personid = %s
    """
    values = (First_Name,Last_name,SSN,Email_address,Phone,Address,City,state,zipcode,country, id)
    cursor.execute(update, values)
    connection.commit()
    display()
def main():
    while True:
        #The main program
        print("Choose the menu below")
        print("""
        Enter
        1 - to Display database
        2 - to Update record
        3 - to Delete record
        4 - to Insert new record
        5 - more values to the database
        6 - to Quit
        """)
        choice = input()
        if choice == "1":
            display()
        elif choice == "2":
            update_record()
        elif choice == "3":
            delete_record()   
        elif choice == "4":
            insert_record() 
        elif choice == "5":
            csv_to_db() 
        elif choice == "6":
            print("Exiting program")
            break
        else:
            print("Choose a valid choice")
#################################################
main()
cursor.close()# closes the cursor object
connection.close()# Terminates the database connection