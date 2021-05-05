"""A Python programming bootcamp in Kinshasa, DRC, is interested to offering a schoolarship
to her students, a class of over 500 students. They reached out to you to come
to their rescue."""
##########################################################################
#functions
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
for student in range(0 ,501):
    student +=1
    print("Student:",student)
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
    while 0 < quiz1 > 100:
        quiz1 = int(input("Quiz1 again: "))

    quiz2 = int(input("Quiz2: "))
    while 0 < quiz2 > 100:
        quiz2 = int(input("Quiz2 again: "))

    quiz3 = int(input("Quiz3: "))
    while 0 < quiz3 >100:
        quiz3 = int(input("Quiz3 again: "))
    
    test1 = int(input("Advanced python test: "))
    while 0 < test1 > 100:
        test1 = int(input("Advanced python test again: "))

    test2 = int(input("Expert python test: "))
    while 0 < test2 > 100:
        test2 = int(input("Expert python test again: "))
    average = (test1 + test2) /2
    total = quiz1 + quiz2 + quiz3 + average + zoom_scores() + homework_submissions()
    performance = (total/419)* 100
    gender = input("Enter your gender kindly: ").upper()

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
            else:
                print("Kindly you are not eligible for this program ")
    elif gender == "FEMALE" and performance >= 76:
            if region == "Africa":
                print("You are eligible for the scholarship")
            else:
                print("Kindly you are not eligible for this program ")                
    else:
        print("Kindly you are not eligible for this program ")

    print("==================================================")

