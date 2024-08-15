myDict={
    "pankha":"fan",
    "Dabba" :"Box",
    "vastu":"item",
    "saamagree":"material",
    "ansh":"fraction ",
    "jangal":"forest",
    "baithiye":"sit",
    "daud":"race",
    "khidakee":"window ",
    "dukaan":"store ",
    "garmee":"summer",
    "rel gaadee":"train "
 
}
 
print("Options are", myDict.keys())
a=input("Enterr the Hindi Word:-")
# print("The meaning of your word is :",myDict[a])

#below line will not throw an error if the key is not present in the dictionary
print("The meaning of your word is :",myDict.get(a))