"""A Python programming bootcamp in Kinshasa, DRC, is interested to offering a schoolarship
to her students, a class of over 500 students. They reached out to you to come
to their rescue."""
##########################################################################
#functions
# def mailing_address_details():
#     """ Fucntion to capture students mailing address"""
#     city = input("Enter your city: ")
#     country = input("Enter your Country of origin: ")
#     region = input("""
#     Which region do you come from: 
#     for Africa choose A
#     for Others choose O
#         """).upper()
#     if region == "A":
#         region = "Africa"
#     elif region == "O":
#          region = "Others"
#     else: 
#         print("Enter a valid choice: ")
#         region = input()
#     mailing_address = []
#     mailing_address.append(city)
#     mailing_address.append(country)
#     mailing_address.append(region)
#     # print((mailing_address))
#     return mailing_address
# def test_scores():
#     """ Gets quizes test scores"""
#     print("Enter what you score in the following: ")
#     quiz1 = input("Quiz1: ")
#     quiz2 = input("Quiz2: ")
#     quiz3 = input("Quiz3: ")
# def test_averages():
#     """Gets the average of Advanced and Expert python tests"""
#     test1 = int(input("Advanced python test: "))
#     test2 = int(input("Expert python test: "))
#     average = (test1 + test2) /2
def zoom_scores():
    """Determines the points based on zoom calls attended"""
    score = 0
    zoom = int(input("How many zoom calls did you attend?: "))
    if zoom == 1:
        score = 3
    elif zoom == 2:
        score = 6
    elif zoom == 3:
        score = 9
    return score
def homework_submissions():
    """Grades homeworks submitted based on those submitted"""
    homework_submitted = int(input("How many assignments did you submit? \n"))
    if homework_submitted < 5:
        homework_submitted = 5
    elif homework_submitted == 6:
        homework_submitted = 6
    elif homework_submitted == 7:
        homework_submitted ==7    
    elif homework_submitted == 8:
        homework_submitted = 8
    elif homework_submitted == 9:
        homework_submitted =9
    elif homework_submitted == 10:
        homework_submitted =10
    else:
        print("You didn't submit any assignment")
    return homework_submitted
# def africa_or_not():
#     location = mailing_address_details()
#     if location[2] == "Africa":
#         print("You are eligible for the scholarship")
#     elif location[2] == "Other":
#         print("You are not eligible for this program")
#     else:
#         print("You have to choose a place kindy")
# def scoresheet():
#     total = quiz1 + quiz2 + quiz3 + average + zoom_scores() + homework_submissions()
#     performance = (total/419)* 100
#     return performance
# def awarding_scholarship():
#     if gender == "Male":
#         if performance == 80:
#             if region == "Africa":
#                 print("You are eligible for the scholarship")
#     elif gender == "Female":
#         if performance == 76:
#             if region == "Africa":
#                 print("You are eligible for the scholarship")

##########################################################################

#student details
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name +" " + last_name
id_no = input("Enter your ID number: ")
city = input("Enter your city: ")
country = input("Enter your Country of origin: ")
region = input("""
    Which region do you come from: 
    for Africa choose A
    for Others choose O
        """)
if region == "A" or region =="a":
    region = "Africa"
elif region == "O" or region =="o":
    region = "Others"
else: 
    print("Enter a valid choice: ")
    region = input()
email = input("Enter your email: ")
phone_number = input("Enter your phone number: ")
print("Enter what you score in the following: ")
quiz1 = int(input("Quiz1: "))
quiz2 = int(input("Quiz2: "))
quiz3 = int(input("Quiz3: "))
test1 = int(input("Advanced python test: "))
test2 = int(input("Expert python test: "))
average = (test1 + test2) /2
total = quiz1 + quiz2 + quiz3 + average + zoom_scores() + homework_submissions()
performance = (total/419)* 100
gender = input("Enter your gender kindly: ").upper()
# if gender == "Male" and performance >= 80:
#         if region == "Africa":
#             male ="You are eligible for the scholarship"
# elif gender == "Female":
#     if performance >= 76:
#         if region == "Africa":
#             female ="You are eligible for the scholarship"
# else:
#     other ="Kindly this program is not within your region"




#Displaying performance
print("=================================================")
print("\tStudent's details")
print("=================================================")
print("Name:",full_name)
print("Identification number:",id_no)
print("Your mailing address is:",city,country,region)
print("Email address:",email)
print("Phone number:",phone_number)
print("You scored\n %d : in Quiz1 \n%d : in Quiz2\n %d : in Quiz3"%(quiz1,quiz2,quiz3))
print("Your scored\n %d: in Test1(Advanced)\n %d: in Test 2(Expert)\n %d: as an average in both"%(test1,test2,average))
print("You had %d as your total points"%performance)
print("Performance in zoom class attendance ",zoom_scores())
if gender == "MALE"and performance >= 80:
        if region == "Africa":
            print("You are eligible for the scholarship")
elif gender == "FEMALE" and performance >= 76:
        if region == "Africa":
            print("You are eligible for the scholarship")
else:
    print("Kindly you are not eligible for this program ")

print("==================================================")



#for details in range(501):
