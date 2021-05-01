import requests
word = input(" Enter the word : ")
language = "en_US"
api = f"https://api.dictionaryapi.dev/api/v2/entries/{language}/{word}"
res = requests.get(api)
var = res.json()
print(var[0]['word']+'. '+var[0]['meanings'][0]['partOfSpeech']+'. '+ var[0]['meanings'][0]['definitions'][0]['definition'])