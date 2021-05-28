import csv 
from getpass import getpass
from mysql.connector import connect, Error, connection, cursor
from faker import Faker
 
record_count = 100
 
fake = Faker()
 
 
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
try:
    connection = connect(
        host = "localhost",
        username = getpass("Enter username: "),
        password = getpass("Enter password: "),
        database = "employee"
    )
except Error as e:
    print(e)
table = """
    CREATE TABLE IF NOT EXISTS Employee_Records(
        personid INT PRIMARY KEY AUTO_INCREMENT,
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        ssn INT (20),
        email VARCHAR(100),
        phonenumber INT(20),
        address VARCHAR(100),
        city VARCHAR(50),
        state VARCHAR(50),
        zipcode VARCHAR(50),
        country VARCHAR(50)
    )
"""
inserting_values = """
        INSERT INTO People(first_name,last_name,ssn,email,phonenumber address, city, state, zipcode, country)
        VALUES(%s, %s, %s, %s, %s, %s, %s,%s,%s,%s)
        """
values = (first_name,last_name,ssn,email,phonenumber, address, city, state, zipcode, country)

cursor = connection.cursor()
cursor.execute(table)
cursor.execute("DESCRIBE TABLE ")
cursor.close()
connection.commit()