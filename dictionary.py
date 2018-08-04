#inteliggent dictionary
import json #json is a inbuilt package
#loading data in python using th load function
from difflib import get_close_matches
data=json.load(open("076 data.json"))

#defining function for performing the task
def translate(word):
    #if condition to check whether word exist
    if word in data:

        return data[word]
    else:
        #incase  there  is no match of the word
        if len(get_close_matches(word,data.keys()))<=0:
            return "Word is out of database"


        #if the user enter something thatis similar to the words in dictionary
        elif len(get_close_matches(word,data.keys(),n=1)) >0:

            print("Did you mean %s instead!!! Enter y or n"% get_close_matches(word,data.keys(),n=1)[0])
            yn=input()
            if yn == 'y' or yn =='Y':
                return data[get_close_matches(word,data.keys())[0]]

            elif yn =='N' or yn =='n':
                return "Sorry word is out of our data base"
            else:
                return "We are not understanding your entry"
#calling the function
word=input("Enter the word you want to search for ")
out=translate(word.lower())#just to make it ase insensitive
count=0
#because the function is giving two type of output  list and string
if type(out)==list:
   for i in out:
        count=count+1
        print(count,"---",i)

else:
    print(out)
