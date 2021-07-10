import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
	word = word.lower()
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif len(get_close_matches(word, data.keys())) > 0:
		yn = input("Did you mean %s instead? Enter Y if yes ,or N for no: " % get_close_matches(word,data.keys())[0])
		if yn == 'Y' or yn == 'y':
			return data[get_close_matches(word,data.keys())[0]]
		elif yn == 'N' or yn == 'n':
			return "oops input word not found"
		else:
			return "we didnt understand you entry"
	else:
		return "word not found"

word = input("enter word: ")

output = translate(word)

if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)