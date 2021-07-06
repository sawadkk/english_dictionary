import json

data = json.load(open("data.json"))

def translate(word):
	word = word.lower()
	if word in data:
		return data[word]
	else:
		return "word not found"

word = input("enter word: ")

print(translate(word))