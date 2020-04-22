import json
from difflib import get_close_matches
data=json.load(open("/Users/gopalkrishnashukla/Downloads/data.json"))
def definition(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: 
        return data[word.title()]
    elif word.upper() in data: 
        return data[word.upper()]
    elif get_close_matches(word, data.keys(), 1, 0.5):
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: "%get_close_matches(word, data.keys(), 1, 0.5)[0])
        if yn=="Y":
            return (data[get_close_matches(word, data.keys(), 1, 0.5)[0]])
        elif yn=="N":
            return ("This word does not exist. Please double check it.")
        else:
            return ("Sorry, I could not understand your query.")
    else:
        return ("This word does not exist. Please double check it.")
word=input("Enter word: ")
output=(definition(word))
if (type(output)==list):
    for i,j in enumerate(output,1):
        print("{}. {}".format(i,j))       
else:
    print(output)
        
