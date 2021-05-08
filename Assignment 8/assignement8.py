# The JSON gitHub url link is for English to lolcat translation
# This program is desingned and already working. Our job is to add Sheng words and meanings in English
# To the same dictionary
# Save the JSON file in local TXT file and make it appendable/you should be able to add new terms.
import json, requests
data = 'https://raw.githubusercontent.com/normansimonr/Dumb-Cogs/master/lolz/tranzlashun.json'
resp = requests.get(data)
dictionary = json.loads(resp.text)

#print(dictionary)

word = input('Original words: ')

if word in dictionary:
    print('The translation is:', dictionary[word] )
else:
    print('Sorry, that word has no translation in the dictionary')
#There seems to be a problem with the json file