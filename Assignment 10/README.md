# CSV TO DATABASE
This program imports a csv file to a mysql database
## imports
csv module 
getpass - to hide sensitive information
faker to generate fake credentials

# Assignment #10:
Now, copy or type and run this code below. See what it produces. The question to ask yourself: Can I ingest the produced Employee_Records.csv file and load it to a MySQL database (Employees)? That is your challenge. All the code is provided except for the last bit. Finish that bit by creating a MySQL database (Employee) and a table (Employee_Records), call the Table Employee_Records, load the csv into the table and display the records. Please capture screenshots of the displayed records, Update the records in the table, Delete option for deleting records and Insert option. Share and upload to GitHub then share with me the link to the code.

import csv
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





