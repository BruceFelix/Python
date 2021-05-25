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
