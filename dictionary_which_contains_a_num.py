''' Write a Python script to generate and print a dictionary which contains a number 
(between 1 and n) in the form(x,x*x). Sample Dictionary (n=5) Expected Output: {1:1, 2:4, 
3:9, 4:16, 5:25}..'''

dict={}
n=int(input("How many numnberdo you want to add in Dictionar:"))
for x in range(1,n+1):
    dict[x]=x*x
print(dict)