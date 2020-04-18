import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))



def translate(word):

    if  word in  data:
        return data[word]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        if  len ((get_close_matches(word, data.keys(), n= 3))) > 0 :
            return "Did you mean : %s" % get_close_matches(word, data.keys()) [0]
        else:
            return "Word not present in the dic"
a = input("keresendo :")
print(translate(a))

