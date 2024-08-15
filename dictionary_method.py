myDict = {
    "fast": "in a Quick manner",
    "yash": "A coder",
    "mark": [2,3,4,6,8],
     "anotherdict":{'yash':'player'},
    1:2
}

#Distionary methods.

print(list(myDict.keys())) #print the keys of the dictionary .
print(list(myDict.values())) #print the Values of the dictionary .
print(list(myDict.items())) #print the (keys , Values) of the dictionary .

print(myDict)

#update the dictionary.
updateDict={

"tejas":"friend",
"dhanu":"friend"

}
myDict.update(updateDict)
print(myDict)

print(myDict.get("yash")) #Print value assocated with key "yash"
print(myDict["yash"]) #Print value assocated with key "yash"

#Different bitween .get and [] syntax in Dictionary .
print(myDict.get("yash!")) # return None value as "yash1" is not present in Dicationaey .
print(myDict["yash1"]) # throws an error value as "yash1" is not present in Dicationaey .

    