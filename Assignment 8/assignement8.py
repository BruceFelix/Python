# The JSON gitHub url link is for English to lolcat translation
# This program is desingned and already working. Our job is to add Sheng words and meanings in English
# To the same dictionary
# Save the JSON file in local TXT file and make it appendable/you should be able to add new terms.
########################################################################
#functions
def dictionary_key_value():
    with open("dictionary.txt",'a+') as file:#This stores the key:pair value of the sheng word and it's meaning
        file.write(str(dictionary))
def dictionary_key():
    with open("dictionary-key.txt", "a+") as file:# This file stores the key from the dictionary
        file.write(str(dictionary.keys()))
def dictionary_value():
    with open("dictionary-value.txt","a+") as file:# This file stores the values from the dictionary
        file.write(str(dictionary.values()))
########################################################################
"""import json, requests
data = 'https://raw.githubusercontent.com/normansimonr/Dumb-Cogs/master/lolz/tranzlashun.json'
resp = requests.get(data)
print(resp)
dictionary = eval(resp.text)
#There seems to be a problem with the json fil
print(dictionary)"""


dictionary = {}
while True:
    print("Do you want to add a new sheng word or get it's translation")
    print("Yes to continue: No to cancel")
    answer = input().upper()
    if answer == "YES":
            word = input('Original words: ')
            if word in dictionary:
                print('The translation is:', dictionary[word] )
            elif word not in dictionary:
                dictionary[word] =input("Enter it's meaning in English: ")
            else:
                
                continue
    elif answer == "NO":
        print("Okay good luck")
        break
    else:
        print("Please choose yes or no")
print(dictionary)
print("This dictionary will be stored in a file")
dictionary_key_value()
dictionary_key()
dictionary_value()



