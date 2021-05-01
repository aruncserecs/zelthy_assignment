import requests
word = input(" Enter the word : ")
language = "en_US"
api = f"https://api.dictionaryapi.dev/api/v2/entries/{language}/{word}"
response = requests.get(api)
result = response.json()
print(result[0]['word']+'. '+result[0]['meanings'][0]['partOfSpeech']+'. '+ result[0]['meanings'][0]['definitions'][0]['definition'])
