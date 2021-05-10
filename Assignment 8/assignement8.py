# The JSON gitHub url link is for English to lolcat translation
# This program is desingned and already working. Our job is to add Sheng words and meanings in English
# To the same dictionary
# Save the JSON file in local TXT file and make it appendable/you should be able to add new terms.
########################################################################
#functions
def dictionary_key_value():
    with open("dictionary.txt","a") as file:#This stores the key:pair value of the sheng word and it's meaning
        file.write(json.dumps( dictionary))
def dictionary_key():
    with open("dictionary-key.txt", "a") as file:# This file stores the key from the dictionary
        file.write(json.dumps(list(dictionary.keys())))
def dictionary_value():
    with open("dictionary-value.txt","a") as file:# This file stores the values from the dictionary
        file.write(json.dumps(list(dictionary.values())))
########################################################################
import json
from pip._vendor import requests
data = 'https://raw.githubusercontent.com/normansimonr/Dumb-Cogs/master/lolz/data/tranzlashun.json'
resp = requests.get(data)
# print(resp)
dictionary = json.loads(resp.text)
with open("dictionary.txt","a") as file:
    file.write(json.dumps(dictionary))#stores the dictionary in a text file
# print(dictionary)

while True:# a loop to ask the user to enter a new word or it's translation
    print("Do you want to add a new sheng word or get it's translation")
    print("Yes to continue: No to cancel")
    answer = input().upper()#converts the answer to capital letters
    if answer == "YES":
        word = input('Original words: ')
        if word in dictionary:#if the word is in the dictionary it is printed
            print('The translation is:', dictionary[word] )
        elif word not in dictionary:#adds the word and it's meaning if it doesn't exist
            dictionary[word] =input("Enter it's meaning in English: ")
        else:
            print("Enter a word")
    elif answer == "NO":
        print("Okay good luck")
        break
    else:
        print("Please choose yes or no")
# print(dictionary)
print("This dictionary will be stored in a file")
#the function calls adds the dictionaries in form of key and values separately and as key:values in one document
dictionary_key_value()
dictionary_key()
dictionary_value()