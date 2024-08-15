# create an empty set.

b=set()
print(type(b))

#add the value to empt set.

b.add(4)
b.add(5)
b.add(7)
b.add(5) # adding a value repeatedly dose not change a set.
b.add(5) # adding a value repeatedly dose not change a set.

# accessing Element
#b.add{(4:5)} # cannot add list or dictionary sets.
print(b)

#Length of the set
print(len(b)) # Print length of this sets.

# Removal of an item.
b.remove(5) # Removes 5 from set b

# b.remove(15) # throes an error while tring to Removes 15 (which is not present is set b)
print(b)